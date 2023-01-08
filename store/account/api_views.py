from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializers, ProfileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Account, OtpCode
from .permissions import IsOwnerOrReadOnly
from utils import send_otp_code
import random


class Register(APIView):
    def post(self, request):
        ser_data = RegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            cd = ser_data.validated_data
            rand = random.randint(1000, 9999)
            send_otp_code(cd['phone_number'], rand)
            OtpCode.objects.create(phone_number=cd['phone_number'], code=rand)
            request.session['user_registration_info'] = {
                'phone_number': cd['phone_number'],
                'firstname': cd['firstname'],
                'lastname': cd['lastname'],
                'password': cd['password']
            }
            # ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):
    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number = user_session['phone_number'])
        ser_data = VerifySerializers(data=request.POST)

class ProfileUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def put(self, request, pk):
        account = Account.objects.get(id=pk)
        self.check_object_permissions(request, account)
        srz_data = ProfileSerializer(
            instance=account, data=request.POST, partial=True)
        print(srz_data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    def get(self, request, pk):
        account = Account.objects.get(id=pk)
        ser_data = ProfileSerializer(instance=account).data
        return Response(ser_data, status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializers , ProfileSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .permissions import IsOwnerOrReadOnly
class Register(APIView):
    def post(self , request):
        ser_data = RegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data , status=status.HTTP_201_CREATED)
        return Response(ser_data.errors ,status=status.HTTP_400_BAD_REQUEST)

class ProfileUpdateView(APIView):
    permission_classes =[IsOwnerOrReadOnly,]
    def put(self, request, pk):
        account = Account.objects.get(id=pk)
        self.check_object_permissions(request ,account)
        srz_data = ProfileSerializer(
            instance=account, data=request.POST, partial=True)
        print(srz_data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
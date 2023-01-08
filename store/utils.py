from kavenegar import *
from django.conf import settings

def send_otp_code(phone_number, code):
    try:
       kavenegar_instance = KavenegarAPI(settings.API_CODE)
        params = {
            'sender': '',
            'receptor': phone_number, 
            'message': f'{code}کد تایید شما ',
        }
        response = settings.API_CODE.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

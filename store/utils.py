from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('56483559532F5741705069372F784A3275476A4F536F4A4472696F4A55734465673670415979764B7A63513D', timeout=20)
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'{code}کد تایید شما ',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

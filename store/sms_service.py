import os
import urllib.parse
import urllib.request


def send_otp_sms(mobile_number, otp_code, gateway_name="bKash"):
    """
    Sends OTP SMS through the configured Greenweb BD gateway.
    SMS_API_KEY must be configured in the environment.
    """

    sms_api_key = os.environ.get('SMS_API_KEY', '')

    sender_id = os.environ.get(
        'SMS_SENDER_ID',
        '8809612345678'
    )

    message = (
        f"Your {gateway_name} verification OTP is "
        f"{otp_code}. Valid for 3 mins. Do NOT share this code."
    )

    # Standardize Bangladeshi mobile number
    mobile = mobile_number.strip()

    if mobile.startswith('0'):
        mobile = '88' + mobile
    elif not mobile.startswith('88'):
        mobile = '880' + mobile

    print(
        f"[SMS Gateway Dispatch] "
        f"To: {mobile} | Message: {message}"
    )

    # Simulated mode when API key is unavailable
    if not sms_api_key:
        return {
            "status": "simulated",
            "mobile": mobile,
            "otp": otp_code,
            "gateway": gateway_name,
            "note": "SMS_API_KEY is not configured."
        }

    try:
        greenweb_url = "https://api.greenweb.com.bd/api.php"

        data = urllib.parse.urlencode({
            'token': sms_api_key,
            'to': mobile,
            'message': message
        }).encode('utf-8')

        request = urllib.request.Request(
            greenweb_url,
            data=data
        )

        with urllib.request.urlopen(
            request,
            timeout=5
        ) as response:

            response_text = response.read().decode('utf-8')

            print(
                f"[Greenweb SMS API Response]: "
                f"{response_text}"
            )

            return {
                "status": "success",
                "provider": "Greenweb BD",
                "response": response_text
            }

    except Exception as error:

        print(f"[SMS API Exception]: {error}")

        return {
            "status": "error",
            "message": str(error)
        }
def send_otp_sms(mobile_number, otp_code, gateway_name="bKash"):
    """
    Sends an OTP message using a standardized
    Bangladeshi mobile number format.
    """

    message = (
        f"Your {gateway_name} verification OTP is "
        f"{otp_code}. Valid for 3 mins. Do NOT share this code."
    )

    mobile = mobile_number.strip()

    if mobile.startswith('0'):
        mobile = '88' + mobile
    elif not mobile.startswith('88'):
        mobile = '880' + mobile

    print(f"[SMS Gateway Dispatch] To: {mobile}")
    print(f"[SMS Message] {message}")

    return {
        "status": "simulated",
        "mobile": mobile,
        "otp": otp_code,
        "gateway": gateway_name
    }
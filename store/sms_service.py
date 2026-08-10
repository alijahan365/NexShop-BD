def send_otp_sms(mobile_number, otp_code, gateway_name="bKash"):
    """
    Basic OTP SMS helper.
    Currently logs the OTP instead of sending a real SMS.
    """

    message = (
        f"Your {gateway_name} verification OTP is "
        f"{otp_code}. Valid for 3 mins. Do NOT share this code."
    )

    print(f"SMS to {mobile_number}: {message}")

    return {
        "status": "simulated",
        "mobile": mobile_number,
        "otp": otp_code,
        "gateway": gateway_name
    }
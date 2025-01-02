import random

def generate_otp():
    otp = ""
    for _ in range(5):
        otp += str(random.randint(0, 9))
    return otp

# Example usage
otp = generate_otp()
print("Generated OTP:", otp)
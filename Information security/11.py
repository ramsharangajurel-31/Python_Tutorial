import pyotp

# Generate a random key (should be stored securely per user)
user_id = pyotp.random_base32()

# Create a TOTP instance
totp = pyotp.TOTP(user_id)

# Generate the OTP
otp = totp.now()
print("User ID:", user_id)
print("Generated OTP:", otp)

# Simulate user input
user_input_otp = input("Enter the OTP: ")

# Verify the OTP
is_valid_otp = totp.verify(user_input_otp)

if is_valid_otp:
    print("OTP is valid.")
else:
    print("OTP is not valid.")
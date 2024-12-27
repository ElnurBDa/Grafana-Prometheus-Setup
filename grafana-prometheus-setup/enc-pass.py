import bcrypt

password = b"SecurePassword"  # Replace with your desired password
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())

from cryptography import fernet
from cryptography.fernet import Fernet

msg = "hai , rohit welcome to pytho life"

key =Fernet.generate_key()
print(key)

fernet_obj =Fernet(key)

encrypted_msg= fernet_obj.encrypt(msg.encode())
print(encrypted_msg)

decrypted_msg = fernet_obj.decrypt(encrypted_msg).encode()
print(decrypted_msg)
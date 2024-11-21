import os
import msvcrt 

clave_aes256 = os.urandom(32)

print("Clave AES-256:", clave_aes256.hex())

print("Presiona cualquier tecla para cerrar...")

msvcrt.getch() 



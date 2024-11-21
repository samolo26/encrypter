from Crypto.Cipher import AES
import os
import time
import sys

titulo = """
 ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓███████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░                                                                                 
"""
calavera = '''
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu   """"""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
'''


candado= '''
            .-""-.
           / .--. ;
          / /    \ ;
          | |    | |
          | |.-""-.|
         ///`.::::.`;
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         //  '::::' /
          `=':-..-'`
'''
def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

time.sleep(0.8)

os.system('color c')

def animar_ascii_art_vertical(titulo, delay=0.1):
    # Dividir el texto en líneas
    lineas = titulo.splitlines()

    # Imprimir línea por línea con un pequeño retraso para la animación
    for i in range(len(lineas)):
        sys.stdout.write("\033c")  # Limpiar la pantalla para dar el efecto de caída
        for j in range(i + 1):  # Mostrar las primeras i+1 líneas
            sys.stdout.write(lineas[j] + '\n')
        sys.stdout.flush()  # Asegura que se imprima inmediatamente
        time.sleep(delay)  # Pausa para dar el efecto de animación

    # Asegurarse de que se imprima todo el contenido después de la animación
    print()

# Llamada a la función con un retardo de 0.1 segundos
animar_ascii_art_vertical(titulo, 0.3)

time.sleep(1.3)
clear_screen()

os.system('color c')

def imprimir_calavera_animada(calavera, delay=0.01):  # Reducir el delay para que sea más rápido
    for i in range(len(calavera)):
        sys.stdout.write(calavera[i])
        sys.stdout.flush()  # Asegura que el texto se imprima inmediatamente
        time.sleep(delay)  # Pausa para crear la animación
    print()  # Para asegurarse de que haya una nueva línea al final

# Llamada a la función con la calavera y un retardo más rápido de 0.01 segundos
imprimir_calavera_animada(calavera, 0.005)

def imprimir_candado_animada(candado, delay=0.01):  # Reducir el delay para que sea más rápido
    for i in range(len(candado)):
        sys.stdout.write(candado[i])
        sys.stdout.flush()  # Asegura que el texto se imprima inmediatamente
        time.sleep(delay)  # Pausa para crear la animación
    print()  # Para asegurarse de que haya una nueva línea al final

# Llamada a la función con la calavera y un retardo más rápido de 0.01 segundos


# Clave AES256 predeterminada
KEY_1 = "d24b8826a2530a9437c7ce9a557cbaf4922c8d1a6943f228a9d5e6fe2a6f303f"

# Inicializar la clave
KEY = None

def key():
    global KEY
    print("\n1. Introduce una KEY AES256")
    print("2. Usar KEY AES256 predeterminada\n")
    choice_1 = input("Seleccione una opción: ").strip()
    clear_screen()

    if choice_1 == '1':
        try:
            KEY = bytes.fromhex(input("Ingrese la clave AES256 que quieres usar (en formato hexadecimal): ").strip())
            clear_screen()
        except ValueError:
            print("Clave no válida. Asegúrate de que sea un valor hexadecimal.")
            time.sleep(1.8)
            clear_screen()
            key()  
    elif choice_1 == '2':
        print("Se usará la KEY predeterminada")
        KEY = bytes.fromhex(KEY_1)
        clear_screen()
    else:
        print("Opción no válida")
        time.sleep(1.8)
        clear_screen()
        key() 

# Función de padding
def pad(data):
    block_size = AES.block_size
    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Función para encriptar archivos
def encrypt_file(filepath):
    base, ext = os.path.splitext(filepath)
    extension = ext.encode().ljust(16, b'\0')  

    with open(filepath, 'rb') as file:
        plaintext = file.read()

    cipher = AES.new(KEY, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(extension + plaintext))

    encrypted_file = f"{base}.encrypted"
    with open(encrypted_file, 'wb') as file:
        file.write(iv + ciphertext)

    os.remove(filepath)  # Eliminar el archivo original
    print(f"Archivo encriptado exitosamente: {encrypted_file}")

# Función para desencriptar archivos
def decrypt_file(filepath):
    if not filepath.endswith(".encrypted"):
        print("El archivo no tiene la extensión .encrypted. No se puede desencriptar.")
        return

    with open(filepath, 'rb') as file:
        content = file.read()

    iv = content[:AES.block_size]
    ciphertext = content[AES.block_size:]

    cipher = AES.new(KEY, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext))

    extension = decrypted_data[:16].rstrip(b'\0').decode()
    plaintext = decrypted_data[16:]

    base = os.path.splitext(filepath)[0]
    decrypted_file = f"{base}{extension}"  

    with open(decrypted_file, 'wb') as file:
        file.write(plaintext)

    #Eliminar el archivo encriptado
    os.remove(filepath)  
    print(f"Archivo desencriptado exitosamente: {decrypted_file}")

def process_directory(directory, action):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if action == "encrypt":
                encrypt_file(filepath)
            elif action == "decrypt":
                decrypt_file(filepath)

def pas():
    time.sleep(1.8)
    clear_screen()

# Menú principal
def main():
    global KEY
    key()  

    # Contraseña para mostrar la clave AES256
    clave_1 = "sbssbs123"  

    imprimir_candado_animada(candado, 0.02)
    time.sleep(1.3)

    print("\n--- Aplicación de Cifrado Avanzado (AES) ---\n")
    while True:
        print("1. Encriptar un archivo")
        print("2. Desencriptar un archivo\n")
        print("3. Encriptar una carpeta")
        print("4. Desencriptar una carpeta\n")
        print("5. Salir")
        print("@. Mostrar clave AES256\n")
        choice = input("Seleccione una opción: ").strip()
        clear_screen()

        #Función encriptar archivos
        if choice == '1':
            filepath = input("Ingrese la ruta completa del archivo a encriptar: ").strip()
            clear_screen()
            if os.path.isfile(filepath):
                encrypt_file(filepath)
                print("Archivo encriptado")
                pas()
            else:
                print("El archivo no existe.")
                pas()
        #Función desencriptar archivo
        elif choice == '2':
            filepath = input("Ingrese la ruta completa del archivo a desencriptar: ").strip()
            clear_screen()
            if os.path.isfile(filepath):
                decrypt_file(filepath)
                print("Archivo desencriptado")
                pas()
            else:
                print("El archivo no existe")
                pas()
        #Función encriptar carpeta
        elif choice == '3':
            directory = input("Ingrese la ruta completa de la carpeta a encriptar: ").strip()
            if os.path.isdir(directory):
                process_directory(directory, "encrypt")
                pas()
            else:
                print("La carpeta no existe")
                pas()
        # Función desencriptar carpeta
        elif choice == '4':
            directory = input("Ingrese la ruta completa de la carpeta a desencriptar: ").strip()
            clear_screen()
            if os.path.isdir(directory):
                process_directory(directory, "decrypt")
                print("Carpeta encriptada")
                pas()
            else:
                print("La carpeta no existe.")
                pas()
           
        # Mostrar clave AES256
        elif choice == '@':
            clave = input("Ingrese la contraseña para mostrar la clave: ")
            if clave == clave_1:
                clear_screen()
                print("--- NO COMPARTAS ESTA CLAVE CON NADIE ---")
                print(f"\n{KEY_1}")
                time.sleep(3.5)
                clear_screen()
            else:
                print("Clave proporcionada por el usuario no válida")
                pas()

        # Salir del programa
        elif choice == '5':
            print("Saliendo de la aplicación.")
            pas()
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            pas()

if __name__ == "__main__":
    main()

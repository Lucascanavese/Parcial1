
usuarios = {
    '1234': '1234',
    'usuario2': 'contraseña2',
    'usuario3': 'contraseña3'
}

def login():
    print("Bienvenido al login de FitConnect")
    
   
    usuario = input("Introducur su nombre de usuario: ")
    contraseña = input("Introducir su contraseña: ")

    
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("Login exitosamente realizado")
    else:
        print("Usuario o contraseña son incorrectas.")


if __name__ == "__main__":
    login()
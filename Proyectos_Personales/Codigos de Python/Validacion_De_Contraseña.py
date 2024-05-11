def verificar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    elif not any(char.isupper() for char in contrasena):
        return False, "La contraseña debe contener al menos una letra mayúscula."
    elif not any(char.islower() for char in contrasena):
        return False, "La contraseña debe contener al menos una letra minúscula."
    elif not any(char.isdigit() for char in contrasena):
        return False, "La contraseña debe contener al menos un número."
    else:
        return True, "La contraseña cumple con los criterios de complejidad."

contrasena = input("Ingrese una contraseña: ")

es_valida, mensaje = verificar_contrasena(contrasena)

if es_valida:
    print("Contraseña válida:", mensaje)
else:
    print("Contraseña inválida:", mensaje)

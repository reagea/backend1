# Valida el código (si es numérico y de longitud 6).
def validar_id(id: str) -> bool:
    return (id.isnumeric() and len(id) == 6)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_nombre(nombre: str) -> bool:
    nombre = nombre.strip()
    return (len(nombre) > 0 and len(nombre) <= 15)

# Valida que la contraseña estén entre 1 y 9.
def validar_contrasena(contrasena: str) -> bool:
    contrasena_texto  = contrasena.strip()
    if contrasena_texto.strip():
        return (len(contrasena) > 0 and len(contrasena) <= 8)
    else:
        return False
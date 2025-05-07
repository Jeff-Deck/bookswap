from django.core.exceptions import ValidationError

def validate_ec_cedula(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError("La cédula debe tener 10 dígitos numéricos.")

    total = 0
    for i in range(9):
        digit = int(value[i])
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    check_digit = (10 - (total % 10)) % 10
    if check_digit != int(value[9]):
        raise ValidationError("La cédula ingresada no es válida.")

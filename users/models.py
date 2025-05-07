from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_ec_cedula

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    cedula = models.CharField(max_length=10, unique=True, validators=[validate_ec_cedula])
    phone = models.CharField(max_length=15)
    country = models.CharField(default='Ecuador', max_length=50)
    
    # Opciones fijas
    PROVINCIAS = [
        ("Azuay", "Azuay"),
        ("Bolívar", "Bolívar"),
        ("Cañar", "Cañar"),
        ("Carchi", "Carchi"),
        ("Chimborazo", "Chimborazo"),
        ("Cotopaxi", "Cotopaxi"),
        ("El Oro", "El Oro"),
        ("Esmeraldas", "Esmeraldas"),
        ("Galápagos", "Galápagos"),
        ("Guayas", "Guayas"),
        ("Imbabura", "Imbabura"),
        ("Loja", "Loja"),
        ("Los Ríos", "Los Ríos"),
        ("Manabí", "Manabí"),
        ("Morona Santiago", "Morona Santiago"),
        ("Napo", "Napo"),
        ("Orellana", "Orellana"),
        ("Pastaza", "Pastaza"),
        ("Pichincha", "Pichincha"),
        ("Santa Elena", "Santa Elena"),
        ("Santo Domingo", "Santo Domingo"),
        ("Sucumbíos", "Sucumbíos"),
        ("Tungurahua", "Tungurahua"),
        ("Zamora Chinchipe", "Zamora Chinchipe"),
    ]
    province = models.CharField(max_length=50, choices=PROVINCIAS)
    city = models.CharField(max_length=50)

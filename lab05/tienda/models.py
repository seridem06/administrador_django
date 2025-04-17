from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateField("date publisher")

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(
        max_length=8,
        unique=True,
        validators=[MinLengthValidator(8)],
        help_text="Ingrese 8 dígitos sin puntos ni guiones"
    )
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    from django.core.validators import MinLengthValidator

    
        



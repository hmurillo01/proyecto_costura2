from django.db import models



# Tabla costureras
class Costureras(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    identificacion = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)

    def __str__(self):
        return self.nombre
    


# Tabla fabrica
class Fabrica(models.Model):
    nit = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    costura = models.ForeignKey( Costureras, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre  


# Tabla Estado, es el estado que va tener las tareas
class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Tabla Tareas
class Tareas(models.Model):
    descripcion = models.TextField()
    cant_prendas = models.IntegerField()
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)
    costurera = models.ForeignKey(Costureras, on_delete=models.SET_NULL, null=True, blank=True)

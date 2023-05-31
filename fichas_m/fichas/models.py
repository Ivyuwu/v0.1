from django.db import models

class Especialidad(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Rol(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Usuario(models.Model):

    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
    
class PersonalSalud(models.Model):

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario
    
class Horas(models.Model):

    fecha = models.DateTimeField()
    id_medico = models.ForeignKey(PersonalSalud, on_delete=models.CASCADE)
    ocupada = models.BooleanField()
    def __str__(self):
        return self.fecha
    
class Ficha(models.Model):

    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
    previcion_salud = models.CharField(max_length=13)
    domicilio = models.CharField(max_length=100)
    sexo= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
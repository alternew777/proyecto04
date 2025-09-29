from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=100)
    cod_carrera = models.CharField(max_length=20)
    duracion = models.IntegerField()  # Duración en años
    is_active = models.BooleanField(default=True)
    Faculty = models.ForeignKey('Faculty', 
        on_delete=models.CASCADE, related_name='carreras',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_carrera
    
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

class Faculty(models.Model):
    nombre_facultad = models.CharField(max_length=100)
    cod_facultad = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    foto=models.ImageField(upload_to='facultad_photos/', null=True, blank=True)

    def __str__(self):
        return self.nombre_facultad
    
    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"
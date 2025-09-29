from django.db import models
from django.utils import timezone
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
        
class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    cod_estudiante = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    fecha_inscripcion = models.DateField(default=timezone.now)
    carrera = models.ForeignKey('Carrera', 
        on_delete=models.CASCADE, 
        related_name='estudiantes',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_estudiante
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        
class Materia(models.Model):
    nombre_materia = models.CharField(max_length=100)
    cod_materia = models.CharField(max_length=20)
    nivel = models.IntegerField(default=0)  # Nivel o semestre
    is_active = models.BooleanField(default=True, verbose_name="¿Esta Activo la Materia?")
    carrera = models.ForeignKey('Carrera', 
        on_delete=models.CASCADE, 
        related_name='materias',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nombre_materia
    
    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"

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
        
class Programar_Materia(models.Model):
    student = models.ForeignKey(
        Estudiante, 
        on_delete=models.CASCADE,
        related_name='programar_student',
        null=True,
        blank=True,
        verbose_name="Estudiante"
    )
    subject = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='programar_subject',
        null=True,
        blank=True,
        verbose_name="Materia"
    )
    is_active = models.BooleanField(default=True, verbose_name="¿Esta Activo la Programacion?")
    fecha_programacion = models.DateField(default=timezone.now)
    
    class Meta:
        verbose_name = "Programar Materia"
        verbose_name_plural = "Programar Materias"
        unique_together = ('student', 'subject', 'fecha_programacion')  # Un estudiante no puede programar la misma materia más de una vez
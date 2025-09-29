from django.contrib import admin
from .models import *
# Register your models here.

class CarreraInline(admin.TabularInline):
    model = Carrera
    extra = 1
    #autocomplete_fields = ('Faculty',)

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre_carrera', 'cod_carrera', 'duracion', 'is_active', 'Faculty')
    search_fields = ('nombre_carrera', 'cod_carrera')
    autocomplete_fields = ('Faculty',)
    list_filter = ('is_active', 'Faculty')
    #ordering = ('nombre_carrera',)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_materia', 'cod_materia', 'nivel', 'is_active', 'carrera')
    search_fields = ('nombre_materia','cod_materia')
    list_filter = ('is_active', 'nivel', 'carrera')
    #ordering = ('nombre_materia',)

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('nombre_facultad', 'cod_facultad', 'ubicacion', 'is_active')
    search_fields = ('nombre_facultad', 'cod_facultad')
    list_filter = ('is_active',)
    ordering = ('nombre_facultad',)
    inlines = [CarreraInline]
    
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre_estudiante', 'email', 'is_active', 'fecha_inscripcion', 'carrera')
    search_fields = ('nombre_estudiante', 'email')
    autocomplete_fields = ('carrera',)
    list_filter = ('fecha_inscripcion', 'carrera')
    #ordering = ('nombre_estudiante',)
    
class Programar_MateriaAdmin(admin.ModelAdmin):
    list_display = ('subject', 'student', 'fecha_programacion', 'is_active')
    #search_fields = ('estudiante__nombre_estudiante', 'materia__nombre_materia')
    #list_filter = ('fecha_programacion', 'calificacion')
    #autocomplete_fields = ('estudiante', 'materia')
    #ordering = ('-fecha_programacion',)
    
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Programar_Materia, Programar_MateriaAdmin)
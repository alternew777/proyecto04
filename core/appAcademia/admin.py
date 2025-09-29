from django.contrib import admin
from .models import *
# Register your models here.

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre_carrera', 'cod_carrera', 'duracion', 'is_active', 'Faculty')
    search_fields = ('nombre_carrera', 'cod_carrera')
    autocomplete_fields = ('Faculty',)
    list_filter = ('is_active', 'Faculty')
    #ordering = ('nombre_carrera',)

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('nombre_facultad', 'cod_facultad', 'ubicacion', 'is_active')
    search_fields = ('nombre_facultad', 'cod_facultad')
    list_filter = ('is_active',)
    ordering = ('nombre_facultad',)
    
    
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Carrera, CarreraAdmin)
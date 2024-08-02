from django.contrib import admin
from .models import AutorDb, FrasesDb, Profesion
# Register your models here.

admin.site.site_header = "Hola"
admin.site.index_title = "hola2"
admin.site.site_title = "so"

@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display=["nombre"]
    fields=["nombre"]

class FraseInLine(admin.TabularInline):
    model = FrasesDb
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_nacimiento", "fecha_fallecimiento", "profesion", "nacionalidad"]
    list_display = ["nombre", "fecha_nacimiento"]
    inlines = [FraseInLine]
    
admin.site.register(AutorDb, AutorAdmin)

@admin.register(FrasesDb)
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fk"]
    list_display = ["cita"]
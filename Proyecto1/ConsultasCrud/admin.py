from django.contrib import admin
from .models import MedicoDb, ClienteDb, CitaDb

admin.site.site_header = "Administración de Citas Médicas"
admin.site.index_title = "Panel de administración"
admin.site.site_title = "Admin Citas"

@admin.register(MedicoDb)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ["nombre_medico", "edad_medico", "especialidad", "sexo_medico"]
    fields = ["nombre_medico", "edad_medico", "especialidad", "sexo_medico"]


@admin.register(ClienteDb)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre_cliente", "edad_medico", "sexo_cliente"]
    fields = ["nombre_cliente", "edad_medico", "sexo_cliente"]

class CitaInline(admin.TabularInline):
    model = CitaDb
    extra = 1

@admin.register(CitaDb)
class CitaAdmin(admin.ModelAdmin):
    list_display = ["cliente_cita_fk", "medico_cita_fk"]
    fields = ["cliente_cita_fk", "medico_cita_fk"]
    list_filter = ["cliente_cita_fk", "medico_cita_fk"]

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre_cliente", "edad_medico", "sexo_cliente"]
    fields = ["nombre_cliente", "edad_medico", "sexo_cliente"]
    inlines = [CitaInline]

class MedicoAdmin(admin.ModelAdmin):
    list_display = ["nombre_medico", "edad_medico", "especialidad", "sexo_medico"]
    fields = ["nombre_medico", "edad_medico", "especialidad", "sexo_medico"]
    inlines = [CitaInline]



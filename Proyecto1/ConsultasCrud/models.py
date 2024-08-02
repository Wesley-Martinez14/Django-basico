from django.db import models

class MedicoDb(models.Model):

    sexo_opciones = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    nombre_medico = models.CharField(max_length=75, verbose_name="Nombre")
    edad_medico = models.IntegerField(verbose_name="Edad")
    especialidad = models.CharField(max_length=50, verbose_name="Especialidad")
    sexo_medico = models.CharField(max_length=1, choices=sexo_opciones, verbose_name="Sexo")

    class Meta:
        db_table = "Medicos"
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __str__(self) -> str:
        return self.nombre_medico

class ClienteDb(models.Model):
    sexo_opciones = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    nombre_cliente = models.CharField(max_length=75, verbose_name="Nombre")
    edad_medico = models.IntegerField(verbose_name="Edad")
    sexo_cliente = models.CharField(max_length=1, choices=sexo_opciones, verbose_name="Sexo")

    class Meta:
        db_table = "Clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self) -> str:
        return self.nombre_cliente

class CitaDb(models.Model):
    cliente_cita_fk = models.ForeignKey(ClienteDb, on_delete=models.CASCADE)
    medico_cita_fk = models.ForeignKey(MedicoDb, on_delete=models.CASCADE)

    class Meta:
        db_table = "Citas"
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
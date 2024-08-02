from rest_framework import serializers
from .models import MedicoDb, ClienteDb, CitaDb

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoDb
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteDb
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente_cita_fk.nombre_cliente', read_only=True)
    medico_nombre = serializers.CharField(source='medico_cita_fk.nombre_medico', read_only=True)
    
    class Meta:
        model = CitaDb
        fields = ['id', 'cliente_cita_fk', 'medico_cita_fk', 'cliente_nombre', 'medico_nombre']
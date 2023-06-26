from rest_framework import serializers
from ong.models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'nome', 'animal', 'sexo', 'raca', 'idade')
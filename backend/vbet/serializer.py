from rest_framework import serializers
from .models import Vbet

class SignatureGeneratorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vbet
        fields = '__all__'
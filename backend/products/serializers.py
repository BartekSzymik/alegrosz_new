from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'description')
        # fields = '__all__' - antypraktyka, wszystkie pola, ale ryzyko zmiany modelu
        # exclude = ('id', ) - wszytkie oprócz


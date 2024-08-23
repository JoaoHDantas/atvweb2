from rest_framework import serializers
from web2app import models

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = '__all__'
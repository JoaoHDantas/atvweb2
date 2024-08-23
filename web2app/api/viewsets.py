from rest_framework import viewsets
from web2app import models
from web2app.api import serializers
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer

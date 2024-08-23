from rest_framework import routers
from web2app.api import viewsets

produto_router = routers.DefaultRouter()
produto_router.register( 'meu_modelo' , viewsets.ProdutoViewSet)
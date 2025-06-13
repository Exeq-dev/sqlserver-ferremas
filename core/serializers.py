from rest_framework import serializers
from .models import *

class RolUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = rolUsuario
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = comuna
        fields = '__all__'

class UsuarioCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarioCustom
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = marca
        fields = '__all__'

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoriaProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = sucursal
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrito
        fields = '__all__'

class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'
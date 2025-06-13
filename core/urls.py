from django.urls import path, include
from .views import *
from .views import CustomLoginView
from django.conf import settings
from django.contrib.staticfiles.urls import static
from rest_framework import routers

# CREAMOS LAS RUTAS PARA LA API
router = routers.DefaultRouter()
router.register(r'roles', RolUsuarioViewSet)
router.register(r'regiones', RegionViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'usuarios', UsuarioCustomViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'categorias', CategoriaProductoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'items-carrito', ItemCarritoViewSet)
router.register(r'seguimientos', SeguimientoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'items-pedido', ItemPedidoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),

    path('', index, name="index"),
    path('shop/', shop, name="shop"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),
    path('contact/', contact, name="contact"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('thankyou/', thankyou, name="thankyou"),
    path('register/', register, name="register"),

    #URLS CRUD PRODUCTOS (AÑADIR, ACTUALIZAR, ELIMINAR):
    path('addProduct/', addProduct, name="addProduct"),
    path('detalle_producto/<int:idProducto>/', detalle_producto, name='detalle_producto'),
    path('producto/<int:idProducto>/modificar/', modificar_producto, name='modificar_producto'),
    path('producto/<int:idProducto>/eliminar/', eliminar_producto, name='eliminar_producto'),

    #PANEL DE ADMINISTRACIÓN (ROL ADMINISTRADOR):
    path('panel_administracion/', panel_administracion, name='panel_administracion'),

    #GESTIÓN DE USUARIOS
    path('gestion_usuarios/', gestion_usuarios, name='gestion_usuarios'),
    path('adduser/', add_user, name="adduser"),
    path('eliminar_usuario/<id>/', eliminar_usuario, name='eliminar_usuario'),
    path('<p_id>/modificar_usuario/', modificar_usuario, name='modificar_usuario'),

    #CARRITO DE COMPRAS:
    path('agregar/<idProducto>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:itemcarrito_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),

    #PEDIDO
    path('crear_pedido/', crear_pedido, name='crear_pedido'),
    path('boleta/<numero_pedido>', boleta, name='boleta'),

    #MIS PEDIDOS
    path('mis_pedidos/', mis_pedidos, name="mis_pedidos"),

    #ADMINISTRAR PEDIDOS:
    path('administrar_pedidos/', administrar_pedidos, name="administrar_pedidos"),
    path('cambiar_estado/<str:numero_orden>/', cambiar_estado, name='cambiar_estado'),

    #SOPORTE CONTACTO:
    path('soporte_contacto/', soporte_contacto, name="soporte_contacto"),

    #PEDIDOS ENTREGADOS Y EXCEL
    path('pedidos_entregados/', pedidos_entregados, name="pedidos_entregados"),
    path('generar_informes/', generar_informes, name="generar_informes"),

    path('obtener_sucursales/', obtener_sucursales, name='obtener_sucursales'),
    
    path('perfil_usuario/', perfil_usuario, name='perfil_usuario'),
]


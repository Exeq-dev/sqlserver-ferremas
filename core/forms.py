from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
import re

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario', help_text='Mínimo 6 caracteres')
    run = forms.CharField(label='RUN (Rol Único Nacional)', help_text='Ejemplo: 12345678-9')
    pnombre = forms.CharField(label='Primer Nombre')
    ap_paterno = forms.CharField(label='Apellido Paterno')
    correo_usuario = forms.EmailField(label='Correo electrónico')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento')
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs={'placeholder': 'Calle, número, comuna'}))
    idComuna = forms.ModelChoiceField(queryset=comuna.objects.all(), label='Comuna')
    idRol = forms.ModelChoiceField(queryset=rolUsuario.objects.all(), label='Rol')

    class Meta:
        model = usuarioCustom
        fields = ['username', 'run', 'pnombre', 'ap_paterno', 'correo_usuario', 'fecha_nacimiento', 'direccion', 'idComuna', 'idRol']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise ValidationError('El nombre de usuario debe tener al menos 6 caracteres.')
        return username

    def clean_run(self):
        run = self.cleaned_data.get('run')
        if not re.match(r'^\d{7,8}-[\dkK]$', run):
            raise ValidationError('El RUN debe tener el formato 12345678-9.')
        return run

class RegisterUserAdminForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', help_text='Mínimo 6 caracteres')
    run = forms.CharField(label='RUN (Rol Único Nacional)', help_text='Ejemplo: 12345678-9')
    pnombre = forms.CharField(label='Primer Nombre')
    ap_paterno = forms.CharField(label='Apellido Paterno')
    correo_usuario = forms.EmailField(label='Correo electrónico')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento')
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs={'placeholder': 'Calle, número, comuna'}))
    idComuna = forms.ModelChoiceField(queryset=comuna.objects.all(), label='Comuna')
    idRol = forms.ModelChoiceField(queryset=rolUsuario.objects.all(), label='Rol')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='Mínimo 8 caracteres')
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, help_text='Repite la contraseña para confirmar')

    class Meta:
        model = usuarioCustom
        fields = ['username', 'run', 'pnombre', 'ap_paterno', 'correo_usuario', 'fecha_nacimiento', 'direccion', 'idComuna', 'idRol', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise ValidationError('El nombre de usuario debe tener al menos 6 caracteres.')
        return username

    def clean_run(self):
        run = self.cleaned_data.get('run')
        if not re.match(r'^\d{7,8}-[\dkK]$', run):
            raise ValidationError('El RUN debe tener el formato 12345678-9.')
        return run

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        return password2

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', help_text='Mínimo 6 caracteres')
    run = forms.CharField(label='RUN (Rol Único Nacional)', help_text='Ejemplo: 12345678-9')
    pnombre = forms.CharField(label='Primer Nombre')
    ap_paterno = forms.CharField(label='Apellido Paterno')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs={'placeholder': 'Calle, número, comuna'}))
    comuna = forms.ModelChoiceField(queryset=comuna.objects.all(), label='Comuna')

    class Meta:
        model = usuarioCustom
        fields = ['username', 'run', 'correo_usuario', 'pnombre', 'ap_paterno', 'fecha_nacimiento', 'direccion', 'comuna']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise ValidationError('El nombre de usuario debe tener al menos 6 caracteres.')
        return username

    def clean_run(self):
        run = self.cleaned_data.get('run')
        if not re.match(r'^\d{7,8}-[\dkK]$', run):
            raise ValidationError('El RUN debe tener el formato 12345678-9.')
        return run

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(
        label=_("Correo Electrónico"),
        widget=forms.EmailInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _(
            "Por favor, ingrese un %(username)s y contraseña correctos. Note que ambos campos pueden ser sensibles a mayúsculas."
        ),
        'inactive': _("Esta cuenta está inactiva."),
    }

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

# FORM CRUD PRODUCTOS (AÑADIR, ACTUALIZAR):
class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'
        labels = {
            'nombreProducto': 'Nombre del Producto',
            'precioProducto': 'Precio del Producto',
            'stockProducto': 'Stock del Producto',
            'imagenProducto': 'Imagen del Producto',
            'descripcionProducto': 'Descripción del Producto',
            'idcategoriaProducto': 'Categoría del Producto',
            'idMarca': 'Marca del Producto',
        }
        widgets = {
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'precioProducto': forms.NumberInput(attrs={'class': 'form-control'}),
            'stockProducto': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagenProducto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcionProducto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'idcategoriaProducto': forms.Select(attrs={'class': 'form-control'}),
            'idMarca': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_precioProducto(self):
        precioProducto = self.cleaned_data.get('precioProducto')
        if precioProducto <= 0:
            raise ValidationError('El precio del producto debe ser mayor a 0.')
        return precioProducto

    def clean_stockProducto(self):
        stockProducto = self.cleaned_data.get('stockProducto')
        if stockProducto < 0:
            raise ValidationError('El stock del producto no puede ser negativo.')
        return stockProducto

class SeguimientoForm(forms.Form):
    numero_orden = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "INGRESE NÚMERO DE PEDIDO"}))
    numero_orden.widget.attrs['class'] = 'text-center'
    numero_orden.label = ''

    def clean_numero_orden(self):
        numero_orden = self.cleaned_data.get('numero_orden')
        if not numero_orden.isdigit():
            raise ValidationError('El número de orden debe contener solo dígitos.')
        return numero_orden

ESTADOS_PEDIDO = [
    ('', ''),
    ('EN PREPARACIÓN', 'EN PREPARACIÓN'),
    ('LISTO PARA ENVÍO', 'LISTO PARA ENVÍO'),
    ('EN REPARTO', 'EN REPARTO'),
    ('ENTREGADO', 'ENTREGADO'),
]

class EstadoPedido(forms.Form):
    pedido_numero = forms.CharField(widget=forms.HiddenInput())
    estado = forms.ChoiceField(choices=ESTADOS_PEDIDO)

class EnvioDomicilioForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    direccion = forms.CharField(max_length=255, required=True)
    region = forms.ModelChoiceField(queryset=region.objects.all(), required=True)
    comuna = forms.ModelChoiceField(queryset=comuna.objects.all(), required=True)
    correo = forms.EmailField()

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise ValidationError('El nombre debe contener solo letras.')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido.isalpha():
            raise ValidationError('El apellido debe contener solo letras.')
        return apellido

class RetiroTiendaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    run = forms.CharField(max_length=20, required=True)

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise ValidationError('El nombre debe contener solo letras.')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido.isalpha():
            raise ValidationError('El apellido debe contener solo letras.')
        return apellido

    def clean_run(self):
        run = self.cleaned_data.get('run')
        if not re.match(r'^\d{7,8}-[\dkK]$', run):
            raise ValidationError('El RUN debe tener el formato 12345678-9.')
        return run

class UsuarioCustomForm(forms.ModelForm):
    class Meta:
        model = usuarioCustom
        fields = ['username', 'run', 'pnombre', 'ap_paterno', 'correo_usuario', 'fecha_nacimiento', 'direccion', 'idComuna']
        labels = {
            'username': 'Nombre de usuario',
            'run': 'Run',
            'pnombre': 'Nombre',
            'ap_paterno': 'Apellido',
            'correo_usuario': 'Correo',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'direccion': 'Dirección',
            'idComuna': 'Comuna',
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6:
            raise ValidationError('El nombre de usuario debe tener al menos 6 caracteres.')
        return username

    def clean_run(self):
        run = self.cleaned_data.get('run')
        if not re.match(r'^\d{7,8}-[\dkK]$', run):
            raise ValidationError('El RUN debe tener el formato 12345678-9.')
        return run

class CheckoutForm(forms.ModelForm):
    metodo_pago = forms.ChoiceField(choices=[('paypal', 'PayPal'), ('transferencia', 'Transferencia Bancaria')], widget=forms.Select())
    comprobante_pago = forms.ImageField(required=False)

    class Meta:
        model = Pedido
        fields = ['tipo_entrega', 'direccion', 'region', 'comuna', 'nombre', 'apellido', 'run', 'correo', 'sucursal', 'metodo_pago', 'comprobante_pago']

    def clean(self):
        cleaned_data = super().clean()
        metodo_pago = cleaned_data.get('metodo_pago')

        if metodo_pago == 'transferencia' and not self.cleaned_data.get('comprobante_pago'):
            raise ValidationError('Debe subir un comprobante de pago para la transferencia bancaria.')
        
        return cleaned_data
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SucursalForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    code = forms.IntegerField(label='Número')


class VendedorForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    area = forms.CharField(max_length=40, label='Area')


class ProductosForm (forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre del producto')
    due_date = forms.DateField(
        label='Fecha de elaboracion',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    is_delivered = forms.BooleanField(label='Entregado', required=False)


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

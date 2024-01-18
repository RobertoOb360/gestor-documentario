from django import forms
from .models import solicitud,usuario,docs,formatos,revision
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = solicitud
        fields = ('empresa', 'ruc', 'correo', 'telefono', 'lugar', 'destinatario', 'puesto', 'voucher')
        widgets = {
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'voucher': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['foto']

class DocsForm(forms.ModelForm):
    class Meta:
        model = docs
        fields = ['nombre','file']
        widgets={
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class FormatoForm(forms.ModelForm):
    class Meta:
        model = formatos
        fields = ['file']
        widgets={
            'file': forms.FileInput(attrs={'class': 'form-control'})
        }

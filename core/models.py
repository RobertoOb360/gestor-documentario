from django.db import models

class usuario(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    dni=models.CharField(max_length=10)
    codigo=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=12)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=255)
    rol=models.IntegerField()
    ciclo=models.IntegerField(null=True, blank=True)
    foto=models.FileField(upload_to="usuarios/perfiles",null=True, blank=True)
    fechreg=models.DateTimeField(null=True, blank=True)
    fechupdt=models.DateTimeField(null=True, blank=True)
    estado=models.IntegerField()

class solicitud(models.Model):
    cod=models.CharField(max_length=20)
    solicitante=models.ForeignKey(usuario,on_delete=models.CASCADE,null=True, blank=True)
    empresa=models.CharField(max_length=100)
    ruc=models.CharField(max_length=30)
    correo=models.EmailField()
    telefono=models.CharField(max_length=15)
    lugar=models.CharField(max_length=150)
    destinatario=models.CharField(max_length=100)
    puesto=models.CharField(max_length=30)
    voucher=models.FileField(upload_to='usuarios/vouchers',null=True, blank=True)
    fechreg=models.DateField(null=True)
    estado=models.IntegerField()

class carta(models.Model):
    cod=models.CharField(max_length=30)
    solicitud=models.ForeignKey(solicitud,on_delete=models.CASCADE)
    atendido_por=models.ForeignKey(usuario,on_delete=models.CASCADE)
    fecha=models.DateField()

class docs(models.Model):
    cod=models.CharField(max_length=30,null=True, blank=True)
    subido_por=models.ForeignKey(usuario,on_delete=models.CASCADE)
    file=models.FileField(upload_to='repositorio/formatos',null=True, blank=True)
    nombre=models.CharField(max_length=50)
    fechareg=models.DateField(null=True, blank=True)

class formatos(models.Model):
    subido_por=models.ForeignKey(usuario,on_delete=models.CASCADE)
    file=models.FileField(upload_to='usuarios/portafolio',null=True, blank=True)
    nombre=models.CharField(max_length=50)
    fechreg=models.DateField()


class revision(models.Model):
    archivo=models.ForeignKey(formatos,on_delete=models.CASCADE)
    revisado_por=models.ForeignKey(usuario,on_delete=models.CASCADE)
    obs=models.CharField(max_length=500)
    estado=models.IntegerField()

class activities(models.Model):
    descripcion=models.CharField(max_length=100)
    
class activity(models.Model):
    pertenece_a=models.ForeignKey(usuario,on_delete=models.CASCADE)
    detalle=models.ForeignKey(activities,on_delete=models.CASCADE)
    fecha=models.DateTimeField(null=True, blank=True)
    
class empresa(models.Model):
    ruc=models.CharField(max_length=20)
    razon=models.CharField(max_length=60)
    correo=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)
    lugar=models.CharField(max_length=50)
    representante=models.CharField(max_length=100)
    puesto=models.CharField(max_length=30)
    
class practicas(models.Model):
    nombre=models.CharField(max_length=30)

class contrato(models.Model):
    nombre=models.CharField(max_length=30)
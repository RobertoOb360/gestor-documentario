from django.shortcuts import render,redirect,get_object_or_404
from .models import usuario,carta,solicitud,activity,activities,docs,empresa,practicas,contrato,revision,formatos
from .forms import SolicitudForm,UsuarioForm,DocsForm,FormatoForm
from django.http import HttpResponse
from datetime import date,datetime
from django.core.mail import send_mail


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = usuario.objects.filter(username=username, password=password).first()
        if user:
            if user.rol == 1:
                return redirect('perfil1',user_id=user.id) # Reemplaza 'pagina_rol_uno' con el nombre de la URL para el rol 1
            elif user.rol == 2:
                return redirect('perfil2',user_id=user.id)  # Reemplaza 'pagina_rol_dos' con el nombre de la URL para el rol 2
            elif user.rol == 3:
                return redirect('perfil3',user_id=user.id)
        return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})

    else:
        # Método GET, muestra la página de inicio de sesión
        return render(request, 'login.html')

def perfil1(request,user_id):
    user = usuario.objects.get(id=user_id)
    actividad=activities.objects.get(id=22)
    historial=activity.objects.filter(pertenece_a=user).order_by('-id')[:5]
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            hoy=datetime.now()
            activity.objects.create(pertenece_a=user,detalle=actividad,fecha=hoy)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request,'master/master.html', {'user': user,'form': form,'historial':historial})

def perfil2(request,user_id):
    user = usuario.objects.get(id=user_id)
    actividad=activities.objects.get(id=22)
    historial=activity.objects.filter(pertenece_a=user).order_by('-id')[:8]
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            hoy=datetime.now()
            activity.objects.create(pertenece_a=user,detalle=actividad,fecha=hoy)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request,'admin/admin.html', {'user': user,'form': form,'historial':historial})

def perfil3(request,user_id):
    user = usuario.objects.get(id=user_id)
    actividad=activities.objects.get(id=22)
    historial=activity.objects.filter(pertenece_a=user).order_by('-id')[:5]
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            hoy=datetime.now()
            activity.objects.create(pertenece_a=user,detalle=actividad,fecha=hoy)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request,'alumno/alumno.html', {'user': user,'form': form,'historial':historial})

def formatos1(request,user_id):
    user = usuario.objects.get(id=user_id)
    plantillas=docs.objects.all()
    docs_form = DocsForm()
    if request.method == 'POST':
        if 'add_document' in request.POST:
            docs_form = DocsForm(request.POST, request.FILES)

            if docs_form.is_valid():
                doc = docs_form.save(commit=False)
                doc.subido_por_id = user_id
                doc.fechareg = date.today()
                doc.save()
                hoy=datetime.now()
                actividad=activities.objects.get(id=25)
                activity.objects.create(pertenece_a=user,detalle=actividad,fecha=hoy)

        elif 'delete_document' in request.POST:
            doc_id_to_delete = request.POST.get('doc_id_to_delete')
            if doc_id_to_delete:
                docs.objects.filter(id=doc_id_to_delete).delete()
                hoy=datetime.now()
                actividad=activities.objects.get(id=26)
                activity.objects.create(pertenece_a=user,detalle=actividad,fecha=hoy)
    else:
        docs_form = DocsForm()
    return render(request,'admin/cargarFormatos.html', {'user': user,'formatos':plantillas,'docs_form': docs_form})

def formatos2(request,user_id):
    user = usuario.objects.get(id=user_id)
    practica=practicas.objects.all()
    contra=contrato.objects.all()
    for_form=FormatoForm()
    if request.method == 'POST':
        for_form=FormatoForm(request.POST, request.FILES)
        if for_form.is_valid():
            doc = for_form.save(commit=False)
            doc.subido_por=user
            doc.nombre=request.POST.get('nombre')
            doc.fechreg=date.today()
            doc.save()
            hoy=datetime.now()
            actividad=activities.objects.get(id=4)
            activity.objects.create(pertenece_a=user,detalle=actividad,fecha=hoy)
            revisor=usuario.objects.get(id=2)
            revision.objects.create(obs='',estado=1,archivo_id=doc.id,revisado_por=revisor)
            return render(request,'alumno/cargarDocs.html', {'user': user,'practicas':practica,'contratos':contra,'formato_form': for_form,'success':'success'})
    return render(request,'alumno/cargarDocs.html', {'user': user,'practicas':practica,'contratos':contra,'formato_form': for_form})

def cartas(request,user_id):
    user = usuario.objects.get(id=user_id)
    cartas=carta.objects.all()
    solicitudes=solicitud.objects.filter(estado=1)
    return render(request,'admin/generarCarta.html', {'user': user, 'cartas': cartas,'solicitudes':solicitudes})

def cartas2(request,user_id):
    user = usuario.objects.get(id=user_id)
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            ruc=request.POST.get('ruc')
            razon=request.POST.get('empresa')
            correo=request.POST.get('correo')
            telefono=request.POST.get('telefono')
            lugar=request.POST.get('lugar')
            representante=request.POST.get('destinatario')
            puesto=request.POST.get('puesto')
            new_empresa=empresa(ruc=ruc,razon=razon,correo=correo,telefono=telefono,lugar=lugar,representante=representante,puesto=puesto)
            new_empresa.save()
            count=solicitud.objects.count()
            coda=count+1
            cod='0'+str(coda)+'-2024'
            fecha=date.today()
            est=1
            new_solicitud = form.save(commit=False)
            new_solicitud.solicitante = user
            new_solicitud.cod=cod
            new_solicitud.fechreg=fecha
            new_solicitud.estado=est
            new_solicitud.save()
            hoy=datetime.now()
            actividad=activities.objects.get(id=1)
            activity.objects.create(pertenece_a=user,detalle=actividad,fecha=hoy)
            return render(request, 'alumno/solicitarCarta.html', {'form': form,'user': user,'success':'success'})
    else:
        form = SolicitudForm()
    return render(request, 'alumno/solicitarCarta.html', {'form': form,'user': user})

def cartas_crear(request,user_id, solicitud_id):
    user = usuario.objects.get(id=user_id)
    soli=solicitud.objects.get(id=solicitud_id)
    return render(request,'admin/cartaDetalle.html', {'user': user, 'solicitud':soli})

def revisiones(request,user_id,archivo_id):
    user = usuario.objects.get(id=user_id)
    archivos=formatos.objects.filter(subido_por=archivo_id).values('id')
    archivos_pendientes=[]
    for archivo in archivos:
        id_archivo=archivo['id']
        print(id_archivo)
    print(archivos)
    if request.method == 'POST':
        estado=request.POST.get('estado')
        obs=request.POST.get('obs')
        id=request.POST.get('id')
        archivo_rev=get_object_or_404(revision, archivo_id=id)
        archivo_rev.estado = estado
        archivo_rev.obs = obs
        archivo_rev.save()
        return render(request,'admin/ArchivoDetalle.html', {'user': user, 'archivos':archivos,'success':'success'})
    return render(request,'admin/ArchivoDetalle.html', {'user': user, 'archivos':archivos})


def reportes(request,user_id):
    user = usuario.objects.get(id=user_id)
    cantObs=revision.objects.filter(estado=2).count()
    cantProc=revision.objects.filter(estado=1).count()
    cantSucc=revision.objects.filter(estado=3).count()
    cantAdm=usuario.objects.filter(rol=1).count()
    cantOfi=usuario.objects.filter(rol=2).count()
    cantEst=usuario.objects.filter(rol=3).count()
    return render(request,'admin/reporteAlumnos.html', {'user': user,'obs':cantObs,'proc':cantProc,'succ':cantSucc,'admi':cantAdm,'ofi':cantOfi,'est':cantEst})

def reportes2(request,user_id):
    user = usuario.objects.get(id=user_id)
    revisiones=revision.objects.filter(archivo__subido_por__id=user_id)
    print(revisiones)
    return render(request,'alumno/miHistorial.html', {'user': user,'archivos':revisiones})

def repositorio(request,user_id):
    user = usuario.objects.get(id=user_id)
    revisiones_distintas = revision.objects.values('archivo__subido_por').distinct()
    usuarios_distintos = []
    for revision_distinta  in revisiones_distintas:
        subido_por = revision_distinta['archivo__subido_por']
        usuario_obj = usuario.objects.get(id=subido_por)
        usuarios_distintos.append(usuario_obj)
        print(usuario_obj.nombres)
    return render(request, 'admin/verDocs.html', {'user': user, 'revisiones_distintas': usuarios_distintos})

def repositorio2(request,user_id):
    user = usuario.objects.get(id=user_id)
    plantillas=docs.objects.all()
    return render(request,'alumno/InfoDocs.html', {'user': user,'formatos':plantillas})

def usuarios(request,user_id):
    user = usuario.objects.get(id=user_id)
    usuarios=usuario.objects.all()
    return render(request,'master/usuarios.html', {'user': user,'usuarios':usuarios})

def empresas(request,user_id):
    user = usuario.objects.get(id=user_id)
    empresas_distintas = empresa.objects.values('ruc').distinct()
    empresas=empresa.objects.filter(ruc__in=empresas_distintas)
    return render(request,'master/empresas.html', {'user': user,'empresas':empresas})

def seguimiento(request,user_id):
    user = usuario.objects.get(id=user_id)
    actividades=activity.objects.all()
    return render(request,'master/seguimiento.html', {'user': user,'actividades':actividades})

def archivos(request,user_id):
    user = usuario.objects.get(id=user_id)
    documentos=formatos.objects.all()
    return render(request,'master/archivos.html', {'user': user,'docs':documentos})





            
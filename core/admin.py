from django.contrib import admin
from .models import usuario,solicitud,activities,activity,carta,docs

# Register your models here.
admin.site.register(usuario)
admin.site.register(solicitud)
admin.site.register(activities)
admin.site.register(activity)
admin.site.register(carta)
admin.site.register(docs)



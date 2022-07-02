from django.contrib import admin
from .models import Ciudad, Cliente, DetallePago, Pago
from .models import Cobro, FichaInscripcion
# Register your models he
admin.site.register(Cliente)
admin.site.register(Cobro)
admin.site.register(Ciudad)
admin.site.register(FichaInscripcion)
admin.site.register(Pago)
admin.site.register(DetallePago)
from django.contrib import admin
from .models import Producto
from .models import Usuario
from .models import Comentario

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Comentario)

# Register your models here.

from django.contrib import admin
from .models import Contacto, Marca, Producto
from .forms import ProductoForm

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo","marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]
    list_per_page = 10
    form = ProductoForm

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)

# Register your models here.

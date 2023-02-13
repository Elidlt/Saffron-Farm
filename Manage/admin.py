from django.contrib import admin

# Register your models here.
from .models import Worker,ResDay,Buyers

admin.site.register(Worker)
admin.site.register(ResDay)
admin.site.register(Buyers)

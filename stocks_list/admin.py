from django.contrib import admin
from .models import Users,Stock,Query

# Register your models here.
admin.site.register(Users)
admin.site.register(Stock)
admin.site.register(Query)


from django.contrib import admin
from core.models import Deal


class DealAdmin(admin.ModelAdmin):
    pass

admin.site.register(Deal,DealAdmin)

# Register your models here.

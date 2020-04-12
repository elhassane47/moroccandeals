from django.contrib import admin
from core.models import Deal, Location, Category


class DealAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Deal,DealAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Category,CategoryAdmin)

# Register your models here.

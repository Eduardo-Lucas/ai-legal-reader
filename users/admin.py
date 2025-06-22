from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import CustomUser

class CustomerUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
        

class CustomUserAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'is_staff', 'is_active')

    resource_classes = [CustomerUserResource]

admin.site.register(CustomUser, CustomUserAdmin)

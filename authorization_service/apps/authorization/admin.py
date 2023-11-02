from django.contrib import admin
from .models import Role, Authorization

# Register your models here.

class RoleAdmin(admin.ModelAdmin):  # Use admin.ModelAdmin here
    list_display = ('name', 'description', 'created', 'updated')
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_filter = ('created', 'updated')

class AuthorizationAdmin(admin.ModelAdmin):  # Use admin.ModelAdmin here
    list_display = ('group_name', 'role', 'satellite_code', 'description', 'created', 'updated')
    search_fields = ('group_name', 'role', 'satellite_code', 'description')
    ordering = ('group_name',)
    list_filter = ('created', 'updated')

# Register the models with the admin site
admin.site.register(Role, RoleAdmin)
admin.site.register(Authorization, AuthorizationAdmin)

from django.contrib import admin
from .models import Fuel, oil

class baksAdmin(admin.ModelAdmin):
    list_display = ['plate_number', 'Date']

admin.site.register(Fuel, baksAdmin)
admin.site.register(oil, baksAdmin)

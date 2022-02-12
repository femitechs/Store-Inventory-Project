from django.contrib import admin
from .models import Inventories


# Register your models here.

@admin.register(Inventories)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('seq_number', 'id', 'equipment_name', 'slug', 'serial_number', 'entry', 'status')
    list_filter = ('status', 'date_added', 'entry', 'manager',)
    search_fields = ('equipment_name',)
    prepopulated_fields = {'slug': ('equipment_name',),}
    raw_id_field = ('manager')
    date_hierarchy = 'entry'
    ordering = ('status', 'entry')
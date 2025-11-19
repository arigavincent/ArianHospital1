from django.contrib import admin
from .models import Department, Doctor, ContactInfo


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'head', 'contact', 'order')
	search_fields = ('name', 'head')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'title', 'phone', 'email', 'order')
	search_fields = ('full_name', 'title')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
	list_display = ('site_name', 'phone', 'email', 'order')
	ordering = ('order',)

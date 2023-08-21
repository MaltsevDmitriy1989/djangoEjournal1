from django.contrib import admin
from mediacontent.models import EducationProgramm, Sports
# Register your models here.

@admin.register(EducationProgramm)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'studyduration', 'modeofstudy', 'degree', 'fieldofstudy')
    fields = ('name', 'studyduration', 'modeofstudy', 'degree', 'image', 'fieldofstudy')
    # readonly_fields = ('description',)
    search_fields = ('name', )
    ordering = ('name', )

@admin.register(Sports)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'description')
    fields = ('name', 'level', 'description', 'image')
    # readonly_fields = ('description',)
    search_fields = ('name', )
    ordering = ('name', )
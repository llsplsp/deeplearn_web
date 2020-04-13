from django.contrib import admin

from deeplearn.models import speciesRecognition

class sepciesAdmin(admin.ModelAdmin):
    list_display = ("id", 'data_photo','created',)
    list_filter = ("created",)
    ordering = ["-created"]

admin.site.register(speciesRecognition,sepciesAdmin)

# Register your models here.

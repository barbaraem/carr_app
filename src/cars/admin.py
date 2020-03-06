from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Car


@admin.register(Car)
class CarAdmin(ImportExportModelAdmin):
    pass

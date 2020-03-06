from departments.models import Department
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import Car


class CarResource(resources.ModelResource):
    department = fields.Field(
        column_name="department",
        attribute="department",
        widget=ForeignKeyWidget(Department,"short_name")
    )

    class Meta:
        model = Car
        fields = (
            "id",
            "registration_no",
            "brand",
            "model",
            "passengers_no",
            "weight",
            "production_date",
            "department",
        )

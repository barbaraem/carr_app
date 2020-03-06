from import_export import resources

from .models import Car


class CarResource(resources.ModelResource):
    class Meta:
        model = Car
        fields = ("id", "department__short_name", "brand", "registration_no")

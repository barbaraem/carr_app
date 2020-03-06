from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _


from rest_framework import status
from rest_framework.decorators import api_view
from tablib import Dataset, core

from .imports import import_process
from .resources import CarResource


@csrf_exempt
def upload_csv(request):
    if request.method == "POST":
        car_resource = CarResource()
        dataset = Dataset()
        new_cars = request.FILES["file"]
        try:
            dataset.load(new_cars.read().decode("utf-8"), format="csv")
        except core.InvalidDimensions:
            return HttpResponse(
                _("Your csv file is incorrect."), status=status.HTTP_400_BAD_REQUEST
            )
        try:
            result = car_resource.import_data(dataset, dry_run=True, raise_errors=True)
        except Exception as e:
            return HttpResponse(e, status=status.HTTP_406_NOT_ACCEPTABLE)
        if not result.has_errors():
            car_resource.import_data(dataset, dry_run=False)
            return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["POST"])
@csrf_exempt
def custom_upload_csv(request):
    if request.method == "POST":
        file = request.FILES["file"]
        file_name = default_storage.save(file.name, file)
        return HttpResponse(import_process(file_name))
    return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

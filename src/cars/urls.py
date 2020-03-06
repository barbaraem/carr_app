from django.urls import path

from .views import upload_csv, custom_upload_csv

urlpatterns = [
    path("import/", upload_csv),
    path("custom_import/", custom_upload_csv)
]

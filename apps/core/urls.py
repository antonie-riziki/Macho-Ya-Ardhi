from django.urls import path
from .views import verify_page, verify_land, report_detail

urlpatterns = [
    path("", verify_page, name="verify_page"),
    path("verify/", verify_page, name="verify_page_alt"),
    path("api/verify-land/", verify_land, name="verify_land"),
    path("api/report/<int:report_id>/", report_detail, name="report_detail"),
]

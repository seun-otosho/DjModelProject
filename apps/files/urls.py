from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("submission", api.submissionViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("files/submission/", views.submissionListView.as_view(), name="files_submission_list"),
    path("files/submission/create/", views.submissionCreateView.as_view(), name="files_submission_create"),
    path("files/submission/detail/<int:pk>/", views.submissionDetailView.as_view(), name="files_submission_detail"),
    path("files/submission/update/<int:pk>/", views.submissionUpdateView.as_view(), name="files_submission_update"),
)

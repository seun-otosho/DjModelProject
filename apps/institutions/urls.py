from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Institution", api.InstitutionViewSet)
router.register("InstitutionCategory", api.InstitutionCategoryViewSet)
router.register("InstitutionOwnership", api.InstitutionOwnershipViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("institutions/Institution/", views.InstitutionListView.as_view(), name="institutions_Institution_list"),
    path("institutions/Institution/create/", views.InstitutionCreateView.as_view(), name="institutions_Institution_create"),
    path("institutions/Institution/detail/<int:pk>/", views.InstitutionDetailView.as_view(), name="institutions_Institution_detail"),
    path("institutions/Institution/update/<int:pk>/", views.InstitutionUpdateView.as_view(), name="institutions_Institution_update"),
    path("institutions/InstitutionCategory/", views.InstitutionCategoryListView.as_view(), name="institutions_InstitutionCategory_list"),
    path("institutions/InstitutionCategory/create/", views.InstitutionCategoryCreateView.as_view(), name="institutions_InstitutionCategory_create"),
    path("institutions/InstitutionCategory/detail/<int:pk>/", views.InstitutionCategoryDetailView.as_view(), name="institutions_InstitutionCategory_detail"),
    path("institutions/InstitutionCategory/update/<int:pk>/", views.InstitutionCategoryUpdateView.as_view(), name="institutions_InstitutionCategory_update"),
    path("institutions/InstitutionOwnership/", views.InstitutionOwnershipListView.as_view(), name="institutions_InstitutionOwnership_list"),
    path("institutions/InstitutionOwnership/create/", views.InstitutionOwnershipCreateView.as_view(), name="institutions_InstitutionOwnership_create"),
    path("institutions/InstitutionOwnership/detail/<int:pk>/", views.InstitutionOwnershipDetailView.as_view(), name="institutions_InstitutionOwnership_detail"),
    path("institutions/InstitutionOwnership/update/<int:pk>/", views.InstitutionOwnershipUpdateView.as_view(), name="institutions_InstitutionOwnership_update"),
)

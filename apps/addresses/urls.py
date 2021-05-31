from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("StreetAddress", api.StreetAddressViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("addresses/StreetAddress/", views.StreetAddressListView.as_view(), name="addresses_StreetAddress_list"),
    path("addresses/StreetAddress/create/", views.StreetAddressCreateView.as_view(), name="addresses_StreetAddress_create"),
    path("addresses/StreetAddress/detail/<int:pk>/", views.StreetAddressDetailView.as_view(), name="addresses_StreetAddress_detail"),
    path("addresses/StreetAddress/update/<int:pk>/", views.StreetAddressUpdateView.as_view(), name="addresses_StreetAddress_update"),
)

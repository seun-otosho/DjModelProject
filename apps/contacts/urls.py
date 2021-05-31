from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("ContactDetail", api.ContactDetailViewSet)
router.register("ContactCategory", api.ContactCategoryViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("contacts/ContactDetail/", views.ContactDetailListView.as_view(), name="contacts_ContactDetail_list"),
    path("contacts/ContactDetail/create/", views.ContactDetailCreateView.as_view(), name="contacts_ContactDetail_create"),
    path("contacts/ContactDetail/detail/<int:pk>/", views.ContactDetailDetailView.as_view(), name="contacts_ContactDetail_detail"),
    path("contacts/ContactDetail/update/<int:pk>/", views.ContactDetailUpdateView.as_view(), name="contacts_ContactDetail_update"),
    path("contacts/ContactCategory/", views.ContactCategoryListView.as_view(), name="contacts_ContactCategory_list"),
    path("contacts/ContactCategory/create/", views.ContactCategoryCreateView.as_view(), name="contacts_ContactCategory_create"),
    path("contacts/ContactCategory/detail/<int:pk>/", views.ContactCategoryDetailView.as_view(), name="contacts_ContactCategory_detail"),
    path("contacts/ContactCategory/update/<int:pk>/", views.ContactCategoryUpdateView.as_view(), name="contacts_ContactCategory_update"),
)

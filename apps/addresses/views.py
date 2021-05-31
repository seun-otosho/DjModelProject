from django.views import generic
from . import models
from . import forms


class StreetAddressListView(generic.ListView):
    model = models.StreetAddress
    form_class = forms.StreetAddressForm


class StreetAddressCreateView(generic.CreateView):
    model = models.StreetAddress
    form_class = forms.StreetAddressForm


class StreetAddressDetailView(generic.DetailView):
    model = models.StreetAddress
    form_class = forms.StreetAddressForm


class StreetAddressUpdateView(generic.UpdateView):
    model = models.StreetAddress
    form_class = forms.StreetAddressForm
    pk_url_kwarg = "pk"

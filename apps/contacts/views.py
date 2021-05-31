from django.views import generic
from . import models
from . import forms


class ContactDetailListView(generic.ListView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm


class ContactDetailCreateView(generic.CreateView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm


class ContactDetailDetailView(generic.DetailView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm


class ContactDetailUpdateView(generic.UpdateView):
    model = models.ContactDetail
    form_class = forms.ContactDetailForm
    pk_url_kwarg = "pk"


class ContactCategoryListView(generic.ListView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm


class ContactCategoryCreateView(generic.CreateView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm


class ContactCategoryDetailView(generic.DetailView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm


class ContactCategoryUpdateView(generic.UpdateView):
    model = models.ContactCategory
    form_class = forms.ContactCategoryForm
    pk_url_kwarg = "pk"

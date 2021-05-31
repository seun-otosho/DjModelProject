from django.views import generic
from . import models
from . import forms


class InstitutionListView(generic.ListView):
    model = models.Institution
    form_class = forms.InstitutionForm


class InstitutionCreateView(generic.CreateView):
    model = models.Institution
    form_class = forms.InstitutionForm


class InstitutionDetailView(generic.DetailView):
    model = models.Institution
    form_class = forms.InstitutionForm


class InstitutionUpdateView(generic.UpdateView):
    model = models.Institution
    form_class = forms.InstitutionForm
    pk_url_kwarg = "pk"


class InstitutionCategoryListView(generic.ListView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm


class InstitutionCategoryCreateView(generic.CreateView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm


class InstitutionCategoryDetailView(generic.DetailView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm


class InstitutionCategoryUpdateView(generic.UpdateView):
    model = models.InstitutionCategory
    form_class = forms.InstitutionCategoryForm
    pk_url_kwarg = "pk"


class InstitutionOwnershipListView(generic.ListView):
    model = models.InstitutionOwnership
    form_class = forms.InstitutionOwnershipForm


class InstitutionOwnershipCreateView(generic.CreateView):
    model = models.InstitutionOwnership
    form_class = forms.InstitutionOwnershipForm


class InstitutionOwnershipDetailView(generic.DetailView):
    model = models.InstitutionOwnership
    form_class = forms.InstitutionOwnershipForm


class InstitutionOwnershipUpdateView(generic.UpdateView):
    model = models.InstitutionOwnership
    form_class = forms.InstitutionOwnershipForm
    pk_url_kwarg = "pk"

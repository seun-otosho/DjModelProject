from django.views import generic
from . import models
from . import forms


class submissionListView(generic.ListView):
    model = models.submission
    form_class = forms.submissionForm


class submissionCreateView(generic.CreateView):
    model = models.submission
    form_class = forms.submissionForm


class submissionDetailView(generic.DetailView):
    model = models.submission
    form_class = forms.submissionForm


class submissionUpdateView(generic.UpdateView):
    model = models.submission
    form_class = forms.submissionForm
    pk_url_kwarg = "pk"

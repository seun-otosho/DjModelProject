from django.views import generic
from . import models
from . import forms


class CommentListView(generic.ListView):
    model = models.Comment
    form_class = forms.CommentForm


class CommentCreateView(generic.CreateView):
    model = models.Comment
    form_class = forms.CommentForm


class CommentDetailView(generic.DetailView):
    model = models.Comment
    form_class = forms.CommentForm


class CommentUpdateView(generic.UpdateView):
    model = models.Comment
    form_class = forms.CommentForm
    pk_url_kwarg = "pk"

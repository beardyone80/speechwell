from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Disorder


class DisorderListView(ListView):
    model = Disorder
    template_name = 'disorder_list.html'
    context_object_name = 'disorders'


class DisorderDetailView(DetailView):
    model = Disorder
    template_name = 'disorder_detail.html'
    context_object_name = 'disorder'
    slug_field = 'slug'

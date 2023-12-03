from django.views.generic import ListView
from .models import Disorder

class DisorderListView(ListView):
    model = Disorder
    template_name = 'disorder_list.html'
    context_object_name = 'disorders'
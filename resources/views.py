from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Therapist

# Create your views here.
class TherapistListView(View):
    def get(self, request):
        therapists = Therapist.objects.all()
        return render(request, 'therapist_list.html', {'therapists': therapists})

class TherapistByLocationListView(ListView):
    model = Therapist
    template_name = 'therapists_by_location.html'
    context_object_name = 'therapists'

    def get_queryset(self):
        location = self.kwargs['location']
        return Therapist.objects.filter(location=location)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = self.kwargs['location']
        return context
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, FormView, DeleteView
from .models import Therapist
from django.views.generic.edit import CreateView
from .forms import TherapistForm
from django.urls import reverse_lazy





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


class TherapistRegistrationView(FormView):
    template_name = 'therapist_form.html'
    form_class = TherapistForm
    success_url = reverse_lazy('therapist_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

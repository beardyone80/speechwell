from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class TherapistRegistrationView(UserPassesTestMixin, FormView):
    template_name = 'therapist_form.html'
    form_class = TherapistForm
    success_url = reverse_lazy('therapist_list')

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # Customize behavior when the user doesn't have permission (redirect, show error, etc.)
        # Here, redirecting to a different page or displaying an error message
        return HttpResponseForbidden("You don't have permission to access this page. Please contact site admin if you wish to register as a therapist.")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

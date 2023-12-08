from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, FormView, UpdateView, TemplateView
from .models import Therapist
from .forms import TherapistForm, TherapistUpdateForm
from django.urls import reverse_lazy, reverse


# Create your views here.

# Display all therapists in database
class TherapistListView(View):
    def get(self, request):
        therapists = Therapist.objects.all()
        return render(
            request, 'therapist_list.html', {'therapists': therapists}
            )


# Display therapists by location using location value
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


# Form to register as a therapist- SU only
class TherapistRegistrationView(UserPassesTestMixin, FormView):
    template_name = 'therapist_form.html'
    form_class = TherapistForm
    success_url = reverse_lazy('therapist_list')

    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.is_staff

    # def handle_no_permission(self):
    #     # Error message if user is not superuser
    #     return HttpResponseForbidden(
    #         "You don't have permission to access this page."
    #         "Please contact site admin if you wish to register as a therapist."
    #         )
    def handle_no_permission(self):
        error_message = (
            "You don't have permission to access this page. "
            "Please contact the site admin if you wish to register "
            "as a therapist."
        )

        go_back_url = reverse('therapist_registration')

        return render(self.request, 'error_template.html', {
            'error_message': error_message,
            'go_back_url': go_back_url,
        })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Confirm deletion of therapist
class ConfirmDeleteTherapistView(TemplateView):
    template_name = 'confirm_delete_therapist.html'

    def get_context_data(self, **kwargs):
        username = kwargs['username']
        therapist = get_object_or_404(Therapist, username=username)
        return {'therapist': therapist}


# Delete therapist record from database
class DeleteTherapistView(View):
    def post(self, request, username):
        therapist = get_object_or_404(Therapist, username=username)
        if 'confirm_delete' in request.POST:
            therapist.delete()
        return redirect('therapist_list')


# Form to update current therapist record
class TherapistUpdateView(UpdateView):
    model = Therapist
    form_class = TherapistUpdateForm
    template_name = 'therapist_update.html'
    success_url = reverse_lazy('therapist_list')

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(Therapist, username=username)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        instance = self.get_object()
        kwargs['instance'] = instance
        return kwargs

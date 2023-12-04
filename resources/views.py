from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .models import Therapist
from django.views.generic.edit import CreateView
from .forms import TherapistForm, TherapistUpdateForm
from django.urls import reverse_lazy, reverse


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


# class DeleteTherapistView(View):
#     def post(self, request, username):
#         therapist = get_object_or_404(Therapist, username=username)
#         therapist.delete()
#         return HttpResponseRedirect(reverse('therapist_list'))

class DeleteTherapistView(View):
    def post(self, request, username):
        therapist = get_object_or_404(Therapist, username=username)
        return render(request, 'confirm_delete_therapist.html', {'therapist': therapist})        




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
        instance = self.get_object()  # Retrieve the instance here
        kwargs['instance'] = instance
        print(instance.username)  # Print some attributes of the instance for debugging
        print(instance.email)  # Example: Print the email field  # Pass the instance to the form
        return kwargs

# class TherapistUpdateView(UpdateView):
#     model = Therapist
#     form_class = TherapistUpdateForm
#     template_name = 'therapist_update.html'
#     success_url = reverse_lazy('therapist_list')

#     def get_object(self, queryset=None):
#         username = self.kwargs.get('username')
#         return get_object_or_404(Therapist, username=username)

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         instance = self.get_object()  # Retrieve the instance here
#         kwargs['instance'] = instance  # Pass the instance to the form
#         return kwargs        
        
# class TherapistUpdateView(UpdateView):
#     model = Therapist
#     form_class = TherapistUpdateForm
#     template_name = 'therapist_update.html'  # Template to render the update form
#     success_url = reverse_lazy('therapist_list')  # Replace 'therapists_list' with your list view name

#     def get_object(self, queryset=None):
#         username = self.kwargs.get('username')
#         return get_object_or_404(Therapist, username=username)

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['instance'] = self.get_object()  # Pass the instance of the therapist to the form
#         return kwargs

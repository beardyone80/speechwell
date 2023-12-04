from django import forms
from .models import Therapist


class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['username', 'email', 'profile_pic', 'phone_number', 'address', 'bio', 'location', 'specialty']



from django import forms
from .models import Therapist
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['username', 'email', 'profile_pic', 'phone_number', 'address', 'bio', 'location', 'specialty']

class TherapistUpdateForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['username', 'email', 'profile_pic', 'phone_number', 'address', 'bio', 'location', 'specialty']

    def __init__(self, *args, **kwargs):
        super(TherapistUpdateForm, self).__init__(*args, **kwargs)
        
        # Iterate through fields and set placeholders
        for field_name, field in self.fields.items():
            if field_name == 'profile_pic':
                # You might not need a placeholder for an image field
                continue

            current_value = self.instance.__dict__.get(field_name)
            if current_value:
                field.widget.attrs['placeholder'] = current_value


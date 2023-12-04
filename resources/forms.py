from django import forms
from .models import Therapist
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['username', 'email', 'profile_pic', 'phone_number', 'address', 'bio', 'location', 'specialty']


# class TherapistUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Therapist
#         fields = ['username', 'email', 'profile_pic', 'phone_number', 'address', 'bio', 'location', 'specialty']


class TherapistUpdateForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['username', 'email', 'profile_pic', 'phone_number', 'address', 'bio', 'location', 'specialty']


# I wasn't able to get the update form fields
# prepopulated

    # def __init__(self, *args, **kwargs):
    #     super(TherapistUpdateForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Update'))

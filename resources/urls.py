from django.urls import path
from .views import TherapistListView
from .views import TherapistByLocationListView, TherapistRegistrationView

urlpatterns = [
    path('therapists/', TherapistListView.as_view(), name='therapist_list'),
    path('therapists/<str:location>/', TherapistByLocationListView.as_view(), name='therapists_by_location'),
    path('therapist/add/', TherapistRegistrationView.as_view(), name='therapist_registration'),
]
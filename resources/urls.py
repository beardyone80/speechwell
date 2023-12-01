from django.urls import path
from .views import TherapistListView

urlpatterns = [
    path('therapists/', TherapistListView.as_view(), name='therapist_list'),
]
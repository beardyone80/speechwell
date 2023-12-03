from django.urls import path
from .views import TherapistListView
from .views import TherapistByLocationListView

urlpatterns = [
    path('therapists/', TherapistListView.as_view(), name='therapist_list'),
    path('therapists/<str:location>/', TherapistByLocationListView.as_view(), name='therapists_by_location'),
]
from django.urls import path
from .views import (
                    TherapistListView, TherapistByLocationListView,
                    TherapistRegistrationView, DeleteTherapistView,
                    TherapistUpdateView, ConfirmDeleteTherapistView
                    )

urlpatterns = [
    path('therapists/', TherapistListView.as_view(), name='therapist_list'),
    path(
        'therapists/<str:location>/', TherapistByLocationListView.as_view(),
        name='therapists_by_location'
        ),
    path(
        'therapist/add/', TherapistRegistrationView.as_view(),
        name='therapist_registration'
        ),
    path(
        'update/<str:username>/', TherapistUpdateView.as_view(),
        name='update_therapist'
        ),
    path(
        'therapist/confirm_delete/<str:username>/',
        ConfirmDeleteTherapistView.as_view(), name='confirm_delete_therapist'
        ),
    path(
        'therapist/delete/<str:username>/', DeleteTherapistView.as_view(),
        name='delete_therapist'
        ),
]

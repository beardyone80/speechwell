from django.urls import path
from .views import DisorderListView

urlpatterns = [
    path('disorders/', DisorderListView.as_view(), name='disorder-list'),
]
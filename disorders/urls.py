from django.urls import path
from .views import DisorderListView, DisorderDetailView

urlpatterns = [
    path('disorders/', DisorderListView.as_view(), name='disorder-list'),
    path('disorders/', DisorderDetailView.as_view(), name='disorder-detail'),
]
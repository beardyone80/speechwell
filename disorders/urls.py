from django.urls import path
from .views import DisorderListView, DisorderDetailView, AddCommentView, DeleteCommentView

urlpatterns = [
    path('disorders/', DisorderListView.as_view(), name='disorder-list'),
    path('disorders/', DisorderDetailView.as_view(), name='disorder-detail'),
    path('disorder/<int:disorder_id>/comment/add/', AddCommentView.as_view(), name='add_comment'),
    path('disorder/<int:disorder_id>/comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]
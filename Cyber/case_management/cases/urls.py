from django.urls import path
from .views import CaseListCreateView, CaseRetrieveUpdateDeleteView

urlpatterns = [
    path('cases/', CaseListCreateView.as_view(), name='case-list-create'),
    path('cases/<int:pk>/', CaseRetrieveUpdateDeleteView.as_view(), name='case-detail'),
]

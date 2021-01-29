from django.urls import path
from .views import AdvanceCreateView, AdvanceDeleteView, AdvanceDetailView, AdvanceUpdateView, AdvanceListView

app_name = 'advance'

urlpatterns = [
    path('', AdvanceListView.as_view(), name='advance'),
    path('advance-create/', AdvanceCreateView.as_view(), name='advance-create'),
    path('advance-detail/<uuid:uuid>', AdvanceDetailView.as_view(), name='advance-detail'),
    path('advance-update/<uuid:uuid>', AdvanceUpdateView.as_view(), name='advance-update'),
    path('advance-delete/<uuid:uuid>', AdvanceDeleteView.as_view(), name= 'advance-delete' ),
]
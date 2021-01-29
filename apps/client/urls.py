from django.urls import path
from .views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientUpdateView, ClientListView

app_name = 'client'

urlpatterns = [
    path('', ClientListView.as_view(), name='client'),
    path('client-create/', ClientCreateView.as_view(), name='client-create'),
    path('client-detail/<uuid:uuid>', ClientDetailView.as_view(), name='client-detail'),
    path('client-update/<uuid:uuid>', ClientUpdateView.as_view(), name='client-update'),
    path('client-delete/<uuid:uuid>', ClientDeleteView.as_view(), name= 'client-delete' ),
]
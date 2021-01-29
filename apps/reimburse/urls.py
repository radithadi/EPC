from django.urls import path
from .views import ReimburseCreateView, ReimburseDeleteView, ReimburseDetailView, ReimburseUpdateView, ReimburseListView

app_name = 'reimburse'

urlpatterns = [
    path('', ReimburseListView.as_view(), name='reimburse'),
    path('reimburse-create/', ReimburseCreateView.as_view(), name='reimburse-create'),
    path('reimburse-detail/<uuid:uuid>', ReimburseDetailView.as_view(), name='reimburse-detail'),
    path('reimburse-update/<uuid:uuid>', ReimburseUpdateView.as_view(), name='reimburse-update'),
    path('reimburse-delete/<uuid:uuid>', ReimburseDeleteView.as_view(), name= 'reimburse-delete' ),
]
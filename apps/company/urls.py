from django.urls import path
from .views import CompanyCreateView, CompanyDeleteView, CompanyListView, CompanyUpdateView

app_name = 'company'

urlpatterns = [
    path('', CompanyListView.as_view(), name='company'),
    path('company-create', CompanyCreateView.as_view(), name='company-create'),
    path('company-update/<uuid:uuid>', CompanyUpdateView.as_view(), name='company-update'),
    path('company-delete/<uuid:uuid>', CompanyDeleteView.as_view(), name='company-delete'),
]
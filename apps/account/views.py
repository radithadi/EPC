from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy
from .forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from company.models import Company
# from client.models import Client
# from project.models import Project
# from advance.models import Advance
# from reimburse.models import Reimburse

class AccountLoginView(LoginView):
    template_name   = 'account/login.html'
    form_class      = AuthenticationForm
    #redirect_authenticated_user = True
    extra_context = {
        'site_title' : 'epci | login',
        'success_url' : reverse_lazy('account:dashboard')
    }
    
class AccountLogoutView(LoginRequiredMixin, LogoutView):
    next_page           = 'account:login'

class AccountPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name       = 'account/password_change_form.html'
    form_class          = PasswordChangeForm
    success_url         = reverse_lazy('account:password_change_done')

class AccountPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name       ='account/password_change_done.html'
    
class AccountPasswordResetView(PasswordResetView):
    template_name       = 'account/password_reset_form.html'
    form_class          = PasswordResetForm
    email_template_name = 'account/password_reset_email.html'
    success_url         = reverse_lazy('account:password_reset_done')

class AccountPasswordResetDoneView(PasswordResetDoneView):
    template_name   = 'account/password_reset_done.html'
    
class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    template_name   = 'account/password_reset_confirm.html'
    form_class      = SetPasswordForm
    success_url     = reverse_lazy('account:password_reset_complete')

class AccountPasswordResetCompleteView(PasswordResetCompleteView):
    template_name   = 'account/password_reset_complete.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name       = 'account/dashboard.html'
    extra_context       = {
        'site_title'    : 'epci | dashboard',
        'page_title'    : 'dashboard',
        # 'company_count' : Company.objects.all().count(),
        # 'client_count'  : Client.objects.all().count(),
        # 'project_count' : Project.objects.all().count(),
        # 'open_count'    : Project.objects.filter(status='open').count(),
        # 'close_count'   : Project.objects.filter(status='close').count(),
    }
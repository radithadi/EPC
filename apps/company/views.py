from django.views.generic import CreateView, DeleteView, UpdateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Company
from .forms import CompanyForm
from copy import copy

class CompanyMixin(LoginRequiredMixin, SuccessMessageMixin, object):
    model = Company
    template_name = "company/company_form.html"
    form_class = CompanyForm
    success_url = reverse_lazy('company:company')
    success_message = None
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    extra_context = {
        'site_title'    : 'epci | companies',
        'page_title'    : 'company list',
    }    

class CompanyListView(CompanyMixin, ListView):
    template_name = 'company/company.html'
    context_object_name = 'companies'
    paginate_by = 8

class CompanyCreateView(CompanyMixin, CreateView):
    success_message = "%(name)s was created successfully"
    extra_context = copy(CompanyMixin.extra_context)
    extra_context['form_name'] = 'form create company'

class CompanyUpdateView(CompanyMixin, UpdateView):
    success_message = "%(name)s was updated successfully"
    extra_context = copy(CompanyMixin.extra_context)
    extra_context['form_name'] = 'form update company'

class CompanyDeleteView(CompanyMixin, DeleteView):
    template_name = 'company/company_delete.html'
    success_message = "%(name)s was deleted successfully"
    
    def delete(self, request, *args, **kwargs):
        from django.contrib import messages
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)
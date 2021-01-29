from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm
from copy import copy

class ClientMixin(LoginRequiredMixin, SuccessMessageMixin, object):
    model = Client
    template_name = "client/client_form.html"
    form_class = ClientForm
    success_url = reverse_lazy('client:client')
    success_message = None
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    extra_context = {
        'site_title'    : 'epci | customer users',
        'page_title'    : 'client list',
    }
    
class ClientListView(ClientMixin, ListView):
    template_name = "client/client.html"
    context_object_name = 'clients'
    paginate_by = 10

class ClientCreateView(ClientMixin, CreateView):
    success_message = "%(name)s was created successfully"
    extra_context = copy(ClientMixin.extra_context)
    extra_context['form_name'] = 'form create client'

class ClientDetailView(ClientMixin, DetailView):
    template_name = 'client/client_detail.html'

class ClientUpdateView(ClientMixin, UpdateView):
    success_message = "%(name)s was updated successfully"
    extra_context = copy(ClientMixin.extra_context)
    extra_context['form_name'] = 'form update client'
    
class ClientDeleteView(ClientMixin, DeleteView):
    template_name = 'client/client_delete.html'
    success_message = "%(name)s was deleted successfully"
    
    def delete(self, request, *args, **kwargs):
        from django.contrib import messages
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)
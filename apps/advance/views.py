from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Advance
from .forms import AdvanceForm
from copy import copy

class AdvanceMixin(LoginRequiredMixin, SuccessMessageMixin, object):
    model = Advance
    template_name = "advance/advance_form.html"
    form_class = AdvanceForm
    success_url = reverse_lazy('advance:advance')
    success_message = None
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    extra_context = {
        'site_title'    : 'epci | advance',
        'page_title'    : 'advance list',
    }
    
    def get_queryset(self):
        queryset = Advance.objects.filter(user=self.request.user)
        return queryset
    
class AdvanceListView(AdvanceMixin, ListView):
    template_name = "advance/advance.html"
    context_object_name = 'advances'
    paginate_by = 10

class AdvanceCreateView(AdvanceMixin, CreateView):
    success_message = "%(name)s was created successfully"
    extra_context = copy(AdvanceMixin.extra_context)
    extra_context['form_name'] = 'form create advance'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AdvanceDetailView(AdvanceMixin, DetailView):
    template_name = 'advance/advance_detail.html'

class AdvanceUpdateView(AdvanceMixin, UpdateView):
    success_message = "%(name)s was updated successfully"
    extra_context = copy(AdvanceMixin.extra_context)
    extra_context['form_name'] = 'form update advance'
    
class AdvanceDeleteView(AdvanceMixin, DeleteView):
    template_name = 'advance/advance_delete.html'
    success_message = "%(name)s was deleted successfully"
    
    def delete(self, request, *args, **kwargs):
        from django.contrib import messages
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)
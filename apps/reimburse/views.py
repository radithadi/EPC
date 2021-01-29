from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Reimburse
from .forms import ReimburseForm
from copy import copy

class ReimburseMixin(LoginRequiredMixin, SuccessMessageMixin, object):
    model = Reimburse
    template_name = "reimburse/reimburse_form.html"
    form_class = ReimburseForm
    success_url = reverse_lazy('reimburse:reimburse')
    success_message = None
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    extra_context = {
        'site_title'    : 'epci | reimburse',
        'page_title'    : 'reimburse list',
    }
    
    def get_queryset(self):
        queryset = Reimburse.objects.filter(user=self.request.user)
        return queryset
    
class ReimburseListView(ReimburseMixin, ListView):
    template_name = "reimburse/reimburse.html"
    context_object_name = 'reimburses'
    paginate_by = 10
class ReimburseCreateView(ReimburseMixin, CreateView):
    success_message = "%(name)s was created successfully"
    extra_context = copy(ReimburseMixin.extra_context)
    extra_context['form_name'] = 'form create reimburse'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReimburseDetailView(ReimburseMixin, DetailView):
    template_name = 'reimburse/reimburse_detail.html'

class ReimburseUpdateView(ReimburseMixin, UpdateView):
    success_message = "%(name)s was updated successfully"
    extra_context = copy(ReimburseMixin.extra_context)
    extra_context['form_name'] = 'form update reimburse'
    
class ReimburseDeleteView(ReimburseMixin, DeleteView):
    template_name = 'reimburse/reimburse_delete.html'
    success_message = "%(name)s was deleted successfully"
    
    def delete(self, request, *args, **kwargs):
        from django.contrib import messages
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)

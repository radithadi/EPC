from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Timesheet
from .forms import TimesheetForm
from copy import copy
from datetime import timedelta, date
from django.http import HttpResponseRedirect

class TimesheetMixin(LoginRequiredMixin, SuccessMessageMixin, object):
    model = Timesheet
    template_name = "timesheet/timesheet_form.html"
    form_class = TimesheetForm
    success_url = reverse_lazy('timesheet:timesheet')
    success_message = None
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    extra_context = {
        'site_title'    : 'epci | timesheet',
        'page_title'    : 'timesheet list',
        'today'         : date.today()
    }
    
class TimesheetListView(TimesheetMixin, ListView):
    template_name = "timesheet/timesheet.html"
    context_object_name = 'timesheets'
    paginate_by = 10

class TimesheetCreateView(TimesheetMixin, CreateView):
    initial = {
        'date'  : date.today()
    }
    success_message = "timesheet was created successfully"
    extra_context = copy(TimesheetMixin.extra_context)
    extra_context['form_name'] = 'form create Timesheet'

    # def get_form(self):
    #     form = super().get_form()
    #     initial = self.get_initial() 
    #     form.initial['user'] = self.request.user
    #     return form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class TimesheetUpdateView(TimesheetMixin, UpdateView):
    success_message = "timesheet was updated successfully"
    extra_context = copy(TimesheetMixin.extra_context)
    extra_context['form_name'] = 'form update Timesheet'

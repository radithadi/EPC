from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, PermissionDenied
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Project
from .forms import ProjectForm
from copy import copy

class ProjectMixin(LoginRequiredMixin, PermissionRequiredMixin, PermissionDenied, SuccessMessageMixin, object):
    model = Project
    template_name = "project/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy('project:project')
    success_message = None
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    extra_context = {
        'site_title'    : 'epci | project',
        'page_title'    : 'project list',
    }
    
    def get_queryset(self):
        queryset = Project.objects.filter(worker=self.request.user)
        return queryset
    
class ProjectListView(ProjectMixin, ListView):
    permission_required  = 'project.view_project'
    template_name = "project/project.html"
    context_object_name = 'projects'
    paginate_by = 10

class ProjectCreateView(ProjectMixin, CreateView):
    permission_required  = 'project.add_project'
    permission_denied_message = 'no have access for this action'
    success_message = "%(name)s was created successfully"
    extra_context = copy(ProjectMixin.extra_context)
    extra_context['form_name'] = 'form create project'

class ProjectDetailView(ProjectMixin, DetailView):
    template_name = 'project/project_detail.html'

class ProjectUpdateView(ProjectMixin, UpdateView):
    success_message = "%(name)s was updated successfully"
    extra_context = copy(ProjectMixin.extra_context)
    extra_context['form_name'] = 'form update project'
    
class ProjectDeleteView(ProjectMixin, DeleteView):
    template_name = 'project/project_delete.html'
    success_message = "%(name)s was deleted successfully"
    
    def delete(self, request, *args, **kwargs):
        from django.contrib import messages
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)
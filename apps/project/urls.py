from django.urls import path
from .views import ProjectCreateView, ProjectDeleteView, ProjectDetailView, ProjectUpdateView, ProjectListView

app_name = 'project'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project'),
    path('project-create/', ProjectCreateView.as_view(), name='project-create'),
    path('project-detail/<uuid:uuid>', ProjectDetailView.as_view(), name='project-detail'),
    path('project-update/<uuid:uuid>', ProjectUpdateView.as_view(), name='project-update'),
    path('project-delete/<uuid:uuid>', ProjectDeleteView.as_view(), name= 'project-delete' ),
]
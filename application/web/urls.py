from django.urls import path

from .views.index import index
from .views.details import details
from .views.workplaces import workplaces


urlpatterns = [
    path('', index, name='index'),
    path('details/<int:id>', details, name='details'),
    path('workplaces/', workplaces, name='workplaces')
]
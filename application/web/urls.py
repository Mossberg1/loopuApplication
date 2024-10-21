from django.urls import path

from .views.index import index
from .views.details import details
from .views.workplaces import workplaces
from .views.inbox import inbox
from .views.profile import profile
from .views.matches import matches
from .views.saved import saved
from .views.plus import plus
from .views.blog import blog


urlpatterns = [
    path('', index, name='index'),
    path('details/<int:id>', details, name='details'),
    path('workplaces/', workplaces, name='workplaces'),
    path('inbox/', inbox, name='inbox'),
    path('profile/', profile, name='profile'),
    path('matches/', matches, name='matches'),
    path('saved/', saved, name='saved'),
    path('plus/', plus, name='plus'),
    path('blog/', blog, name='blog'),
]
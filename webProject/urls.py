from django.contrib import admin
from django.conf.urls import include
from django.urls import path
# from django.views.generic import TemplateView
from apps.boards import views as boards_views
from apps.core import views as core_views

from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse


urlpatterns = [
    path("",boards_views.BoardListView.as_view(), name='home'),
    path("core/",core_views.home, name='core'),
    # path("demo/",doit(request):HttpResponse("MegaMiilion Demo Hello!")),
    # path("core/",TemplateView.as_view(template_name=""), name='home'),
    path('boards/',include('apps.boards.urls')),
    path('accounts/',include('apps.accounts.urls')),    
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




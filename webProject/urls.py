from django.contrib import admin
from django.conf.urls import include
from django.urls import path
# from django.views.generic import TemplateView
from apps.boards import views as boards_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",boards_views.BoardListView.as_view(), name='home'),
    # path("",TemplateView.as_view(template_name=""), name='home'),
    path('boards/',include('apps.boards.urls')),
    path('accounts/',include('apps.accounts.urls')),    
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




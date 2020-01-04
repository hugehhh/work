from django.urls import path
from rango import views
from rango.views import AboutView
from django_project import settings
from django.conf.urls.static import static

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', AboutView.as_view(), name='about')
    path('like/', views.like_category, name='like_category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('pions/', views.ArticlesClass, name='pion'),
    path('orchids/', views.orchids_view, name='orchids'),
    path('pions/<int:article_id>/', views.article_detail, name='article_detail'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
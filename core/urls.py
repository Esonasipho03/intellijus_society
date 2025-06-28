from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from core.views import sitemap_xml
from core.views import google_verification_file
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('membership/', views.membership, name='membership'),
    path('download-form/', views.download_form, name='download_form'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('download-form/', views.download_form, name='download_form'),
    path('download-constitution/', views.download_constitution, name='download_constitution'),  
    path('gallery/', views.gallery, name='gallery'),
    path('robots.txt', views.robots_txt),
    path('sitemap.xml', sitemap_xml, name='sitemap'),
    path('google3c1cb1b5cdd53735.html', google_verification_file),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


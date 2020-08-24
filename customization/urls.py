from django.contrib import admin
from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static
# from .admin import site
# admin.site = site
# admin.autodiscover()

urlpatterns = [
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##### Changing Django Admin Details #####
admin.site.site_header = 'The Coffee Company'
admin.site.site_title = 'The Coffee Company'
admin.site.index_title = 'Welcome to the Homepage!'

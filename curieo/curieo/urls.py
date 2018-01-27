
from django.conf.urls import url
from django.contrib import admin
from music import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.tags_home,name='home'),
    url(r'^create/$', views.post_tags,name='create'),
    url(r'^(?P<id>\d+)/$', views.tags_detail,name='detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

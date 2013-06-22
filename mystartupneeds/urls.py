from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from need.views import NeedView, NeedDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',  # empty prefix

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', NeedView.as_view(), name='need'),
    url(r'^(?P<slug>[-\w]+)/$', NeedDetailView.as_view(), name='need_detail'),
)


# Serve statics during development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

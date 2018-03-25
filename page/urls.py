from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$', views.rd_list, name='rd_list'),
    url(r'^kontakt/$', views.contact_list, name='contact_list'),
    url(r'^projekty/$', views.rd_list, name='rd_list'),
    url(r'^vizualizace/$', views.viz_list, name='viz_list'),
    url(r'^projekty/(?P<pk>[0-9]+)/(?P<ip>[0-9]+)/$', views.RD_detail, name='RD_detail'),
    url(r'^projekty/rodinne_domy/$', views.rd_filter_RD, name='rd_filter_RD'),
    url(r'^projekty/interiery/$', views.rd_filter_INTER, name='rd_filter_INTER'),
    url(r'^projekty/jine/$', views.rd_filter_JINE, name='rd_filter_JINE')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()

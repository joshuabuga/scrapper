from django.conf.urls import patterns, include, url
from django.contrib import admin
from scrapper import settings
from django.conf.urls.static import static
from scrapper.views import properties_list,Upload,UpdateList,Search,dashboard
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrapper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^upload/$', Upload.as_view()),
    url(r'^dashboard/$', dashboard),
    url(r'^search/$', Search.as_view()),
    url(r'^update/$', UpdateList.as_view()),
	url(r'^$', properties_list),
	

    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'html/login.html'}),
    	(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    	 


)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

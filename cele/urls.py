from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cele.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls',namespace = "polls")),
    
    #spiderpro is my django spider program by ray
    url(r'^spiderpro',include('spiderpro.urls',namespace = "spiderpro"))
   
)

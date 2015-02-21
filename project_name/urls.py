from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib import admin


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^admin/', include(admin.site.urls)),
)

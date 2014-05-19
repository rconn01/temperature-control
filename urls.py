from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from temperatureLog import views

urlpatterns = patterns('',
    url(r'^$', views.helloWorld, name='index'),
    url(r'^uploadTemperature$',views.uploadTemperatureReading,name='uploadTemperature'),
    url(r'^sensorReadings/([0-9]+)$',views.getAllReadingsBySensor,name ="getAllReadings"),
    url(r'^detail/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^chartTest$',TemplateView.as_view(template_name="temperatureLog/chartbase.html")),
    url(r'^shellTest',views.shellTest)
)

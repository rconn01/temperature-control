from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt 
from django.utils import timezone
from temperatureLog.models import Reading   
from django.views import generic
import datetime
                                      
@csrf_exempt
@require_http_methods(['POST'])
def uploadTemperatureReading(request):
	postParams = request.POST
	sensor = postParams["sensorId"]
	temperature = postParams["temperature"]
	dateStr = postParams.get("date","null")
	if dateStr== "null":
		date = timezone.now()
		
	else:
		date = datetime.datetime.fromtimestamp(float(dateStr))
	
	reading = Reading(sensor_id=sensor,value=temperature, date=date)
	reading.save()
		
	return HttpResponse("complete")
	
def helloWorld(request):
	return HttpResponse("Hello, world. You're at the poll index.")
	
def getAllReadingsBySensor(request,sensorId):
	readings = Reading.objects.filter(sensor__id=sensorId)
	data = serializers.serialize("json",readings)
	return HttpResponse(data,content_type="application/json")
	
def shellTest(request):
	return render(request,'temperatureLog/shell.html')
class DetailView(generic.DetailView):
	model=Reading
	template_name = 'temperatureLog/detail.html'


	

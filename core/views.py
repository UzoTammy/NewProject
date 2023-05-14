# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
import time, datetime
import json

# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/index.html'

    

class StreamView(TemplateView): 
    template_name = 'core/event_stream.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            with open('core/static/time.json') as rf:
                content = json.load(rf)
            context['dt'] = content['time']
        except:
            content = ''
        
        return context

class GetTimeView(View):    
    def get(self, request):
        def timer():
            with open('core/static/time.json', 'w') as wf:
                """get the time"""
                ticker = time.gmtime()
                # Extract day, hour, minutes, and seconds
                data = {
                    "time": {"day": str(ticker.tm_mday).zfill(2),
                             "hour": str(ticker.tm_hour).zfill(2),
                             "minutes": str(ticker.tm_min).zfill(2),
                             "seconds": str(ticker.tm_sec).zfill(2)
                            },
                        }
                json.dump(data, wf, indent=2)
                
            time.sleep(1)
        
        response = HttpResponse(timer(), content_type='text/event-stream')
        response['Cache-Control'] = 'no-cache'
        return response
    
    
from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request,offset):
    # try: 
    #     offset = int(offset)
    # except ValueError:
    #     raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(offset)
    html = "<html><body>In %s hours, it will be %s." %(offset,dt)
    return HttpResponse(html)
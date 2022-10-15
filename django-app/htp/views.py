from django.http import HttpResponse
from django.template import loader
from django.contrib.staticfiles.views import serve

from django.conf import settings

def index(request):
    return serve(request, 'index.html', settings.STATIC_ROOT)
    # template = loader.get_template("htp/index.html")
    # context = {}
    # return HttpResponse(template.render(context, request))

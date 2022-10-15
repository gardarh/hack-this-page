from pathlib import Path

from django.http import HttpResponse

from django.conf import settings


def index(request):
    index_file = Path(settings.STATIC_ROOT, "index.html")
    with open(index_file, "r") as f:
        return HttpResponse(f.read())

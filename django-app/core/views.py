from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from rest_framework import generics, viewsets

from core.models import Article
from core.serializers import ArticleSerializer


def index(request):
    index_file = Path(settings.STATIC_ROOT, "index.html")
    with open(index_file, "r") as f:
        return HttpResponse(f.read())


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by("-id")
    serializer_class = ArticleSerializer

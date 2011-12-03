# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from models import Artigo

def artigo(request, slug):
#    artigo = Artigo.objects.get(slug=slug)
    artigo = get_object_or_404(Artigo, slug=slug)
    return render_to_response('blog/artigo.html', locals(), context_instance = RequestContext(request))

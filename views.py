from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from forms import FormRegistro, FormContato
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

def contato(request):
#    form = FormContato()
    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
            mostrar = 'Contato Enviado!'
    else:
        form = FormContato()
    return render_to_response('contato.html', locals(), context_instance = RequestContext(request),)

def registrar(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            novo_formulario = form.save()
            return HttpResponseRedirect('/')

    else:
        form = FormRegistro()

    return render_to_response('registrar.html', locals(), context_instance = RequestContext(request),)

@permission_required('ver_todos_os_usuarios')
def todos_os_usuarios(request):
    usuarios = User.objects.all()
    return render_to_response(
        'todos_os_usuarios.html',
        locals(),
        context_instance=RequestContext(request),
      )



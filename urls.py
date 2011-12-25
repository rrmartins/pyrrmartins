from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog.models import Artigo
admin.autodiscover()
from blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index',
        {'queryset': Artigo.objects.all(),
         'date_field': 'publicacao'}),
    url(r'^admin/', include(admin.site.urls)),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict' : { 'ultimos': UltimosArtigos}}),
    (r'^artigo/(?P<slug>[\w_-]+)/$', 'blog.views.artigo'),
#    (r'^media/(.*)$', 'django.views.static.serve',
#        {'document_root': settings.MEDIA_ROOT}),
    (r'^contato/$', 'views.contato'),
    (r'^comments/', include('django.contrib.comments.urls')), 
    (r'^galeria/', include('galeria.urls')),
    (r'^tags/', include('tags.urls')),
    (r'^contas/', include('contas.urls')),
    (r'^entrar/$', 'django.contrib.auth.views.login',
            {'template_name': 'entrar.html'}, 'entrar'),
    (r'^sair/$', 'django.contrib.auth.views.logout',
            {'template_name': 'sair.html'}, 'sair'),
    (r'^registrar/$', 'views.registrar', {}, 'registrar'),
    (r'^todos_os_usuarios/$', 'views.todos_os_usuarios',
            {}, 'todos_os_usuarios'),
    (r'^mudar_senha/$',
        'django.contrib.auth.views.password_change',{'template_name': 'mudar_senha.html'},'mudar_senha'),
    (r'^mudar_senha/concluido/$','django.contrib.auth.views.password_change_done',
        {'template_name': 'mudar_senha_concluido.html'}, 'mudar_senha_concluido'),

)

if settings.LOCAL:
    urlpatterns += patterns('', (r'^media/(.*)$', 'django.views.static.serve',
                                  {'document_root': settings.MEDIA_ROOT}),
                   )

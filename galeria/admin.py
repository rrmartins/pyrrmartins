# -*- coding: utf-8 -*- 
try:
    import Image
except ImportError:
    from PIL import Image
from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from models import Album, Imagem
from tags import aplicar_tags, tags_para_objeto

class AdminAlbum(ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

class FormImagem(forms.ModelForm):
    class Meta:
        model = Imagem
    
    tags = forms.CharField(max_length=30, required=False)
    def __init__(self, *args, **kwargs):
        super(FormImagem, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.initial['tags'] = tags_para_objeto(
            self.instance
            )
    
    def save(self, *args, **kwargs):
        """Metodo declarado para criar miniatura da imagem depois
        de salvar"""
        imagem = super(FormImagem, self).save(*args, **kwargs)
        
        if 'original' in self.changed_data:
            extensao = imagem.original.name.split('.')[-1]
            imagem.thumbnail = 'galeria/thumbnail/%d.%s'%( imagem.id, extensao )
            miniatura = Image.open(imagem.original.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(imagem.thumbnail.path)
            imagem.save()


        aplicar_tags(imagem, self.cleaned_data['tags'])
        
        return imagem
    
class AdminImagem(ModelAdmin):
    list_display = ('album','titulo',)
    list_filter = ('album',)
    search_fields = ('titulo','descricao',)
    form = FormImagem

admin.site.register(Album, AdminAlbum)
admin.site.register(Imagem, AdminImagem)

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from tags import aplicar_tags, tags_para_objeto
from django import forms
from models import Artigo

class FormArtigo(forms.ModelForm):
    class Meta:
        model = Artigo

    tags = forms.CharField(max_length=30, required=False)

    def __init__(self, *args, **kwargs):
        super(FormArtigo, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.initial['tags'] = tags_para_objeto(self.instance)

    def save(self, *args, **kwargs):
        artigo = super(FormArtigo, self).save(*args, **kwargs)
        aplicar_tags(artigo, self.cleaned_data['tags'])
        return artigo


class AdminArtigo(ModelAdmin):
    form = FormArtigo

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicacao',)
    prepopulated_fields= {'slug': ('titulo',)}

admin.site.register(Artigo,AdminArtigo)

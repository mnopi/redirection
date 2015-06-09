# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import Textarea, TextInput
from redirect.models import *
from django import forms



# class PageAdmin(admin.ModelAdmin):
#     list_display = (
#         '__unicode__',
#     )
#
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'40'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
#     }
#
#     class PageRedirectionInline(admin.TabularInline):
#
#         class RedirectionInlineFormset(forms.models.BaseInlineFormSet):
#             def clean(self):
#                 """Comprobamos que:
#                     - No haya una redirección con un lenguaje dado sin otra con lenguaje por defecto
#                     - No haya más de una plataforma para una misma redirección
#                 """
#
#                 # diccionario con tantas plataformas como hayan con la redirección dada. Cada clave de la
#                 # plataforma tiene una lista con los idiomas que tiene"""
#                 platforms_langs = {}
#
#                 for r in self.forms:
#                     if 'DELETE' in r.changed_data:
#                         continue
#                     else:
#                         platform = r.instance.get_platform_display()
#                         # comprobamos si la plataforma ya existe
#                         if platform in platforms_langs:
#                             if r.instance.language in platforms_langs[platform]:
#                                 # si ya estaba ese lenguaje para esa plataforma en anteriores forms del redirection formset
#                                 raise ValidationError('Pairs (platform - lang): %s - %s must be uniques. Found more than 1.'
#                                                       % (platform, r.instance.language or 'Null'))
#                             else:
#                                 platforms_langs[platform].append(r.instance.language)
#                         else:
#                             platforms_langs[platform] = [r.instance.language]
#
#                 # miramos si al menos tenemos como mínimo una plataforma cargada (incluída all)
#                 if platforms_langs:
#                     # miramos en cada plataforma si tiene el lenguaje por defecto
#                     for platform, langs in platforms_langs.items():
#                         # django guarda los charfields vacíos en los forms como '' y no como null
#                         # https://docs.djangoproject.com/en/dev/ref/models/fields/#null
#                         if '' not in langs:
#                             raise ValidationError('Platform %s has no default language redirection' % platform)
#                 else:
#                     raise ValidationError('Page must have at least one redirection associated')
#
#         model = Redirection
#         formset = RedirectionInlineFormset
#         extra = 0
#
#     inlines = (
#         PageRedirectionInline,
#     )
#
#
# class PageAliasAdmin(admin.ModelAdmin):
#     list_display = (
#         '__unicode__',
#         'page',
#     )
#
#
# class RedirectionAdmin(admin.ModelAdmin):
#     list_display = (
#         '__unicode__',
#         'page',
#     )
#
#
# admin.site.register(Page, PageAdmin)
# admin.site.register(PageAlias, PageAliasAdmin)
# admin.site.register(Redirection, RedirectionAdmin)

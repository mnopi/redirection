# -*- coding: utf-8 -*-
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from user_agents import parse
from redirect.models import Page, PageAlias, Redirection


def redirector(request, uri):
    def get_platform():
        userAgent = request.META['HTTP_USER_AGENT']
        user_agent = parse(userAgent)
        if user_agent.os.family == 'Android':
            return Redirection.ANDROID
        elif user_agent.os.family == 'iOS':
            return Redirection.IOS
        else:
            return Redirection.OTHERS

    try:
        page = Page.objects.get(uri=uri)
    except Page.DoesNotExist:
        page = PageAlias.objects.get(uri=uri).page

    platform = get_platform()
    lang = translation.get_language_from_request(request)
    lang = lang[:2] if lang else None

    try:
        redirection = page.redirections.get(platform=platform, language=lang)
    except Redirection.DoesNotExist:
        try:
            redirection = page.redirections.get(platform=platform, language='')
        except Redirection.DoesNotExist:
            # si no existe la plataforma con el lenguaje por defecto miramos la redirección para todas las plataformas
            try:
                redirection = page.redirections.get(platform=platform, language=lang)
            except Redirection.DoesNotExist:
                # si no existe el lenguaje para todas las plataformas devolvemos de todas plataformas para todos los lenguajes
                redirection = page.redirections.get(platform=None, language='')

    # pillamos la url hacia la imágen de la card
    if page.card_img_file:
        page.card_img_full_url = request.build_absolute_uri(page.card_img_file.url)
    elif page.card_img_url:
        page.card_img_full_url = page.card_img_url
    else:
        page.card_img_full_url = None

    page.full_url = request.build_absolute_uri()

    return render_to_response(
        'redirection.html',
        {'page': page, 'redirection_url': redirection.url},
        context_instance=RequestContext(request)
    )


def test(request):
    return render_to_response('test.html')


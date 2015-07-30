# -*- coding: utf-8 -*-
import datetime
from django.db import transaction
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation
from pytz import utc
from user_agents import parse
from redirect.models import *
# from redirect.models import Page, PageAlias, Redirection


def redirector(request, uri=None):

    def comes_from_twitter():
        """Nos dice si el usuario viene o no de hacer click en un link publicado en twitter por un bot"""
        return't.co' in get_referer()

    def get_referer():
        return request.META['HTTP_REFERER'] if 'HTTP_REFERER' in request.META else 'unknown'

    def get_ip():
        return request.META['HTTP_X_REAL_IP'] if 'HTTP_X_REAL_IP' in request.META else '0.0.0.0'

    def get_url_to_redirect():

        if promo.project.name.lower() == 'bogadia':
            return 'http://www.bogadia.com/?p=%s' % promo.name
        else:
            link_all = promo.link_all
            link_android = promo.link_android
            link_ios = promo.link_ios
            link_others = promo.link_others

            # si existe link_all devuelve el link, sino el correspondiente al user_agent
            if link_all:
                return link_all
            if user_agent.os.family == 'Android':
                return link_android
            elif user_agent.os.family == 'iOS':
                return link_ios
            else:
                return link_others

    def register_mutweet_click():
        """Registra cada click que se hace en los mutweets, incluso si hay varios clicks sobre mismo mutweet"""

        def register_clicked_mutweet():
            with transaction.atomic():
                clicked_mt = ProjectClickedmutweet(
                    bot_sender=bot_sender,
                    mentioned_user=mentioned_twitteruser,
                    promo_msg=muTweet.promo_msg,
                    msg_sent=muTweet.msg_sent,
                    domain=muTweet.domain
                )
                clicked_mt.save()

                mentioned_twitteruser.has_clicked_mutweet = True
                mentioned_twitteruser.save()

        mentioned_twitteruser = ProjectTwitteruser.objects.get(pk=muTweet.mentioned_twitteruser_id)
        bot_sender = CoreTwitterbot.objects.get(pk=muTweet.bot_sender_id)

        # se registra el click en el enlace del tweet en la base de datos
        try:
            clicked_mutweet = ProjectClickedmutweet.objects.get(mentioned_user=mentioned_twitteruser,
                                                                promo_msg=promo_msg)
        except ProjectClickedmutweet.DoesNotExist:
            # si no existe el registro de mutweet clickeado entonces se crea antes
            register_clicked_mutweet()
        except ProjectClickedmutweet.MultipleObjectsReturned:
            ProjectClickedmutweet.objects.filter(mentioned_user=mentioned_twitteruser,
                                                 promo_msg=promo_msg).delete()
            register_clicked_mutweet()
        finally:
            clicked_mutweet = ProjectClickedmutweet.objects.get(mentioned_user=mentioned_twitteruser,
                                                                promo_msg=promo_msg)
            if user_agent.os.family == 'Android':
                platform = 0
            elif user_agent.os.family == 'iOS':
                platform = 1
            else:
                platform = 2
            mutweet_click = ProjectMutweetclick(
                clicked_mutweet=clicked_mutweet,
                date_clicked=datetime.datetime.utcnow().replace(tzinfo=utc),
                raw_useragent=raw_useragent,
                platform=platform,
                ip=get_ip(),
                referer=get_referer()
            )
            mutweet_click.save()

    def is_human():
        return raw_useragent != 'Twitterbot/1.0' \
               and raw_useragent != 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)'\
               and raw_useragent != 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    # Cogemos el id del tweet de la uri
    a = uri.split('/')
    tweet_id = int(a[len(a)-1])
    muTweet = ProjectMutweet.objects.get(pk=tweet_id)
    promo_msg = ProjectPromomsg.objects.get(pk=muTweet.promo_msg._get_pk_val)
    promo = promo_msg.promo_msg_generator_expr.promo

    raw_useragent = request.META['HTTP_USER_AGENT']
    user_agent = parse(raw_useragent)

    if is_human() and comes_from_twitter():
        register_mutweet_click()


    # lang = translation.get_language_from_request(request)
    # lang = lang[:2] if lang else None

    # try:
    #     redirection = page.redirections.get(platform=platform, language=lang)
    # except Redirection.DoesNotExist:
    #     try:
    #         redirection = page.redirections.get(platform=platform, language='')
    #     except Redirection.DoesNotExist:
    #         # si no existe la plataforma con el lenguaje por defecto miramos la redirección para todas las plataformas
    #         try:
    #             redirection = page.redirections.get(platform=platform, language=lang)
    #         except Redirection.DoesNotExist:
    #             # si no existe el lenguaje para todas las plataformas devolvemos de todas plataformas para todos los lenguajes
    #             redirection = page.redirections.get(platform=None, language='')
    #
    # # pillamos la url hacia la imágen de la card
    # if page.card_img_file:
    #     page.card_img_full_url = request.build_absolute_uri(page.card_img_file.url)
    # elif page.card_img_url:
    #     page.card_img_full_url = page.card_img_url
    # else:
    #     page.card_img_full_url = None
    #
    # page.full_url = request.build_absolute_uri()

    return render_to_response(
        'redirection.html',
        {'redirection_url': get_url_to_redirect()},
        context_instance=RequestContext(request)
    )


def test(request):
    return render_to_response('test.html')


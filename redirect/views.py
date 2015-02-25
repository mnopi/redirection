from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from user_agents import parse
from redirect.models import Page

def redirector(request, uri):
    userAgent = request.META['HTTP_USER_AGENT']
    page = Page.objects.get(uri=uri)
    user_agent = parse(userAgent)
    if page.all:
        redirection_url = page.all
    elif user_agent.os.family == 'Android':
        redirection_url = page.android
    elif user_agent.os.family == 'iOS':
        redirection_url = page.ios
    else:
        redirection_url = page.other

    page.card_img_full_url = request.build_absolute_uri(page.card_img.url)
    page.full_url = request.build_absolute_uri()

    return render_to_response(
        'redirection.html',
        {'page': page, 'redirection_url': redirection_url},
        context_instance=RequestContext(request)
    )


def test(request):
    return render_to_response('test.html')


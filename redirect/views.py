from django.shortcuts import redirect, render_to_response
from user_agents import parse
from redirect.models import Page

def redirector(request, uri):
    userAgent = request.META['HTTP_USER_AGENT']
    url = Page.objects.get(uri=uri)
    user_agent = parse(userAgent)
    if url.all:
        redirection_url = url.all
    elif user_agent.os.family == 'Android':
        redirection_url = url.android
    elif user_agent.os.family == 'iOS':
        redirection_url = url.ios
    else:
        redirection_url = url.other

    return render_to_response('redirection.html', {'redirection_url': redirection_url})


def test(request):
    return render_to_response('test.html')


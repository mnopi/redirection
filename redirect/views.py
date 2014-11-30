from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from user_agents import parse
from redirect.models import Page

def redirector(request, id):
    userAgent = request.META['HTTP_USER_AGENT']
    url = Page.objects.get(pk=id)
    user_agent = parse(userAgent)
    if url.all:
        return redirect(url.all)
    elif user_agent.os.family == 'Android':
        return redirect(url.android)
    elif user_agent.os.family == 'iOS':
        return redirect(url.ios)
    else:
        return redirect(url.other)

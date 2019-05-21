from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext


def greeting_page(request):
    return render(request, 'greeting.html')

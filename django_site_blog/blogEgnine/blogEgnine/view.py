from django.shortcuts import render, redirect


def greeting_page(request):
    return render(request, 'greeting.html')

from django.shortcuts import render


def home_view(request):
    context = {

    }
    return request(render,'',context)
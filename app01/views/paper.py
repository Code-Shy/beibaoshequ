from django.shortcuts import render, redirect

from app01 import models
from app01.views.forms import ResourceForm


def paper_list(request):
    type = 0
    queryset = models.Resource.objects.filter(type=type)

    return render(request, 'resource_list.html', {
        'data_list': queryset,
        'type': type
    })


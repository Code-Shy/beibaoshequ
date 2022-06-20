from django.shortcuts import render, redirect

from app01 import models
from app01.views.forms import ResourceForm


def resource_list(request):
    type = 1
    queryset = models.Resource.objects.filter(type=type)

    return render(request, 'resource_list.html', {
        'data_list': queryset,
        'type': type
    })


def resource_add(request, type):
    if request.method == "GET":
        form = ResourceForm()
        return render(request, "resource_add.html", {
            "form": form,
        })
    form = ResourceForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        if type == 1:
            return redirect('resource_list')
        else:
            return redirect('paper_list')
    return render(request, "resource_add.html", {
        "form": form,
    })

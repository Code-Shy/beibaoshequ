from django.http import JsonResponse
from django.utils import timezone

from app01 import models


def comment(request):
    obj = models.Comment.objects.create(**request.GET.dict())

    return JsonResponse({
        'status': True,
        'time': timezone.localtime(obj.time).strftime('%Y-%m-%d %H:%M:%S')
    })

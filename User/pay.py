# Author Jingxuan Chen
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
import json
from User import models as user_models
from Operator import models as operator_models


def pay_view(request):
    order_id = request.GET.get('order_id')
    order = user_models.order.objects.filter(pk=order_id)
    if not order.exists():
        return HttpResponse('No such order!')
    if order.first().is_complete:
        return HttpResponseRedirect('pay_success?order_id=' + order_id)
    
    order_info = {}
    order_info['order_id'] = order.first().id
    order_info['bike_id'] = order.first().bike.id
    order_info['duration'] = order.first().get_duration()
    order_info['amount'] = order.first().due_amount
    return render(request, 'pay.html', order_info)

@api_view(('POST',))
def pay(request):
    order_id = request.POST['order_id']
    try:
        order = user_models.order.objects.filter(pk=order_id).first()
        user_cmodels.order.objects.filter(pk=order_id).update(is_complete = True, fix_amount = order.due_amount)
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=500)


def pay_success_view(request):
    order_id = request.GET.get('order_id')
    order = user_models.order.objects.filter(pk=order_id)
    if not order.exists():
        return HttpResponse('No such order!')
    if not order.first().is_complete:
        return HttpResponseRedirect('settlement?order_id=' + order_id)
    order_info = {}
    order_info['order_id'] = order.first().id
    order_info['bike_id'] = order.first().bike.id
    order_info['duration'] = order.first().get_duration()
    order_info['amount'] = order.first().due_amount
    return render(request, 'pay_success.html', order_info)

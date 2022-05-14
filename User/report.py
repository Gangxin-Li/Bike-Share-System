# -*- coding: utf-8 -*-
#from django import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
import json
from User import models as user_models
from Operator import models as operator_models
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# @login_required(redirect_field_name='',login_url='ulogin/')
def report_view(request):
    print(request.user.id)
    return render(request, 'report.html')

# get bike by bike id
def getBike(id):
    bike = operator_models.Bike.objects.filter(pk=id)
    return bike


# Save defectiveness report and set is_faulty of bike as TRUE
# and set in_use as FALSE
def saveReportAndEditBike(report, bike):
    # Check whether report part has been reported. If so, do not add record more
    report_record = operator_models.defectiveness_report.objects.filter(
        bike=bike, defective_parts=report["defective_parts"], is_fixed=False)
    if not report_record.exists():
        try:
            # Save report
            operator_models.defectiveness_report.objects.create(
                defective_parts=report["defective_parts"],
                description=report["description"],
                bike=report["bike"]
                # report_user=report["report_user"]
            )

            # Edit bike: is_faulty = true & in_use = false
            bike.is_faulty = True
            bike.in_use = False
            bike.save()
            return True
        except:
            return False
    return True

@api_view(('POST',))
def submit_defectives(request):
    bike_id = request.POST['bike_id']
    defective_parts = request.POST['defective_parts']
    description = request.POST['description']

    # current_user = user_models.account_account.objects.get(pk=1)
    # current_user = request.user.id

    bike = getBike(bike_id)
    if not bike.exists():
        return HttpResponse(status=404)
        # return HttpResponse("No such bike id, try another one.", content_type='application/json')

    report = {
        "bike": bike.first(),
        "defective_parts": defective_parts,
        "description": description
        # "report_user": current_user
    }

    if saveReportAndEditBike(report, bike.first()):
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)
        # return HttpResponse("Report Fail, try again.", content_type='application/json')

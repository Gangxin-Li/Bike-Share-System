# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 01:20:30 2021

@author: LiGangxin
"""
from django.http import HttpResponse
from User import models
import datetime
from django.utils import timezone
##Add
def acount_acount_ADD(name,email,pwd):

    date_joined =default=timezone.now

    last_login = default=timezone.now
    role = ""
    is_admin = 0
    is_active = 1
    is_staff = 0
    is_superuser = 0
    hires_in_progress = 0
    wallet_balance = 0
    amount_owed = 0

    ADD = models.account_account(username=name,password = pwd,email=email,\
                                 date_joined = date_joined,\
                                     last_login = last_login,\
                                         role = role, is_admin = is_admin,\
                                             is_active=is_active,is_staff=is_staff,\
                                                 is_superuser = is_superuser,\
                                                     hires_in_progress =hires_in_progress,\
                                                         wallet_balance = wallet_balance,\
                                                             amount_owed = amount_owed)
    try:    
        ADD.save()
        return True
    except:
        return False
    
##Delete
def acount_acount_Delete(email):
    try:
        models.objects.filter(email=email).delete()
        return True
    except:
        return False
    
##Update
def acount_acount_Update(email,pwd):
    try:
        models.objects.filter(email=email).update(password=pwd).save()
        return True
    except:
        return False
    
##Search
def acount_acount_Search(email,pwd):
    try:
        response = models.object.fliter(emai = email,password = pwd)
        return response
    except:
        return False
    
#Recharge
def acount_acount_Recharge(id,pounds):
    try:
        purchase = models.objects.filter(id=id)
        purchase.wallet_balance+=pounds
        purchase.save()
        return True
    except:
        return False
"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User import views
from User import report, pay
#test
# from User import test_database 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ulogin/', views.ulogin),
    path('ulogin_post/',views.ulogin_post),
    path('uregist_post/',views.uregist_post),
    path('ume/',views.ume),
    path('urecharge/',views.urecharge),
    path('report', report.report_view),
    path('report/submit_defective', report.submit_defectives),
    path('defbikes/',views.viewDefectiveBikes),
    path('repbikes/',views.repairbikes),
    path('trackbikes/<int:station_id>/',views.trackBikes),
    path('movebikes/',views.moveBikes),
    path('viewDefbikes/',views.viewDefBikes),
    path('trackBikeshtml/',views.trackBikeshtml),
    path('getStations/',views.getStations),
    path('settlement',pay.pay_view),
    path('pay',pay.pay),
    path('pay_success', pay.pay_success_view),
    path('moveBikes/',views.moveBikeshtml),
    path('getCurrentStation/<int:id>',views.getCurrentStations),
    path('getDefectiveReports/<int:operator_id>/',views.getDefectiveReports),
    path('viewReports/<int:operator_id>/',views.viewReports)
    

    #Test for User
    # path('account_database',test_database.testdb)
]

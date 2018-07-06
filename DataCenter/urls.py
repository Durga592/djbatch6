"""DataCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from cooling.views import temprature, courseregistrationform, student_reg_form, student_reg_form1, student_reg_form2, student_reg_form3, student_reg_form4, student_reg_form5
'''
def temprature(temprature):
	return HttpResponse("hello") 
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_temp/', temprature),
    url(r'^register_form/', courseregistrationform),
    url(r'^student_register_form/', student_reg_form),
    url(r'^student_register_form1/', student_reg_form1),
    url(r'^student_register_form2/', student_reg_form2),
    url(r'^student_register_form3/', student_reg_form3),
    url(r'^student_register_form4/', student_reg_form4),
    url(r'^student_register_form5/', student_reg_form5),
]

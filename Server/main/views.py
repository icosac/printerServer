from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.forms import ValidationError

from main.models import printFormModel
from main.forms import pageForm

from main.utils import findPrinters, findOptions

import time, json, subprocess, shlex

def main(request):
    l_printers=findPrinters()
    printer_options=findOptions(l_printers[0])
    pageform=pageForm()
    if request.method=='POST': 
        print(request.FILES)
        formForm=pageForm(request.POST, request.FILES)
        if formForm.is_valid():
            form=formForm.save()
            print(form.command())
            subprocess.run(shlex.split(form.command()))
        else:
            return render(request, 'html/main.html', {
                "error" : formForm.errors, #['__all__'],
                "options" : printer_options,
                "form" : pageform
            })
    return render(request, 'html/main.html', {
        'options' : printer_options,
        "form" : pageform
    })

def addDate(s):
    l=s.split(".")
    f=""
    if len(l)>1:
        for i in range(0, len(l)-1):
            f+=l[i]
        timestr=time.strftime("--%Y-%m-%d-%H:%M:%S")
        f+=timestr
        f+=("."+l[-1])
    else:
        timestr=time.strftime("--%Y-%m-%d-%H:%M:%S")
        f=s
        f+=timestr
    print(f)
    return f






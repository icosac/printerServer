from django.shortcuts import render, redirect
import subprocess, shlex

def setting(request):
    return render(request, "html/settings.html")

def readCommandError(command, err):
    proc=subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        line=proc.stdout.readline()
        if not line:
            break
        err+=(line.decode("utf-8")+"\n")
    return err

def restartServer(request):
    err=""
    err=readCommandError("lprm -", err)
    err=readCommandError("cupsdisable -c HP_Officejet_5615", err)
    err=readCommandError("cupsenable HP_Officejet_5615", err)
    if err!="":
        return render(request, "html/settings.html", {"error" : err} )
        #return redirect("/settings/", error=err)
    else:
        return redirect("/settings/")

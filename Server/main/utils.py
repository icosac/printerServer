import subprocess, shlex, json

from django.conf import settings
from os import path
import time

def findPrinters():
    command="lpstat -e"
    output=subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    l=list()
    while True:
        line=output.stdout.readline()
        if not line:
            break
        l.append(line.decode("utf-8").split("\n")[0])
    return l

def findOptions(printer):
    j=""
    with open("jsons/"+printer+".json", "r") as j_file:
        for line in j_file:
            j+=line
    jj=json.loads(j)
    return jj

def okPages(string):
    final_string=""
    for i in range(len(string)):
        c=string[i]
        if c!=' ':
            final_string+=c
        if not(c.isdigit()) and c!='-' and c!=',':
            return [False, ""]
    return [True, final_string]

def addDate(i, s):
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
    print(path.join(settings.MEDIA_ROOT, f))
    return path.join(settings.MEDIA_ROOT, f)




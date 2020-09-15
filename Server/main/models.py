from django.db import models
from main.utils import addDate

class printFormModel(models.Model):
    ID=models.AutoField(primary_key=True)
    direction=models.CharField(max_length=255, blank=False)
    color=models.CharField(max_length=255, blank=False)
    nCopies=models.PositiveIntegerField(blank=False)
    pages=models.CharField(max_length=255, blank=False)
    File=models.FileField(blank=False, upload_to=addDate)

    def __str__(self):
        print(self.color)
        if self.pages=="Tutte":
            return ("lp -o "+self.direction+" -oOutputMode="+self.color+" -n "+str(self.nCopies))
        else:
            return ("lp -o "+self.direction+" -oOutputMode="+self.color+" -n "+str(self.nCopies)+" -P "+str(self.pages))
            
    def command (self):
        return (str(self)+" "+str(self.File))

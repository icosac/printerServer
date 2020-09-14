from django import forms

from main.models import printFormModel
from main.utils import findPrinters, findOptions, okPages

class pageForm(forms.ModelForm):
    direction=forms.ChoiceField(required=True, label="Orientamento")
    color=forms.ChoiceField(required=True, label="Colore")
    nCopies=forms.IntegerField(required=True, label="Numero di copie", initial=1)
    pages=forms.CharField(max_length=255, label="Pagine da stampare", initial="Tutte")
    File=forms.FileField(required=True)
    printer=""

    def __init__ (self, *args):
        super().__init__(*args)

        self.fields['direction'].choices=[["vertical", "Verticale"],["landscape", "Orizzontale"]]

        self.printer=findPrinters()[0]
        options=findOptions(self.printer)
        self.fields['color'].choices=[(options['colors'][i], options['colors'][i]) for i in range(len(options['colors']))]

    def clean(self):
        cd=self.cleaned_data

        direc=cd.get("direction")
        if direc!="vertical" and direc!="landscape":
            raise forms.ValidationError("Orientamento sbagliato")
        col=cd.get("color")
        if col not in findOptions(self.printer)['colors']:
            raise forms.ValidationError("Colore non supportato")
        nCop=cd.get("nCopies")
        if nCop<1 or nCop>20:
            raise forms.ValidationError("Numero di copie minore di 0 o troppo alto (>20)")
        ps=cd.get("pages")
        [b, s]=okPages(ps)
        if ps!="Tutte" and not(b):
            raise forms.ValidationError("Il formato delle pagine da stampre non è corretto")
        else:
            self.pages=s
    
    def save(self, commit=True):
        instance=super(pageForm, self).save(commit=False)
        f=self['File'].value()
        if commit:
            instance.save()
        return instance

    class Meta:
        model=printFormModel
        fields = ("direction", "color", "nCopies", "pages", "File")



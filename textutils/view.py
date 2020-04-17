# I have crea=te the file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analayze(request):
   #Get the text
   djtext = (request.POST.get('text','default'))

   #Chacking the chackbox value
   removepunc = request.POST.get('removepunc', 'off')
   fullcaps = request.POST.get('fullcaps','off')
   newlineremover = request.POST.get('newlineremover','off')
   extraspaceremover = request.POST.get('extraspaceremover','off')
   charectorcounter = request.POST.get('charectorcounter','off')

   #Check removepunccheckbox is on
   #Check removepunccheckbox is on
   if removepunc == 'on':
       punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
       analayzed1 = ""

       for char in djtext:
           if char not in punctuations:
               analayzed1 = analayzed1 + char
       params1 = {'purpose1':'Changr To Uppercase','analayzed_text1':analayzed1}
       return render(request,'analayze.html',params1)
       # returning the error if Check is if not on


   #Checking the uppercasechackbox is on
   if(fullcaps == 'on'):
       analayzed2 = ""

       for char in djtext:
           analayzed2 = analayzed2 + char.upper()
       params2 = {'purpose2': 'Changr To Uppercase', 'analayzed_text2': analayzed2}
       return render(request,'analayze.html',params2)
   # returning the error if Check is if not on


   if newlineremover=='on' :
       analayzed3 = ""

       for char in djtext:
           if char !="\n":
                analayzed3 = analayzed3 + char.upper()
       params3 = {'purpose3': 'New Line Remover', 'analayzed_text3': analayzed3}
       return render(request, 'analayze.html', params3)
       # returning the error if Check is if not on


   if extraspaceremover == "on":
       analayzed4 = ""

       for index,char in enumerate(djtext):
           if djtext[index] == " " and djtext[index+1] == " ":
               pass
           else:
               analayzed4 = analayzed4 + char.upper()
       params4 = {'purpose4': 'Extra Space Remover', 'analayzed_text4': analayzed4}
       return render(request, 'analayze.html', params4)
       # returning the error if Check is if not on


   if  charectorcounter == "on":
       analayzed5 = 0

       for char in (djtext):
           if char !=" ":
               analayzed5 = analayzed5 + 1
       params5 = {'purpose5': 'Charector Counter', 'analayzed_text5': analayzed5}
       return render(request, 'analayze.html', params5)

       # returning the error if Check is if not on

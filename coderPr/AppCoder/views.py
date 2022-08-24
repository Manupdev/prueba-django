from django.shortcuts import render

from AppCoder.models import Familia

def familiares(request):
    familiar1 = Familia(nombre = 'Manuel',edad = 27 ,fecha = '1995-07-07' )
    familiar1.save()
    

    familiar2 = Familia(nombre = 'Santiago',edad = 25 ,fecha = '1996-09-23' )
    familiar1.save()
    

    familiar3 = Familia(nombre = 'Belen',edad = 23 ,fecha = '1999-04-13' )
    familiar1.save()
    contexto = {
        'familiar1' : familiar1,
        'familiar2' : familiar2,
        'familiar3' : familiar3
    }



    return render(request, 'flia.html', contexto)

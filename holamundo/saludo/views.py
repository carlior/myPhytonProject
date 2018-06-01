from django.shortcuts import render #importamos render de django

# Create your views here.

def saludo(request):
	nombre = "Israel"
	blog = "https://www.uno-de-piera.com"
	tupla = (1,2,3,4,5,6,7,8,9,10)
	context = {
    	'saludo': 'hola que ase', 
    	'tupla':tupla,
    	'nombre': nombre,
    	'blog': blog
    }
    # devolvemos los datos a la vista saludo.html para printarlos
	return render(request, 'saludo.html', context)
from django.shortcuts import render

# Create your views here.
layout="""

<h1>Practica: Evalucion de Capacidad 3</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Integrantes</a>
    </li>
    <li>
        <a href="/rango2/10/15">Mostrar Numeros [a,b]</a>
    </li>
</ul>
<hr/>

    


"""


def inicio(request):
    mensaje="""
    
    <h1>CURSO: LENGUAJE DE PROGRAMACION 3</h1>
    <h2>INTEGRANTES:</h2>
    <li>
        <a>Tinoco Aguilar Victor</a>
    </li>
    <li>
        <a>Artega Ciprian Jeanpaul</a>
    </li>
    <li>
        <a>Zuñiga Aucasi Yessenia</a>
    </li>

    """
    return HttpResponse(layout + mensaje)


def rango2(request,a,b):

    resultado = f"""
    
    <h2>Numeros de [{a},{b}]</h2>
    Resultado:<br>
    <ul>
 
 """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a += 1

    resultado += "</ul"
    return HttpResponse(layout + resultado)

from django.shortcuts import render
from imc.models import Persona

def index(request):

    if request.GET:
        nombre = request.GET.get("nombre")
        altura = float(request.GET.get("altura"))
        peso = float(request.GET.get("peso"))
        print("-----------------------------")
        print(f"{nombre},{altura}, {peso}")
        print("-----------------------------")
        persona = Persona(nombre=nombre, imc_calculado=0)
        persona.calcular_imc(altura, peso)
        persona.save()

        return render (request, "imc/index.html", { "persona": persona } )

    return render(request, "imc/index.html", {})


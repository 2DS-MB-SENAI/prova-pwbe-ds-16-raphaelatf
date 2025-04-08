from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from .forms import ConsultaForm
from .models import Consulta

def listar_medicos(request):
    especialidade = request.GET.get('especialidade', '')
    medicos = Medico.objects.all()
    
    if especialidade:
        medicos = medicos.filter(especialidade=especialidade)
    
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'form': form})

def detalhes_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    return render(request, 'clinica/detalhes_consulta.html', {'consulta': consulta})


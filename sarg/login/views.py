from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from  datetime import datetime
from painel_gmuds.models import GMUDS
from painel_oportunidades.models import OPORTUNIDADES
from painel_projetos.models import PROJETOS
from painel_bugs.models import FalhasEmAberto
from painel_demandas.models import DEMANDAS
from painel_incidentes.models import OcorrenciasEmAberto
from django.db.models import Sum

from login.models import homeImagens

def index(request):
   # return render(request, 'login/login.html')
    if not request.user.is_authenticated:
        return render(request, 'login/login.html')
    else:
        data = datetime.now()
        amount_gmuds = GMUDS.objects.filter(status = 'Ativa').count()
        amount_oportunidades = OPORTUNIDADES.objects.exclude(status='Finalizada').count()	
        amount_projetos = PROJETOS.objects.filter(status__in=[1,2,3,4]).count()
        QUANTIDADE_FALHAS_EM_ABERTO = FalhasEmAberto.objects.count()
        amount_demandas = DEMANDAS.objects.count()
        QUANTIDADE_OCORRENCIAS_EM_ABERTO = OcorrenciasEmAberto.objects.count()
        imagens = homeImagens.objects.filter(status = 'Ativo').all()
        
        return render(request, 'login/index.html',
            {
                'data': data,
                'amount_gmuds': amount_gmuds,
                'amount_oportunidades': amount_oportunidades,
                'amount_projetos': amount_projetos,
                'QUANTIDADE_FALHAS_EM_ABERTO': QUANTIDADE_FALHAS_EM_ABERTO,
                'amount_demandas': amount_demandas,
                'QUANTIDADE_OCORRENCIAS_EM_ABERTO': QUANTIDADE_OCORRENCIAS_EM_ABERTO,
                'imagens': imagens,
            }
        )

def index2(request):
   # return render(request, 'login/login.html')
    data = datetime.now()
    amount_gmuds = GMUDS.objects.filter(status = 'Ativa').count()
    amount_oportunidades = OPORTUNIDADES.objects.count()
    amount_projetos = PROJETOS.objects.count()
    amount_bugs = BUGS.objects.using('monitorcs').filter(tipo='FALHAS_ABERTAS').aggregate(Sum('quantidade'))['quantidade__sum']
    amount_demandas = DEMANDAS.objects.count()
    amount_incidentes = INCIDENTES.objects.using('monitorcs').filter(tipo='CHAMADOS_ABERTOS').aggregate(Sum('quantidade'))['quantidade__sum']		
    return render(request, 'login/index2.html',
        {
            'data': data,
            'amount_gmuds': amount_gmuds,
            'amount_oportunidades': amount_oportunidades,
            'amount_projetos': amount_projetos,
            'amount_bugs': amount_bugs,
            'amount_demandas': amount_demandas,
            'amount_incidentes': amount_incidentes,
        }
    )

def login_user(request):
   if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(username=username, password=password)
       if user is not None:
           if user.is_active:
               login(request, user)
               data = datetime.now()	
               amount_gmuds = GMUDS.objects.filter(status = 'Ativa').count()
               amount_oportunidades = OPORTUNIDADES.objects.exclude(status=4).count()	
               amount_projetos = PROJETOS.objects.filter(status__in=[1,2,3,4]).count()
               QUANTIDADE_FALHAS_EM_ABERTO = FalhasEmAberto.objects.count()
               amount_demandas = DEMANDAS.objects.count()
               QUANTIDADE_OCORRENCIAS_EM_ABERTO = OcorrenciasEmAberto.objects.count()
               imagens = homeImagens.objects.filter(status = 'Ativo').all()
               return render(request, 'login/index.html',
                   {
                        'data': data,			
                        'amount_gmuds': amount_gmuds,
                        'amount_oportunidades': amount_oportunidades,
                        'amount_projetos': amount_projetos,
                        'QUANTIDADE_FALHAS_EM_ABERTO': QUANTIDADE_FALHAS_EM_ABERTO,
                        'amount_demandas': amount_demandas,
                        'QUANTIDADE_OCORRENCIAS_EM_ABERTO': QUANTIDADE_OCORRENCIAS_EM_ABERTO,
                        'imagens': imagens,	
                   }
               )
           else:
               return render(request, 'login/login.html', {'error_message':'Your account has been disabled'})
       else:
           return render(request, 'login/login.html', {'error_message': 'Login invalido'})
   return render(request, 'login/login.html')

def logout_user(request):
   logout(request)
   form = UserForm(request.POST or None)
   context = {
       "form": form,
   }
   return render(request, 'login/login.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login/login.html', {'success_message': 'Conta criada com sucesso! Digite suas credenciais acima.'})
    context = {
        "form": form,
    }
    return render(request, 'login/register.html', context)

def homeCarroussel(request):
    data = datetime.now()
    imagens = homeImagens.objects.filter(status = 'Ativo').all()
    return render(request, 'login/index2.html',
        {
            'data': data,
            'imagens': imagens,
			
        }
    )
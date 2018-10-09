# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from painel_gmuds.models import GMUDS

@login_required(login_url='/login')
def ShowGmuds(request):
    from datetime import datetime
    data = datetime.now()	
    #Gmuds = GMUDS.objects.filter(status = 'Ativa').values()
    Gmuds = GMUDS.objects.all()
    amount_gmuds = GMUDS.objects.filter(status = 'Ativa').count()
    return render(request, 'painel_gmuds/gmuds.html',
        {
            'Gmuds': Gmuds,
			   'data': data,
			   'amount_gmuds': amount_gmuds,
        })
def ShowGmuds_tv(request):
    from datetime import datetime
    data = datetime.now()
    #Gmuds = GMUDS.objects.filter(status = 'Ativa').values()
    Gmuds = GMUDS.objects.all()
    return render(request, 'painel_gmuds/gmuds_tv.html',
        {
            'Gmuds': Gmuds,
            'data': data,
        })


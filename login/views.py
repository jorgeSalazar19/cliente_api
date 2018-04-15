from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests
from social_django.models import UserSocialAuth
import twitter, json
from django.conf import settings
from django.utils.html import escape
from sodapy import Socrata
import pandas as pd
from .models import *
import plotly
import plotly.offline as opy
import plotly.plotly as py
import plotly.graph_objs as go

def index(request):
    template = loader.get_template('index.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))

def logOut(request):
    if request.user.is_authenticated() or request.user is not None:
        logout(request)
        return redirect('/')


@login_required
def home(request):
    template = loader.get_template('home.html')
    ctx={}
    return HttpResponse(template.render(ctx,request))

@login_required
def ConsultaDatos(request):
    template = loader.get_template('consulta.html')
    departamentos = Departamentos.objects.all()
    if request.method == 'GET':
        ctx = {
            'departamentos' : departamentos,
        }
        return HttpResponse(template.render(ctx,request))

    if request.method == 'POST':
        client = Socrata("www.datos.gov.co", "5yzK70sZPLjXhV8ENN4xSiV29", username="jorgemsm12316@utp.edu.co" , password="Jorge970208" )
        departamento = request.POST.get('departamento')
        dia =request.POST.get('dia') 
        departamento = departamento.upper()
        results = client.get("w9k9-bn7g", limit=700)
        results_df = pd.DataFrame(results)
        lista = results_df[(results_df['departamento']==departamento) & (results_df['d_a']==dia)]

        lista1 = results_df[(results_df['departamento']==departamento) & (results_df['d_a']=='Lunes')]
        lista2 = results_df[(results_df['departamento']==departamento) & (results_df['d_a']=='Martes')]
        lista3 = results_df[(results_df['departamento']==departamento) & (results_df['d_a']=='Miercoles')]
        lista4 = results_df[(results_df['departamento']==departamento) & (results_df['d_a']=='Jueves')]
        lista5 = results_df[(results_df['departamento']==departamento) & (results_df['d_a']=='Viernes')]

        plotly.tools.set_credentials_file(username='jorgesalazar19', api_key='8mK4qbSqP7UqPUNLQFIc')
        plotly.tools.set_config_file(world_readable=True)

        labels=['Lunes','Martes','Miercoles','Jueves' , 'Viernes']
        values=[len(lista1.index),len(lista2.index),len(lista3.index),len(lista4.index),len(lista5.index)]
        trace=go.Pie(labels=labels,values=values)
        div = opy.plot([trace], auto_open=False , output_type='div')


        lista = lista.rename(columns={   
                    '':'id' ,
                    'barrio' : 'Barrio',
                    'c_digo_dane' : 'Codigo Dane',
                    'cantidad' : 'Cantidad',
                    'clase_de_sitio' : 'Clase de Sitio',
                    'd_a' : 'Día',
                    'departamento' : 'Departamento',
                    'fecha' : 'Fecha',
                    'hora' : 'Hora',
                    'municipio': 'Municipio',
                    'zona' : 'Zona'

                  })
        lista_table = lista.to_html(classes='table' , justify='center', columns=['Barrio' , 'Cantidad' , 'Clase de Sitio' , 'Día' , 'Departamento' , 'Fecha' , 'Municipio'] , col_space=1)

    ctx = {
            'departamentos' : departamentos,
            'table' : lista_table,
            'grafica' : div,
    }
    return HttpResponse(template.render(ctx,request))

@login_required
def grafica(request):
    template = loader.get_template('grafica.html')
    ctx = {}
    return HttpResponse(template.render(ctx,request))
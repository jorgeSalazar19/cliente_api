from django.contrib import admin
from django.conf.urls import url , include

from login.views import *

urlpatterns = [
	url('', include('social.apps.django_app.urls' , namespace='social')
		),
    url('admin/', admin.site.urls),

    url(r'^$', index , name='index' ),

    url(r'^logout/' , logOut , name='logout' ),

    url(r'^home/' , home , name='home' ),

    url(r'^Consulta_datos/' , ConsultaDatos , name='consulta' ),
   
    url(r'^Graficar_datos/' , grafica , name='grafica' ),
   
]

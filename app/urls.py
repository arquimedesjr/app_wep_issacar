from django.conf.urls import url

from views.jovem_views import *
from .views.login_views import *
from .views.relatorio_views import *
from .views.index_view import *

urlpatterns = (

    # login
    url('logar/$', logar, name='logar'),

    #  Dashbord
    url('index/$', index, name='index'),

    url(r'^$', deslogar, name='deslogar'),

    url('lista_jovem/$', lista_jovens_presenca, name='lista_jovens'),

    url(r'^delet_jovem/(?P<pk>[0-9]+)', delete_jovem, name='delete_jovem'),

    url(r'^edit_jovem/(?P<pk>[0-9]+)', editar_jovem, name='edit_jovem'),

    url(r'^presenca_jovem/(?P<pk>[0-9]+)', presenca_jovem, name='presenca_jovem'),

    url('cadastro/$', cadastrarJovem, name='cadastro_jovens'),

    url('relatorio/$', lista_relatorio, name='relatorio'),

    # url('', TemplateView.as_view(template_name='login.html'), name='logar'),

)

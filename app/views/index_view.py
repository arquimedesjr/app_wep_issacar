import itertools
from django.contrib.auth.decorators import login_required

from django.db import connection
from django.shortcuts import render


@login_required
def index(request, template_name="index.html"):
    cursor = connection.cursor()

    cursor.execute('SELECT * from app_relatorio')
    consul_relatorio = cursor.fetchone()
    print(consul_relatorio)

    if consul_relatorio is not '' or consul_relatorio is not None:
        cursor.execute('SELECT qnt_Jovem from app_relatorio WHERE reuniao_id = 1 ORDER by id DESC LIMIT 1')
        result_algo = cursor.fetchone()
        print(result_algo)

        cursor.execute('SELECT qnt_Jovem from app_relatorio WHERE reuniao_id = 2 ORDER by id DESC LIMIT 1')
        result_encontro = cursor.fetchone()
        print(result_encontro)

        cursor.execute('SELECT qnt_Jovem from app_relatorio WHERE reuniao_id = 1 ORDER by id DESC LIMIT 4')
        result_mensal_algo = [i for i in itertools.chain(*cursor.fetchall())]
        result_mensal_algo.reverse()

        cursor.execute('SELECT qnt_Jovem from app_relatorio WHERE reuniao_id = 2 ORDER by id DESC LIMIT 4')
        result_mensal_encontro = [i for i in itertools.chain(*cursor.fetchall())]
        result_mensal_encontro.reverse()
        cursor = connection.cursor()

        cursor.execute('SELECT data from app_relatorio WHERE reuniao_id = 2 ORDER by id DESC LIMIT 4')
        result_mensal_encontro_data = [i.strftime("%d/%m/%y") for i in itertools.chain(*cursor.fetchall())]
        result_mensal_encontro_data.reverse()
        cursor = connection.cursor()

        cursor.execute('SELECT data from app_relatorio WHERE reuniao_id = 1 ORDER by id DESC LIMIT 4')
        result_mensal_algo_data = [i.strftime("%d/%m/%y") for i in itertools.chain(*cursor.fetchall())]
        result_mensal_algo_data.reverse()

    if type(result_encontro) is not tuple or result_encontro is None:
        result_encontro = (0,)

    if type(result_algo) is not tuple or result_algo is None:
        result_algo = (0,)

    print(result_algo)
    print(result_encontro)

    result = result_encontro + result_algo
    r = {'result': result[0], 'result_algo': result[1], 'result_mensal_algo': result_mensal_algo,
         'result_mensal_encontro': result_mensal_encontro,
         'result_mensal_encontro_data': result_mensal_encontro_data,
         'result_mensal_algo_data': result_mensal_algo_data}

    return render(request, template_name, r)


def registrado(request, template_name="registrado.html"):
    return render(request, template_name)

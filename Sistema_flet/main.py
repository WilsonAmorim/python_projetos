import flet as ft
from flet import *

def main(page):
    page.theme_mode = "light",
    dict_values = {
        'contratante': '',
        'medida_judical': '',
        'outra_parte': '',
        'prolabore': '',
        'exito': '',
        'foro': '',
        'data': ''
    }
    
    titulo = Text(value='Gerador de Contrato de Prestação deServiços Advocatícios')
    
    contratante = TextField(label='Nome do Contratante', autofocus=True)
    medida_judicial = TextField(label='Medida Judicial')
    outra_parte = TextField(label='Outra Parte')
    prolabore = TextField(label='Prolabore', prefix_text='R$')
    exito = TextField(label='Exito', suffix_text='%')
    foro = TextField(label='Foro')
    data = TextField(label='Data do Contrato')
    
    botao_gerar = FilledButton(text='Gerar Contrato')
    
    page.add(
        titulo,
        contratante,
        medida_judicial,
        outra_parte,
        prolabore,
        exito,
        foro,
        data,
        botao_gerar
    )
    
ft.app(target=main)
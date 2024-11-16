from flask import Flask, Blueprint, render_template, request  
from models.dados import itens  
import math  # Importa o módulo math (parecido com o do js) para realizar cálculos matemáticos

ItensController = Blueprint('ItensController', __name__)

@ItensController.route('/')
def index():
    # Define o número de itens por página
    tamanho_pagina = 3

    # Calcula o número total de páginas necessárias para exibir todos os itens
    total_paginas = math.ceil(len(itens) / tamanho_pagina)

    # Obtém o número da página atual a partir dos parâmetros da URL. Se não for fornecido, assume como 1.
    pagina = request.args.get('pagina', 1, type=int)

    # Calcula o índice inicial e final para aparecer as divisões da lista
    inicio = (pagina - 1) * tamanho_pagina  # Índice inicial dos itens na página atual
    fim = inicio + tamanho_pagina  # Índice final dos itens na página atual

    # Seleciona a parte da lista correspondente à página atual
    itens_ = itens[inicio:fim]

    return render_template('index.html', itens=itens_, total_paginas=total_paginas, pagina=pagina)

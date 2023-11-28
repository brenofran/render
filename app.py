import webbrowser
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_html = 'prova.html'
caminho_completo = os.path.join(diretorio_atual, arquivo_html)

# Abre o arquivo HTML no navegador padrão
webbrowser.open('file://' + caminho_completo, new=2)

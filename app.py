import webbrowser

arquivo_html = 'prova.html'
caminho_completo = f'https://raw.githubusercontent.com/brenofran/render/main/{arquivo_html}'

# Abre o arquivo HTML no navegador padrão
webbrowser.open('file://' + caminho_completo, new=2)

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return '''
    <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neymar na Copa de 2014</title>
    <style>
        body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            padding: 20px;
            text-align: center;
        }

        section {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
        }

        h1, h2 {
            color: #ff4500;
        }

        p {
            line-height: 1.5;
        }

        a {
            color: #4caf50;
        }
    </style>
</head>
<body>
    <header>
        <h1>Neymar na Copa de 2014</h1>

        <img src="https://s2.glbimg.com/s_LSlTnxag6EN4NiUkYWcoVZvu0=/620x465/s.glbimg.com/jo/g1/f/original/2014/07/04/montagem_1.jpg" alt="Lesão do Neymar na Copa de 2014">

    </header>
    <section>
        <h2>Lesão na Copa de 2014</h2>
        <p>Neymar sofreu uma lesão durante a Copa do Mundo de 2014, que teve um impacto significativo em sua carreira.</p>
        <p>A lesão de Neymar durante a Copa do Mundo de 2014 foi um momento crucial no torneio. O jogador brasileiro sofreu uma fratura na vértebra durante o jogo contra a Colômbia nas quartas de final.</p>

        <p>A lesão ocorreu em 4 de julho de 2014, quando Neymar foi atingido por uma joelhada nas costas pelo jogador colombiano Juan Camilo Zúñiga. A gravidade da lesão impediu Neymar de continuar no torneio, deixando a seleção brasileira sem uma de suas principais estrelas.</p>

        <p>A ausência de Neymar foi profundamente sentida pela equipe brasileira, que acabou perdendo por 7 a 1 para a Alemanha na semifinal, em um dos resultados mais surpreendentes e memoráveis da história da Copa do Mundo.</p>

        <h2>Desafios Após a Lesão</h2>
        <p>Após a lesão na Copa do Mundo de 2014, Neymar enfrentou diversos desafios em sua carreira. A fratura na vértebra, sofrida durante o torneio, não apenas o tirou da competição, mas também teve repercussões significativas em sua trajetória esportiva.</p>
        <p>Neymar passou por um período de recuperação e readaptação física, que demandou cuidados intensivos e atenção especial para retornar ao mais alto nível. Após deixar o Barcelona, transferindo-se para o Paris Saint-Germain (PSG) em 2017, ele enfrentou a pressão e as expectativas associadas à transferência mais cara da história do futebol na época.</p>
        <p>Além disso, lesões ao longo de sua carreira no PSG e desafios físicos apresentaram obstáculos constantes. A busca por sucesso tanto no cenário doméstico quanto nas competições europeias implicou em uma exigência constante de desempenho.</p>
        <p>Apesar desses desafios, Neymar manteve sua influência no cenário internacional, representando a seleção brasileira em várias competições e sendo parte fundamental da conquista da Copa América em 2019. Sua habilidade excepcional, criatividade em campo e resiliência diante de adversidades contribuíram para a continuidade de sua destacada carreira no futebol mundial.</p>            

        <h2>Carreira Antes da Lesão</h2>
        <p>Neymar teve uma carreira brilhante antes da lesão, conquistando grandes marcos, como:</p>
        <ul>
            <li>Participação em clubes brasileiros, como Santos FC.</li>
            <li>Transferência para o Barcelona em 2013.</li>
            <li>Conquista de títulos, incluindo a Copa Libertadores da América e a Recopa Sul-Americana pelo Santos.</li>
            <li>Recebeu prêmios individuais, como o Prêmio Puskas da FIFA em 2011.</li>
            <!-- Adicione mais dados relevantes sobre a carreira anterior à lesão aqui -->
        </ul>

        <h2>Carreira Pós Lesão</h2>
        <p>Mesmo enfrentando adversidades, Neymar continuou a se destacar e alcançou...</p>
        <ul>
            <li>Após a lesão na Copa do Mundo de 2014, Neymar Jr. continuou a sua carreira no futebol com o Barcelona até 2017. Durante esse período, ele ganhou vários títulos, incluindo a Liga dos Campeões da UEFA e a La Liga. Em agosto de 2017, Neymar transferiu-se para o Paris Saint-Germain (PSG) em uma transferência recorde mundial.</li>
            <li>Com o PSG, Neymar teve um impacto significativo na equipe, ajudando a conquistar títulos nacionais, como a Ligue 1, e contribuindo para o sucesso do clube nas competições europeias. No entanto, durante esse período, Neymar também enfrentou algumas lesões que o afastaram de algumas partidas.</li>
            <li>A partir de 2021, Neymar continuou sendo uma peça fundamental para o PSG e também representou a seleção brasileira em várias competições. Em particular, ele participou da Copa América de 2021, onde o Brasil foi coroado campeão, derrotando a Argentina na final.</li>
        </ul>
    </section>
    <footer>
        <p>Para mais informações, visite o <a href="https://pt.wikipedia.org/wiki/Neymar"> site oficial com informações do Neymar</a>.</p>
    </footer>
</body>
</html>

  '''

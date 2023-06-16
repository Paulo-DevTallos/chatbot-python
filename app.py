import os

"""
String formatada é algo semelhante ao que temos com o template string, pois é possível repassar valores dinamicos para sua descrição.
elif - Poupa processamento não permitindo que um if seja executado varias vezes.
Para que o bot seja executado sempre é necessário incluí-lo em um laço de repetição. Assim ao fim de um ciclo de pergintas ele inicia novamente.
"""
# respostas
def process_reply(reply, name):
    if reply == '1':
        print(f'{os.linesep}{name} na minha visão vale muito a pena, isso porque o mercado de tecnologia é um dos que mais cresce no mundo inteiro!{os.linesep}')
    elif reply == '2':
        print(f'{os.linesep}{name} isso sempre irá variar de acordo com o seu esforço e dedicação, do quanto você entrega em seus estudos dia a dia!{os.linesep}')
    elif reply == '3':
        print(f'{os.linesep}{name}, primeiro procure entender o funcionamento da linguagem e sua base, ninguem pode se tornar BOM do dia para a noite, tudo é um processo{os.linesep}')
    elif reply == '4':
        print(f'{os.linesep}{name} {os.linesep}')
    else:
        print('Digite apenas 1, 2, 3, 4')

def start():
    # Apresentar o chatbot
    input('Ola, seja bem vindo ao chatbot do Dev')
    # Pedir o nome
    name = input('Digite o seu nome: ')
    # Pedir o email
    email = input('Agora digite o seu e-mail: ')

    while True:
        # Oferecer o menu de opções
        replies = input(
            f'O que gostaria de saber hoje?{os.
            linesep}[1] - Vale a pena aprender a programar?{os.
            linesep}[2] - Quanto tempo leva para conseguir um emprego como programador?{os.
            linesep}[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?{os.
            linesep}[4] - Onde me recomenda estudar programação para conseguir um emprego?{os.
            linesep}') #(f'Entrega um string formatado' utilizando o module 'os' para quebrar a linha)
        # Processar a resposta enviada
        process_reply(replies, name)

# Assim que iniciar o programa será executada a função start
if __name__ == '__main__':
    start()
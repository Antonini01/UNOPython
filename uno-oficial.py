import random
from time import sleep
print(f'{"---------------":>44}')
print('                              U     N     O')
print(f'{"---------------":>44}')
# fazer suporte a múltiplos idiomas
cartas = { # todas as cartas do jogo
    'vermelho': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+2', '+2','+2', '+2', '<==', '<=='],
    'verde': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+2', '+2', '+2', '+2','<==', '<=='],
    'azul': [0, 1, 2, 3, 4, 5,6, 7, 8, 9, '+2', '+2','+2', '+2', '<==', '<=='],
    'amarelo': [0, 1, 2, 3, 4, 5,6, 7, 8, 9, '+2', '+2','+2', '+2', '<==', '<==']
}
nomes = ['Ana', 'Rafael', 'Rosa', 'Júnior', 'Bia', 'Krikor', 'Nakamura', 'Carlsen', 'Ronaldinho',
         'O maioral', 'Carcomido', 'Jéssica', 'Ambulante'] # dá nome aos bots
retorno = { # responsável por guardar as cartas jogadas que serão embaralhadas quando o dicionário cartas ficar vazio
    'vermelho': [],
    'verde': [],
    'azul': [],
    'amarelo': []
}
def formata(): # detalhe estético
    sleep(1)
    print('Aguarde enquanto estamos preparando tudo...', end = '')
    sleep(2.4)
sleep(1)
print('Bem vindo ao UNO!', end = ' ')
sleep(1.5)
while True:
    try: # tratamento de erros
        jogadores = int(input('Quantos jogadores irão participar? '))
        break
    except ValueError:
        print('Entrada inválida! Tente novamente')
        sleep(1)
print('Ótimo!', end = ' ')
sleep(1)
botv = 0
inverter = False
if jogadores == 1:
    print('Um jogador.', end = ' ')
    formata()
elif jogadores == 2 or jogadores == 3:
    print(f'{jogadores} jogadores.', end = ' ')
    sleep(1)
    botv = str(input('Quer jogar contra bot [S/N]? ')).lower()
    while botv not in 'sn':
        print('Digite uma letra válida!\n')
        botv = str(input('Quer jogar contra bot [S/N]? ')).lower()
    formata()
else:
    print(f'{jogadores} jogadores.', end = ' ')
    sleep(1)
    formata()
while True: # Responsável por não permitir que a primeira carta do topo do descarte seja especial
    chave = random.choice(list(cartas.keys()))
    valor = random.randint(0,9)
    numero = cartas[chave][valor]
    if numero == int(numero):
        break
del(cartas[chave][valor])
print()
def aparencia(): # Função que atualiza a carta do topo do descarte
    print('-'*37)
    print(f'carta no topo do descarte: {chave} {numero}')
    print('-'*37)
def rodada(i):
    sleep(1)
    print(f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= RODADA {i} =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
def distribuicartas(): # será utilizado na linha 337, na função gerador_da_mao_de_todos
    i = 0
    lista = []
    while i < 7:
        chave = random.choice(list(cartas.keys())) # seleciona cartas aleatórias do dicionário cartas
        if len(cartas[chave])>0:
            valor = random.choice(cartas[chave])
            tupla = (chave, valor)
            lista.append(tupla) # adiciona essas cartas na mão do jogador
            cartas[chave].remove(valor) # remove a carta selecionada do dicionário cartas
            i += 1
    return lista
def estrategia(lista,adicao): # Estratéia para jogar a melhor carta +2 que o jogador tiver
    i = 0 
    maior = 0
    while i < len(lista):
        if lista[i][1] == numero:
            estrategia = lista[i][0]
            j = 0
            teste = 0
            while j < len(lista):
                if lista[j][0] == estrategia: # analisa quantas cartas da mesma cor o usuário tem
                    teste += 1 # guarda essa quantidade na variável teste
                j += 1
            if teste >= maior: # a carta que tiver o maior valor de teste
                maior = teste 
                chave = estrategia # vai ser a nova chave (cor) do código
        i += 1
    i = 0
    while i < len(lista):
        if lista[i][0] == chave and lista[i][1] == numero:
            lista.pop(i) # retira a carta da mão do jogador
            retorno[chave].append(numero) # guarda essa carta no dicionário retorno
            sleep(1)
            print(f'Carta jogada foi {chave} +2') 
            adicao += 2 # soma +2
            break
        i += 1   
    return lista, adicao, chave 
def exibir_cartas(jogador, lista): # responsável por mostrar a mão do jogador em todas as rodadas
    i = 0
    sleep(1)
    print(f'Jogador {jogador}')
    print('Suas cartas: ', end = '')
    while i < len(lista):
        cor, num = lista[i] # cor e num recebem as informações da tupla dentro da lista
        if i < len(lista) - 1:
            end_virgula = ', '
        else:
            end_virgula = ''
        print(f'{cor} {num}', end = end_virgula)
        i +=1  
    print()

def jogaram_mais2_antes_de_mim(lista, adicao, jogador, chave, robo):  # robo é um booleano, pode ser False ou True para indicar se é humano ou boyt
    tem_mais2 = False # booleano responsável por ativar ou não parte do código, caso o usuário tenha ou não uma carta +2 
    possivel_pegar_cartas = False # caso seja True, responsavel por fazer o usuário comprar as cartas do +2
    i = 0
    while i < len(lista): # verifica se o usuário tem +2 mesmo
        if lista[i][1] == numero: 
            tem_mais2 = True # torna o booleano verdadeiro
        i += 1
    if tem_mais2 == False: # se não tiver +2
        sleep(1)
        possivel_pegar_cartas = True # torna esse booleano verdadeiro e compra forçadamente as cartas pro usuário
        if robo  == False:
            print('\033[4;31;40mVocê não tem carta +2.\033[m')  # essa mensagem só aparece para humanos, não para bots
    else: # se tiver +2
        if robo == True: # se for bot
            lista, adicao, chave = estrategia(lista,adicao)
        else: # se for humano
            controle = False # esse booleano é inicializado na função player como True e qnd é False impede que o input escolha (linha 217) seja executado
            sleep(1) # ou seja, o suário não precisa/deve escolher uma carta se passou por aqui
            rebater = str(input('\nDeseja jogar a carta +2 [S/N]? ')).lower()
            while rebater not in 'sn':
                sleep(1)
                print('Digite uma entrada válida.')
                sleep(1)
                rebater = str(input('Deseja jogar a carta +2 [S/N]? ')).lower()
            if rebater == 'n': # se o usuário não quiser jogar a carta +2
                possivel_pegar_cartas = True # torna esse booleano verdadeiro e compra forçadamente as cartas pro usuário
            else: # se quiser jogar o +2
                lista, adicao, chave = estrategia(lista,adicao) # a função estrategia decide qual a melhor escolha e joga
    if possivel_pegar_cartas == True: # responsavel por fazer o usuário comprar as cartas do +2
        controle = False # de novo, o usuário não precisa/deve escolher uma carta se passou por aqui
        sleep(1)
        print(f'{adicao} cartas foram adicionadas à mão do jogador {jogador}')
        i = 0
        while i < adicao: # adiciona o tanto de cartas que for necessário ao jogador
            if len(cartas['vermelho']) != 0 or len(cartas['verde']) != 0 or len(cartas['azul']) != 0 or len(cartas['amarelo']) != 0: 
                chave1 = random.choice(list(cartas.keys())) 
                if len(cartas[chave1])>0:
                    valor1 = random.choice(cartas[chave1])                       
                    tupla1 = (chave1, valor1)
                    lista.append(tupla1)                        
                    cartas[chave1].remove(valor1) 
                    i += 1
            else:
                sleep(1)
                print('\n\n\033[4;31;40mNão foi possível pegar todas as cartas por insuficiência de cartas no baralho.\033[m')
                break
        adicao = -1 # responsável por informar que o jogador anterior já comprou as cartas forçadamente. Vai auxiliar na parte em que o jogador decide se quer jogar uma carta especial ou normal de cor semelhante 
    if robo == False: # se for humano
        return adicao, controle, chave, numero, lista
    else: # se for bot
        return adicao, chave, numero, lista

def carta_jogada_eh_valida(escolha, lista, chave, numero, k, execucao, adicao1, inverter1): # verifica se a carta existe na mão do usuário ou se condiz com a carta do topo do descarte
    global inverter, adicao # adicao1 e inverter1 linha 233 e 235
    i = 0
    while i < len(lista):
        if (escolha[0] == lista[i][0] and escolha[1] == lista[i][1]) and (escolha[0] == chave or escolha[1] == numero): # aqui é feita essa analise
            execucao = True # se encontrar uma carta válida, execucao recebe True que serve para encerrar o loop infinito da funcao player e passar a vez para o próximo jogador
            chave = escolha[0] # chave receberá a nova cor da carta jogada que será apresentada no topo do descarte
            numero = escolha[1] # numero receberá o novo número da carta jogada que será apresentada no topo do descarte
            lista.pop(i)
            retorno[chave].append(numero)  # adiciona essa carta no dicionário retorno
            if k == -3: # Inicializado na funçao jogada normal, responsável por dizer que o jogador anterior já comprou obrigatoriamente as cartas do +2
                adicao = 0 # e zerar a variável adicao ()
                if escolha[1] == '+2': 
                    adicao = 2 
                    adicao1 = False
            if adicao1 == True:
                adicao += 2
            if inverter1 == True: # lógica do inverter
                if inverter == False:
                    inverter = True
                elif inverter == True:
                    inverter = False
            break
        else:
            execucao = False # É inicializado na função player. Se nenhuma carta for encontrada, execucao recebe False. linha 263
            i += 1 # i recebe ele mesmo + 1 caso não encontar uma carta válida
    return lista, chave, numero, execucao, adicao, inverter
def uno(lista):
    if len(lista) == 1:
        sleep(1)
        print('\033[4;31;40mUNO!\033[m')
        sleep(0.8)
        print('Estou por uma\n')
def jogada_normal(lista, chave, numero, execucao, controle, retorno, k):
    global inverter, adicao
    if adicao == -1:
        k = -3 # serve pra dizer que o anterior já comprou obrigatoriamente as cartas do +2 e zerar adicao, como na função acima
        print('\n\033[4;32;40mJogue uma carta especial ou uma normal de cor semelhante.\033[m\n ')
        sleep(1)
    if controle == True: # como já foi dito, as linhas 140 e 153 tornam controle False e impedem a linha seguinte
        escolha = str(input('Jogue uma carta ou digite "pegar" para pegar uma carta: ')).split() # escolha da carta pelo usuário. Guardada numa lista (função split)
    if len(escolha) == 1:
        if escolha[0] == 'pegar': # pegar umas carta
            while True:
                chave1 = random.choice(list(cartas.keys())) 
                valor1 = random.choice(cartas[chave1])
                tupla1 = (chave1, valor1)
                lista.append(tupla1)
                cartas[chave1].remove(valor1)
                print(f'Você pegou {chave1} {valor1}')
                sleep(1)
                break
# =============================================================================
#         elif escolha[0] == 'cor': preciso pensar em como colocar isso no dicionario cartas
#             print('Altere a cor do topo para:\n1. Vermelho\n2.Verde\n3. Azul\n4. Amarelo')
# =============================================================================
    elif len(escolha) == 2: # necessário para não dar erro quando o usuário não digitar nada em escolha
        if escolha[1].isdigit(): # se o escolha[1] digitado pelo usuário for um digito
            escolha[1] = int(escolha[1]) # escolha[1] recebe o tipo inteiro dele mesmo e executa a função acima (linha 176)
            lista, chave, numero, execucao, adicao, inverter = carta_jogada_eh_valida(escolha, lista, chave, numero,k, execucao, False, False)
        elif escolha[1] == '+2': # se o escolha[1] digitado pelo usuário for +2, executa função da linha 176
            lista, chave, numero, execucao, adicao, inverter = carta_jogada_eh_valida(escolha, lista, chave, numero,k, execucao, True, False)
        elif escolha[1] == '<==': # se o escolha[1] digitado pelo usuário for <==, executa função da linha 176
            lista, chave, numero, execucao, adicao, inverter = carta_jogada_eh_valida(escolha, lista, chave, numero,k, execucao, False, True)
        #elif escolha[1] == 'bk':
            
    else: # para qualquer escolha com tamanho fora do intervalo fechado entre 1 e 2
        execucao = False # execucao recebe False. Na função player, ele que diz que a carta digitada não pode ser jogada linha 263
    return lista, chave, numero, adicao, execucao, inverter
def monte_acabou(cartas,retorno): # se o dicionário cartas estiver vazio, é aqui que o dicionário retorno entra em ação
    if len(cartas['vermelho']) == 0 and len(cartas['verde']) == 0 and len(cartas['azul']) == 0 and len(cartas['amarelo']) == 0 :
        print('\nAs cartas do monte acabaram.')
        print('Vamos embaralhar as que já foram jogadas.\n')
        for cor in cartas: 
            cartas[cor] += retorno[cor] # soma do dicionario cartas com o retorno, retornando todas as cartas já jogadas ao monte principal
    return cartas
def player(jogador, lista, retorno): # aqui é a função principal do jogador humano. Aqui organiza tudo
    global chave, numero, adicao, inverter
    k = 0
    aparencia() # mostra a carta do topo do descarte
    while True:
        execucao = True # avalia se a carta pode ou não ser jogada. Torna-se False nas linhas 181, 200, 236
        controle = True # impede a variável escolha caso seja False. linhas 140, 153
        encerra = False # serve para encerrar o loop infinito da função jogar_ordem linha 355. Significa que o jogador venceu
        monte_acabou(cartas,retorno) # antes de cada jogador jogar, é verificado se têm cartas no monte principal
        exibir_cartas(jogador, lista) # mostra a mão do jogador
        if numero == '+2' and adicao >= 0: # se o numero do topo do descarte for +2 com adição != -1, obrigatoriamente o jogador tem que jogar +2 ou comprar
            adicao, controle, chave, numero, lista = jogaram_mais2_antes_de_mim(lista, adicao, jogador, chave, False)
        else: # aqui são todas as jogadas normais já elencadas acima
            lista, chave, numero, adicao, execucao, inverter = jogada_normal(lista, chave, numero, execucao,controle, retorno, k)
        if len(lista) == 0: # analisa o tamanho da mao do jogador, se for 0, ganhou 
            print(f'\033[4;32;40mJOGADOR {jogador} GANHOU! PARABÉNS!!!\033[m')
            encerra = True # e encerra se torna True para impedir o loop infinito da função da linha 355 e finalizar o jogo
        if execucao == False: # verificação se a carta jogada é válida. Voltar na linha 250 e ler de novo
            print('\nVOCÊ NÃO PODE JOGAR ESTA CARTA!\n')
            sleep(1)
        else: # se a carta jogada for válida
            uno(lista)
            break # interrompe o loop infinito acima e passa a vez para o próximo jogador 
    return chave, numero, execucao, adicao, encerra, inverter
def PC_jogada_normal(lista, chave, numero, retorno, k, adicao): # bot
    global inverter
    carta_jogada = False # responsável por fazer comprar ou não uma carta
    i = 0
    if adicao == -1: # se o jogador anterior comprou a somatória dos +2
        k = -3 # k recebe - 3
    while i < len(lista) and not carta_jogada :
        if lista[i][0] == chave or lista[i][1] == numero: # pc analisa se tem uma carta válida. A primeira que encontrar, joga
            carta_jogada = True # se torna True e não executa a parte de comprar uma carta
            chave = lista[i][0] # chave receberá a nova cor da carta jogada que será apresentada no topo do descarte
            numero = lista[i][1] # numero receberá o novo número da carta jogada que será apresentada no topo do descarte
            if numero == '+2': 
                if k == -3: # serve pra dizer que o anterior já comprou obrigatoriamente as cartas do +2 e zerar adicao
                    adicao = 0
                adicao += 2 # se o anterior não comprou forçosamente, significa que ou é o primeiro a jogar +2 ou está na sequencia obrigatória de jogar +2
            else: # se puder jogar qualquer outra carta
                adicao = 0 # adicao recebe 0
            if numero == '<==':
                if inverter == False: # logica do inverter
                    inverter = True
                    
                elif inverter == True:
                    inverter = False
            lista.pop(i) # exclui a carta da mão do bot
            retorno[chave].append(numero)
            sleep(1)
            print(f'Jogou a carta {chave} {numero}')
            break
        else: 
            i += 1 # i recebe ele mesmo + 1 caso não encontar uma carta válida
    if carta_jogada == False: # comprar uma carta
        while True:
            chave3 = random.choice(list(cartas.keys()))
            if len(cartas[chave3])>0:
                valor3 = random.choice(cartas[chave3])
                tupla3 = (chave3, valor3)
                lista.append(tupla3)
                cartas[chave3].remove(valor3)
                break
        sleep(1)
        print('Comprou uma carta.')   
    return chave, numero, lista, retorno, adicao, inverter, k
def bot(jogador, lista, retorno):
    global chave, numero, adicao, inverter
    encerra = False # serve para encerrar o loop infinito da função jogar_ordem linha 355. Significa que o jogador venceu
    k = 0
    monte_acabou(cartas,retorno) # antes de cada bot jogar, é verificado se têm cartas no monte principal
    sleep(1)
    print(f'Bot {jogador} pensando...')
    if numero == '+2' and adicao >= 0: # se o numero do topo do descarte for +2 com adição != -1, obrigatoriamente o bot tem que jogar +2 ou comprar
        adicao, chave, numero, lista = jogaram_mais2_antes_de_mim(lista, adicao, jogador, chave, 1)
    else:  # aqui são todas as jogadas normais já elencadas acima
        chave, numero, lista, retorno, adicao, inverter, k = PC_jogada_normal(lista, chave, numero, retorno, k, adicao)
    uno(lista)
    if len(lista) == 0: # analisa o tamanho da mao do jogador, se for 0, ganhou 
        print(f'\033[4;32;40m{jogador} VENCEU!\033[m')
        encerra = True # e encerra se torna True para impedir o loop infinito da função da linha 355 e finalizar o jogo
    return chave, numero, adicao, encerra, inverter
def nomebot(nomes, num_bots = 0): # seleciona aleatóriamente os nomes para os bots
    if num_bots != 0:
        nome_aleatorio = []
        i = 0
        while i < num_bots: 
            nome = random.choice(nomes)
            nome_aleatorio.append(nome)
            nomes.remove(nome)
            i += 1
        return nome_aleatorio
def gerador_da_mao_de_todos(): # gera a mão de todo mundo
    maos = []
    if botv == 's':
        i = 0
        while i < jogadores:
            mao = distribuicartas() # utiliza a função da linha 69
            maos.append(mao)
            i +=1
    else:
        i = 0
        while i < 4:
            mao = distribuicartas()
            maos.append(mao)
            i +=1
    return maos
adicao = 0 # soma do +2
maos = gerador_da_mao_de_todos()
def jogar_ordem(jogadores, num_bots=0): # coloca em sequência a ordem dos jogadores. A lógica do inverter está aqui, começa na linha 362
    nome_aleatorio = nomebot(nomes, num_bots)
    i = 1
    while True:
        rodada(i) 
        l = 0 
        while l < jogadores: # jogadores humanos
            chave, numero, execucao, adicao, encerra, inverter = player(l + 1, maos[l], retorno)
            if inverter == False:
                l += 1
                if l == jogadores:
                    if num_bots == 0: # se não tiver bots
                        l = 0 # l voltar pra zero faz com que nao vá pro loop do bot
            else:  # se estiver invertido
                l -= 1
                if l == -1 :
                    if num_bots == 0:
                        l = (jogadores - 1)
                    else: # se tiver bot
                        break # interrompe quando l == -1 e passa a vez pro bot 
            if encerra == True: # se alguém ganhar
                break # interrompe o loop acima
        print()
        if encerra == True:  # se alguém ganhar
            break # interrompe o loop infinito
        if inverter == False: # começa a lógica do bot
            j = (4 - num_bots)
            c = 0
        else:
            j = len(maos) - 1
            c = len(nome_aleatorio) - 1        
        while j < len(maos): # bots
            chave, numero, adicao, encerra, inverter = bot(nome_aleatorio[c], maos[j], retorno)
            if inverter == False:   
                j +=1
                c += 1
                if j == jogadores:
                   j = (4 - num_bots)
                   c = 0
            else:
                j -= 1
                c -= 1
                if j == 0:
                    break
            print()
            if encerra == True:
                break            
        if encerra == True:
            break
        i += 1 # Atualiza a rodada   
if jogadores == 1:
    jogar_ordem(1,3) # 1 humano, 3 bots
elif jogadores == 2:
    if botv == 'n':
        jogar_ordem(2) # 2 humanos e 0 bots
    else:
        jogar_ordem(2, 2) # tenho q corrigir o bug pra qnd tem menos de 3 bots
elif jogadores == 3:
    if botv == 'n':
        jogar_ordem(3)
    else:
        jogar_ordem(3, 1) 
elif jogadores == 4:
    jogar_ordem(4)
    
    
       

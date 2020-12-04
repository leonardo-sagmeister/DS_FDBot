import logging
import random
import os.path
from time import sleep
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = input("Insira o TOKEN do seu BOT: ")


#------------------IMPORTANTE--------------------
#PRA FACILITAR NOSSA VIDA, BASTA DAR CTRL+F E BUSCAR O QUE DESEJA:
# Para ir para a rodada 1 procure por rodada1
# Para ir para a rodada 2 procure por rodada2 e por aí vai
#Se tiverem ideias para atalhos, podem botar =D
#------------------IMPORTANTE--------------------


#-------------CRIAÇÃO DE ARQUIVOS TODOS JUNTOS PARA NOS AJUDAR
if os.path.exists('rodada.txt') == False:
    arquivo = open('rodada.txt', 'w+')
    arquivo.close()
if os.path.exists('Usuariosvidas.txt') == False:
    arquivo = open('Usuariosvidas.txt', 'w+')
    arquivo.close()
# if os.path.exists('Usuarioscartas.txt') == False:
#     arquivo = open('Usuarioscartas.txt', 'w+')
#     arquivo.close()
if os.path.exists('Jogadas.txt') == False:
    arquivo = open('Jogadas.txt', 'w+')
    arquivo.close()
if os.path.exists("usuariosfez.txt") == False:
    arquivo = open('usuariosfez.txt', 'w+')
    arquivo.close()
if os.path.exists('vezjogada.txt') == False:
    arquivo = open('vezjogada.txt', 'w')
    arquivo.close()
if os.path.exists('Usuariospalpites.txt') == False:
    arquivop = open('Usuariospalpites.txt', 'w+')
    arquivop.close()
if os.path.exists('ousuarios.txt') == False:
    arquivoo = open('ousuarios.txt', 'w+')
    arquivoo.close()
if os.path.exists('Usuarios.txt') == False:
    arquivo = open("Usuarios.txt", "w+")
    arquivo.close()
if os.path.exists('vez.txt') == False:
    arquivo = open('vez.txt', 'w+')
    arquivo.write("1")
    arquivo.close()
if os.path.exists('arquivoGanhador.txt') == False:
    arquivo = open("arquivoGanhador.txt", "w+")
    arquivo.close()
#------------------APAGANDO CONTEÚDO DOS ARQUIVOS PARA NAO PRECISAR FICAR APAGANDO TODAS AS VEZES
if os.path.exists('rodada.txt') == True:
    arquivo = open('rodada.txt', 'w+')
    arquivo.truncate(0)
    arquivo.close()
if os.path.exists('Usuariosvidas.txt') == True:
    arquivo = open('Usuariosvidas.txt', 'w+')
    arquivo.truncate(0)
    arquivo.close()
# if os.path.exists('Usuarioscartas.txt') == True:
#     arquivo = open('Usuarioscartas.txt', 'w+')
#     arquivo.truncate(0)
#     arquivo.close()
if os.path.exists('Jogadas.txt') == True:
    arquivo = open('Jogadas.txt', 'w+')
    arquivo.truncate(0)
    arquivo.close()
if os.path.exists("usuariosfez.txt") == True:
    arquivo = open('usuariosfez.txt', 'w+')
    arquivo.truncate(0)
    arquivo.close()
if os.path.exists('vezjogada.txt') == True:
    arquivo = open('vezjogada.txt', 'w')
    arquivo.truncate(0)
    arquivo.close()
if os.path.exists('Usuariospalpites.txt') == True:
    arquivo = open('Usuariospalpites.txt', 'w+')
    arquivo.truncate(0)
    arquivo.close()
if os.path.exists('ousuarios.txt') == True:
    arquivo = open('ousuarios.txt', 'w+')
    arquivo.truncate(0)
    arquivo.close()
if os.path.exists('Usuarios.txt') == True:
    arquivo = open("Usuarios.txt", "w+")
    arquivo.truncate(0)
    arquivo.close()
if os.path.exists('vez.txt') == True:
    arquivo = open('vez.txt', 'w+')
    arquivo.write("1")
    arquivo.close()
if os.path.exists('arquivoGanhador.txt') == True:
    arquivo = open('arquivoGanhador.txt', "w+")
    arquivo.truncate(0)
    arquivo.close()


def somapalpites():
    spalpite = 0
    arqpalpites = open("Usuariospalpites.txt", "r")
    for linha in arqpalpites:
        palpite = linha.split()
        spalpite += int(palpite[1])
    arqpalpites.close()
    somadepalpites = open("spalpites.txt", 'w+')
    somadepalpites.write(str(spalpite))
    somadepalpites.close()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Atribuindo o código da figurinha as variaveis de cartas
zap = "CAACAgEAAxkBAAOjX40im97tNxuWNUKwOU8-5vyYAAE6AAIhAAOCFRY2Ezylu98G3FIbBA"
copas = "CAACAgEAAxkBAAOkX40iuVC-sD4RxSxxWknzswbPmikAAg4AA4IVFjadPcs09HwT6xsE"
espadilha = "CAACAgEAAxkBAAO1X43J8Gqs5fML2F4Qbvv5ScBMMwgAAhEAA4IVFjaCjVIgaC0x-BsE"
ouros7 = "CAACAgEAAxkBAAPBX43LuyEOXiLKYs1oHaltlTjGENkAAg8AA4IVFjZOjRImz1DqhBsE"
joker = "CAACAgEAAxkBAAPAX43Lt-pvzdh34GkKtNgXrRmtL04AAhQAA4IVFjY0nFnyVFB2thsE"
paus3 = "CAACAgEAAxkBAAO_X43LamqbvpIj-PAr18qwcVuvW2oAAg0AA4IVFjaW4avxCN1XcxsE"
copas3 = "CAACAgEAAxkBAAO-X43LaNnSJjF89gY5gcQFMdqYT-AAAgoAA4IVFjYUWC1QSdQhChsE"
espadas3 = "CAACAgEAAxkBAAO9X43LZqZKPJbJNsZf8VzlEwHjVDoAAgsAA4IVFjZ__wMHThM67xsE"
ouros3 = "CAACAgEAAxkBAAO8X43LZDWFEet2pYK_lEhpUKoU4RcAAgwAA4IVFjbwaLMp1YeJFhsE"
paus2 = "CAACAgEAAxkBAAO7X43KpLkrJfSdv99imAi7wufxWBQAAgkAA4IVFjZTLQnSuERnVRsE"
copas2 = "CAACAgEAAxkBAAO6X43Kob570RlEDS0ByiPGjN8jpukAAgYAA4IVFjag0l3hWjeLaxsE"
espadas2 = "CAACAgEAAxkBAAO5X43KnmVXF3YGFrieZ1_TvfqKEJcAAgcAA4IVFjYPq6yKzjZRUhsE"
ouros2 = "CAACAgEAAxkBAAO4X43Km2KVTYCog2j2ij3Mssx2bBQAAggAA4IVFjZKI5muQ65F_BsE"
aspaus = "CAACAgEAAxkBAAO3X43J93iQH2fUs8nj4gZvEZUU8g8AAhMAA4IVFjbzqnpsekpO9RsE"
ascopas = "CAACAgEAAxkBAAO2X43J9Jy25nLigjyYJ2Xn_FMp1XgAAhAAA4IVFjayn7taqb_SQRsE"
asouros = "CAACAgEAAxkBAAO0X43J7PY2Kjrt01Q_l9xPhsQsQ6kAAhIAA4IVFjZY5T-EbvfgKhsE"
kpaus = "CAACAgEAAxkBAAOzX43Jhx6Ipg5cY8e3hU9DWRzFbMsAAhwAA4IVFjZGDfDS2hm28BsE"
kcopas = "CAACAgEAAxkBAAOyX43JhLaJtdwivesqUgPI16QWG9AAAhkAA4IVFjZgDwABp0RVogMbBA"
kespadas = "CAACAgEAAxkBAAOvX43ILuwDcNel-OY-bwQNwOAM33gAAhoAA4IVFjaDJFm0rb14BxsE"
kouros = "CAACAgEAAxkBAAPCX43Pi2EqxTZbg1DcXojoVUhSHywAAhsAA4IVFjaN5tjjcoNjGhsE"
jpaus = "CAACAgEAAxkBAAOtX43HSe83D2AjO7WNMji7GjyKQEEAAh8AA4IVFjZ_9lyldZnmyBsE"
jcopas = "CAACAgEAAxkBAAOsX43HRWjc8O9e-V4_Kzn9KVm74pUAAh0AA4IVFjYyR1X0LWcBmxsE"
jespadas = "CAACAgEAAxkBAAOrX43HRASuiB-AzIw-us6FG_Cfpi8AAiAAA4IVFjbFXeRcjq_OxRsE"
jouros = "CAACAgEAAxkBAAOqX43HPwV7sphHSdh2R_--fc8LQ2YAAh4AA4IVFjZbm1aHv01wchsE"
qpaus = "CAACAgEAAxkBAAOpX40sckXcTuBRRaEyzlfo8fSUxgUAAhgAA4IVFjaw8Fiu2L4LKBsE"
qcopas = "CAACAgEAAxkBAAOnX40sUryRoFxrvS_7AUfHs_xweOYAAhUAA4IVFjb_txkWAUYo5BsE"
qespadas = "CAACAgEAAxkBAAOlX40sIalN2qnz13Mn32ftAAFC0CEiAAIWAAOCFRY2qrzrD-YUiI0bBA"
qouros = "CAACAgEAAxkBAAOmX40sOPFAdYBPehbVg7g2Mafe8n8AAhcAA4IVFjabn8s4CMkHnBsE"
bw = "CAACAgEAAxkBAAIHC1-cQ4oGWhB8evXf5qsDI8jK2YpoAAIiAAOCFRY2xZv1cewnL-kbBA"

# Atribuindo valor as cartas
zap > copas > espadilha > ouros7 > joker > paus3 > copas3 > espadas3 > ouros3 > paus2 > copas2 > espadas2 > ouros2 > aspaus > ascopas > asouros > kpaus > kcopas > kespadas > kouros > jpaus > jcopas > jespadas > jouros > qpaus > qcopas > qespadas > qouros


print("Bot iniciado, tenha um bom jogo =D")



@dp.message_handler(commands='jogadores')  #Para ver os jogadores participantes
async def leitura_players(message: types.Message):
    i = 0
    arquivoplayers = open('Usuarios.txt', 'r')
    tjogadores = []
    for linha in arquivoplayers:
        jogadores = linha.split()
        print(jogadores)
        print(jogadores[1])
        print(i)
        sleep(1)
        tjogadores.append(str(jogadores[1]))
        i+=1

    arquivoplayers.close()
    await message.reply("Os jogadores que estão participando são: " + str(tjogadores) )
    

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Olá!\nEu sou o FDPBOT!\nDesenvolvido pela FDBot Developer Team.\nÉ muito legal ter você aqui comigo :)"
                        "\nEu utilizo a API da aiogram,\nVocê pode consulta-la aqui: https://docs.aiogram.dev/en/latest/index.html.\n\n")
    await message.reply("O jogo foi iniciando, para cadastrar os jogadores envie /join e todos devem apertar em 'SIM' para participar, para ver os jogadores participantes digite: /jogadores")


@dp.message_handler(commands='join')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    texto = (
        ('SIM!', 'sim'),
        ('NÃO!', 'nao'),
    )

    rbotao = (types.InlineKeyboardButton(tex, callback_data=dat)
              for tex, dat in texto)

    keyboard_markup.row(*rbotao)

    await message.reply("Deseja participar do game?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='sim')
@dp.callback_query_handler(text='nao')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')
    
    arquivovidas = open('Usuariosvidas.txt', 'a')
    arquivofez = open('usuariosfez.txt', 'a')

    if user_data == 'sim':

        if os.path.exists('Usuarios.txt') == False:
            arquivo = open('Usuarios.txt', 'w+')
            arquivo.close()

        arquivo = open('Usuarios.txt', 'r')
        linha = arquivo.readline()

        while linha:

            if linha == (str(query.from_user.id) + " " + str(query.from_user.full_name) + "\n"):
                cont = 1

            linha = arquivo.readline()
        arquivo.close
        arquivo = open('Usuarios.txt', 'a')

        if cont != 1:
            arquivo.write(str(query.from_user.id) + " " +
                          str(query.from_user.full_name) + "\n")

            arquivovidas.write(str(query.from_user.id) + " " + "4" + " " + str(query.from_user.first_name) + " " + "\n")
            arquivofez.write(str(query.from_user.id) + " " + "0" + " \n")
            texto1 = "TOP DEMAIS MANO, BORA JOGAR!"


        elif cont == 1:
            texto1 = "VOCE JA ESTA JOGANDO!"
        arquivo.close()
        arquivovidas.close()
        arquivofez.close()
    elif user_data == 'nao':
        texto1 = "BELEZA, NÃO AGUENTA PERDER NÉ?"
    else:
        texto1 = f'Entrada não esperada: {user_data!r}!'
    await bot.send_message(query.message.chat.id, query.from_user.first_name + " está participando!")
    await bot.send_message(query.from_user.id, texto1)


@dp.message_handler(commands='nrodada')
async def criadorderodadas(message: types.Message):
    tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
               ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
    reset = open('Usuarioscartas.txt', 'r+')
    reset.truncate(0)
    reset.close()
    ordem = 1

    with open('rodada.txt') as f:
        contagem = sum(1 for _ in f)
    arquivo2 = open('Usuarioscartas.txt', 'a')

    with open('Usuarios.txt') as f:
        players = sum(1 for _ in f)


    if contagem == 0:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
                
        # resetando cartas dos usuarios
        reset = open('Usuarioscartas.txt', 'r+')
        reset.truncate(0)
        reset.close()
        #resetando palpites dos usuarios
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()

        
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo.write('1\n')
        arquivo.close()
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        cbotao = (
            ("0", "01"),
            ("1", "11"),
        )
        ctexto = (types.InlineKeyboardButton(ctex, callback_data=cdat)
                  for ctex, cdat in cbotao)

        keyboard_markup.row(*ctexto)
        ncartas = players
        totcartas = 28
        arquivou.close()

        arquivou = open('Usuarios.txt', 'r')

        for user in arquivou:  # Adicionando ordem aos players no arquivo
            print("ENTROU AQUI")
            usersid = user.split()
            arquivoo = open('ousuarios.txt', 'a')
            arquivoo.write(str(usersid[0]) + ' ' + str(ordem) + "\n")
            ordem += 1
            arquivoo.close()

        arquivou.close()

        arquivoo = open('ousuarios.txt', 'r')
        arquivovez = open('vezjogada.txt', 'a')
        for linha1 in arquivoo:
            split = linha1.split()
            if split[1] == str(1):
                arquivovez.write(linha1)
            else:
                pass
        arquivovez.close()
        arquivoo.close()

        arquivou = open('Usuarios.txt', 'r')
        while ncartas > 0:
            print("ENVIANDO CARTAS")

            for linha in arquivou:
                userid = linha.split()
                send = random.randrange(0, totcartas)

                arquivo2.write(userid[0] + ' ' + tcartas[send] + " " + str(send) + " "  + userid[1] +" \n")
                await message.reply_sticker(tcartas[send])

                del (tcartas[send])
                ncartas -= 1
                totcartas -= 1

        await message.reply("Quantas você vai fazer?", reply_markup=keyboard_markup)
        print("ENVIOU O PALPITE")

        arquivou.close()
        arquivo2.close()

        @dp.callback_query_handler(text='01')
        @dp.callback_query_handler(text='11')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            eouser = False
            verpalpite = 0
            user_data = query.data[0]
            players = 0
            with open('Usuarios.txt') as f:
                players = sum(1 for _ in f)
            #-------------------GODOY E LEO MODIFICARAM AQUI-------------------
            if os.path.exists('vez.txt') == False:
                arquivo = open('vez.txt', 'w+')
                arquivo.write("1")
                arquivo.close()
            arquivovezz = open("vez.txt", 'r')
            for linha in arquivovezz:
                vezz = linha
            arquivovezz.close()
            usertentativa = str(query.from_user.id) + " " + str(vezz)
            print (usertentativa)
            sleep(1)
            arquivoou = open('ousuarios.txt', 'r')
            for linha in arquivoou:
                userver = linha.split()
                print(userver)
                sleep(1)
                if str(userver[0]) + " " + str(userver[1]) == usertentativa:
                    eouser = True
                    print("Na hora certa")
                    with open('Usuariospalpites.txt', 'r') as f:
                        quantpalpites = sum(1 for _ in f)
                    if quantpalpites == players-1: #certificando se é o último usuário
                        somapalpites()
                        somadepalpites = open('spalpites.txt', 'r')
                        linha = somadepalpites.readline()
                        if int(linha) + int(user_data) == 1:
                            await bot.send_message(query.message.chat.id, query.from_user.first_name + ", Você não pode dar esse palpite ): , tente outro!")
                        
                        else:
                            arquivopalpite = open('Usuariospalpites.txt', 'a')
                            npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                            arquivopalpite.write(npalpite)
                            arquivopalpite.close()
                            await bot.send_message(query.message.chat.id, query.from_user.first_name + " Disse que faz: " + str(user_data) + " vezes")
                            arquivovezz = open("vez.txt", 'w')
                            vezz = int(vezz)

                            if vezz == players:
                                vezz = 1
                                arquivovezz.write(str(vezz))
                            else:
                                vezz +=1
                                arquivovezz.write(str(vezz))
                            
                            arquivovezz.close()
                        somadepalpites.close()
                    else:
                        arquivopalpite = open('Usuariospalpites.txt', 'a')
                        npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                        arquivopalpite.write(npalpite)
                        arquivopalpite.close()
                        await bot.send_message(query.message.chat.id, query.from_user.first_name + " Disse que faz: " + str(user_data) + " vezes")
                        arquivovezz = open("vez.txt", 'w')
                        vezz = int(vezz)
                        

                        if vezz == players:
                            vezz = 1
                            arquivovezz.write(str(vezz))
                        else:
                            vezz +=1
                            arquivovezz.write(str(vezz))
                        
                        arquivovezz.close()
            if eouser == False:
                await bot.send_message(query.message.chat.id, query.from_user.first_name + ", calma aê!!! Não é sua vez parça!")
            arquivoou.close()
            sleep(1)
            quantpalpites = 0
            upalpites = open('Usuariospalpites.txt', 'r')
            for linhapalpites in upalpites:
                quantpalpites += 1
            upalpites.close()
            print(quantpalpites)
            print(players)
            if quantpalpites == players: #Certificando que todos os players deram palpite

                mcarta = 0
                i=0
                arquivocartas = open('Usuarioscartas.txt', 'r')
                for linha in arquivocartas:
                    carta = linha.split()
                    if int(carta[2]) > mcarta:
                        mcarta = int(carta[2])
                        cartawin = i
                    i+=1
                arquivocartas.close()
                with open("Usuarioscartas.txt", "r") as f:
                    todcartas = f.readlines()
                winner = todcartas[cartawin]
                with open("vencedoratual.txt", "w+") as h:
                    h.writelines(winner)
                arquivo = open("vencedoratual.txt", 'r')
                for linha in arquivo:
                    vencedor = linha.split()
                arquivo.close()
                await bot.send_message(query.message.chat.id, "O vencedor dessa rodada foi: " + vencedor[3])
                with open("usuariosfez.txt", "r") as j:
                    todfez = j.readlines()
                todfez[cartawin] = winner[1] + ' 1 \n'
                with open("usuariosfez.txt", "w") as k:
                    k.writelines(todfez)
                vidas()

            await query.answer(f'Você respondeu com {user_data!r}')

    #rodada2
    if contagem == 1:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]

        # resetando cartas dos usuarios
        reset = open('Usuarioscartas.txt', 'r+')
        reset.truncate(0)
        reset.close()
        #resetando palpites dos usuarios
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()

        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')
        arquivo.write('2\n')
        arquivo.close()

        ousers = []  # Vetor que aramazena a ordem dada pelo arquivo criado na rodada anterior
        posicao = 0  # Posicao na array ousers

        arquivoo = open('ousuarios.txt', 'r')
        for users in arquivoo:  # Ciclo que adiciona os valores das ordens e diminui um no seu valor, para criar a nova ordem
            usersid2 = users.split()
            if int(usersid2[1]) == 1:
                ousers.append(players)
            else:
                ousers.append(int(usersid2[1]) - 1)
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'r+')
        arquivoo.truncate(0)  # LIMPANDO ARQUIVO
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'a')
        for ids in arquivou:  # Ciclo que adiciona o user id com a nova ordem de cada player
            ids2 = ids.split()
            arquivoo.write(str(ids2[0]) + ' ' + str(ousers[posicao]) + "\n")
            posicao += 1
        arquivoo.close()
        arquivou.close()

        arquivou = open('Usuarios.txt', 'r')

        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        cbotao = (
            ("0", "02"),
            ("1", "12"),
            ("2", "22"),
        )
        ctexto = (types.InlineKeyboardButton(ctex, callback_data=cdat)
                  for ctex, cdat in cbotao)
        keyboard_markup.row(*ctexto)

        lista = []
        for linhas in arquivou:
            userid = linhas.split()
            lista.append(userid[0])
            lista.append(userid[0])

        ncartas = (2*players)
        i = 0
        totcartas = 28
        while ncartas > 0:
            send = random.randrange(0, totcartas)
            arquivo2.write(lista[i] + ' ' + tcartas[send] + "\n")
            await bot.send_sticker(lista[i], tcartas[send])
            del (tcartas[send])
            ncartas -= 1
            i += 1
            totcartas -= 1

        await message.reply("Quantas você vai fazer?", reply_markup=keyboard_markup)
        arquivou.close()
        arquivo2.close()

        @dp.callback_query_handler(text='02')
        @dp.callback_query_handler(text='12')
        @dp.callback_query_handler(text='22')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            eouser = False
            verpalpite = 0
            user_data = query.data[0]
            quantpalpites = 0
            with open('Usuarios.txt') as f:
                players = sum(1 for _ in f)
            #-------------------GODOY E LEO MODIFICARAM AQUI-------------------
            if os.path.exists('vez.txt') == False:
                arquivo = open('vez.txt', 'w+')
                arquivo.write("1")
                arquivo.close()
            arquivovezz = open("vez.txt", 'r')
            for linha in arquivovezz:
                vezz = linha
            arquivovezz.close()
            usertentativa = str(query.from_user.id) + " " + str(vezz)
            print (usertentativa)
            sleep(1)
            arquivoou = open('ousuarios.txt', 'r')
            for linha in arquivoou:
                userver = linha.split()
                print(userver)
                sleep(1)
                if str(userver[0]) + " " + str(userver[1]) == usertentativa:
                    eouser = True
                    print("Na hora certa")
                    with open('Usuariospalpites.txt', 'r') as f:
                        quantpalpites = sum(1 for _ in f)
                    if quantpalpites == players-1: #certificando se é o último usuário
                        somapalpites()
                        somadepalpites = open('spalpites.txt', 'r')
                        linha = somadepalpites.readline()
                        if int(linha) + int(user_data) == 2:
                            await bot.send_message(query.message.chat.id, query.from_user.first_name + ", Você não pode dar esse palpite ): , tente outro!")
                        
                        else:
                            arquivopalpite = open('Usuariospalpites.txt', 'a')
                            npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                            arquivopalpite.write(npalpite)
                            await bot.send_message(query.message.chat.id, query.from_user.first_name + " Disse que faz: " + str(user_data) + " vezes")
                            arquivovezz = open("vez.txt", 'w')
                            vezz = int(vezz)
                            

                            if vezz == players:
                                vezz = 1
                                arquivovezz.write(str(vezz))
                            else:
                                vezz +=1
                                arquivovezz.write(str(vezz))
                            
                            arquivovezz.close()
                        somadepalpites.close()
                    else:
                        arquivopalpite = open('Usuariospalpites.txt', 'a')
                        npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                        arquivopalpite.write(npalpite)
                        await bot.send_message(query.message.chat.id, query.from_user.first_name + " Disse que faz: " + str(user_data) + " vezes")
                        arquivovezz = open("vez.txt", 'w')
                        vezz = int(vezz)
                        

                        if vezz == players:
                            vezz = 1
                            arquivovezz.write(str(vezz))
                        else:
                            vezz +=1
                            arquivovezz.write(str(vezz))
                        
                        arquivovezz.close()
                        arquivopalpite.close()
            if eouser == False:
                await bot.send_message(query.message.chat.id, query.from_user.first_name + ", calma aê!!! Não é sua vez parça!")
            arquivoou.close()
            if quantpalpites == players: #Certificando que todos os players deram palpite
                await bot.send_message(query.message.chat.id, "Agora que todos deram seus palpites, façam suas jogadas!")  
                     

    #rodada3
    elif contagem == 2:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        
        # resetando cartas dos usuarios
        reset = open('Usuarioscartas.txt', 'r+')
        reset.truncate(0)
        reset.close()
        #resetando palpites dos usuarios
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()


        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')

        # Resetando a vez da jogada

        # arquivovez = open("vezjogada.txt",'w+')
        # arquivovez.write('1')
        # arquivovez.close()

        ousers = []  # Variavel que aramazena a ordem dada pelo arquivo criado na rodada anterior
        posicao = 0  # Posicao na array ousers

        arquivoo = open('ousuarios.txt', 'r')
        for users in arquivoo:  # Ciclo que adiciona os valores das ordens e diminui um no seu valor, para criar a nova ordem
            usersid2 = users.split()
            if int(usersid2[1]) == 1:
                ousers.append(players)
            else:
                ousers.append(int(usersid2[1]) - 1)
            # ousers.append(int(usersid2[1]) - 1)
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'r+')
        arquivoo.truncate(0)  # LIMPANDO ARQUIVO
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'a')
        for ids in arquivou:  # Ciclo que adiciona o user id com a nova ordem de cada player
            ids2 = ids.split()
            arquivoo.write(str(ids2[0]) + ' ' + str(ousers[posicao]) + "\n")
            posicao += 1
        arquivoo.close()
        arquivou.close()

        arquivou = open('Usuarios.txt', 'r')

        arquivo.write('3\n')
        arquivo.close()

        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        cbotao = (
            ("0", "03"),
            ("1", "13"),
            ("2", "23"),
            ("3", "33"),
        )
        ctexto = (types.InlineKeyboardButton(ctex, callback_data=cdat)
                  for ctex, cdat in cbotao)

        keyboard_markup.row(*ctexto)
        lista = []
        for linhas in arquivou:
            userid = linhas.split()
            lista.append(userid[0])
            lista.append(userid[0])
            lista.append(userid[0])

        ncartas = (3*players)
        i = 0
        while ncartas > 0:
            send = random.randrange(0, 28)
            arquivo2.write(lista[i] + ' ' + tcartas[send] + "\n")
            await bot.send_sticker(lista[i], tcartas[send])
            del (tcartas[send])
            ncartas -= 1
            i += 1

        await message.reply("Quantas você vai fazer?", reply_markup=keyboard_markup)

        @dp.callback_query_handler(text='03')
        @dp.callback_query_handler(text='13')
        @dp.callback_query_handler(text='23')
        @dp.callback_query_handler(text='33')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            verpalpite = 0
            user_data = query.data[0]
            with open('Usuarios.txt') as f:
                players = sum(1 for _ in f)
            #-------------------GODOY E LEO MODIFICARAM AQUI-------------------
            if os.path.exists('vez.txt') == False:
                arquivo = open('vez.txt', 'w+')
                arquivo.write("1")
                arquivo.close()
            arquivovezz = open("vez.txt", 'r')
            for linha in arquivovezz:
                vezz = linha
            arquivovezz.close()
            usertentativa = str(query.from_user.id) + " " + str(vezz)
            print (usertentativa)
            sleep(1)
            arquivoou = open('ousuarios.txt', 'r')
            for linha in arquivoou:
                userver = linha.split()
                print(userver)
                sleep(1)
                if str(userver[0]) + " " + str(userver[1]) == usertentativa:
                    print("Na hora certa")
                    with open('Usuariospalpites.txt', 'r') as f:
                        quantpalpites = sum(1 for _ in f)
                    if quantpalpites == players-1: #certificando se é o último usuário
                        somapalpites()
                        somadepalpites = open('spalpites.txt', 'r')
                        linha = somadepalpites.readline()
                        if int(linha) + int(user_data) == 3:
                            await bot.send_message(query.message.chat.id, query.from_user.first_name + ", Você não pode dar esse palpite ): , tente outro!")
                        
                        else:
                            arquivopalpite = open('Usuariospalpites.txt', 'a')
                            npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                            arquivopalpite.write(npalpite)
                            arquivovezz = open("vez.txt", 'w')
                            vezz = int(vezz)
                            

                            if vezz == players:
                                vezz = 1
                                arquivovezz.write(str(vezz))
                            else:
                                vezz +=1
                                arquivovezz.write(str(vezz))
                            
                            arquivovezz.close()
                        somadepalpites.close()
                    else:
                        arquivopalpite = open('Usuariospalpites.txt', 'a')
                        npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                        arquivopalpite.write(npalpite)
                        arquivovezz = open("vez.txt", 'w')
                        vezz = int(vezz)
                        

                        if vezz == players:
                            vezz = 1
                            arquivovezz.write(str(vezz))
                        else:
                            vezz +=1
                            arquivovezz.write(str(vezz))
                        
                        arquivovezz.close()
                        arquivopalpite.close()
                else:
                    print("Na hora errada")
            arquivoou.close()


    #rodada4
    elif contagem == 3:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        
        # resetando cartas dos usuarios
        reset = open('Usuarioscartas.txt', 'r+')
        reset.truncate(0)
        reset.close()
        #resetando palpites dos usuarios
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()

        
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')
        arquivo.write('4\n')
        arquivo.close()

        # #Resetando a vez da jogada

        # arquivovez = open("vezjogada.txt",'w+')
        # arquivovez.write('1')
        # arquivovez.close()

        ousers = []  # Variavel que aramazena a ordem dada pelo arquivo criado na rodada anterior
        posicao = 0  # Posicao na array ousers

        arquivoo = open('ousuarios.txt', 'r')
        for users in arquivoo:  # Ciclo que adiciona os valores das ordens e diminui um no seu valor, para criar a nova ordem
            usersid2 = users.split()
            if int(usersid2[1]) == 1:
                ousers.append(players)
            else:
                ousers.append(int(usersid2[1]) - 1)
            # ousers.append(int(usersid2[1]) - 1)
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'r+')
        arquivoo.truncate(0)  # LIMPANDO ARQUIVO
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'a')
        for ids in arquivou:  # Ciclo que adiciona o user id com a nova ordem de cada player
            ids2 = ids.split()
            arquivoo.write(str(ids2[0]) + ' ' + str(ousers[posicao]) + "\n")
            posicao += 1
        arquivoo.close()
        arquivou.close()

        arquivou = open('Usuarios.txt', 'r')

        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        cbotao = (
            ("0", "04"),
            ("1", "14"),
            ("2", "24"),
            ("3", "34"),
            ("4", "44"),
        )
        ctexto = (types.InlineKeyboardButton(ctex, callback_data=cdat)
                  for ctex, cdat in cbotao)

        keyboard_markup.row(*ctexto)
        lista = []
        for linhas in arquivou:
            userid = linhas.split()
            lista.append(userid[0])
            lista.append(userid[0])
            lista.append(userid[0])
            lista.append(userid[0])

        ncartas = (4*players)
        i = 0
        totcartas = 28
        while ncartas > 0:
            send = random.randrange(0, totcartas)
            arquivo2.write(lista[i] + ' ' + tcartas[send] + "\n")
            await bot.send_sticker(lista[i], tcartas[send])
            del (tcartas[send])
            ncartas -= 1
            i += 1
            totcartas -= 1

        await message.reply("Quantas você vai fazer?", reply_markup=keyboard_markup)

        @dp.callback_query_handler(text='04')
        @dp.callback_query_handler(text='14')
        @dp.callback_query_handler(text='24')
        @dp.callback_query_handler(text='34')
        @dp.callback_query_handler(text='44')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            verpalpite = 0
            user_data = query.data[0]
            with open('Usuarios.txt') as f:
                players = sum(1 for _ in f)
            #-------------------GODOY E LEO MODIFICARAM AQUI-------------------
            if os.path.exists('vez.txt') == False:
                arquivo = open('vez.txt', 'w+')
                arquivo.write("1")
                arquivo.close()
            arquivovezz = open("vez.txt", 'r')
            for linha in arquivovezz:
                vezz = linha
            arquivovezz.close()
            usertentativa = str(query.from_user.id) + " " + str(vezz)
            print (usertentativa)
            sleep(1)
            arquivoou = open('ousuarios.txt', 'r')
            for linha in arquivoou:
                userver = linha.split()
                print(userver)
                sleep(1)
                if str(userver[0]) + " " + str(userver[1]) == usertentativa:
                    print("Na hora certa")
                    with open('Usuariospalpites.txt', 'r') as f:
                        quantpalpites = sum(1 for _ in f)
                    if quantpalpites == players-1: #certificando se é o último usuário
                        somapalpites()
                        somadepalpites = open('spalpites.txt', 'r')
                        linha = somadepalpites.readline()
                        if int(linha) + int(user_data) == 4:
                            await bot.send_message(query.message.chat.id, query.from_user.first_name + ", Você não pode dar esse palpite ): , tente outro!")
                        
                        else:
                            arquivopalpite = open('Usuariospalpites.txt', 'a')
                            npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                            arquivopalpite.write(npalpite)
                            arquivovezz = open("vez.txt", 'w')
                            vezz = int(vezz)
                            

                            if vezz == players:
                                vezz = 1
                                arquivovezz.write(str(vezz))
                            else:
                                vezz +=1
                                arquivovezz.write(str(vezz))
                            
                            arquivovezz.close()
                        somadepalpites.close()
                    else:
                        arquivopalpite = open('Usuariospalpites.txt', 'a')
                        npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                        arquivopalpite.write(npalpite)
                        arquivovezz = open("vez.txt", 'w')
                        vezz = int(vezz)
                        

                        if vezz == players:
                            vezz = 1
                            arquivovezz.write(str(vezz))
                        else:
                            vezz +=1
                            arquivovezz.write(str(vezz))
                        
                        arquivovezz.close()
                        arquivopalpite.close()
                else:
                    print("Na hora errada")
            arquivoou.close()


    #rodada5
    elif contagem == 4:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        
        # resetando cartas dos usuarios
        reset = open('Usuarioscartas.txt', 'r+')
        reset.truncate(0)
        reset.close()
        #resetando palpites dos usuarios
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()

        
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')
        arquivo.write('5\n')
        arquivo.close()

        # #Resetando a vez da jogada

        # arquivovez = open("vezjogada.txt",'w+')
        # arquivovez.write('1')
        # arquivovez.close()

        ousers = []  # Variavel que aramazena a ordem dada pelo arquivo criado na rodada anterior
        posicao = 0  # Posicao na array ousers

        arquivoo = open('ousuarios.txt', 'r')
        for users in arquivoo:  # Ciclo que adiciona os valores das ordens e diminui um no seu valor, para criar a nova ordem
            usersid2 = users.split()
            if int(usersid2[1]) == 1:
                ousers.append(players)
            else:
                ousers.append(int(usersid2[1]) - 1)
            # ousers.append(int(usersid2[1]) - 1)
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'r+')
        arquivoo.truncate(0)  # LIMPANDO ARQUIVO
        arquivoo.close()

        arquivoo = open('ousuarios.txt', 'a')
        for ids in arquivou:  # Ciclo que adiciona o user id com a nova ordem de cada player
            ids2 = ids.split()
            arquivoo.write(str(ids2[0]) + ' ' + str(ousers[posicao]) + "\n")
            posicao += 1
        arquivoo.close()
        arquivou.close()

        arquivou = open('Usuarios.txt', 'r')

        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        cbotao = (
            ("0", "05"),
            ("1", "15"),
            ("2", "25"),
            ("3", "35"),
            ("4", "45"),
            ("5", "55"),
        )
        ctexto = (types.InlineKeyboardButton(ctex, callback_data=cdat)
                  for ctex, cdat in cbotao)

        keyboard_markup.row(*ctexto)
        lista = []
        for linhas in arquivou:
            userid = linhas.split()
            lista.append(userid[0])
            lista.append(userid[0])
            lista.append(userid[0])
            lista.append(userid[0])
            lista.append(userid[0])

        ncartas = (5*players)
        i = 0
        totcartas = 28
        while ncartas > 0:
            send = random.randrange(0, totcartas)
            arquivo2.write(lista[i] + ' ' + tcartas[send] + "\n")
            await bot.send_sticker(lista[i], tcartas[send])
            del (tcartas[send])
            ncartas -= 1
            i += 1
            totcartas -= 1

        await message.reply("Quantas você vai fazer?", reply_markup=keyboard_markup)

        @dp.callback_query_handler(text='05')
        @dp.callback_query_handler(text='15')
        @dp.callback_query_handler(text='25')
        @dp.callback_query_handler(text='35')
        @dp.callback_query_handler(text='45')
        @dp.callback_query_handler(text='55')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            verpalpite = 0
            user_data = query.data[0]
            verpalpite = 0
            user_data = query.data
            with open('Usuarios.txt') as f:
                players = sum(1 for _ in f)
            #-------------------GODOY E LEO MODIFICARAM AQUI-------------------
            if os.path.exists('vez.txt') == False:
                arquivo = open('vez.txt', 'w+')
                arquivo.write("1")
                arquivo.close()
            arquivovezz = open("vez.txt", 'r')
            for linha in arquivovezz:
                vezz = linha
            arquivovezz.close()
            usertentativa = str(query.from_user.id) + " " + str(vezz)
            print (usertentativa)
            sleep(1)
            arquivoou = open('ousuarios.txt', 'r')
            for linha in arquivoou:
                userver = linha.split()
                print(userver)
                sleep(1)
                if str(userver[0]) + " " + str(userver[1]) == usertentativa:
                    print("Na hora certa")
                    with open('Usuariospalpites.txt', 'r') as f:
                        quantpalpites = sum(1 for _ in f)
                    if quantpalpites == players-1: #certificando se é o último usuário
                        somapalpites()
                        somadepalpites = open('spalpites.txt', 'r')
                        linha = somadepalpites.readline()
                        if int(linha) + int(user_data) == 5:
                            await bot.send_message(query.message.chat.id, query.from_user.first_name + ", Você não pode dar esse palpite ): , tente outro!")
                        
                        else:
                            arquivopalpite = open('Usuariospalpites.txt', 'a')
                            npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                            arquivopalpite.write(npalpite)
                            arquivovezz = open("vez.txt", 'w')
                            vezz = int(vezz)
                            

                            if vezz > players:
                                vezz = 1
                                arquivovezz.write(str(vezz))
                            else:
                                vezz +=1
                                arquivovezz.write(str(vezz))
                            
                            arquivovezz.close()
                        somadepalpites.close()
                    else:
                        arquivopalpite = open('Usuariospalpites.txt', 'a')
                        npalpite = str(query.from_user.id) + " " + str(user_data) + "\n"
                        arquivopalpite.write(npalpite)
                        arquivovezz = open("vez.txt", 'w')
                        vezz = int(vezz)
                        

                        if vezz > players:
                            vezz = 1
                            arquivovezz.write(str(vezz))
                        else:
                            vezz +=1
                            arquivovezz.write(str(vezz))
                        
                        arquivovezz.close()
                        arquivopalpite.close()
                else:
                    print("Na hora errada")
            arquivoou.close()


    #rodadareset
    elif contagem == 5:
        print("RESETOU AS RODADAS")
        reset = open('rodada.txt', 'r+')
        reset.truncate(0)
        reset.close()
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()

#Comando para contabilizar as vidas
# @dp.message_handler(commands='finaliza')
# async def start_conta_vidas(message: types.Message):

    # arquivopalpites = open('Usuariospalpites.txt', 'r')

    # for palpite in arquivopalpites:
    #     lpalpite = palpite.split()
    #     arquivofez = open('usuariosfez.txt', 'r')
    #     for userfez in arquivofez:
    #         ufez = userfez.split()
    #         if ufez[0] == lpalpite[0]: #Se os ids são iguais então eu posso comparar o palpite com o quantas fez
    #             if ufez[1] != lpalpite[1]: #Se quantas fez for diferente do palpite

    #                 i = 0 #Se inicia em 1 pois as linhas no arquivo começam a partir de 1                   
    #                 arquivovidas = open("Usuariosvidas.txt", 'r') #Abro o arquivo aqui pois preciso que o cursor seja resetado ao inicio
    #                 for lvida in arquivovidas:
    #                     llvida = lvida.split()
                        
    #                     if llvida[0] == ufez[0]: #Se o id do arquivo de vidas for igual ao usuario em questão

    #                         nlinha = i #Para salvar a posição da linha do usuário
    #                         useratual = llvida #Salva o usuario em que vamos alterar a vida
    #                     i += 1
                        
    #                 arquivovidas.close() #Fecho o arquivo aqui pois preciso que o cursor seja resetado ao inicio
    #                 with open('Usuariosvidas.txt', 'r') as f:
    #                     vidas = f.readlines() #Armazena tudo o que está dentro de vidas

    #                 vidaatual = int(llvida[1])-1

    #                 vidas[nlinha] = (useratual[0] + " " + str(vidaatual) + "\n")

    #                 with open('Usuariosvidas.txt', 'w') as f:
    #                     f.writelines(vidas)
        
    #     arquivofez.close()

    # arquivopalpites.close()

    # await message.reply(vidas)


@dp.message_handler(commands='zap')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simZap'),
        ('NÃO!', 'naoZap'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um zap?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simZap')
@dp.callback_query_handler(text='naoZap')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'sim':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOjX40im97tNxuWNUKwOU8-5vyYAAE6AAIhAAOCFRY2Ezylu98G3FIbBA" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])
            arquivoJogadas.close()
            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                print("Entrou onde escreve no arquivo")
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) +' CAACAgEAAxkBAAOjX40im97tNxuWNUKwOU8-5vyYAAE6AAIhAAOCFRY2Ezylu98G3FIbBA' + " 28" + '\n')
                arquivoJogadas.close()
                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOjX40im97tNxuWNUKwOU8-5vyYAAE6AAIhAAOCFRY2Ezylu98G3FIbBA")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoZap':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #
    

@dp.message_handler(commands='coringa')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simCoringa'),
        ('NÃO!', 'naoCoringa'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um coringa?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simCoringa')
@dp.callback_query_handler(text='naoCoringa')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simCoringa':
        # ------> Adicionar aqui verificação de turno!!!
        u ={}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAPAX43Lt-pvzdh34GkKtNgXrRmtL04AAhQAA4IVFjY0nFnyVFB2thsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAPAX43Lt-pvzdh34GkKtNgXrRmtL04AAhQAA4IVFjY0nFnyVFB2thsE' + " 27" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAPAX43Lt-pvzdh34GkKtNgXrRmtL04AAhQAA4IVFjY0nFnyVFB2thsE")

        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoCoringa':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data_naipe = query.data
    await query.answer(f'Você respondeu com {user_data_naipe!r}')


@dp.message_handler(commands='copas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simCopas'),
        ('NÃO!', 'naoCopas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um copas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simCopas')
@dp.callback_query_handler(text='naoCopas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simCopas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOkX40iuVC-sD4RxSxxWknzswbPmikAAg4AA4IVFjadPcs09HwT6xsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOkX40iuVC-sD4RxSxxWknzswbPmikAAg4AA4IVFjadPcs09HwT6xsE' + " 26" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOkX40iuVC-sD4RxSxxWknzswbPmikAAg4AA4IVFjadPcs09HwT6xsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoCopas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='espadilha')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simEspadilha'),
        ('NÃO!', 'naoEspadilha'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um espadilha?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simEspadilha')
@dp.callback_query_handler(text='naoEspadilha')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simEspadilha':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO1X43J8Gqs5fML2F4Qbvv5ScBMMwgAAhEAA4IVFjaCjVIgaC0x-BsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAO1X43J8Gqs5fML2F4Qbvv5ScBMMwgAAhEAA4IVFjaCjVIgaC0x-BsE' + " 25" +'\n')
                arquivoJogadas.close()
                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO1X43J8Gqs5fML2F4Qbvv5ScBMMwgAAhEAA4IVFjaCjVIgaC0x-BsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoEspadilha':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #


@dp.message_handler(commands='ouros')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simOuros'),
        ('NÃO!', 'naoOuros'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um ouros?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simOuros')
@dp.callback_query_handler(text='naoOuros')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simOuros':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAPBX43LuyEOXiLKYs1oHaltlTjGENkAAg8AA4IVFjZOjRImz1DqhBsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAPBX43LuyEOXiLKYs1oHaltlTjGENkAAg8AA4IVFjZOjRImz1DqhBsE' + " 24" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAPBX43LuyEOXiLKYs1oHaltlTjGENkAAg8AA4IVFjZOjRImz1DqhBsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoOuros':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='tresDePaus')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simTresDePaus'),
        ('NÃO!', 'naoTresDePaus'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 3 de paus?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simTresDePaus')
@dp.callback_query_handler(text='naoTresDePaus')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simTresDePaus':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO_X43LamqbvpIj-PAr18qwcVuvW2oAAg0AA4IVFjaW4avxCN1XcxsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) +' CAACAgEAAxkBAAO_X43LamqbvpIj-PAr18qwcVuvW2oAAg0AA4IVFjaW4avxCN1XcxsE' + " 23" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO_X43LamqbvpIj-PAr18qwcVuvW2oAAg0AA4IVFjaW4avxCN1XcxsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoTresDePaus':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='tresDeCopas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simTresDeCopas'),
        ('NÃO!', 'naoTresDeCopas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 3 de copas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simTresDeCopas')
@dp.callback_query_handler(text='naoTresDeCopas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simTresDeCopas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO-X43LaNnSJjF89gY5gcQFMdqYT-AAAgoAA4IVFjYUWC1QSdQhChsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id)+' CAACAgEAAxkBAAO-X43LaNnSJjF89gY5gcQFMdqYT-AAAgoAA4IVFjYUWC1QSdQhChsE' + " 22" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO-X43LaNnSJjF89gY5gcQFMdqYT-AAAgoAA4IVFjYUWC1QSdQhChsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoTresDeCopas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #




@dp.message_handler(commands='tresDeEspadas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simTresDeEspadas'),
        ('NÃO!', 'naoTresDeEspadas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 3 de espadas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simTresDeEspadas')
@dp.callback_query_handler(text='naoTresDeEspadas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simTresDeEspadas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO9X43LZqZKPJbJNsZf8VzlEwHjVDoAAgsAA4IVFjZ__wMHThM67xsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) +' CAACAgEAAxkBAAO9X43LZqZKPJbJNsZf8VzlEwHjVDoAAgsAA4IVFjZ__wMHThM67xsE' + " 21" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO9X43LZqZKPJbJNsZf8VzlEwHjVDoAAgsAA4IVFjZ__wMHThM67xsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoTresDeEspadas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #




@dp.message_handler(commands='tresDeOuros')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simTresDeOuros'),
        ('NÃO!', 'naoTresDeOuros'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 3 de ouros?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simTresDeOuros')
@dp.callback_query_handler(text='naoTresDeOuros')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simTresDeOuros':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO8X43LZDWFEet2pYK_lEhpUKoU4RcAAgwAA4IVFjbwaLMp1YeJFhsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) +' CAACAgEAAxkBAAO8X43LZDWFEet2pYK_lEhpUKoU4RcAAgwAA4IVFjbwaLMp1YeJFhsE' + " 20" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO8X43LZDWFEet2pYK_lEhpUKoU4RcAAgwAA4IVFjbwaLMp1YeJFhsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoTresDeOuros':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #




@dp.message_handler(commands='doisDePaus')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDoisDePaus'),
        ('NÃO!', 'naoDoisDePaus'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 2 de paus?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDoisDePaus')
@dp.callback_query_handler(text='naoDoisDePaus')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDoisDePaus':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO7X43KpLkrJfSdv99imAi7wufxWBQAAgkAA4IVFjZTLQnSuERnVRsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) +' CAACAgEAAxkBAAO7X43KpLkrJfSdv99imAi7wufxWBQAAgkAA4IVFjZTLQnSuERnVRsE' + " 19" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO7X43KpLkrJfSdv99imAi7wufxWBQAAgkAA4IVFjZTLQnSuERnVRsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDoisDePaus':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='doisDeCopas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDoisDeCopas'),
        ('NÃO!', 'naoDoisDeCopas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 2 de copas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDoisDeCopas')
@dp.callback_query_handler(text='naoDoisDeCopas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDoisDeCopas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO6X43Kob570RlEDS0ByiPGjN8jpukAAgYAA4IVFjag0l3hWjeLaxsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAO6X43Kob570RlEDS0ByiPGjN8jpukAAgYAA4IVFjag0l3hWjeLaxsE' + " 18" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO6X43Kob570RlEDS0ByiPGjN8jpukAAgYAA4IVFjag0l3hWjeLaxsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDoisDeCopas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='doisDeEspadas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDoisDeEspadas'),
        ('NÃO!', 'naoDoisDeEspadas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 2 de espadas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDoisDeEspadas')
@dp.callback_query_handler(text='naoDoisDeEspadas')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDoisDeEspadas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO5X43KnmVXF3YGFrieZ1_TvfqKEJcAAgcAA4IVFjYPq6yKzjZRUhsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAO5X43KnmVXF3YGFrieZ1_TvfqKEJcAAgcAA4IVFjYPq6yKzjZRUhsE' + " 17" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO5X43KnmVXF3YGFrieZ1_TvfqKEJcAAgcAA4IVFjYPq6yKzjZRUhsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDoisDeEspadas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #




@dp.message_handler(commands='doisDeOuros')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDoisDeOuros'),
        ('NÃO!', 'naoDoisDeOuros'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um 2 de ouros?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDoisDeOuros')
@dp.callback_query_handler(text='naoDoisDeOuros')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDoisDeOuros':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO4X43Km2KVTYCog2j2ij3Mssx2bBQAAggAA4IVFjZKI5muQ65F_BsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAO4X43Km2KVTYCog2j2ij3Mssx2bBQAAggAA4IVFjZKI5muQ65F_BsE' + " 16" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO4X43Km2KVTYCog2j2ij3Mssx2bBQAAggAA4IVFjZKI5muQ65F_BsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDoisDeOuros':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='asDePaus')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simAsDePaus'),
        ('NÃO!', 'naoAsDePaus'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um ás de paus?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simAsDePaus')
@dp.callback_query_handler(text='naoAsDePaus')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simAsDePaus':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO3X43J93iQH2fUs8nj4gZvEZUU8g8AAhMAA4IVFjbzqnpsekpO9RsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAO3X43J93iQH2fUs8nj4gZvEZUU8g8AAhMAA4IVFjbzqnpsekpO9RsE' + " 15" +'\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO3X43J93iQH2fUs8nj4gZvEZUU8g8AAhMAA4IVFjbzqnpsekpO9RsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoAsDePaus':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='asDeCopas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simAsDeCopas'),
        ('NÃO!', 'naoAsDeCopas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um ás de copas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simAsDeCopas')
@dp.callback_query_handler(text='naoAsDeCopas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simAsDeCopas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO2X43J9Jy25nLigjyYJ2Xn_FMp1XgAAhAAA4IVFjayn7taqb_SQRsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAO2X43J9Jy25nLigjyYJ2Xn_FMp1XgAAhAAA4IVFjayn7taqb_SQRsE' + ' 14' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO2X43J9Jy25nLigjyYJ2Xn_FMp1XgAAhAAA4IVFjayn7taqb_SQRsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoAsDeCopas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='asDeOuros')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simAsDeOuros'),
        ('NÃO!', 'naoAsDeOuros'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um ás de ouros?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simAsDeOuros')
@dp.callback_query_handler(text='naoAsDeOuros')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simAsDeOuros':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAO0X43J7PY2Kjrt01Q_l9xPhsQsQ6kAAhIAA4IVFjZY5T-EbvfgKhsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAO0X43J7PY2Kjrt01Q_l9xPhsQsQ6kAAhIAA4IVFjZY5T-EbvfgKhsE' + ' 13' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAO0X43J7PY2Kjrt01Q_l9xPhsQsQ6kAAhIAA4IVFjZY5T-EbvfgKhsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoAsDeOuros':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='reiDePaus')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simReiDePaus'),
        ('NÃO!', 'naoReiDePaus'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um rei de paus?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simReiDePaus')
@dp.callback_query_handler(text='naoReiDePaus')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simReiDePaus':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOzX43Jhx6Ipg5cY8e3hU9DWRzFbMsAAhwAA4IVFjZGDfDS2hm28BsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOzX43Jhx6Ipg5cY8e3hU9DWRzFbMsAAhwAA4IVFjZGDfDS2hm28BsE' + ' 12' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOzX43Jhx6Ipg5cY8e3hU9DWRzFbMsAAhwAA4IVFjZGDfDS2hm28BsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoReiDePaus':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='reiDeCopas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simReiDeCopas'),
        ('NÃO!', 'naoReiDeCopas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um rei de copas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simReiDeCopas')
@dp.callback_query_handler(text='naoReiDeCopas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simReiDeCopas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOyX43JhLaJtdwivesqUgPI16QWG9AAAhkAA4IVFjZgDwABp0RVogMbBA" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOyX43JhLaJtdwivesqUgPI16QWG9AAAhkAA4IVFjZgDwABp0RVogMbBA' + ' 11' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOyX43JhLaJtdwivesqUgPI16QWG9AAAhkAA4IVFjZgDwABp0RVogMbBA")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoReiDeCopas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='reiDeEspadas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simReiDeEspadas'),
        ('NÃO!', 'naoReiDeEspadas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um rei de espadas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simReiDeEspadas')
@dp.callback_query_handler(text='naoReiDeEspadas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simReiDeEspadas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOvX43ILuwDcNel-OY-bwQNwOAM33gAAhoAA4IVFjaDJFm0rb14BxsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOvX43ILuwDcNel-OY-bwQNwOAM33gAAhoAA4IVFjaDJFm0rb14BxsE' + ' 10' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOvX43ILuwDcNel-OY-bwQNwOAM33gAAhoAA4IVFjaDJFm0rb14BxsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoReiDeEspadas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='reiDeOuros')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simReiDeOuros'),
        ('NÃO!', 'naoReiDeOuros'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um rei de ouros?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simReiDeOuros')
@dp.callback_query_handler(text='naoReiDeOuros')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simReiDeOuros':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAPCX43Pi2EqxTZbg1DcXojoVUhSHywAAhsAA4IVFjaN5tjjcoNjGhsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAPCX43Pi2EqxTZbg1DcXojoVUhSHywAAhsAA4IVFjaN5tjjcoNjGhsE' + ' 9' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAPCX43Pi2EqxTZbg1DcXojoVUhSHywAAhsAA4IVFjaN5tjjcoNjGhsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoReiDeOuros':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='valeteDePaus')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simValeteDePaus'),
        ('NÃO!', 'naoValeteDePaus'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um valete de paus?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simValeteDePaus')
@dp.callback_query_handler(text='naoValeteDePaus')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simValeteDePaus':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOtX43HSe83D2AjO7WNMji7GjyKQEEAAh8AA4IVFjZ_9lyldZnmyBsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOtX43HSe83D2AjO7WNMji7GjyKQEEAAh8AA4IVFjZ_9lyldZnmyBsE' + ' 8' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOtX43HSe83D2AjO7WNMji7GjyKQEEAAh8AA4IVFjZ_9lyldZnmyBsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoValeteDePaus':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='valeteDeCopas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simValeteDeCopas'),
        ('NÃO!', 'naoValeteDeCopas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um valete de copas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simValeteDeCopas')
@dp.callback_query_handler(text='naoValeteDeCopas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simValeteDeCopas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOsX43HRWjc8O9e-V4_Kzn9KVm74pUAAh0AA4IVFjYyR1X0LWcBmxsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOsX43HRWjc8O9e-V4_Kzn9KVm74pUAAh0AA4IVFjYyR1X0LWcBmxsE' + ' 7' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOsX43HRWjc8O9e-V4_Kzn9KVm74pUAAh0AA4IVFjYyR1X0LWcBmxsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoValeteDeCopas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='valeteDeEspadas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simValeteDeEspadas'),
        ('NÃO!', 'naoValeteDeEspadas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um valete de espadas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simValeteDeEspadas')
@dp.callback_query_handler(text='naoValeteDeEspadas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simValeteDeEspadas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOrX43HRASuiB-AzIw-us6FG_Cfpi8AAiAAA4IVFjbFXeRcjq_OxRsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOrX43HRASuiB-AzIw-us6FG_Cfpi8AAiAAA4IVFjbFXeRcjq_OxRsE' + ' 6' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOrX43HRASuiB-AzIw-us6FG_Cfpi8AAiAAA4IVFjbFXeRcjq_OxRsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoValeteDeEspadas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='valeteDeOuros')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simValeteDeOuros'),
        ('NÃO!', 'naoValeteDeOuros'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar um valete de ouros?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simValeteDeOuros')
@dp.callback_query_handler(text='naoValeteDeOuros')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simValeteDeOuros':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOqX43HPwV7sphHSdh2R_--fc8LQ2YAAh4AA4IVFjZbm1aHv01wchsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOqX43HPwV7sphHSdh2R_--fc8LQ2YAAh4AA4IVFjZbm1aHv01wchsE' + ' 5' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOqX43HPwV7sphHSdh2R_--fc8LQ2YAAh4AA4IVFjZbm1aHv01wchsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoValeteDeOuros':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='damaDePaus')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDamaDePaus'),
        ('NÃO!', 'naoDamaDePaus'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar uma dama de paus?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDamaDePaus')
@dp.callback_query_handler(text='naoDamaDePaus')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDamaDePaus':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOpX40sckXcTuBRRaEyzlfo8fSUxgUAAhgAA4IVFjaw8Fiu2L4LKBsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOpX40sckXcTuBRRaEyzlfo8fSUxgUAAhgAA4IVFjaw8Fiu2L4LKBsE' + ' 4' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOpX40sckXcTuBRRaEyzlfo8fSUxgUAAhgAA4IVFjaw8Fiu2L4LKBsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDamaDePaus':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='damaDeCopas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDamaDeCopas'),
        ('NÃO!', 'naoDamaDeCopas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar uma dama de copas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDamaDeCopas')
@dp.callback_query_handler(text='naoDamaDeCopas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDamaDeCopas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOnX40sUryRoFxrvS_7AUfHs_xweOYAAhUAA4IVFjb_txkWAUYo5BsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOnX40sUryRoFxrvS_7AUfHs_xweOYAAhUAA4IVFjb_txkWAUYo5BsE' + ' 3' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOnX40sUryRoFxrvS_7AUfHs_xweOYAAhUAA4IVFjb_txkWAUYo5BsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDamaDeCopas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='damaDeEspadas')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDamaDeEspadas'),
        ('NÃO!', 'naoDamaDeEspadas'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar uma dama de espadas?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDamaDeEspadas')
@dp.callback_query_handler(text='naoDamaDeEspadas')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDamaDeEspadas':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOlX40sIalN2qnz13Mn32ftAAFC0CEiAAIWAAOCFRY2qrzrD-YUiI0bBA" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOlX40sIalN2qnz13Mn32ftAAFC0CEiAAIWAAOCFRY2qrzrD-YUiI0bBA' + ' 2' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOlX40sIalN2qnz13Mn32ftAAFC0CEiAAIWAAOCFRY2qrzrD-YUiI0bBA")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDamaDeEspadas':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")
    #



@dp.message_handler(commands='damaDeOuros')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    ctexto = (
        ('SIM!', 'simDamaDeOuros'),
        ('NÃO!', 'naoDamaDeOuros'),
    )

    cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

    keyboard_markup.row(*cbotao)
    
    await message.reply("Deseja jogar uma dama de ouros?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simDamaDeOuros')
@dp.callback_query_handler(text='naoDamaDeOuros')

async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'simDamaDeOuros':
        # ------> Adicionar aqui verificação de turno!!!
        u = {}

        arquivo = open('Usuarioscartas.txt', 'r')
        
        # Pegando a lista de cartas na mão do User
        for linha in arquivo: #Lendo os arquivo que tem as cartas
            usercarddata = linha.split() #Lendo linha por linha
            if usercarddata[0] not in u:
                u[usercarddata[0]] = list()
            u[usercarddata[0]].append(usercarddata[1])

        cartas = u[str(query.from_user.id)]
        
        if "CAACAgEAAxkBAAOmX40sOPFAdYBPehbVg7g2Mafe8n8AAhcAA4IVFjabn8s4CMkHnBsE" in cartas:

            if os.path.exists('Jogadas.txt') == False:
                arquivoJogadas = open('Jogadas.txt', 'w+')
                arquivoJogadas.close()

            jogaram = []
            arquivoJogadas = open('Jogadas.txt', 'r')
            for linha in arquivoJogadas:
                userid = linha.split()
                jogaram.append(userid[0])

            if str(query.from_user.id) in jogaram:
                await bot.send_message(query.from_user.id, "EPA! Você já jogou nessa rodada! Espere todos jogarem, e utilize o comando de finalizar a rodada!")

            else:
                arquivoJogadas = open('Jogadas.txt', 'a')
                arquivoJogadas.write(str(query.from_user.id) + ' CAACAgEAAxkBAAOmX40sOPFAdYBPehbVg7g2Mafe8n8AAhcAA4IVFjabn8s4CMkHnBsE' + ' 1' + '\n')

                arquivoJogadas.close()
                await bot.send_sticker(query.message.chat.id, "CAACAgEAAxkBAAOmX40sOPFAdYBPehbVg7g2Mafe8n8AAhcAA4IVFjabn8s4CMkHnBsE")
        
        else:
            await bot.send_message(query.from_user.id, "Você não tem essa carta! Escolha outra com base nas enviadas no privado!")

    elif user_data == 'naoDamaDeOuros':
        await bot.send_message(query.from_user.id, "Ué, mudou de ideia?! Ok, pode escolher outra!")

    else:
        await bot.send_message(query.from_user.id, "Entrada inexperada. O QUE VOCÊ FEZ?!")


@dp.message_handler(commands='vidas')
async def mostrar_vidas(message: types.Message):
    tvida = []
    arquivovidas = open('Usuariosvidas.txt','r')
    for linha in arquivovidas:
        uvida = linha.split()
        tvida.append(str(uvida[2]) + " " + str(uvida[1]))
    arquivovidas.close()
    await message.reply("Vidas: " + str(tvida))


@dp.message_handler(commands='finaliza')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    texto = (
        ('SIM!', 'simfinaliza'),
        ('NÃO!', 'naofinaliza'),
    )

    rbotao = (types.InlineKeyboardButton(tex, callback_data=dat)
              for tex, dat in texto)

    keyboard_markup.row(*rbotao)

    await message.reply("Deseja finalizar este turno?", reply_markup=keyboard_markup)


@dp.callback_query_handler(text='simfinaliza')
@dp.callback_query_handler(text='naofinaliza')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    if user_data == 'simfinaliza':
        with open("Usuarios.txt", "r") as f:
            players = sum(1 for _ in f)
        with open("Jogadas.txt", "r") as j:
            jogadas = sum(1 for _ in j)

        if players == jogadas:
            finaliza()
            with open('arquivoGanhador.txt', 'r') as f:
                ganhador = f.readline()
            await bot.send_message(query.message.chat.id, "Todos ja mandaram suas cartas e quem fez foi: " + ganhador) #Implementar aqui o quem fez que tem lá em cima
        
        else:
            await bot.send_message(query.message.chat.id, "Calma, alguns jogadores não mandaram suas cartas, aguarde que todos enviem e envie o /finaliza novamente")
    else:
        await message.reply("Ok, podem continuar jogando suas cartas =D")

# # @dp.message_handler(commands='finaliza')
# # async def finalizar_turno(message: types.Message):
#     with open("Usuarios.txt", "r") as f:
#         players = sum(1 for _ in f)
#     with open("Jogadas.txt", "r") as j:
#         jogadas = sum(1 for _ in j)

#     if players == jogadas:
#         await bot.send_message(query.message.chat.id, "Todos ja mandaram suas cartas e quem fez foi: ") #Implementar aqui o quem fez que tem lá em cima
    
#     else:
#         await bot.send_message(query.message.chat.id, "Calma, alguns jogadores não mandaram suas cartas, aguarde que todos enviem e envie o /finaliza novamente")


def finaliza():
    print("ENTROU EM FINALIZAÇÃO")
    with open('Usuarios.txt', 'r') as j:
        players = sum(1 for _ in j)
    with open('Jogadas.txt','r') as f:#-------VENDO SE TODOS JOGARAM
        jogadas = sum(1 for _ in f)
    print("Players= " + str(players) )
    print("jogadas= " + str(jogadas) )
    if players == jogadas:
        print("Players foi igual a jogadas")
    #-----------------------VERIFICANDO QUEM ERROU----------------------------
        mcarta = 0 #Definindo valor inicial
        print("Valor de mcarta = " + str(mcarta))
        i=0
        arquivojogadas = open('Jogadas.txt', 'r')
        for linha in arquivojogadas:
            jogada = linha.split()
            if int(jogada[2]) > mcarta: #Verifica se o valor de carta lida é maior que a maior carta atual
                mcarta = int(jogada[2])
                print("Novo valor de mcarta = " + str(mcarta))
                cartawin = i #Salvando a linha da carta vencedora
                print("Linha da carta vencedora = " + str(i))
            i+=1 #aumentando junto com as linhas
        arquivojogadas.close()
        with open('Jogadas.txt', 'r') as f:
            todjogadas = f.readlines()
        winner = todjogadas[cartawin]
        print(winner)
        nomesUsuarios = open('Usuarios.txt', 'r')
        arquivoGanhador = open('arquivoGanhador.txt', 'w')
        vencedor = winner.split()
        for linha in nomesUsuarios:
            usuarios = linha.split()
            print(usuarios[0])
            print(vencedor[0])
            nomeCompletoGanhador = ''
            if str(vencedor[0]) == str(usuarios[0]):
                for nomes in usuarios[1:]:
                    nomeCompletoGanhador = nomeCompletoGanhador + ' ' + nomes
                arquivoGanhador.write(nomeCompletoGanhador)
        arquivoGanhador.close()
        nomesUsuarios.close()
        vidas()
        resetJogadas = open('Jogadas.txt', 'r+')
        resetJogadas.truncate(0)
        resetJogadas.close()
    #-----------------------FIM VERIFICANDO QUEM ERROU----------------------------

def vidas():
    #=-----------------------TODo O CÓDIGO ABAIXO É PARA TIRAR VIDAS DAQUELES QUE ERRARAM
    arquivopalpites = open('Usuariospalpites.txt', 'r')

    for palpite in arquivopalpites:
        lpalpite = palpite.split()
        arquivofez = open('usuariosfez.txt', 'r')
        for userfez in arquivofez:
            ufez = userfez.split()
            if ufez[0] == lpalpite[0]: #Se os ids são iguais então eu posso comparar o palpite com o quantas fez
                if ufez[1] != lpalpite[1]: #Se quantas fez for diferente do palpite

                    i = 0 #Se inicia em 0 pois as linhas no arquivo começam a partir de 0                  
                    arquivovidas = open("Usuariosvidas.txt", 'r') #Abro o arquivo aqui pois preciso que o cursor seja resetado ao inicio
                    for lvida in arquivovidas:
                        llvida = lvida.split()
                        
                        if llvida[0] == ufez[0]: #Se o id do arquivo de vidas for igual ao usuario em questão

                            nlinha = i #Para salvar a posição da linha do usuário
                            useratual = llvida #Salva o usuario em que vamos alterar a vida
                        i += 1
                        
                    arquivovidas.close() #Fecho o arquivo aqui pois preciso que o cursor seja resetado ao inicio
                    with open('Usuariosvidas.txt', 'r') as f:
                        vidas = f.readlines() #Armazena tudo o que está dentro de vidas

                    vidaatual = int(llvida[1])-1
                    if vidaatual == 0:
                        vidas[nlinha] = ""
                    else:
                        vidas[nlinha] = (useratual[0] + " " + str(vidaatual) + " " + useratual[2] +"\n")

                    with open('Usuariosvidas.txt', 'w') as f:
                        f.writelines(vidas)
        
        arquivofez.close()

    arquivopalpites.close()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

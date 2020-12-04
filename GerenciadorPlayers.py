import logging
import random
import os.path
from time import sleep
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1255502823:AAFduKDPX5DJEkIio5xPG8fYRpHCse55Ba4'
# API_TOKEN = '1194976667:AAGrxoVyWVWjvVJL4EA2bvjxdglaVwTmytM'

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
# Vetor contendo todas as cartas
# tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
#            ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]


@dp.message_handler(commands=['start', 'help', 'Ola'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    if os.path.exists('rodada.txt') == False:
        arquivo = open('rodada.txt', 'w+')
        arquivo.close()
    if os.path.exists('vezjogada.txt') == False:
        arquivo = open('vezjogada.txt', 'w+')
        arquivo.write("1")
        arquivo.close()
    await message.reply("Olá!\nEu sou o FDPBOT!\nDesenvolvido pela FDBot Developer Team.\nÉ muito legal ter você aqui comigo :)"
                        "\nEu utilizo a API da aiogram,\nVocê pode consulta-la aqui: https://docs.aiogram.dev/en/latest/index.html, VOCE INICIOU O BOT")


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
            texto1 = "TOP DEMAIS MANO, BORA JOGAR!"
        elif cont == 1:
            texto1 = "VOCE JA ESTA JOGANDO!"
        arquivo.close
    elif user_data == 'nao':
        texto1 = "BELEZA, NÃO AGUENTA PERDER NÉ?"
    else:
        texto1 = f'Entrada não esperada: {user_data!r}!'

    await bot.send_message(query.from_user.id, texto1)


@dp.message_handler(commands='nrodada')
async def criadorderodadas(message: types.Message):
    tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
               ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]

    ordem = 1

    if os.path.exists('rodada.txt') == False:
        arquivo = open('rodada.txt', 'w+')
        arquivo.close()

    if os.path.exists('ousuarios.txt') == False:
        arquivoo = open('ousuarios.txt', 'w+')
        arquivoo.close()

    with open('rodada.txt') as f:
        contagem = sum(1 for _ in f)
    arquivo2 = open('Usuarioscartas.txt', 'a')

    with open('Usuarios.txt') as f:
        players = sum(1 for _ in f)
    if contagem == 0:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo.write('1\n')
        arquivo.close()
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        cbotao = (
            ("0", "0"),
            ("1", "1"),
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
            arquivoo.write(str(usersid[0]) + ' ' + str(ordem) + " " + str(usersid[1]) +"\n")
            ordem += 1
            arquivoo.close()

        arquivou.close()
        arquivou = open('Usuarios.txt', 'r')
        while ncartas > 0:
            print("ENVIANDO CARTAS")

            for linha in arquivou:
                userid = linha.split()
                send = random.randrange(0, totcartas)

                arquivo2.write(userid[0] + ' ' + tcartas[send] + "\n")
                await message.reply_sticker(tcartas[send])

                del (tcartas[send])
                ncartas -= 1
                totcartas -= 1

        await message.reply("Quantas você vai fazer?", reply_markup=keyboard_markup)
        print("ENVIOU O PALPITE")


        arquivou.close()
        arquivo2.close()

        @dp.callback_query_handler(text='0')
        @dp.callback_query_handler(text='1')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            verpalpite = 0
            user_data = query.data
            
            arquivovez = open('vezjogada.txt', 'r')
            for leituravez in arquivovez:
                vez = leituravez.split()
                arquivoo = open('ousuarios.txt', 'r')
                for linha in arquivoo:
                    posicao = linha.split()

                    uservez = str(query.from_user.id) + " " + str(vez[0])
                    userposicao = str(posicao[0])+ " " + str(posicao[1])
                    print(uservez)
                    print(userposicao)

                if userposicao == uservez:
                    print("O cara deu palpite na hora certa")
                    arquivovez = open('vezjogada.txt', 'w')
                    contxx = int(str(vez[0])) + 1 #Tava sem criatividade pra variavel xD, mas ela converte o VEZ para string (para aparecer
                    #somente o necessario e então converte para inteiro para que possa ser somada)
                    arquivovez.write(str(contxx))
                    arquivovez.close()
                    if contagem > 0:
                        arquivo = open("Usuariospalpites.txt", "r")
                        for linha in arquivo:
                            ver = linha.split()
                            if(str(query.from_user.id) == str(ver[0])):
                                await bot.send_message(query.from_user.id, "Você já deu seu palpite, não tem volta haha")
                                verpalpite = 1
                        arquivo.close()
                    if verpalpite == 0:
                        arquivo = open("Usuariospalpites.txt", "a")
                        arquivo.write(str(query.from_user.id) +
                                        " " + str(user_data) + "\n")
                else:
                    print("Não é a vez do cara")
                    await bot.send_message(query.from_user.id, "Não é sua vez de dar o palpite, por favor espere =)")
                arquivoo.close()
            arquivovez.close()


            await query.answer(f'Você respondeu com {user_data!r}')


            arquivo = open("Usuariospalpites.txt", "r")
            spalpites = 0
            for palpite in arquivo:
                userpalpite = palpite.split()
                spalpites = int(userpalpite[1]) + spalpites
            arquivo.close()
            print(spalpites)

    if contagem == 1:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')
        arquivo.write('2\n')
        arquivo.close()
        
        #Resetando a vez da jogada
        
        arquivovez = open("vezjogada.txt",'w+')
        arquivovez.write('1')
        arquivovez.close()

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
            ("0", "0"),
            ("1", "1"),
            ("2", "2"),
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

        @dp.callback_query_handler(text='0')
        @dp.callback_query_handler(text='1')
        @dp.callback_query_handler(text='2')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            if os.path.exists('Usuariospalpites.txt') == False:
                arquivo = open('Usuariospalpites.txt', 'w+')
                arquivo.close()
            verpalpite = 0
            user_data = query.data
            
            arquivovez = open('vezjogada.txt', 'r')
            for leituravez in arquivovez:
                vez = leituravez.split()
                arquivoo = open('ousuarios.txt', 'r')
                for linha in arquivoo:
                    posicao = linha.split()

                    uservez = str(query.from_user.id) + " " + str(vez[0])
                    userposicao = str(posicao[0])+ " " + str(posicao[1])
                    print(uservez)
                    print(userposicao)

                if userposicao == uservez:
                    print("O cara deu palpite na hora certa")
                    arquivovez = open('vezjogada.txt', 'w')
                    contxx = int(str(vez[0])) + 1 #Tava sem criatividade pra variavel xD, mas ela converte o VEZ para string (para aparecer
                    #somente o necessario e então converte para inteiro para que possa ser somada)
                    arquivovez.write(str(contxx))
                    arquivovez.close()
                    if contagem > 0:
                        arquivo = open("Usuariospalpites.txt", "r")
                        for linha in arquivo:
                            ver = linha.split()
                            if(str(query.from_user.id) == str(ver[0])):
                                await bot.send_message(query.from_user.id, "Você já deu seu palpite, não tem volta haha")
                                verpalpite = 1
                        arquivo.close()
                    if verpalpite == 0:
                        arquivo = open("Usuariospalpites.txt", "a")
                        arquivo.write(str(query.from_user.id) +
                                        " " + str(user_data) + "\n")
                else:
                    print("Não é a vez do cara")
                    await bot.send_message(query.from_user.id, "Não é sua vez de dar o palpite, por favor espere =)")
                arquivoo.close()
            arquivovez.close()


            await query.answer(f'Você respondeu com {user_data!r}')

            arquivo = open("Usuariospalpites.txt", "r")
            spalpites = 0
            for palpite in arquivo:
                userpalpite = palpite.split()
                spalpites = int(userpalpite[1]) + spalpites
            arquivo.close()
            print(spalpites)

            # resetando cartas dos usuarios
            reset = open('Usuarioscartas.txt', 'r+')
            reset.truncate(0)
            reset.close()

    elif contagem == 2:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')

        #Resetando a vez da jogada
        
        arquivovez = open("vezjogada.txt",'w+')
        arquivovez.write('1')
        arquivovez.close()


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
            ("0", "0"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
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
            # lista.append(userid[0])
            # lista.append(userid[0])
            # lista.append(userid[0])

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

        @dp.callback_query_handler(text='0')
        @dp.callback_query_handler(text='1')
        @dp.callback_query_handler(text='2')
        @dp.callback_query_handler(text='3')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            if os.path.exists('Usuariospalpites.txt') == False:
                arquivo = open('Usuariospalpites.txt', 'w+')
                arquivo.close()
            
            user_data = query.data
            verpalpite = 0           
            
            arquivovez = open('vezjogada.txt', 'r')
            for leituravez in arquivovez:
                vez = leituravez.split()
                arquivoo = open('ousuarios.txt', 'r')
                for linha in arquivoo:
                    posicao = linha.split()

                    uservez = str(query.from_user.id) + " " + str(vez[0])
                    userposicao = str(posicao[0])+ " " + str(posicao[1])
                    print(uservez)
                    print(userposicao)

                if userposicao == uservez:
                    print("O cara deu palpite na hora certa")
                    arquivovez = open('vezjogada.txt', 'w')
                    contxx = int(str(vez[0])) + 1 #Tava sem criatividade pra variavel xD, mas ela converte o VEZ para string (para aparecer
                    #somente o necessario e então converte para inteiro para que possa ser somada)
                    arquivovez.write(str(contxx))
                    arquivovez.close()
                    if contagem > 0:
                        arquivo = open("Usuariospalpites.txt", "r")
                        for linha in arquivo:
                            ver = linha.split()
                            if(str(query.from_user.id) == str(ver[0])):
                                await bot.send_message(query.from_user.id, "Você já deu seu palpite, não tem volta haha")
                                verpalpite = 1
                        arquivo.close()
                    if verpalpite == 0:
                        arquivo = open("Usuariospalpites.txt", "a")
                        arquivo.write(str(query.from_user.id) +
                                        " " + str(user_data) + "\n")
                else:
                    print("Não é a vez do cara")
                    await bot.send_message(query.from_user.id, "Não é sua vez de dar o palpite, por favor espere =)")
                arquivoo.close()
            arquivovez.close()


            await query.answer(f'Você respondeu com {user_data!r}')

            arquivo = open("Usuariospalpites.txt", "r")
            spalpites = 0
            for palpite in arquivo:
                userpalpite = palpite.split()
                spalpites = int(userpalpite[1]) + spalpites
            arquivo.close()
            print(spalpites)

            reset = open('Usuarioscartas.txt', 'r+')
            reset.truncate(0)
            reset.close()
    elif contagem == 3:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')
        arquivo.write('4\n')
        arquivo.close()
        
        #Resetando a vez da jogada
        
        arquivovez = open("vezjogada.txt",'w+')
        arquivovez.write('1')
        arquivovez.close()

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
            ("0", "0"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
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

        @dp.callback_query_handler(text='0')
        @dp.callback_query_handler(text='1')
        @dp.callback_query_handler(text='2')
        @dp.callback_query_handler(text='3')
        @dp.callback_query_handler(text='4')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            if os.path.exists('Usuariospalpites.txt') == False:
                arquivo = open('Usuariospalpites.txt', 'w+')
                arquivo.close()
            user_data = query.data
            verpalpite = 0           
            
            arquivovez = open('vezjogada.txt', 'r')
            for leituravez in arquivovez:
                vez = leituravez.split()
                arquivoo = open('ousuarios.txt', 'r')
                for linha in arquivoo:
                    posicao = linha.split()

                    uservez = str(query.from_user.id) + " " + str(vez[0])
                    userposicao = str(posicao[0])+ " " + str(posicao[1])
                    print(uservez)
                    print(userposicao)

                if userposicao == uservez:
                    print("O cara deu palpite na hora certa")
                    arquivovez = open('vezjogada.txt', 'w')
                    contxx = int(str(vez[0])) + 1 #Tava sem criatividade pra variavel xD, mas ela converte o VEZ para string (para aparecer
                    #somente o necessario e então converte para inteiro para que possa ser somada)
                    arquivovez.write(str(contxx))
                    arquivovez.close()
                    if contagem > 0:
                        arquivo = open("Usuariospalpites.txt", "r")
                        for linha in arquivo:
                            ver = linha.split()
                            if(str(query.from_user.id) == str(ver[0])):
                                await bot.send_message(query.from_user.id, "Você já deu seu palpite, não tem volta haha")
                                verpalpite = 1
                        arquivo.close()
                    if verpalpite == 0:
                        arquivo = open("Usuariospalpites.txt", "a")
                        arquivo.write(str(query.from_user.id) +
                                        " " + str(user_data) + "\n")
                else:
                    print("Não é a vez do cara")
                    await bot.send_message(query.from_user.id, "Não é sua vez de dar o palpite, por favor espere =)")
                arquivoo.close()
            arquivovez.close()


            await query.answer(f'Você respondeu com {user_data!r}')


            arquivo = open("Usuariospalpites.txt", "r")
            spalpites = 0
            for palpite in arquivo:
                userpalpite = palpite.split()
                spalpites = int(userpalpite[1]) + spalpites
            arquivo.close()
            print(spalpites)

            reset = open('Usuarioscartas.txt', 'r+')
            reset.truncate(0)
            reset.close()

    elif contagem == 4:
        tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus,
                   ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros, bw]
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()
        arquivou = open('Usuarios.txt', 'r')
        arquivo = open('rodada.txt', 'a')
        arquivo2 = open('Usuarioscartas.txt', 'a')
        arquivo.write('5\n')
        arquivo.close()

        #Resetando a vez da jogada
        
        arquivovez = open("vezjogada.txt",'w+')
        arquivovez.write('1')
        arquivovez.close()

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
            ("0", "0"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
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

        @dp.callback_query_handler(text='0')
        @dp.callback_query_handler(text='1')
        @dp.callback_query_handler(text='2')
        @dp.callback_query_handler(text='3')
        @dp.callback_query_handler(text='4')
        @dp.callback_query_handler(text='5')
        async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
            if os.path.exists('Usuariospalpites.txt') == False:
                arquivo = open('Usuariospalpites.txt', 'w+')
                arquivo.close()
            user_data = query.data
            verpalpite = 0           
            
            arquivovez = open('vezjogada.txt', 'r')
            for leituravez in arquivovez:
                vez = leituravez.split()
                arquivoo = open('ousuarios.txt', 'r')
                for linha in arquivoo:
                    posicao = linha.split()

                    uservez = str(query.from_user.id) + " " + str(vez[0])
                    userposicao = str(posicao[0])+ " " + str(posicao[1])
                    print(uservez)
                    print(userposicao)

                if userposicao == uservez:
                    print("O cara deu palpite na hora certa")
                    arquivovez = open('vezjogada.txt', 'w')
                    contxx = int(str(vez[0])) + 1 #Tava sem criatividade pra variavel xD, mas ela converte o VEZ para string (para aparecer
                    #somente o necessario e então converte para inteiro para que possa ser somada)
                    arquivovez.write(str(contxx))
                    arquivovez.close()
                    if contagem > 0:
                        arquivo = open("Usuariospalpites.txt", "r")
                        for linha in arquivo:
                            ver = linha.split()
                            if(str(query.from_user.id) == str(ver[0])):
                                await bot.send_message(query.from_user.id, "Você já deu seu palpite, não tem volta haha")
                                verpalpite = 1
                        arquivo.close()
                    if verpalpite == 0:
                        arquivo = open("Usuariospalpites.txt", "a")
                        arquivo.write(str(query.from_user.id) + " " + str(user_data) + "\n")
                else:
                    print("Não é a vez do cara")
                    await bot.send_message(query.from_user.id, "Não é sua vez de dar o palpite, por favor espere =)")
                arquivoo.close()
            arquivovez.close()


            await query.answer(f'Você respondeu com {user_data!r}')


            arquivo = open("Usuariospalpites.txt", "r")
            spalpites = 0
            for palpite in arquivo:
                userpalpite = palpite.split()
                spalpites = int(userpalpite[1]) + spalpites
            arquivo.close()
            print(spalpites)

            reset = open('Usuarioscartas.txt', 'r+')
            reset.truncate(0)
            reset.close()

    elif contagem == 5:
        print("RESETOU AS RODADAS")
        reset = open('rodada.txt', 'r+')
        reset.truncate(0)
        reset.close()
        resetpalpite = open('Usuariospalpites.txt', 'r+')
        resetpalpite.truncate(0)
        resetpalpite.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

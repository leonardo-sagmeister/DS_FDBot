#Utilize CTRL+C no terminal para encerrar o bot

import logging, os.path, random, asyncio
from time import sleep
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1255502823:AAFduKDPX5DJEkIio5xPG8fYRpHCse55Ba4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
i = 0

@dp.message_handler(commands=['start', 'help', 'Ola'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Olá!\nEu sou o FDPBOT!\nDesenvolvido pela FDBot Developer Team.\nÉ muito legal ter você aqui comigo :)"
    "\nEu utilizo a API da aiogram,\nVocê pode consulta-la aqui: https://docs.aiogram.dev/en/latest/index.html, VOCE INICIOU O BOT")
    await initrodada()
        

async def initrodada(*check):
    rodada = 0
    # print(str(rodada) + " initrodada")
    await plus_rodada(rodada, check)


async def plus_rodada(rodada, *check):
    
    for x in range(int(rodada),5):
        print("Rodada número: " + str(rodada)) 
        rodada += 1 # iterar rodada com +1 int
        sleep(0.7)
        await game(rodada)
        
 

        #ans = input("Nova rodada?")
        if check == (('v',),):
            await plus_rodada(rodada)
            print("ENTROU AQUI")
            check = ''
        else:
            print("resto do jogo")
            game(rodada)

        if rodada > 5:
            print("nº máx de rodadas atingido")
            await initrodada()

async def game(rodada):
    print("Rodada no game é: ")
    print(rodada)
    sleep(1)
    # controdada = rodada
    # print("----inicio de game-----")
    # print(controdada)
    @dp.message_handler(commands='join') 
    async def start_cmd_handler(message: types.Message):
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        texto = (
            ('SIM!', 'sim'),
            ('NÃO!', 'nao'),
        )

        rbotao = (types.InlineKeyboardButton(tex, callback_data=dat) for tex, dat in texto)

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
            #arquivo.write(str(query.from_user.id) + "\n")
            if cont != 1:
                arquivo.write(str(query.from_user.id) + " " + str(query.from_user.full_name) + "\n")
                texto1 = "TOP DEMAIS MANO, BORA JOGAR!"
            elif cont == 1:
                texto1 = "VOCE JA ESTA JOGANDO!"
            arquivo.close
        elif user_data == 'nao':
            texto1 = "BELEZA, NÃO AGUENTA PERDER NÉ?"
        else:
            texto1 = f'Entrada não esperada: {user_data!r}!'
        
        await bot.send_message(query.from_user.id, texto1)


    #Atribuindo o código da figurinha as variaveis de cartas
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
    #Atribuindo valor as cartas
    zap>copas>espadilha>ouros7>joker>paus3>copas3>espadas3>ouros3>paus2>copas2>espadas2>ouros2>aspaus>ascopas>asouros>kpaus>kcopas>kespadas>kouros>jpaus>jcopas>jespadas>jouros>qpaus>qcopas>qespadas>qouros
    #Vetor contendo todas as cartas
    tcartas = [zap, copas, espadilha, ouros7, joker, paus3, copas3, espadas3, ouros3, paus2, copas2, espadas2, ouros2, aspaus, ascopas, asouros, kpaus, kcopas, kespadas, kouros, jpaus, jcopas, jespadas, jouros, qpaus, qcopas, qespadas, qouros]
    #Carta recebida
    rcarta = []

    @dp.message_handler(commands='carta') 
    async def start_cmd_handler(message: types.Message):
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        ctexto = (
            ('Distribuir', 'simd'),
            ('NÃO distribuir!', 'naod'),
        )

        cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

        keyboard_markup.row(*cbotao)
        
        await message.reply("Deseja distribuir as cartas agora?", reply_markup=keyboard_markup)

    @dp.callback_query_handler(text='simd')
    @dp.callback_query_handler(text='naod')
    async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
        user_data = query.data
        await query.answer(f'Você respondeu com {user_data!r}')
        ncartas = 28
        if user_data == 'simd':
                
            while ncartas > 0:
                arquivo = open('Usuarios.txt', 'r')
                arquivo2 = open('Usuarioscartas.txt', 'a')
                for linha in arquivo:
                    userid = linha.split() 
                    send = random.randrange(0, ncartas)

                    arquivo2.write(userid[0] + ' ' + tcartas[send] + "\n")


                    await bot.send_sticker(userid[0], tcartas[send])
                    del (tcartas[send])  
                    ncartas = ncartas-1
                arquivo.close()
                arquivo2.close()
                #---------COMO OBTER AS CARTAS---------------
                # arquivo2 = open('Usuarioscartas.txt', 'r')
                # for linha in arquivo2:
                #     ucarta = linha.split()
                #     print(ucarta[0]+ ' Recebeu a carta '+ ucarta[1])
                # arquivo.close()
        else:
            texto1 = f'Entrada não esperada: {user_data!r}!'

    @dp.message_handler(commands='palpite') 
    async def botaopalpite(message: types.Message):
        
        print("---------------PALPITE---------------------------------")
        print(rodada)
        sleep(1)
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
        if rodada == 1:
            cbotao = (
                ("0","0"),
                ("1","1"),
            )
        if rodada == 2:
            cbotao = (
                ("0","0"),
                ("1","1"),
                ("2","2"),
            )
        if rodada == 3:
            cbotao = (
                ("0","0"),
                ("1","1"),
                ("2","2"),
                ("3","3"),
            )
        if rodada == 4:
            cbotao = (
                ("0","0"),
                ("1","1"),
                ("2","2"),
                ("3","3"),
                ("4","4"),
            )
        if rodada == 5:
            cbotao = (
                ("0","0"),
                ("1","1"),
                ("2","2"),
                ("3","3"),
                ("4","4"),
                ("5","5"),
            )

        ctexto = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in cbotao)

        keyboard_markup.row(*ctexto)
        
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
        await query.answer(f'Você respondeu com {user_data!r}')
        if user_data == '0':
            arquivo = open("Usuariospalpites.txt","a")
            arquivo.write(str(query.from_user.id) + " " + str(user_data))



    #Contador de rodada improvisado
    @dp.message_handler(commands='novarodada') 
    async def start_rodada(message: types.Message):
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

        ctexto = (
            ('Começar nova rodada', 'rodada'),
            ('Não começar nova rodada', 'nrodada'),
        )

        cbotao = (types.InlineKeyboardButton(ctex, callback_data=cdat) for ctex, cdat in ctexto)

        keyboard_markup.row(*cbotao)
        
        await message.reply("Deseja iniciar uma nova rodada?", reply_markup=keyboard_markup)


    @dp.callback_query_handler(text='rodada')
    @dp.callback_query_handler(text='nrodada')
    async def Receptor_botao_rodada(query: types.CallbackQuery):
        user_data = query.data
        if user_data == "rodada":
            check = "v"
            await plus_rodada(rodada, *check)
        await query.answer(f'Você respondeu com {user_data!r}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
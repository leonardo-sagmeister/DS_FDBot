#Utilize CTRL+C no terminal para encerrar o bot

import logging, os.path, random
from time import sleep
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1255502823:AAFduKDPX5DJEkIio5xPG8fYRpHCse55Ba4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help', 'Ola'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    if os.path.exists('rodada.txt') == False:
        arquivo = open('rodada.txt', 'w+')
        arquivo.close()
    await message.reply("Olá!\nEu sou o FDPBOT!\nDesenvolvido pela FDBot Developer Team.\nÉ muito legal ter você aqui comigo :)"
                        "\nEu utilizo a API da aiogram,\nVocê pode consulta-la aqui: https://docs.aiogram.dev/en/latest/index.html, VOCE INICIOU O BOT \nVocê pode dar um /comandos para ver todos os comandos")


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


@dp.message_handler(commands=['players','jogadores'])
async def show_players(message: types.Message):
    users = []
    arquivou = open("Usuarios.txt",'r')
    for user in arquivou:
        username = user.split()
        users.append(str(username[1]))
        
    await message.reply(str(users) + '\n' + 'Estão participando do game')

@dp.message_handler(commands=['comandos'])
async def help_message(message: types.Message):
    
    await message.reply('Lista de comandos :\n /start Informações sobre o BOT\n /players Verificar quem está participando do game\n'
    ' /join Juntar-se a partida\n /nrodada Iniciar uma nova rodada\n')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
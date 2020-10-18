"""
This is a echo bot.
It echoes any incoming text messages.
"""

#Utilize CTRL+C no terminal para encerrar o bot

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1217146552:AAHnCqhnKifnogXmDz6ZC2i1qXTSOF-KfMg'

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
    await message.reply("Olá!\nEu sou o FDPBOT!\nDesenvolvido pela FDBot Developer Team.\nÉ muito legal ter você aqui comigo :)"
    "\nEu utilizo a API da aiogram,\nVocê pode consulta-la aqui: https://docs.aiogram.dev/en/latest/index.html")
    

@dp.message_handler(commands='botao') 
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

    texto = (
        ('SIM!', 'sim'),
        ('NÃO!', 'nao'),
    )

    rbotao = (types.InlineKeyboardButton(tex, callback_data=dat) for tex, dat in texto)

    keyboard_markup.row(*rbotao)
    
    await message.reply("Deseja participar do game?", reply_markup=keyboard_markup)

    


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


@dp.callback_query_handler(text='sim')
@dp.callback_query_handler(text='nao')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    user_data = query.data
    cont = 0
    await query.answer(f'Você respondeu com {user_data!r}')

    if user_data == 'sim':
        
        # try:
        #     with open('Usuario.txt', 'r') as f:
        #         processar_arquivo(f)
        # except IOError:
        #     criacao = open('Usuarios.txt', 'w+')
        #     criacao.close()
        #Precisamos tentar implementar isso ^^^^
        
        arquivo = open('Usuarios.txt', 'r')
        linha = arquivo.readline()

        while linha:
            #ids = linha.split()
            
            #print(ids)
            #print(str(query.from_user.id))
            if linha == (str(query.from_user.id) + ": " + str(query.from_user.full_name) + "\n"):
                cont = 1
            
            linha = arquivo.readline()
        arquivo.close
        arquivo = open('Usuarios.txt', 'a')
        #arquivo.write(str(query.from_user.id) + "\n")
        if cont != 1:
            arquivo.write(str(query.from_user.id) + ": " + str(query.from_user.full_name) + "\n")
            texto1 = "TOP DEMAIS MANO, BORA JOGAR!"
        elif cont == 1:
            texto1 = "VOCE JA ESTA JOGANDO!"
        arquivo.close
    elif user_data == 'nao':
        texto1 = "BELEZA, NÃO AGUENTA PERDER NÉ?"
    else:
        texto1 = f'Entrada não esperada: {user_data!r}!'
    
    await bot.send_message(query.from_user.id, texto1)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    

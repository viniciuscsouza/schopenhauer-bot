import telepot
import time

from database import *
from random import randint
from settings import *

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg['from']['first_name']
        txt = msg['text']
        if '/pensamento' in txt:
            qtd_frases = contaRegistros()
            frase = selecionaDados(randint(0, qtd_frases))
            bot.sendMessage(chat_id, '{}'.format(frase))
        else:
            bot.sendMessage(chat_id, '{} eu nao entendi o seu comando'.format(name))

bot = telepot.Bot(TELEGRAM['TOKEN'])
bot.message_loop(on_chat_message)
print ('O bot esta funcionando...')
while 1:
    time.sleep(10)
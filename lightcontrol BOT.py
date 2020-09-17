!pip install adafruit-io
!pip install python-telegram-bot
x = "Technobot"  #ENTER ADAFRUIT_IO_USERNAME
y = "aio_bPje87dfvLLK5ENh6o4LjnQfkVle"  #ENTER ADAFRUIT_IO_KEY
from Adafruit_IO import Client,Feed
aio = Client(x,y)
feed = Feed(name = 'lightbot')  # Create a feed
result = aio.create_feed(feed)
from Adafruit_IO import Data

from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('lightbot',Data(value = 1))
  bot.send_message(chat_id = chat_id,text = "Lights On")

def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('lightbot',Data(value = 0))
  bot.send_message(chat_id = chat_id,text = "Lights Off")

u = Updater('1309808865:AAEYelDqlFfCqML5azSJp7UlcIQmFsyB0EI')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()

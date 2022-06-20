import sys
import telebot

bot = telebot.TeleBot(sys.argv[1])


@bot.message_handler(content_types='new_chat_members')
def handle_message(message):
    bot.send_animation(message.chat.id, open("welcome.gif", 'rb'), reply_to_message_id=message.id)


bot.polling(none_stop=True)

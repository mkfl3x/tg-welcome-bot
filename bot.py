import os
import telebot

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])


@bot.message_handler(content_types='new_chat_members')
def handle_message(message):
    if message.json['new_chat_member']['id'] != bot.get_me().id:
        bot.send_animation(message.chat.id, open("welcome.gif", 'rb'), reply_to_message_id=message.id)


bot.polling(none_stop=True)

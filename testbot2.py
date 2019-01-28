from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from check_live import SendGet
from data_sites import site_list as site_list

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello I am bot")


def check_live(bot, update, args):
    send_get = SendGet(site_list)
    prod = [i for i in site_list if i[-10:] != '.db.rv.ua/']
    stage = [i for i in site_list if i[-10:] == '.db.rv.ua/']
    if len(args) == 1 and args[0] == 'stage':
        for i in stage:
            bot.send_message(chat_id=update.message.chat_id, text=send_get.send_request_one_site(i))
    if len(args) == 1 and args[0] == 'prod':
        for i in prod:
            bot.send_message(chat_id=update.message.chat_id, text=send_get.send_request_one_site(i))
    if len(args) == 0:
        for i in site_list:
            bot.send_message(chat_id=update.message.chat_id, text=send_get.send_request_one_site(i))
    #if len(args) >= 1:
        #bot.send_message(chat_id=update.message.chat_id, text='unknown argument')


def job_live_prod(bot, job):
    send_get = SendGet(site_list)
    prod = [i for i in site_list if i[-10:] != '.db.rv.ua/']
    for i in prod:
        bot.send_message(chat_id='408478598', text=send_get.send_request_one_site(i))


def sitemap(bot, update, args):
    send_get = SendGet(site_list)
    prod = [i for i in site_list if i[-10:] != '.db.rv.ua/']
    stage = [i for i in site_list if i[-10:] == '.db.rv.ua/']
    if len(args) == 1 and args[0] == 'stage':
        for site in stage:
            for i in send_get.check_sitemap(site, 'sitemap.xml'):
                bot.send_message(chat_id=update.message.chat_id, text=i)
    if len(args) == 1 and args[0] == 'prod':
        for site in prod:
            for i in send_get.check_sitemap(site, 'sitemap.xml'):
                bot.send_message(chat_id=update.message.chat_id, text=i)


def unknown_message(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Unknown message')


def unknown_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Unknown command')


def main():
    updater = Updater('688280487:AAF-WNXpjFBx8lJa6-p-DS2HswhIzh-gDz8', request_kwargs={'read_timeout': None})
    disp = updater.dispatcher
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("check_live", check_live, pass_args=True))
    disp.add_handler(CommandHandler("sitemap", sitemap, pass_args=True))

    job_live = updater.job_queue
    job_live.run_repeating(job_live_prod, interval=2400, first=900)


    disp.add_handler(MessageHandler(Filters.text, unknown_message))
    disp.add_handler(MessageHandler(Filters.command, unknown_command))
    updater.start_polling()


if __name__ == "__main__":
    main()

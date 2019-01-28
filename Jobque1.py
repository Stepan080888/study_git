from telegram.ext import Updater


def callback_minute(bot, job):
    bot.send_message(chat_id='408478598', text='One message every minute')

def callback_30(bot, job):
    bot.send_message(chat_id='408478598', text='A single message with 30s delay')

u = Updater('688280487:AAF-WNXpjFBx8lJa6-p-DS2HswhIzh-gDz8')
j = u.job_queue
job_minute = j.run_repeating(callback_minute, interval=30, first=0)
#j.run_once(callback_30, 30)
#job_minuteenabled = False
#job_minute.schedule_removal()
u.start_polling()

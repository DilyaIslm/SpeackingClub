import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from anketa import anketa_start, anketa_name, anketa_time, anketa_comment
from handlers import eng_level, greet_user, error_callback, payment, back, free, eng_level, eng_level1, weekday, time, choose_teacher, choose_teacher_all, choose_time



logging.basicConfig(filename='bot.log', level=logging.INFO)




def main():
    mybot = Updater("5221898631:AAEFjmV1aPTBSvm0HJuzOfmJmIpj-uxKwPY", use_context=True)

    dp = mybot.dispatcher

    anketa = ConversationHandler(
        entry_points=[
        MessageHandler(Filters.regex('^(Продолжить без преподавателя)$'), anketa_start)
        ],
        states={
            "name": [MessageHandler(Filters.text, anketa_name)],
            "weekday": [MessageHandler(Filters.regex('^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$'), anketa_time)],
            "comment": [MessageHandler(Filters.text, anketa_comment)]
            },
        fallbacks=[]
    )
    dp.add_handler(anketa)

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(C преподавателем)$'), payment))
    dp.add_handler(MessageHandler(Filters.regex('^(Назад)$'), back))
    dp.add_handler(MessageHandler(Filters.regex('^(Без преподавателя)$'), free))
    #dp.add_handler(MessageHandler(Filters.regex('^(https://t.me/SpeakingClubEnglish_bot)$'), kanal))
    dp.add_handler(MessageHandler(Filters.regex('^(Продолжить без преподавателя)$'), eng_level))
    dp.add_handler(MessageHandler(Filters.regex('^(Продолжить с преподавателем)$'), eng_level1))
    dp.add_handler(MessageHandler(Filters.regex('^(Уровень от Elementary A1 - Pre-Intermediate A2-B1)$'), weekday))
    dp.add_handler(MessageHandler(Filters.regex('^(Уровень от Intermediate B1 - Advanced C1)$'), weekday))
    dp.add_handler(MessageHandler(Filters.regex('^(Уровень от Elementary  A1 - Pre-Intermediate A2-B1)$'), choose_teacher))
    dp.add_handler(MessageHandler(Filters.regex('^(Уровень от Intermediate  B1 - Advanced C1)$'), choose_teacher))
    dp.add_handler(MessageHandler(Filters.regex('^(Выбери преподавателя)$'), choose_teacher_all))
    #доделать времяdp.add_handler(MessageHandler(Filters.regex('^(9:00-10:00|13:00-14:00|20:00-21:00|Без разницы)$'), time))
    #dp.add_handler(MessageHandler(Filters.regex('^(с 9-00 - 10-00)$'), time))
    #dp.add_handler(MessageHandler(Filters.regex('^(с 13-00 - 14-00)$'), time))
    #dp.add_handler(MessageHandler(Filters.regex('^(с 20-00 - 21-00)$'), time))
    #dp.add_handler(MessageHandler(Filters.regex('^(Без разницы)$'), time))
    #dp.add_handler(MessageHandler(Filters.regex('^(Назад)$'), free))
   
    #dp.add_handler(MessageHandler(Filters.regex('^(<-)$'), news_back))
    #dp.add_handler(MessageHandler(Filters.regex('^(->)$'), news_forward))
    dp.add_error_handler(error_callback)


    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()    
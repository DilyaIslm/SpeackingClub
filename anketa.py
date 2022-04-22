from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from utils import main_keyboard, free_keyboard, eng_level_keyboard

def anketa_start(update, context):
    update.message.reply_text('Выбери свой уровень английского', reply_markup=eng_level_keyboard())
    

def anketa_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста, напиши имя и фамилию")
        return "name"
    else:
        context.user_data["anketa"] = {"name": user_name}
        reply_keyboard = [["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]]
        update.message.reply_text(
            "Введи удобный для общения день недели",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        ) 
    
        return "weekday"

def anketa_time(update, context):
    #context.user_data["anketa"]["weekday"] = update.message.text

    update.message.reply_text(
        "Введи удобное время для созвона с собеседником и любой комментарий, если есть. Мы найдем для тебя собеседника."
    )
    return "comment" 

def anketa_comment(update, context):
    pass
    #context.user_data["anketa"]["comment"] = update.message.text
    #user_text = f"""<b>Имя Фамилия:</b> {context.user_data['anketa']['name']}
#<b>День недели:</b> {context.user_data['anketa']['weekday']}
#<b>Время и комментарий:</b> {context.user_data['anketa']['comment']}"""

    #update.message.reply_text(user_text, reply_markup=main_keyboard(),
                                #parse_mode=ParseMode.HTML)
    
    #return ConversationHandler.END

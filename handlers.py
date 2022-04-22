from encodings import utf_8

from telegram import replymarkup, ReplyKeyboardRemove
from utils import main_keyboard, payment_keyboard, free_keyboard, kanal_keyboard, eng_level_keyboard, eng_level1_keyboard, weekday_keyboard, time_keyboard, choose_teacher_keyboard



def greet_user(update, context):
    update.message.reply_text(
                            f' Привет, моя миссия помочь тебе найти собеседника, чтобы прокачать скиллы разговорного английского.\n'
                            f'Выбери формат участия:\n'
                            f'- Без преподавателя 1 на 1 с собеседником (бесплатно)\n'
                            f'- С преподавателем в группе от 2 до 6 человек (с оплатой)\n'
                            f'Подпишись на наш  канал - https://t.me/speaking_en_club, здесь будем давать полезные материалы: планы для разговоров, лексику и разные игровые практики\n'
                            f'Для продуктивного общения, нужно определить свой уровень английского языка. Если сомневаешься, можешь пройти тест - https://www.cambridgeenglish.org.ru/test-your-english/general-english/.', reply_markup=main_keyboard()
                            )
        




def payment(update, context):
    update.message.reply_text('Отлично, надеюсь, я смогу помочь подобрать тебе собеседника. Для этого нужно заполнить небольшую форму. Это займет примерно 5 минут; если у тебя возникнут какие-то сложности, пожалуйста, напиши @lera_k0p', reply_markup=payment_keyboard())

def back(update, context):
    update.message.reply_text('Возвращаемся назад', reply_markup=main_keyboard())

def free(update, context):
    update.message.reply_text('Отлично, надеюсь, я смогу помочь подобрать тебе собеседника. Для этого нужно заполнить небольшую форму. Это займет примерно 5 минут; если у тебя возникнут какие-то сложности, пожалуйста, напиши @lera_k0p', reply_markup=free_keyboard())

#def kanal(update, context):
    #update.message.reply_text('Здесь наш телеграм-канал - ___', reply_markup=kanal_keyboard())

def eng_level(update, context):
    update.message.reply_text('Выбери свой уровень английского', reply_markup=eng_level_keyboard())

def eng_level1(update, context):
    update.message.reply_text('Выбери свой уровень английского', reply_markup=eng_level1_keyboard())      

def weekday(update, context):
    update.message.reply_text('Выбери день, когда ты можешь заниматься на этой неделе', reply_markup=weekday_keyboard())


def time(update, context):
    update.message.reply_text('Выбери удобное для занятия время (по мск)', reply_markup=time_keyboard())

def choose_teacher(update, context):
    update.message.reply_text(
                            f'Привет, мы молодая платформа, на данный момент у нас есть только один преподаватель. Ознакомься с  информацией о нем. Если тебя все устроит, в ответном сообщении напиши удобные день и время и преподаватель с тобой свяжется.', reply_markup=choose_teacher_keyboard())


def choose_teacher_all(update, context):
    update.message.reply_text(
                            f'- Имя: Диана Черникова @Chernikdi\n'
                            f'- Опыт преподавания: 6 лет\n'
                            f'- Образование: дипломированный  преподаватель, лингвист; cертифицированный преподаватель TEFL/TESOL.\n'
                            f'- Ссылка на телеграмм канал: https://t.me/teachme_d \n'
                            f'- Время занятия:\n'
                            f'сб:\n'
                                f' 14:30-15:30 \n'
                                f' 16:00-17:00 \n'
                                f'вс:\n'
                                f' 12:00-13:00 \n'
                                f' 13:00-14:00 \n'
                                f' 14:00-15:00 \n'
                                f' 15:00-16:00 \n'
                            f'- Длительность занятия: 60 мин\n'
                            f'- Стоимость: 500 руб.\n', reply_markup=ReplyKeyboardRemove()
                            )
    return "date"
    #else:
        #context.user_data["anketa"] = {"name": user_name}
        #reply_keyboard = [["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]]
        #update.message.reply_text(
            #"Введи удобный для общения день недели",
            #reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        #) 
    
        #return "weekday"

def choose_teacher_all_end(update, context):
    update.message.reply_text(
                            f'Отлично, жди сообщение от преподавателя с подтверждением времени и ссылкой на оплату.',reply_markup=main_keyboard()
                            )                              

def choose_time(update, context):
    update.message.reply_text(
                            f'Напиши время, когда тебе удобнее заниматься\n'
                            f'с 9-00 - 10-00\n'
                            f'с 13-00 - 14-00\n'
                            f'с 20-00 - 21-00\n'
                            f'Без разницы\n', reply_markup=main_keyboard()
                            )   

             
               



def error_callback(update, error):
    try:
        raise error
    except:
        print("Telegram Error")
        print(f'Error with {update.message.text}')
        update.message.reply_text(f'Error with {update.message.text}. Try again')
        print(error)
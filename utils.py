from telegram import ReplyKeyboardMarkup, KeyboardButton
#import settings

def main_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('C преподавателем')],
                                [KeyboardButton('Без преподавателя')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)
                               


def payment_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Продолжить с преподавателем')],
                                #[KeyboardButton('Анкета')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)

def free_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Продолжить без преподавателя')],
                                #[KeyboardButton('Анкета')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)

def eng_level_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Уровень от Elementary A1 - Pre-Intermediate A2-B1')],
                                [KeyboardButton('Уровень от Intermediate B1 - Advanced C1')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)

def eng_level1_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Уровень от Elementary  A1 - Pre-Intermediate A2-B1')],
                                [KeyboardButton('Уровень от Intermediate  B1 - Advanced C1')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)                               

def weekday_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Будние')],
                                [KeyboardButton('Выходные')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)

def time_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('с 9-00 - 10-00')],
                                [KeyboardButton('с 13-00 - 14-00')],
                                [KeyboardButton('с 20-00 - 21-00')],
                                [KeyboardButton('Без разницы' )],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True) 



def choose_teacher_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Выбери преподавателя')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)                                
                                                                                                                                                              

def kanal_keyboard():
    return ReplyKeyboardMarkup([[KeyboardButton('Ссылка на канал')],
                                [KeyboardButton('Темы недели')],
                                [KeyboardButton('Назад')]
                                ], resize_keyboard=True)
#def news_keyboard():
    #return ReplyKeyboardMarkup([[KeyboardButton('<-'), KeyboardButton('Вверх'), KeyboardButton('->')]
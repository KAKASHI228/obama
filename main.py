command = { # Описание команд использующиеся в команде /help
    'start' : 'Стартовое сообщение и предложение зарегестрироваться',
    'help' : 'Информация о боте и список доступных команд',
    'registration' : 'Выбор учебного заведения, выбор факультета и группы для вывода информации',
    'send_report' : 'Отправка обратной связи',
    'auto_posting_on <ЧЧ:ММ>' : 'Подписка на автоматическую рассылку расписания'
    'auto_posting_off' : 'Выключение автоматической отправки сообщения'
}
#Создаём клавиатуру на все дни
def get_date_keyboard():
    
import datetime as dt


class Record:
    def __init__(self, amount=float, comment=str, date=None):
        self.amount = amount
        self.comment = comment
        now = dt.datetime.now()
        if date is None:
            self.date = now.date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record: Record):
        self.records.append(record)

    def get_today_stats(self):
        sum_amount = 0
        now = dt.datetime.now()
        for record in self.records:
            if record.date == now.date():
                sum_amount += record.amount
        return sum_amount

    def get_week_stats(self):
        now = dt.datetime.now()
        amount_7sum = 0
        seven_days_ago = now.date() - dt.timedelta(days=7)
        for record in self.records:
            if seven_days_ago <= record.date <= now.date():
                amount_7sum += record.amount
        return amount_7sum


class CashCalculator(Calculator):
    USD_RATE = float(75.53)
    EURO_RATE = float(91.52)
    today_cash_remained = 0

    def get_today_cash_remained(self, currency):
        if currency == 'usd':
            today_cash_remained = round(((
                self.limit - self.get_today_stats()) / self.USD_RATE), 2)
            currency_value = 'USD'
        elif currency == 'eur':
            today_cash_remained = round(((
                self.limit - self.get_today_stats()) / self.EURO_RATE), 2)
            currency_value = 'Euro'
        elif currency == 'rub':
            today_cash_remained = round((
                self.limit - self.get_today_stats()), 2)
            currency_value = 'руб'

        if self.get_today_stats() < self.limit:
            answer_cash1 = 'На сегодня осталось ' + str(today_cash_remained) + ' ' + str(currency_value)
            return answer_cash1
        elif self.get_today_stats() == self.limit:
            answer_cash2 = 'Денег нет, держись'
            return answer_cash2
        else:
            answer_cash3 = 'Денег нет, держись: твой долг - ' + str(abs(today_cash_remained)) + ' ' + str(currency_value)
            return answer_cash3


class CaloriesCalculator(Calculator):
    today_calories_remained = 0

    def get_calories_remained(self):
        today_calories_remained = abs(self.limit - self.get_today_stats())
        if self.get_today_stats() < self.limit:
            answer_calor1 = 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более ' + str(today_calories_remained) + ' ' + 'кКал'
            return answer_calor1
        else:
            answer_calor2 = 'Хватит есть!'
            return answer_calor2
# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи должна автоматически
# добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(
    amount=3000, comment="бар в Танин др", date="08.11.2019"))

calories_calculator.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
calories_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
calories_calculator.add_record(Record(
    amount=3000, comment="бар в Танин др", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained("rub"))
print(calories_calculator.get_calories_remained())

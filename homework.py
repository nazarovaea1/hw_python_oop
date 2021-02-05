import datetime as dt


class Record:
    def __init__(self, amount=float, comment=str, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record: Record):
        self.records.append(record)

    def get_today_stats(self):
        sum_amount = [record.amount for record in self.records if
                      record.date == dt.date.today()]
        return sum(sum_amount)

    def get_week_stats(self):
        seven_days_ago = dt.date.today() - dt.timedelta(days=7)
        amount_7sum = [record.amount for record in self.records if
                       seven_days_ago <= record.date <= dt.date.today()]
        return sum(amount_7sum)


class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00
    today_cash_remained = 0
    currency_dict = {
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro'),
        'rub': (1.00, 'руб'),
        }

    def get_today_cash_remained(self, currency):
        a = self.currency_dict[currency]
        today_cash_remained = round(((
            self.limit - self.get_today_stats()) / a[0]), 2)
        if self.get_today_stats() < self.limit:
            answer_cash = (f'На сегодня осталось {today_cash_remained} '
                           f'{a[1]}')
            return answer_cash
        elif self.get_today_stats() == self.limit:
            return 'Денег нет, держись'
        else:
            cash_rem_abs = abs(today_cash_remained)
            answer_cash2 = ('Денег нет, держись: твой долг - '
                            f'{cash_rem_abs} {a[1]}')
            return answer_cash2


class CaloriesCalculator(Calculator):
    today_calories_remained = 0

    def get_calories_remained(self):
        today_calories_remained = abs(self.limit - self.get_today_stats())
        if self.get_today_stats() < self.limit:
            answer_calor = ('Сегодня можно съесть что-нибудь ещё, но с общей '
                            'калорийностью не более '
                            f'{today_calories_remained} кКал')
            return answer_calor
        return 'Хватит есть!'

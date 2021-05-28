import locale
from datetime import datetime, timedelta

"""
Домашнее задание №2
Дата и время
1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime
"""

locale.setlocale(locale.LC_ALL, "russian")


def print_days():
      """
      Эта функция вызывается автоматически при запуске скрипта в консоли
      В ней надо заменить pass на ваш код
      """

      dt_now = datetime.today().date()
      delta = timedelta(days=1)
      dt_yesterday = dt_now - delta
      dt_30dago = dt_now - 30 * delta

      dt_now_str = dt_now.strftime('%d-%B-%Y')
      dt_yesterday_str = dt_yesterday.strftime('%d-%B-%Y')
      dt_30dago_str = dt_30dago.strftime('%d-%B-%Y')

      print(f"Сегодня: {dt_now_str}, вчера: {dt_yesterday_str},"
            f" 30 дней назад: {dt_30dago_str} \n")


def str_2_datetime(date_string):
      """
      Эта функция вызывается автоматически при запуске скрипта в консоли
      В ней надо заменить pass на ваш код
      """
      try:
            date_ex = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
      except ValueError as err:
            return f'не удалось преобразовать время в объект datetime:\n{err}'


      return f"объект datetime: {date_ex}, тип: {type(date_ex)}"


if __name__ == "__main__":
      print_days()
      print(str_2_datetime("01/01/20 12:10:03.234567"))


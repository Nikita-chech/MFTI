import calendar

print(dir(calendar)) #выводим список атрибутов

print(calendar.isleap(2023)) #является ли 2023 год високосным

print(calendar.weekday(2000, 5, 25)) #выводит день недели для этой даты

print(calendar.calendar(2023)) #выводит календарь на 2023 год
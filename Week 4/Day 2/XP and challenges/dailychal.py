# import datetime

# today = datetime.date.today()
# print(today)



 
# # birthdate = input("yyyy-mm-dd: ")
# year = int(input('year'))
# month = int(input('month'))
# day = int(input('day'))

# your_bday = datetime.date(year, month, day)
# print(your_bday)

# days_apart = (today - your_bday)

# print(age)
# #######
# print(bday)


# formatted_date = datetime.date.strftime(date_object, "%m/%d/%Y")
# print(formatted_date)




birthdate = input("birthdate in MM/DD/YYYY")

day, month, year =list(map(int,birthdate.split('/')))

print(day, month, year)
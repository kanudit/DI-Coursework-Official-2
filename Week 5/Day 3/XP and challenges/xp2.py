from datetime import datetime
# ex 1
def today():
    return datetime.now()

# ex 2 how to get current date and time
def until_new_years():
    today = datetime.now()
    new_year = datetime(day=1, month=1, year=2022)
    days_left = new_year - today
    print (f'Time until New Years {days_left}')

until_new_years()

# ex 3

def minutes_of_suffering(yom,chodesh,shana):
    dob = datetime(day=yom, month=chodesh, year=shana)
    today = datetime.now()
    time_alive = today - dob
    seconds_alive = time_alive.total_seconds()
    minutes_suffered = seconds_alive/60
    print(f'{int(minutes_suffered)}  Minutes Alive')
    

minutes_of_suffering(7,11,1996)



def until_holiday():
    today = datetime.now()
    holiday_date = datetime(day=6, month=9, year=2021)
    holiday_name = "Labor Day"
    time_left = holiday_date - today
    print (f'Time until {holiday_name} is  {time_left}')

until_holiday()

def space_years():
    seconds = int(input('seconds you\'ve been alive: '))
    years = seconds/60/60/24/365

    earth_years = years
    mercury_years = years/0.2408467 
    venus_years = years/0.61519726
    Mars_years = years/1.8808158 
    jupiter_years = years/11.862615 
    saturn_years = years/29.447498
    uranus_years = years/84.016846
    neptune_years = years/164.79132

    print (f'You are {jupiter_years} years old on Jupiter')

space_years()

from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

users = []

def add_user():
    num_users = int(input('Number of users: '))
    #need to validate, how?

    for people in range(num_users):
        users.append({'name': fake.name() , 'address': fake.address(), 'language': fake.language_name()})
    for person in users:
        print (f"{person['name']} {person['address']}, {person['language']}\n")

    # print(users)
add_user()




















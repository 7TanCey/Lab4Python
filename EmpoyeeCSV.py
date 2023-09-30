import random
import datetime
import pandas as pd
from faker import Faker

fake = Faker('en_US')

data = {
    'Прізвище': [],
    'Ім’я': [],
    'По-батькові': [],
    'Стать': [],
    'Дата народження': [],
    'Посада': [],
    'Місто проживання': [],
    'Адреса проживання': [],
    'Телефон': [],
    'Email': []
}

for _ in range(2000):
    gender = 'Чоловіча' if random.random() <= 0.6 else 'Жіноча'

    last_name = fake.last_name()
    if gender == 'Чоловіча':
        first_name = fake.first_name_male()
        middle_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()
        middle_name = fake.first_name_female()

    birthdate = fake.date_of_birth(minimum_age=15, maximum_age=85)
    position = fake.job()
    city = fake.city()
    address = fake.address()
    phone_number = fake.phone_number()
    email = fake.email()

    data['Прізвище'].append(last_name)
    data['Ім’я'].append(first_name)
    data['По-батькові'].append(middle_name)
    data['Стать'].append(gender)
    data['Дата народження'].append(birthdate.strftime('%d.%m.%Y'))
    data['Посада'].append(position)
    data['Місто проживання'].append(city)
    data['Адреса проживання'].append(address)
    data['Телефон'].append(phone_number)
    data['Email'].append(email)

df = pd.DataFrame(data)
df.to_csv('employee.csv', index=False, encoding='utf-8')
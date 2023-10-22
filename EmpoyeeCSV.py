import csv
from faker import Faker
import random

fake = Faker('uk_UA')

with open('employee.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження',
                  'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    print("Дані записано у файл!")

    male_middle_names = ['Іванович', 'Петрович', 'Олегович', 'Андрійович', 'Михайлович', 'Васильович', 'Сергійович', 'Ярославович', 'Денисович', 'Артемович']
    female_middle_names = ['Іванівна', 'Петрівна', 'Олегівна', 'Андріївна', 'Михайлівна', 'Василівна', 'Сергіївна', 'Ярославівна', 'Денисівна', 'Артемівна']

    for _ in range(2000):
        gender = 'Чоловіча' if random.random() <= 0.6 else 'Жіноча'

        last_name = fake.last_name()
        first_name = fake.first_name_male() if gender == 'Чоловіча' else fake.first_name_female()
        middle_name = random.choice(male_middle_names) if gender == 'Чоловіча' else random.choice(female_middle_names)

        birthdate = fake.date_of_birth(minimum_age=15, maximum_age=85)
        position = fake.job()
        city = fake.city()
        address = fake.address()
        phone_number = fake.phone_number()
        email = fake.email()

        writer.writerow({
            'Прізвище': last_name,
            'Ім’я': first_name,
            'По батькові': middle_name,
            'Стать': gender,
            'Дата народження': birthdate.strftime('%d.%m.%Y'),
            'Посада': position,
            'Місто проживання': city,
            'Адреса проживання': address,
            'Телефон': phone_number,
            'Email': email
        })

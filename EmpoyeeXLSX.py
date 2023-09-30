import pandas as pd
from datetime import datetime

try:
    df = pd.read_csv('employee.csv', encoding='utf-8')
except FileNotFoundError:
    print("Файл CSV не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка завантаження файлу CSV: {str(e)}")
    exit(1)

def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, '%d.%m.%Y')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

df['Вік'] = df['Дата народження'].apply(calculate_age)

df.insert(0, '№', range(1, len(df) + 1))

df_younger_18 = df[df['Вік'] < 18]
df_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)]
df_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)]
df_older_70 = df[df['Вік'] > 70]

try:
    with pd.ExcelWriter('employee.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='all', index=False)
        df_younger_18.to_excel(writer, sheet_name='younger_18', index=False)
        df_18_45.to_excel(writer, sheet_name='18-45', index=False)
        df_45_70.to_excel(writer, sheet_name='45-70', index=False)
        df_older_70.to_excel(writer, sheet_name='older_70', index=False)

    print("Все добре.")
except Exception as e:
    print(f"Помилка створення XLSX файлу: {str(e)}")
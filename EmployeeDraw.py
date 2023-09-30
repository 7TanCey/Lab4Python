import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def process_csv_file(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        print("Ok: Файл CSV успішно завантажено.")
    except FileNotFoundError:
        print("Помилка: файл CSV не знайдено або немає доступу.")
        return
    except Exception as e:
        print(f"Помилка при завантаженні файлу CSV: {str(e)}")
        return

    date_of_birth_column = "Дата народження"

    df[date_of_birth_column] = pd.to_datetime(df[date_of_birth_column], format='%d.%m.%Y', errors='coerce')
    today = pd.to_datetime('today')
    df['Вік'] = today.year - df[date_of_birth_column].dt.year - ((today.month > df[date_of_birth_column].dt.month) | ((today.month == df[date_of_birth_column].dt.month) & (today.day >= df[date_of_birth_column].dt.day)))


    gender_counts = df['Стать'].value_counts()
    print("\nКількість співробітників чоловічої та жіночої статі:")
    print(gender_counts)

    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    plt.title('Розподіл співробітників за статтю')
    plt.show()

    bins = [0, 18, 45, 70, 100]
    age_labels = ["Молодше 18", "18-45", "45-70", "Старше 70"]
    df['Вікова категорія'] = pd.cut(df['Вік'], bins, labels=age_labels, right=False)
    age_category_counts = df['Вікова категорія'].value_counts().sort_index()
    print("\nКількість співробітників у кожній віковій категорії:")
    print(age_category_counts)

    plt.figure(figsize=(8, 6))
    age_category_counts.plot(kind='bar')
    plt.title('Розподіл співробітників за віковою категорією')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.show()

    gender_age_counts = df.groupby(['Стать', 'Вікова категорія']).size().unstack(fill_value=0)
    print("\nКількість співробітників жіночої та чоловічої статі в кожній віковій категорії:")
    print(gender_age_counts)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for i, ax in enumerate(axes.flatten()):
        category = age_labels[i]
        gender_age_counts[category].plot(kind='bar', ax=ax)
        ax.set_title(f'{category} - Чоловіча та Жіноча')
        ax.set_xlabel('Стать')
        ax.set_ylabel('Кількість співробітників')
    plt.tight_layout()
    plt.show()
process_csv_file('employee.csv')
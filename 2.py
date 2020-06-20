def my_user(name, surname, year, city, email, tel):
    print(f"Имя - {name}; Фамилия - {surname}; Год рождения - {year}; "
          f"Город проживания - {city}; Email - {email}; Telephone = {tel}")


my_user(name=input('Введите имя: '), surname=input('Введите фамилию: '),
        year=input('Введите год рождения: '), city=input('Введите город проживания: '),
        email=input('Введите email: '), tel=input('Введите номер телефона: '))

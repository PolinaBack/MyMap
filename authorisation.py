from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.Qt import *
import sqlite3
from geopy.geocoders import Nominatim
# подключение используемых библиотек

# глобальные переменные для работы создания и изменения заметок
username = ''
user_id = 0
name_for_redacting = ''
name_for_redacting2 = ''
previous_username = ''
counter = 0
counter_2 = 0

# класс авторизации пользователя
class Another_autharisation(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/authorisation.ui', self)
        self.setWindowTitle('Авторизация')
        self.log_in.clicked.connect(self.login)
        self.sign_up.clicked.connect(self.signUp)
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.pushButton_3.clicked.connect(self.open_main_form)
        qApp.setStyleSheet("QMessageBox QPushButton{background-color: white;}")

    # функция для входа в свой аккаунт
    def login(self):
        global username
        global user_id
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        username = self.login_edit.text()
        password = self.pass_edit.text()
        # создание параметров для вывода вспомогательного окна-сообщения
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        result = cur.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchall()
        # проверка на ошибки
        if result != [] and result[0][2] == password:
            user_id = cur.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchall()[0][0]
            print('here')
            self.open_second_form()
        elif result != [] and result[0][2] != password:
            valid.setText('Проверьте правильность ввода пароля!')
            valid.exec()
        else:
            valid.setText('Проверьте правильность ввода данных!')
            valid.exec()

        cur.close()
        con.close()

    # функция регистрации
    def signUp(self):
        global username
        global user_id
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        username = self.login_edit.text()
        password = self.pass_edit.text()
        # создание параметров для вывода вспомогательного окна-сообщения
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        result = cur.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchall()
        # проверка на ошибки
        if username == '' and password == '':
            valid.setText('Ошибка! Вы не ввели данные!')
            valid.exec()

        elif username != '' and password == '':
            valid.setText('Ошибка! Вы не ввели пароль!')
            valid.exec()

        elif username == '' and password != '':
            valid.setText('Ошибка! Вы не ввели имя пользователя!')
            valid.exec()

        elif result:
            valid.setText('Ошибка! Такой ник уже используется!')
            valid.exec()

        elif not result and username != '' and password != '':
            # успешная регистрация, запись данных в бд
            cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
            con.commit()
            valid.setText('Вы успешно зарегистрированы!')
            valid.exec()
            user_id = cur.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchall()[0][0]
        cur.close()
        con.close()


    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция для обратного перехода к главному меню
    def open_main_form(self):
        from main import Entering
        self.second_form = Entering()
        self.second_form.show()
        self.close()

    # функция для открытия личного кабинета пользователя
    def open_second_form(self):
        self.second_form = User_inside()
        self.second_form.show()
        self.close()

# класс личного кабинета пользователя
class User_inside(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/user_profil.ui', self)
        self.setWindowTitle('Личный кабинет')
        self.add_button.clicked.connect(self.add_new_group)
        self.redact_last_button.clicked.connect(self.redact_last)
        self.pushButton_3.clicked.connect(self.open_main_form)
        self.label.setText(f'Приветствуем, {username}!')
        self.tomap.clicked.connect(self.open_map)
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        # установка настоящего количества сделанных заметок и путешествий
        travels = cur.execute(f"""SELECT group_name FROM Files WHERE username = '{username}'""").fetchall()
        print(set(travels))
        place = cur.execute(f"""SELECT place_name FROM Files WHERE username = '{username}'""").fetchall()
        print(place)
        con.commit()
        con.close()
        self.travels_label.setText(str(len(set(travels))))
        self.place_label.setText(str(len(set(place))))

    # функция для открытия собственной карты
    def open_map(self):
        from main import MyApp
        self.second_form = MyApp(username=username)
        self.second_form.show()
        self.close()

    # функция по открытию класса для добавления новой заметки
    def add_new_group(self):
        self.second_form = Add_file()
        self.second_form.show()
        self.close()

    # функция по редактированию заметки
    def redact_last(self):
        self.second_form = Redact_file()
        self.second_form.show()
        self.close()


    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def open_main_form(self):
        from main import Entering
        self.second_form = Entering()
        self.second_form.show()
        self.close()

# класс по добавлению новой заметки
class Add_file(QWidget):
    def __init__(self):
        super().__init__()
        global username
        uic.loadUi('forms/add_new_place.ui', self)
        self.setWindowTitle('Добавление заметки')
        print('here')
        self.pushButton_3.clicked.connect(self.open_form_before)
        self.save_button.clicked.connect(self.adding)
        self.add_one_more.clicked.connect(self.clean_for_add)

    def adding(self):
        global counter_2
        global name_for_redacting2
        # создание параметров для вывода вспомогательного окна-сообщения
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # проверка на добавление новой заметки или на повторное сохранение уже добавленной
        if name_for_redacting2 != self.plainTextEdit_2.toPlainText():
            counter_2 = 0
        name_place = self.plainTextEdit_2.toPlainText()
        name_for_redacting2 = name_place
        name_travel = self.name_travel.text()
        note_message = self.plainTextEdit.toPlainText()

        con = sqlite3.connect('data_base/users_data.db')
        # по названию определяем координаты города для проставления маркера
        geolocator = Nominatim(user_agent="Tester")  # Указываем название приложения (так нужно, да)
        location = geolocator.geocode(name_place)
        cur = con.cursor()
        result = cur.execute(f'SELECT * FROM Files WHERE username = "{username}" and place_name = "{name_place}"').fetchall()
        # реакции на ошибки
        if name_place == '' and self.sender().text() == 'Сохранить':
            valid.setText('Назовите город!')
            valid.exec()
        elif location == None:
            print('no loc')
            valid.setText('Мы не нашли такого места, попробуйте еще раз')
            valid.exec()
        elif result and counter_2 == 0:
            valid.setText(f"<html><body><p>Заметка об этом месте уже существует!</p> "
                          f"<p>Для её редактирования, выберите соответствующую команду</p></body></html>")
            valid.exec()
        elif counter_2 == 1:
            # повторное сохранение существующей заметки
            coords = f"{location.latitude}, {location.longitude}"
            print(coords)
            result1 = cur.execute(
                f"""UPDATE Files SET note = '{note_message}', group_name = '{name_travel}', place_name = '{name_place}', 
                 coords_place = '{coords}' WHERE username = '{username}' and place_name = '{name_place}'""").fetchone()
            valid.setText('Заметка успешно обновлена')
            valid.exec()
            con.commit()
            con.close()
        else:
            # добавление новой заметки
            coords = f"{location.latitude}, {location.longitude}"
            print(coords)
            result = cur.execute(
                f"""INSERT INTO Files (username, place_name, coords_place, group_name, note) VALUES('{username}', '{name_place}',
                                 '{coords}', '{name_travel}', '{note_message}')""").fetchall()
            valid.setText('Заметка успешно добавлена')
            valid.exec()
            counter_2 = 1
            con.commit()
            con.close()

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # обработка кнопки "назад"
    def open_form_before(self):
        self.second_form = User_inside()
        self.second_form.show()
        self.close()

    # очищение полей для добавления еще одной заметки с тем же путешествием
    def clean_for_add(self):
        global counter_2
        self.plainTextEdit.setPlainText('')
        self.plainTextEdit_2.setPlainText('')
        counter_2 = 0

# класс редактирования заметки
class Redact_file(QWidget):
    def __init__(self):
        super().__init__()
        global username
        uic.loadUi('forms/redact_place.ui', self)
        self.setWindowTitle('Редактирование заметки')
        print('here')
        self.label_3.setText('Имя редактируемого места')
        self.add_one_more.setText('Найти заметку')
        self.save_button.setText('Сохранить изменения')
        self.pushButton_3.clicked.connect(self.open_form_before)
        self.save_button.clicked.connect(self.redacting)
        self.add_one_more.clicked.connect(self.find_redact_file)
        self.del_button.clicked.connect(self.del_file)

    # функция с поиском необходимой редактируемой заметки
    def find_redact_file(self):
        global name_for_redacting
        global previous_username
        global counter
        flag = True
        # создание параметров для вывода вспомогательного окна-сообщения
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # поиск заметки, в названии места которой присутсвует искомое слово
        # при повторном нажатии кнопки перелистывается на следующую найденную заметку
        if name_for_redacting in self.plainTextEdit_2.toPlainText() and name_for_redacting != '':
            counter += 1
            flag = False
        # обнуление результатов поиска при изменении искомого слова
        if username != previous_username:
            name_for_redacting = ''
            counter = 0
        try:
            con = sqlite3.connect('data_base/users_data.db')
            cur = con.cursor()
            if flag:
                name_for_redacting = self.plainTextEdit_2.toPlainText()
            result = cur.execute(f"""SELECT place_name, group_name, note FROM Files WHERE place_name LIKE '%{name_for_redacting}%' and username = '{username}'""").fetchall()
            if counter > len(result) - 1:
                counter = 0
            # реакция на ошибки
            if not result:
                valid.setText("Не найдено ни одной заметки с похожим названием")
                valid.exec()
            if self.plainTextEdit_2.toPlainText() == '':
                valid.setText("Вы не ввели названия искомого города!")
                valid.exec()
            else:
                # вывод информации о найденной заметке
                self.name_travel.setText(result[counter][1])
                self.plainTextEdit_2.setPlainText(result[counter][0])
                self.plainTextEdit.setPlainText(result[counter][2])
            con.commit()
            con.close()
            previous_username = username
        except Exception:
            pass

    # функция редактирования заметки
    def redacting(self):
        global username
        # создание параметров для вывода вспомогательного окна-сообщения
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        name_place = self.plainTextEdit_2.toPlainText()
        name_travel = self.name_travel.text()
        note_message = self.plainTextEdit.toPlainText()
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        try:
            if name_place == '':
                valid.setText('Данная заметка не найдена!')
                valid.exec()
            else:
                result1 = cur.execute(
                    f"""UPDATE Files SET note = '{note_message}', group_name = '{name_travel}' WHERE username = '{username}' and place_name = '{name_place}'""").fetchone()
                con.commit()
                valid.setText('Изменения успешно сохранены')
                valid.exec()
        except Exception:
            print('непредвиденная ошибка')


    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # обработка кнопки "назад"
    def open_form_before(self):
        self.second_form = User_inside()
        self.second_form.show()
        self.close()

    # функция по удалению заметки
    def del_file(self):
        global username
        # создание параметров для вывода вспомогательного окна-сообщения
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        print('here')

        name_place = self.plainTextEdit_2.toPlainText()
        name_travel = self.name_travel.text()
        note_message = self.plainTextEdit.toPlainText()
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        try:
            if name_place == '':
                valid.setText('Данная заметка не найдена!')
                valid.exec()
            else:
                # создание параметров для вывода вспомогательного окна-сообщения
                # окно - подтверждение об удалении замети
                valid2 = QMessageBox()
                valid2.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                                    "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                                    "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
                valid2.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                yes_but = valid2.addButton('Да', valid2.YesRole)
                valid2.addButton('Нет', valid2.NoRole)
                valid2.setText('Вы действительно хотите удалить заметку?')
                valid2.exec()
                if valid2.clickedButton() == yes_but:
                    result1 = cur.execute(
                        f"""DELETE FROM Files WHERE username = '{username}' and place_name = '{name_place}' 
                        and note = '{note_message}' and group_name = '{name_travel}'""").fetchone()
                    con.commit()
                    valid.setText('Заметка успешно удалена')
                    valid.exec()
                    self.plainTextEdit_2.setPlainText('')
                    self.name_travel.setText('')
                    self.plainTextEdit.setPlainText('')
        except Exception:
            print('ошибка')

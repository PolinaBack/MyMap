import time
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, qApp
import sys
import math
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sqlite3
from geopy.geocoders import Nominatim
import io
import folium
from folium.plugins import Geocoder
from PyQt5.QtWebEngineWidgets import QWebEngineView

# удаление заметки

username = ''
user_id = 0
name_for_redacting = ''
name_for_redacting2 = ''
previous_username = ''
counter = 0
counter_2 = 0


# сделать ли поле интересный факт при авторизации, лэйбл авторизации убрать и оставить слово авторизация только в заголовке окна

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

    def login(self):
        global username
        global user_id
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        username = self.login_edit.text()
        password = self.pass_edit.text()
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        result = cur.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchall()

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


    def signUp(self):
        global username
        global user_id
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        username = self.login_edit.text()
        password = self.pass_edit.text()
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        result = cur.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchall()

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
            print('here')
            cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")

            con.commit()
            valid.setText('Вы успешно зарегистрированы!')
            valid.exec()
            user_id = cur.execute(f'SELECT * FROM Users WHERE username = "{username}"').fetchall()[0][0]
        cur.close()
        con.close()


    def closeEvent(self, event):
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def open_main_form(self):
        from all_work2_222 import Entering
        self.second_form = Entering()
        self.second_form.show()
        self.close()

    def open_second_form(self):
        self.second_form = User_inside()
        self.second_form.show()
        self.close()


class User_inside(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/user_profil.ui', self)
        self.setWindowTitle('Личный кабинет')
        # print('here')
        self.add_button.clicked.connect(self.add_new_group)
        self.redact_last_button.clicked.connect(self.redact_last)
        # print('here')
        self.pushButton_3.clicked.connect(self.open_main_form)
        self.label.setText(f'Приветствуем, {username}!')
        self.tomap.clicked.connect(self.open_map)
        # print('here')
        # for i in range(1, 10000):
        #     self.travels_label.setText(str(i))
        #     time.sleep(0.02)
        # print('here')
        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        travels = cur.execute(f"""SELECT group_name FROM Files WHERE username = '{username}'""").fetchall()
        print(set(travels))
        place = cur.execute(f"""SELECT place_name FROM Files WHERE username = '{username}'""").fetchall()
        print(place)
        con.commit()
        con.close()
        self.travels_label.setText(str(len(set(travels))))

        # print('here')
        # for j in range(1, 10000):
        #     self.place_label.setText(str(j))
            # time.sleep(0.02)
        self.place_label.setText(str(len(set(place))))
        # print('here')

    def open_map(self):
        from all_work2_222 import MyApp
        self.second_form = MyApp(username=username)
        self.second_form.show()
        self.close()


    def add_new_group(self):
        self.second_form = Add_file()
        self.second_form.show()
        self.close()


    def redact_last(self):
        self.second_form = Redact_file()
        self.second_form.show()
        self.close()


    def closeEvent(self, event):
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def open_main_form(self):
        from all_work2_222 import Entering
        self.second_form = Entering()
        self.second_form.show()
        self.close()


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
        # так себе идея с таким огромным количеством глобальных переменных..
        print(counter_2)
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        print('here')
        if name_for_redacting2 != self.plainTextEdit_2.toPlainText():
            counter_2 = 0
        name_place = self.plainTextEdit_2.toPlainText()
        name_for_redacting2 = name_place
        print(name_place)
        name_travel = self.name_travel.text()
        note_message = self.plainTextEdit.toPlainText()
        print('here!')
        con = sqlite3.connect('data_base/users_data.db')
        geolocator = Nominatim(user_agent="Tester")  # Указываем название приложения (так нужно, да)
        location = geolocator.geocode(name_place)
        print(location)
        cur = con.cursor()
        result = cur.execute(f'SELECT * FROM Files WHERE username = "{username}" and place_name = "{name_place}"').fetchall()

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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def open_form_before(self):
        self.second_form = User_inside()
        self.second_form.show()
        self.close()

    def clean_for_add(self):
        global counter_2
        self.plainTextEdit.setPlainText('')
        self.plainTextEdit_2.setPlainText('')
        counter_2 = 0


class Redact_file(QWidget):
    def __init__(self):
        super().__init__()
        global username
        uic.loadUi('forms/redact_place.ui', self)
        self.setWindowTitle('Добавление заметки')
        print('here')
        self.label_3.setText('Имя редактируемого места')
        self.add_one_more.setText('Найти заметку')
        self.save_button.setText('Сохранить изменения')
        self.pushButton_3.clicked.connect(self.open_form_before)
        self.save_button.clicked.connect(self.redacting)
        self.add_one_more.clicked.connect(self.find_redact_file)
        self.del_button.clicked.connect(self.del_file)

    def find_redact_file(self):
        global name_for_redacting
        global previous_username
        global counter
        flag = True
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        if name_for_redacting in self.plainTextEdit_2.toPlainText() and name_for_redacting != '':
            counter += 1
            flag = False
        if username != previous_username:
            name_for_redacting = ''
            counter = 0

        print(counter)
        print(name_for_redacting)
        try:
            con = sqlite3.connect('data_base/users_data.db')
            cur = con.cursor()
            if flag:
                name_for_redacting = self.plainTextEdit_2.toPlainText()
            # previous_name_for_redacting = name_for_redacting
            print(name_for_redacting)
            result = cur.execute(f"""SELECT place_name, group_name, note FROM Files WHERE place_name LIKE '%{name_for_redacting}%' and username = '{username}'""").fetchall()
            print(result)
            if counter > len(result) - 1:
                counter = 0
            print('here!')
            if not result:
                valid.setText("Не найдено ни одной заметки с похожим названием")
                valid.exec()
            if self.plainTextEdit_2.toPlainText() == '':
                valid.setText("Вы не ввели названия искомого города!")
                valid.exec()
            else:
                print('hrerererer')
                self.name_travel.setText(result[counter][1])
                self.plainTextEdit_2.setPlainText(result[counter][0])
                self.plainTextEdit.setPlainText(result[counter][2])
            # self.text_edit.setPlainText(result[0])
            con.commit()
            con.close()
            previous_username = username
            # self.defaut_text = self.text_edit.toPlainText()
        except Exception:
            pass

    def redacting(self):
        global username
        valid = QMessageBox()
        valid.setStyleSheet("QMessageBox {background-color: rgba(48, 57, 77, 200); font-size: 13pt;}"
                            "QLabel {font-family: 'Arial' 'Optima'; font-size: 13pt; color: white;} "
                            "QPushButton{background-color: rgba(191, 112, 151, 200); color: white;}")
        valid.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        print('here')

        name_place = self.plainTextEdit_2.toPlainText()
        print(name_place)
        name_travel = self.name_travel.text()
        note_message = self.plainTextEdit.toPlainText()
        print('here!!!')
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
            print('ошибкааааааааааа')


    def closeEvent(self, event):
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def open_form_before(self):
        self.second_form = User_inside()
        self.second_form.show()
        self.close()

    def del_file(self):
        global username
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
            print('ошибкааааааааааа')







# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Redact_file()
#     ex.show()
#     sys.exit(app.exec())
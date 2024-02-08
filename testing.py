import time
from PyQt5 import uic
import math
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *
# подключение используемых библиотек

# словарь для подсчета и вывода результатов тестирования
SLOVAR_RESULT_TEST = {'forms/sanatory': 0, 'forms/sea': 0, 'forms/museum': 0, 'forms/mountains': 0}

class Test1_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test1.ui', self)
        self.setWindowTitle('Вопрос 1/10')
        self.pushButton.clicked.connect(self.open_test2_form)
        self.pushButton_2.clicked.connect(self.open_main_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием главного меню
    def open_main_form(self):
        from main import Entering
        self.second_form = Entering()
        self.second_form.show()
        self.close()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test2_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 1
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            SLOVAR_RESULT_TEST['forms/mountains'] += 1
            self.second_form = Test2_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 1
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            SLOVAR_RESULT_TEST['forms/mountains'] += 2
            self.second_form = Test2_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 1
            SLOVAR_RESULT_TEST['forms/mountains'] += 1
            self.second_form = Test2_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 1
            SLOVAR_RESULT_TEST['forms/mountains'] += 2
            self.second_form = Test2_form()
            self.second_form.show()
            self.close()


class Test2_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test2.ui', self)
        self.setWindowTitle('Вопрос 2/10')
        self.pushButton.clicked.connect(self.open_test3_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test3_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 5
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            self.second_form = Test3_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/mountains'] += 5
            self.second_form = Test3_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 5
            SLOVAR_RESULT_TEST['forms/museum'] += 5
            self.second_form = Test3_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 5
            self.second_form = Test3_form()
            self.second_form.show()
            self.close()


class Test3_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test3.ui', self)
        self.setWindowTitle('Вопрос 3/10')
        self.pushButton.clicked.connect(self.open_test4_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test4_form(self):
        if self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 1
            self.second_form = Test4_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/museum'] += 1
            SLOVAR_RESULT_TEST['forms/mountains'] += 1
            self.second_form = Test4_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/mountains'] += 2
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            self.second_form = Test4_form()
            self.second_form.show()
            self.close()

class Test4_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test4.ui', self)
        self.setWindowTitle('Вопрос 4/10')
        self.pushButton.clicked.connect(self.open_test5_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test5_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            self.second_form = Test5_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/mountains'] += 2
            self.second_form = Test5_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            self.second_form = Test5_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            self.second_form = Test6_form()
            self.second_form.show()
            self.close()


class Test5_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test5.ui', self)
        self.setWindowTitle('Вопрос 5/10')
        self.pushButton.clicked.connect(self.open_test6_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test6_form(self):
        if self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/museum'] += 1
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            self.second_form = Test6_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 1
            SLOVAR_RESULT_TEST['forms/mountains'] += 2
            self.second_form = Test6_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 1
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            self.second_form = Test6_form()
            self.second_form.show()
            self.close()


class Test6_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test6.ui', self)
        self.setWindowTitle('Вопрос 6/10')
        self.pushButton.clicked.connect(self.open_test7_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test7_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/mountains'] += 3
            self.second_form = Test7_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/mountains'] += 3
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            self.second_form = Test7_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/mountains'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 3
            self.second_form = Test7_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            self.second_form = Test7_form()
            self.second_form.show()
            self.close()


class Test7_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test7.ui', self)
        self.setWindowTitle('Вопрос 7/10')
        self.pushButton.clicked.connect(self.open_test8_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test8_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            self.second_form = Test8_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/mountains'] += 1
            self.second_form = Test8_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 1
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            SLOVAR_RESULT_TEST['forms/sanatory'] += 1
            SLOVAR_RESULT_TEST['forms/mountains'] += 2
            self.second_form = Test8_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/museum'] += 3
            self.second_form = Test8_form()
            self.second_form.show()
            self.close()


class Test8_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test8.ui', self)
        self.setWindowTitle('Вопрос 8/10')
        self.pushButton.clicked.connect(self.open_test9_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test9_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/mountains'] += 7
            self.second_form = Test9_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/mountains'] += 4
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            self.second_form = Test9_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/mountains'] += 3
            SLOVAR_RESULT_TEST['forms/sea'] += 2
            self.second_form = Test9_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 6
            SLOVAR_RESULT_TEST['forms/sanatory'] += 3
            SLOVAR_RESULT_TEST['forms/museum'] += 7
            self.second_form = Test9_form()
            self.second_form.show()
            self.close()


class Test9_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test9.ui', self)
        self.setWindowTitle('Вопрос 9/10')
        self.pushButton.clicked.connect(self.open_test10_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_test10_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 7
            self.second_form = Test10_form()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/mountains'] += 5
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            self.second_form = Test10_form()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 5
            SLOVAR_RESULT_TEST['forms/museum'] += 3
            SLOVAR_RESULT_TEST['forms/sanatory'] += 7
            self.second_form = Test10_form()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 3
            SLOVAR_RESULT_TEST['forms/sanatory'] += 4
            SLOVAR_RESULT_TEST['forms/museum'] += 7
            self.second_form = Test10_form()
            self.second_form.show()
            self.close()


class Test10_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test10.ui', self)
        self.setWindowTitle('Вопрос 10/10')
        self.pushButton.clicked.connect(self.open_prog_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с открытием следующего вопроса теста
    # подсчет результатов ответа на данный вопрос
    def open_prog_form(self):
        if self.radioButton.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 2
            SLOVAR_RESULT_TEST['forms/museum'] += 3
            self.second_form = Interface()
            self.second_form.show()
            self.close()
        elif self.autmn_spirng.isChecked():
            SLOVAR_RESULT_TEST['forms/sanatory'] += 3
            SLOVAR_RESULT_TEST['forms/museum'] += 2
            self.second_form = Interface()
            self.second_form.show()
            self.close()
        elif self.winter.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 3
            self.second_form = Interface()
            self.second_form.show()
            self.close()
        elif self.summer.isChecked():
            SLOVAR_RESULT_TEST['forms/sea'] += 1
            SLOVAR_RESULT_TEST['forms/mountains'] += 3
            self.second_form = Interface()
            self.second_form.show()
            self.close()

class ProgressHandler(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)

    def run(self):
        for step in range(0, 101):
            self.mysignal.emit(['Загрузка', step])
            time.sleep(0.07)

# класс для прогресс бара
# показ формы обработки данных
# (прогресс бар) - небольшая анимация, счётчик результатов
class Interface(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/error.ui', self)

        self.pushButton.hide()
        self.pushButton.clicked.connect(self.next_form)

        self.handler = ProgressHandler()
        self.handler.mysignal.connect(self.signal_handler)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.progressBar.setValue(0)
        self.handler.start()

    def signal_handler(self, value):
        # реация при полной загрузке данных
        if value[1] == 100:
            self.pushButton.show()

        # надпись на прогресс баре при загрузке
        if value[0] == 'Загрузка':
            current_value = self.progressBar.value()
            self.progressBar.setValue(current_value + 1)

    # открытие класс для показа результатов
    def next_form(self):
        self.second_form = Museum_form()
        self.second_form.show()
        self.close()

# класс с показанием результата прохождения теста
class Museum_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/mainform2.ui', self)
        self.setWindowTitle('Культура')

        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel {\n"
                                 "font-family: \'Arial\' \'Optima\';\n"
                                 "font: bold;\n"
                                 "font-size: 13pt;\n"
                                 "color: rgba(255, 255, 255, 255);\n"
                                 "}")
        self.label.setObjectName("label")
        slovar_value = sorted(SLOVAR_RESULT_TEST.values())
        # проверка на максимальное количество баллов в словаре
        # и добавление соответствующего комментария к прохождению теста
        if SLOVAR_RESULT_TEST['forms/sea'] == max(slovar_value):
            self.setWindowTitle('Море, однозначно море')
            self.label.setText('<html><head/><body><p align="center"> Вы ратуете за комфорт и размеренный отдых, </p>'
                               '<p align="center"> не перегруженный как большим количеством новой информации,</p>'
                               '<p align="center"> так и активными перемещениями. В окружении леса или</p>'
                               '<p align="center"> на тихом морском побережье — там, где вы собираетесь </p>'
                               '<p align="center">провести отпуск, все должно настраивать на умиротворение</p>'
                               '<p align="center"> и способствовать накоплению новых жизненных сил.</p>'
                           '<p align="center">Подходящие города-курорты: Сочи, Анапа, Светлогорск, Судак, Ялта</p></body></html>')
        elif SLOVAR_RESULT_TEST['forms/mountains'] == max(slovar_value):
            self.setWindowTitle('Горы')
            self.label.setText('<html><head/><body><p align="center"> Считается, что лучший отдых - это смена деятельности, '
                               '<p align="center">и для вас это актуально вдвойне ведь </p>'
                           '<p align="center">&quot;деятельность&quot; и &quot;движение&quot; - это ваши ключевые слова,'
                           '<p align="center"> отсюда любовь к активным или даже экстремальным видам туризма. </p>'
                           '<p align="center">Походы, сплавы и восхождения - вы полны энергии, не боитесь непредвиденных</p>'
                           '<p align="center"> ситуаций и готовы отправиться хоть на край света за новыми ощущениями.</p>'
                           '<p align="center">Подходящие города-курорты: Белокуриха, Манжерок, Архыз, Домбай</p></body></html>')
        elif SLOVAR_RESULT_TEST['forms/sanatory'] == max(slovar_value):
            self.setWindowTitle('Санаторий')
            self.label.setText('<html><head/><body><p align="center"> Согласно результатам теста, в данный момент вы физически истощены. </p>'
                               '<p align="center">Вашему организму нужно восстановиться и прийти в норму. </p>'
                               '<p align="center">И большое количество сна не спасет данную ситуацию. </p>'
                               '<p align="center">Для лучшего эффекта необходимо добавить массаж, йогу, спа-процедуры, </p>'
                               '<p align="center">расслабляющие ванны, растяжку – все то, что поможет телу расслабиться.<p>'
                               '<p align="center">Подходящие города-курорты: Старая Русса, Пятигорск, Саки, Белокуриха</p></body></html>')

        elif SLOVAR_RESULT_TEST['forms/museum'] == max(slovar_value):
            self.setWindowTitle('Культура')
            self.label.setText('<html><head/><body><p align="center">Залог хорошего отдыха для вас — переместиться в незнакомую обстановку. <p>'
                               '<p align="center">Вы открыты и общительны и находите удовольствие в знакомстве </p>'
                               '<p align="center">с новой культурой, ее традициями. Музеи, памятники архитектуры, </p>'
                               '<p align="center">набережные и т. д. — даже не важно, сможете ли вы обойти все интересные</p>'
                               '<p align="center"> места незнакомого города, главное — идти навстречу новым впечатлениям!</p>'
                               '<p>Подходящие города-курорты: Томск, Владивосток, Тула</p></body></html>')

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(300, 200, 111, 28))
        self.pushButton.setCheckable(True)
        self.pushButton.setText('Посмотреть на карте')
        self.pushButton.setStyleSheet("QPushButton {\nbackground-color: rgba(127, 143, 24, 100);\nborder-radius: 5px;"
                                      "\npadding: 10px;\nfont-size: 12pt;\ncolor: rgba(255, 255, 255, 200);"
                                      "\nmargin-left: 100px;\nmargin-right: 100px;\n}"
                                      "\nQPushButton:hover {\nbackground-color: rgba(127, 143, 24, 200);\n}")
        self.pushButton.setObjectName("pushButton")

        # добавление карты России из шестиугольников
        from main import GraphicsView
        self.view = GraphicsView()

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label)
        vbox.addWidget(self.view)
        vbox.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.open_map_form)

    def closeEvent(self, event):
        # обработка окна при закрытии
        from main import Entering
        if not self.pushButton.isChecked():
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    # функция с обращением к глобальной карте,
    # но с изначальным выделением полученного в результате теста направления
    def open_map_form(self):
        global SLOVAR_RESULT_TEST
        from main import MyApp
        slovar_value = sorted(SLOVAR_RESULT_TEST.values())
        if SLOVAR_RESULT_TEST['forms/sea'] == max(slovar_value):
            self.second_form = MyApp(show_seas=True)
        elif SLOVAR_RESULT_TEST['forms/museum'] == max(slovar_value):
            self.second_form = MyApp(show_museums=True)
        elif SLOVAR_RESULT_TEST['forms/mountains'] == max(slovar_value):
            self.second_form = MyApp(show_mountains=True)
        elif SLOVAR_RESULT_TEST['forms/sanatory'] == max(slovar_value):
            self.second_form = MyApp(show_sanatories=True)
        SLOVAR_RESULT_TEST = {'forms/sanatory': 0, 'forms/sea': 0, 'forms/museum': 0, 'forms/mountains': 0}
        self.second_form.show()
        self.close()

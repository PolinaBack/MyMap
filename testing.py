import time
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys
import math
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
# from all_work2_222 import Entering

# словарь для подсчета и вывода результатов тестирования
SLOVAR_RESULT_TEST = {'forms/sanatory': 0, 'forms/sea': 0, 'forms/museum': 0, 'forms/mountains': 0}
SPISOK_COORDS = [120, 180, 180, 70, 297, 150, 30, 242, 110, 20, 265, 200, 40, 370, 130, 20, 393, 165,
                         14, 380, 190, 80, 48, 145, 70, 7, 229,
                         40, 80, 215, 11, 98, 184, 50, -35, 168, 30, -20, 118, 26, -58, 124, 30, 116, 112]

class QRegularPolygon(QGraphicsPolygonItem):
    def __init__(self, sides, radius, center, angle=None, parent=None):
        super(QRegularPolygon, self).__init__(parent)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)

        self._sides = sides
        self._radius = radius
        if angle != None:
            self._angle = angle
        else:
            self._angle = 0.0
        self._center = center

        points = list()
        for s in range(self._sides):
            angle = self._angle + (2 * math.pi * s / self._sides)
            x = center.x() + (radius * math.cos(angle))
            y = center.y() + (radius * math.sin(angle))
            points.append(QPointF(x, y))

        self.setPolygon(QPolygonF(points))

        self.tx, self.ty = 200, 200

    # def doRotate(self, alfa):
    #     tr = QTransform()
    #     tr.translate(self.tx, self.ty)
    #     tr.rotate(alfa)
    #     tr.translate(-self.tx, -self.ty)
    #     self.r, self.g, self.b = random.randint(0, 255), \
    #         random.randint(0, 255), \
    #         random.randint(0, 255)
    #     self.setBrush(QColor(self.r, self.g, self.b))
    #     self.setTransform(tr)


class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        def draw_hexagon(radius, xcenter, ycenter):
            ri = int(radius / 2.6 * math.sqrt(3))  # радиус вписанной окружности
            sides = 6  # сторон у hexagon
            angle = math.pi / 2
            center = QPointF(xcenter, ycenter)
            self.hexagon2 = QRegularPolygon(sides, ri, center, angle)
            self.hexagon2.setPen(QPen(QColor(115, 67, 67), 4, Qt.SolidLine))
            self.hexagon2.setBrush(QColor(153, 68, 68))
            self.scene.addItem(self.hexagon2)

        for i in range(0, 42, 3):
            draw_hexagon(SPISOK_COORDS[i], SPISOK_COORDS[i + 1], SPISOK_COORDS[i + 2])


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


class Test1_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test1.ui', self)
        self.setWindowTitle('Вопрос 1/10')
        self.pushButton.clicked.connect(self.open_test2_form)
        self.pushButton_2.clicked.connect(self.open_main_form)

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


# класс для поиска курорта по нажатию на кнопки пользователем
class Test2_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/test2.ui', self)
        self.setWindowTitle('Вопрос 2/10')
        self.pushButton.clicked.connect(self.open_test3_form)

    def closeEvent(self, event):
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def open_test6_form(self):
        print('here')
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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()


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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()


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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()


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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

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
        from all_work2_222 import Entering
        if self.sender() == None:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

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
        if value[1] == 100:
            self.pushButton.show()

        if value[0] == 'Загрузка':
            current_value = self.progressBar.value()
            self.progressBar.setValue(current_value + 1)

    def next_form(self):
        self.second_form = Museum_form()
        self.second_form.show()
        self.close()

# class Sea_form(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('forms/sea.ui', self)
#         self.setWindowTitle('Однозначно море')
#         self.pushButton.clicked.connect(self.open_main_form)
#
#     def open_main_form(self):
#         print('here!')
#         from all_work2_222 import Entering
#         self.second_form = Entering()
#         self.second_form.show()
#         self.close()

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
        if SLOVAR_RESULT_TEST['forms/sea'] == max(slovar_value):
            self.setWindowTitle('Море, однозначно море')
            self.label.setText('<html><head/><body><p align="center"> Вы ратуете за комфорт и размеренный отдых, не перегруженный как большим количеством </p>'
                               '<p align="center">новой информации, так и активными перемещениями. В окружении леса или</p>'
                               '<p align="center"> на тихом морском побережье — там, где вы собираетесь провести отпуск, все должно настраивать </p>'
                               '<p align="center">на умиротворение и способствовать накоплению новых жизненных сил.</p>'
                           '<p>Подходящие города-курорты: Сочи, Анапа, Светлогорск, Судак, Ялта</p></body></html>')
        elif SLOVAR_RESULT_TEST['forms/mountains'] == max(slovar_value):
            self.setWindowTitle('Горы')
            self.label.setText('<html><head/><body><p align="center"> Считается, что лучший отдых - '
                           'это смена деятельности, и для вас это актуально вдвойне</p>'
                           '<p align="center">ведь &quot;деятельность&quot; и &quot;движение&quot; - это ваши '
                           'ключевые слова, отсюда любовь к </p><p align="center">активным или '
                           'даже экстремальным видам туризма. Походы, сплавы и восхождения</p>'
                           '<p align="center">- вы полны энергии, не боитесь непредвиденных '
                           'ситуаций и готовы отправиться</p><p align="center">хоть на край'
                           'света за новыми ощущениями.</p>'
                           '<p>Подходящие города-курорты: Белокуриха, Манжерок, Сочи, Домбай, Архыз, Мончегорск</p></body></html>')
        elif SLOVAR_RESULT_TEST['forms/sanatory'] == max(slovar_value):
            self.setWindowTitle('Санаторий')
            self.label.setText('<html><head/><body><p align="center"> Согласно результатам теста, в данный момент вы физически истощены. '
                               '</p> <p align="center">Вашему организму нужно восстановиться и прийти в норму. '
                               'И большое количество сна </p>'
                               '<p align="center">не спасет данную ситуацию. Для лучшего эффекта необходимо добавить массаж, '
                               'йогу, </p> <p align="center">спа-процедуры, расслабляющие ванны, растяжку – все то, что поможет телу расслабиться.<p>'
                               '<p>Подходящие города-курорты: Старая Русса, Пятигорск, Саки, Белокуриха</p></body></html>')

        elif SLOVAR_RESULT_TEST['forms/museum'] == max(slovar_value):
            self.setWindowTitle('Культура')
            self.label.setText('<html><head/><body><p align="center"> Залог хорошего отдыха для вас — переместиться в незнакомую обстановку. <p>'
                               '<p align="center">Вы открыты и общительны и находите удовольствие в знакомстве </p>'
                               '<p align="center">с новой культурой, ее традициями. Музеи, памятники архитектуры, набережные </p>'
                               '<p align="center">и т. д. — даже не важно, сможете ли вы обойти все интересные места незнакомого города,</p>'
                               '<p align="center"> главное — идти навстречу новым впечатлениям!</p>'
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

        self.view = GraphicsView()
        # self.sld = QSlider(Qt.Horizontal, self)
        # self.sld.setRange(-180, 180)
        # self.sld.valueChanged.connect(self.changeValue)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label)
        vbox.addWidget(self.view)
        # vbox.addWidget(self.sld)
        vbox.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.open_map_form)

    def closeEvent(self, event):
        from all_work2_222 import Entering
        if not self.pushButton.isChecked():
            self.main_for = Entering()
            self.main_for.show()
        event.accept()


    # def changeValue(self):
    #     self.view.hexagon.doRotate(self.sld.value())

    def open_map_form(self):
        from all_work2_222 import MyApp
        slovar_value = sorted(SLOVAR_RESULT_TEST.values())
        if SLOVAR_RESULT_TEST['forms/sea'] == max(slovar_value):
            self.second_form = MyApp(show_seas=True)
        elif SLOVAR_RESULT_TEST['forms/museum'] == max(slovar_value):
            self.second_form = MyApp(show_museums=True)
        elif SLOVAR_RESULT_TEST['forms/mountains'] == max(slovar_value):
            self.second_form = MyApp(show_mountains=True)
        elif SLOVAR_RESULT_TEST['forms/sanatory'] == max(slovar_value):
            self.second_form = MyApp(show_sanatories=True)
        self.second_form.show()
        self.close()

# class Mountains_form(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('forms/mainform2.ui', self)
#         self.setWindowTitle('Горы и свежий воздух')
#
#         self.label = QtWidgets.QLabel()
#         self.label.setStyleSheet("QLabel {\n"
#                                  "font-family: \'Arial\' \'Optima\';\n"
#                                  "font: bold;\n"
#                                  "font-size: 13pt;\n"
#                                  "color: rgba(255, 255, 255, 255);\n"
#                                  "}")
#         self.label.setObjectName("label")
#         self.label.setText('<html><head/><body><p align="center"> Считается, что лучший отдых - '
#                            'это смена деятельности, и для вас это актуально вдвойне</p>'
#                            '<p align="center">ведь &quot;деятельность&quot; и &quot;движение&quot; - это ваши '
#                            'ключевые слова, отсюда любовь к </p><p align="center">активным или '
#                            'даже экстремальным видам туризма. Походы, сплавы и восхождения</p>'
#                            '<p align="center">- вы полны энергии, не боитесь непредвиденных '
#                            'ситуаций и готовы отправиться</p><p align="center">хоть на край'
#                            'света за новыми ощущениями.</p>'
#                            '<p>Подходящие города-курорты: Белокуриха, Манжерок, Сочи, Домбай, Архыз, Мончегорск</p></body></html>')
#
#         self.pushButton = QtWidgets.QPushButton()
#         self.pushButton.setGeometry(QtCore.QRect(300, 200, 111, 28))
#         self.pushButton.setCheckable(True)
#         self.pushButton.setText('На главное меню')
#         self.pushButton.setStyleSheet("QPushButton {\nbackground-color: rgba(127, 143, 24, 100);\nborder-radius: 5px;"
#                                       "\npadding: 10px;\nfont-size: 12pt;\ncolor: rgba(255, 255, 255, 200);"
#                                       "\nmargin-left: 100px;\nmargin-right: 100px;\n}"
#                                       "\nQPushButton:hover {\nbackground-color: rgba(127, 143, 24, 200);\n}")
#         self.pushButton.setObjectName("pushButton")
#
#         self.view = GraphicsView()
#         # self.sld = QSlider(Qt.Horizontal, self)
#         # self.sld.setRange(-180, 180)
#         # self.sld.valueChanged.connect(self.changeValue)
#
#         vbox = QVBoxLayout(self)
#         vbox.addWidget(self.label)
#         vbox.addWidget(self.view)
#         # vbox.addWidget(self.sld)
#         vbox.addWidget(self.pushButton)
#
#         self.pushButton.clicked.connect(self.open_main_form)
#
#     # def changeValue(self):
#     #     self.view.hexagon.doRotate(self.sld.value())
#
#     def open_main_form(self):
#         from all_work2_222 import Entering
#         self.second_form = Entering()
#         self.second_form.show()
#         self.close()
# # class Sanatory_form(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('forms/sanatory.ui', self)
#         self.setWindowTitle('Санаторий')
#         self.pushButton.clicked.connect(self.open_main_form)
#
#     def open_main_form(self):
#         from all_work2_222 import Entering
#         self.second_form = Entering()
#         self.second_form.show()
#         self.close()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Mountains_form()
#     ex.show()
#     sys.exit(app.exec())
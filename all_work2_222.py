import sqlite3
import io
import folium
import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from folium.plugins import MarkerCluster
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from testing import Test1_form
from authorisation import Another_autharisation
from PyQt5.Qt import *
import math
from folium.plugins import Geocoder
import base64
from folium import IFrame

# https://yandex.ru/video/preview/863603398243140909
# https://yandex.ru/video/preview/16079287292389509257
# https://sutochno.ru/info/lechebnye-kurorty-rossii

SPISOK_COORDS = [120, 180, 180, 70, 297, 150, 30, 242, 110, 20, 265, 200, 40, 370, 130, 20, 393, 165,
                         14, 380, 190, 80, 48, 145, 70, 7, 229,
                         40, 80, 215, 11, 98, 184, 50, -35, 168, 30, -20, 118, 26, -58, 124, 30, 116, 112]
# класс, созданный для входа как пользователь или как администратор

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
        self.resize(500, 500)
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
            draw_hexagon(SPISOK_COORDS[i], SPISOK_COORDS[i+1], SPISOK_COORDS[i+2])

        # draw_hexagon(120, 180, 180)
        # draw_hexagon(70, 330, 150)
        # draw_hexagon(30, 266, 93)
        # draw_hexagon(20, 290, 210)
        # draw_hexagon(40, 420, 120)
        # draw_hexagon(20, 450, 163)
        # draw_hexagon(14, 442, 194)
        # draw_hexagon(80, 22, 118)
        # draw_hexagon(68, -30, 223)
        # draw_hexagon(26, -60, 292)
        # draw_hexagon(20, -102, 272)
        # draw_hexagon(8, -76, 266)
        # draw_hexagon(40, 56, 215)
        # draw_hexagon(11, 76, 172)
        # draw_hexagon(50, -83, 143)
        # draw_hexagon(30, -66, 78)
        # draw_hexagon(26, -112, 88)
        # draw_hexagon(30, 110, 86)
        # draw_hexagon(20, 402, 168)
        # # draw_hexagon(9, 93, 114)

class Entering(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/mainform2.ui', self)

        self.view = GraphicsView()

        self.label = QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel {\n"
                                 "font-family: \'Arial\' \'Optima\';\n"
                                 "font: bold;\n"
                                 "font-size: 18pt;\n"
                                 "color: rgba(255, 255, 255, 255);\n"
                                 "}")
        self.label.setObjectName("label")
        self.label.setText('<html><head/><body><p align="center"><span '
                           'style=" font-size:18pt;">Добро пожаловать на </span><span '
                           'style=" font-size:18pt; text-decoration: underline;">главное меню</span><span '
                           'style=" font-size:18pt;">!</span></p></body></html>')

        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(300, 200, 111, 28))
        self.pushButton.setCheckable(True)
        self.pushButton.setText('Тест')
        self.pushButton.setStyleSheet("QPushButton {\n"
                                  "background-color: rgba(0,0, 0, 0);\n"
                                  "border: 2px solid rgba(127, 57, 91, 255);\n"
                                  "border-style: inset;\n"
                                  "border-radius: 5px;\n"
                                  "padding: 12px;\n"
                                  "font-size: 15pt;\n"
                                  "color: rgba(255, 255, 255, 230);\n"
                                  "margin-left: 50px;\n"
                                  "margin-right: 50px; margin-top:10px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "background-color: qconicalgradient(cx:0.431909, cy:1, angle:270.1, stop:0 rgba(0, 0, 0, 255), stop:0.39548 rgba(191, 112, 151, 100));\n"
                                  "}")
        self.pushButton.setObjectName("pushButton_2")

        self.label_test = QtWidgets.QLabel()
        self.label_test.setStyleSheet("QLabel {\n"
                                 "font-family: \'Arial\' \'Optima\';\n"
                                 "font: bold;\n"
                                 "font-size: 13pt;\n"
                                 "color: rgba(255, 255, 255, 255);\n"
                                 "}")
        self.label_test.setObjectName("label")
        self.label_test.setText('Узнайте, какой отдых вам необходим, и определите направление для вашего отпуска.')

        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setGeometry(QtCore.QRect(300, 200, 111, 28))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setText('Вход')
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "background-color: rgba(0,0, 0, 0);\n"
                                        "border: 2px solid rgba(127, 57, 91, 255);\n"
                                        "border-style: inset;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 12px;\n"
                                        "font-size: 15pt;\n"
                                        "color: rgba(255, 255, 255, 230);\n"
                                        "margin-left: 50px;\n"
                                        "margin-right: 50px; margin-top:10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qconicalgradient(cx:0.431909, cy:1, angle:270.1, stop:0 rgba(0, 0, 0, 255), stop:0.39548 rgba(191, 112, 151, 100));\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_enter = QtWidgets.QLabel()
        self.label_enter.setStyleSheet("QLabel {\n"
                                      "font-family: \'Arial\' \'Optima\';\n"
                                      "font: bold;\n"
                                      "font-size: 13pt;\n"
                                      "color: rgba(255, 255, 255, 255);\n"
                                      "}")
        self.label_enter.setObjectName("label")
        self.label_enter.setText('Авторизуйтесь или зарегистрируйтесь в приложении.')

        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setGeometry(QtCore.QRect(300, 200, 111, 28))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setText('Карта')
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "background-color: rgba(0,0, 0, 0);\n"
                                        "border: 2px solid rgba(127, 57, 91, 255);\n"
                                        "border-style: inset;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 12px;\n"
                                        "font-size: 15pt;\n"
                                        "color: rgba(255, 255, 255, 230);\n"
                                        "margin-left: 50px;\n"
                                        "margin-right: 50px; margin-top:10px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: qconicalgradient(cx:0.431909, cy:1, angle:270.1, stop:0 rgba(0, 0, 0, 255), stop:0.39548 rgba(191, 112, 151, 100));\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_map = QtWidgets.QLabel()
        self.label_map.setStyleSheet("QLabel {\n"
                                      "font-family: \'Arial\' \'Optima\';\n"
                                      "font: bold;\n"
                                      "font-size: 13pt;\n"
                                      "color: rgba(255, 255, 255, 255);\n"
                                      "}")
        self.label_map.setObjectName("label")
        self.label_map.setText('Откройте карту для выбора подходящего курорта.')

        self.pushButton.clicked.connect(self.testing)
        self.pushButton_3.clicked.connect(self.parol)
        self.pushButton_2.clicked.connect(self.maining)

        # self.sld = QSlider(Qt.Horizontal, self)
        # self.sld.setRange(-180, 180)
        # self.sld.valueChanged.connect(self.changeValue)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label)
        vbox.addWidget(self.pushButton_3)
        vbox.addWidget(self.label_enter)
        vbox.addWidget(self.pushButton)
        vbox.addWidget(self.label_test)
        vbox.addWidget(self.pushButton_2)
        vbox.addWidget(self.label_map)
        vbox.addWidget(self.view)
        # vbox.addWidget(self.sld)

    def testing(self):
        print('here')
        self.main_forms = Test1_form()
        self.main_forms.show()
        self.close()

    def parol(self):
        self.parols = Another_autharisation()
        self.close()
        self.parols.show()

    def maining(self):
        self.main_for = MyApp()
        self.close()
        self.main_for.show()

    # def changeValue(self):
    #     self.view.hexagon.doRotate(self.sld.value())

# class Entering(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('forms/enter.ui', self)
#         self.pushButton.clicked.connect(self.testing)
#         self.pushButton_3.clicked.connect(self.parol)
#         self.pushButton_2.clicked.connect(self.maining)
#
#     def testing(self):
#         print('here')
#         self.main_forms = Test1_form()
#         self.main_forms.show()
#         self.close()
#
#     def parol(self):
#         self.parols = Admin_form()
#         self.close()
#         self.parols.show()
#
#     def maining(self):
#         self.main_for = MyApp()
#         self.close()
#         self.main_for.show()


# класс проверка пароля, открытие других окон, если хотят зайти как админ
class Admin_form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/strongparol.ui', self)
        self.pushButton.clicked.connect(self.result)
        self.pushButton_2.clicked.connect(self.result)
        self.pushButton_3.clicked.connect(self.result)
        self.pushButton_4.clicked.connect(self.result)
        self.lineEdit.setEchoMode(QLineEdit.Password)

    def result(self):
        try:
            send = self.sender().text()
            stroka = self.lineEdit.text()
            print()
            if send == "Назад":
                self.addi = Entering()
                self.addi.show()
                self.close()
            assert stroka == 'redactingDB'
            if send == "Добавить элемент":
                self.addi = Adding()
                self.addi.show()
            elif send == "Удалить элемент":
                self.addi = Deleting()
                self.addi.show()
            elif send == "Изменить элемент":
                self.addi = Changing()
                self.addi.show()
            elif send == "Назад":
                self.addi = Entering()
                self.addi.show()
        except AssertionError:
            self.label.setText('❌❌❌❌ Неверный пароль, попробуйте снова ❌❌❌❌')


# класс, работающий для добавления новых элементов (горнолыжных курортов) в бд
class Adding(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/add_element.ui', self)
        self.numbbtn.clicked.connect(self.knowledge)
        self.addbtn.clicked.connect(self.add_process)
        self.con = sqlite3.connect("data_base/base.db")
        self.cur = self.con.cursor()
        self.num_el = self.cur.execute("""SELECT MAX(id) FROM ski""").fetchone()[0]
        self.elements_number.setText(f"Последний элемент в списке (id): {str(self.num_el)}")

    def knowledge(self):
        try:
            subj = self.line_numb.text()
            if not subj[0].isupper():
                subj = subj.capitalize()
            count = self.cur.execute("SELECT count(*) FROM subjects WHERE subject=?", (subj,)).fetchone()[0]
            assert count == 1
            idi = self.cur.execute("SELECT id FROM subjects WHERE subject=?", (subj,)).fetchall()
            self.nomer.setText(f"{str(idi[0])[1:-2]}")
        except AssertionError:
            self.nomer.setText('Ошибка. Попробуйте заново ввести название субъекта.')

    def add_process(self):
        try:
            elements_to_add = self.line_ad.text().split('; ')
            assert len(elements_to_add) == 7
            assert elements_to_add[0].isdigit()
            assert elements_to_add[1].isdigit()
            assert elements_to_add[3].isdigit()
            assert elements_to_add[4].isdigit()
            assert elements_to_add[5].isdigit()
            assert int(elements_to_add[0]) > int(self.num_el)
            assert int(elements_to_add[1]) <= 56
            coords = elements_to_add[6].split(', ')
            assert len(coords) == 2
            assert -90 <= int(float(coords[0])) <= 90 and -180 <= float(coords[1]) <= 180
            que = "INSERT INTO ski(id, subject, ski_resort, total_length, number_trass, height_diff, coords) VALUES("
            que += ", ".join([f"'{element}'" for element in elements_to_add])
            que += ')'
            self.cur.execute(que)
            self.con.commit()
            self.resbtn.setText('Запрос успешно выполнен')
            self.num_el = self.cur.execute("""SELECT MAX(id) FROM ski""").fetchone()[0]
            self.elements_number.setText(f"Последний элемент в списке (id): {str(self.num_el)}")
        except AssertionError:
            self.resbtn.setText('Что-то пошло не так')
        except ValueError:
            self.resbtn.setText('Что-то пошло не так')


# класс, работающий для удаления элементов (горнолыжных курортов) в бд
class Deleting(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/deleting_element.ui', self)
        self.name_del.clicked.connect(self.deleting_name)
        self.coord_del.clicked.connect(self.deleting_coord)
        self.con = sqlite3.connect("data_base/base.db")
        self.cur = self.con.cursor()

    def deleting_name(self):
        try:
            nam = self.name_line.text()
            exist_name = self.cur.execute("SELECT EXISTS(SELECT ski_resort FROM ski WHERE ski_resort = ?)",
                                          (nam,)).fetchone()[0]
            assert exist_name == 1
            self.cur.execute("DELETE from ski WHERE ski_resort = ?", (nam,))
            self.con.commit()
            self.resbtn.setText('Запрос успешно выполнен')
        except AssertionError:
            self.resbtn.setText('Что-то пошло не так')

    def deleting_coord(self):
        try:
            coo = self.coords_line.text()
            exist_cord = self.cur.execute("SELECT EXISTS(SELECT coords FROM ski WHERE coords = ?)",
                                          (coo,)).fetchone()[0]
            assert exist_cord == 1
            self.cur.execute("DELETE from ski WHERE coords = ?", (coo,))
            self.con.commit()
            self.resbtn2.setText('Запрос успешно выполнен')
        except AssertionError:
            self.resbtn2.setText('Что-то пошло не так')


# класс, работающий для изменения элементов (горнолыжных курортов) в бд
class Changing(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/changing_element2.ui', self)
        self.btnchange.clicked.connect(self.chane_smth)
        self.con = sqlite3.connect("data_base/base.db")
        self.cur = self.con.cursor()
        self.dict_changes = {'id': '', 'subject': '', 'ski_resort': '', 'total_length': '', 'number_trass': '',
                             'height_diff': '', 'coords': ''}
        self.list_changes = ['id', 'subject', 'ski_resort', 'total_length', 'number_trass', 'height_diff', 'coords']
        self.search_id.clicked.connect(self.search)

    def chane_smth(self):
        try:
            count = 0
            difference = self.change_line.text().split('; ')
            assert len(difference) == 7
            assert difference[0] != '*'
            print(f"Claer {self.dict_changes}")
            for i in self.list_changes:
                if difference[count] != '*':
                    self.dict_changes[i] = difference[count]
                    if count in [0, 1, 3, 4, 5]:
                        assert difference[count].isdigit()
                else:
                    del self.dict_changes[i]
                count += 1
            if 'coords' in self.dict_changes:
                print('here')
                coords = self.dict_changes['coords'].split(', ')
                assert len(coords) == 2
                assert -90 <= float(coords[0]) <= 90 and -180 <= float(coords[1]) <= 180
            idi = self.dict_changes['id']
            del self.dict_changes['id']
            assert self.dict_changes != {}
            exist_id = self.cur.execute("SELECT EXISTS(SELECT ski_resort FROM ski WHERE id = ?)",
                                          (idi,)).fetchone()[0]
            assert exist_id == 1
            que = "UPDATE ski SET "
            que += ", ".join([f"{key}='{self.dict_changes.get(key)}'"
                              for key in self.dict_changes.keys()])
            que += " WHERE id = ?"
            self.cur.execute(que, (idi, ))
            self.con.commit()
            self.resbtn.setText('Запрос успешно выполнен')
            self.dict_changes = {'id': '', 'subject': '', 'ski_resort': '', 'total_length': '', 'number_trass': '',
                                 'height_diff': '', 'coords': ''}
        except AssertionError:
            self.resbtn.setText('Что-то пошло не так')
            self.dict_changes = {'id': '', 'subject': '', 'ski_resort': '', 'total_length': '', 'number_trass': '',
                                 'height_diff': '', 'coords': ''}
        except ValueError:
            self.resbtn.setText('Что-то пошло не так')
            self.dict_changes = {'id': '', 'subject': '', 'ski_resort': '', 'total_length': '', 'number_trass': '',
                                 'height_diff': '', 'coords': ''}

    def search(self):
        try:
            nam = self.name_line.text()
            coo = self.coords_line.text()
            assert nam != '' or coo != ''
            if nam == '':
                exist_cord = self.cur.execute("SELECT EXISTS(SELECT coords FROM ski WHERE coords = ?)",
                                              (coo,)).fetchone()[0]
                assert exist_cord == 1
                idi_prtn = self.cur.execute("SELECT id FROM ski WHERE coords = ?", (coo, )).fetchone()[0]
                self.con.commit()
                self.num_id.setText(f"id элемента: {idi_prtn}")
            elif coo == '':
                exist_name = self.cur.execute("SELECT EXISTS(SELECT ski_resort FROM ski WHERE ski_resort = ?)",
                                              (nam,)).fetchone()[0]
                assert exist_name == 1
                idi_prtn = self.cur.execute("SELECT id FROM ski WHERE ski_resort = ?", (nam,)).fetchone()[0]
                self.con.commit()
                self.num_id.setText(f"id элемента: {idi_prtn}")
        except AssertionError:
            self.num_id.setText('Что-то пошло не так')


# класс для поиска курорта по вводу пользователя
# class Searching(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('forms/search.ui', self)
#         self.pushButton.clicked.connect(self.finding)
#
#     def finding(self):
#         a = self.lineEdit.text()
#         print('i')
#         try:
#             assert 'лыж' in a.lower() or 'сноуборд' in a.lower()
#             self.second_form3 = MyApp()
#             self.second_form3.show()
#         except AssertionError:
#             for i in a:
#                 print('here')
#                 if i in 'qwertyuiopasdfghjklzxcvbnm':
#                     self.label_2.setText('Поменяйте раскладку клавиатуры.')
#                 else:
#                     self.label_2.setText('По Вашему запросу ничего не найдено')


# класс ошибки, на недоработанные формы (планируются развиваться в дальнейшем будущем проекта)
# class Development(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('forms/error.ui', self)


# класс по работе с картой (основная задумка)
class MyApp(QWidget):
    def __init__(self, show_museums=False, show_sanatories=False, show_seas=False, show_mountains=False, username=None):
        super().__init__()
        self.setWindowTitle('Карта')
        self.name_label = QLabel(self)
        self.name_label.setText("")
        self.name_label.move(10, 10)
        self.window_width, self.window_height = 770, 545
        self.setMinimumSize(self.window_width, self.window_height)
        self.flag = False
        try:
            # Создание базы карты
            self.m = folium.Map(location=[64.31828134466166, 93.04953260959422], zoom_start=3)
            # Добавление фильтров и разных видов карт
            Geocoder().add_to(self.m)
            # Создание отдельного фильтра для показателя на карте
            self.fg = folium.FeatureGroup(name='Курорты в горах', show=show_mountains)
            self.sanat = folium.FeatureGroup(name='Популярные лечебно-оздоровительные санатории', show=show_sanatories)
            self.museum = folium.FeatureGroup(name='Исторические города России', show=show_museums)
            self.seas = folium.FeatureGroup(name='Главные морские курорты', show=show_seas)
            self.m.add_child(self.fg)
            self.m.add_child(self.sanat)
            self.m.add_child(self.museum)
            self.m.add_child(self.seas)
            print('here')
            self.basdan()
            print('here')
            self.all_resorts()
            self.sanatories()
            self.museums()
            self.seas_resort()

            if username != None:
                self.usernamers = folium.FeatureGroup(name='Мои поездки', show=True)
                self.m.add_child(self.usernamers)
                self.func_for_username(username)

            folium.LayerControl().add_to(self.m)

            # ПЕРЕВОД В QT
            layout = QVBoxLayout()
            self.setLayout(layout)
            data = io.BytesIO()
            self.m.save(data, close_file=False)
            webView = QWebEngineView()
            webView.setHtml(data.getvalue().decode())
            layout.addWidget(webView)
        except ImportError:
            self.name_label.setText("Установите все модули и библиотеки. (Install requirements)")

    def closeEvent(self, event):
        if self.flag:
            from authorisation import User_inside
            self.main_for = User_inside()
            self.main_for.show()
        else:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def basdan(self):
        # что делать с базой данных нз, надо будет придумать.........
        # ВСЁ ПОЛУЧИЛОСЬ
        self.con = sqlite3.connect("data_base/base_3.db")
        self.cur = self.con.cursor()
        self.information = self.cur.execute("""SELECT ski_resort, height_diff, number_trass, total_length, coords, url_images
                                            FROM ski""").fetchall()
        self.sanatories_info = self.cur.execute("""SELECT sanatory_resorts, information, coords, url_images
                                                    FROM sanatory""").fetchall()

        self.museus_info = self.cur.execute("""SELECT museum_resort, museum_information, coords, url_images
                                                            FROM museums""").fetchall()

        self.seas_info = self.cur.execute("""SELECT sea_resorts, information, coords, url_images
                                                            FROM seas""").fetchall()
        self.con.commit()



    def all_resorts(self):
        marker_claster = MarkerCluster().add_to(self.fg)
        for i in self.information:
            htm = f""" <img src="{i[5]}" alt="нет фото" height="200" width="260">
            <h4>{i[0]}</h4>
            <p>Общая длина: {i[3]} км </br>
            Количество трасс: {i[2]} </br>
            Перепад высот: {i[1]} м</p>"""

            iframe = folium.IFrame(html=htm, width=300, height=200)
            popup = folium.Popup(iframe, max_width=2650)

            marker = folium.Marker(
                location=[float(i[4].split(',')[0]), float(i[4].split(',')[1])],
                popup=popup,
                icon=folium.DivIcon(html=f"""<div><svg><polygon points="20, 20, 30, 0, 10, 0" fill="#955f20"></svg>
                                    </div>"""))
            marker.add_to(marker_claster)

    def sanatories(self):
        marker_claster = MarkerCluster().add_to(self.sanat)

        for i in self.sanatories_info:
            htm = f""" <img src="{i[3]}" alt="нет фото" height="200" width="260">
            <h4>{i[0]}</h4>
            <p>{i[1]}</p> """
            iframe = folium.IFrame(html=htm, width=300, height=200)
            popup = folium.Popup(iframe, max_width=2650)

            marker = folium.Marker(
                location=[float(i[2].split(',')[0]), float(i[2].split(',')[1])],
                popup=popup,
                icon=folium.DivIcon(html=f"""<div><svg><polygon points="20, 20, 30, 0, 10, 0" fill="#00e600"></svg>
                                                    </div>"""))
            marker.add_to(marker_claster)

    def museums(self):
        marker_claster = MarkerCluster().add_to(self.museum)
        for j in self.museus_info:
            htm = f""" <img src="{j[3]}" alt="нет фото" height="200" width="260">
                    <h4>{j[0]}</h4>
                    <p>{j[1]}</p> """
            iframe = folium.IFrame(html=htm, width=300, height=200)
            popup = folium.Popup(iframe, max_width=2650)

            marker = folium.Marker(
                location=[float(j[2].split(',')[0]), float(j[2].split(',')[1])],
                popup=popup,
                icon=folium.DivIcon(html=f"""<div><svg><polygon points="20, 20, 30, 0, 10, 0" fill="#6c6960"></svg>
                                                            </div>"""))
            marker.add_to(marker_claster)


    def seas_resort(self):
        marker_claster = MarkerCluster().add_to(self.seas)

        for i in self.seas_info:
            htm = f""" <img src="{i[3]}" alt="нет фото" height="200" width="260">
                    <h4>{i[0]}</h4>
                    <p>{i[1]}</p> """
            iframe = folium.IFrame(html=htm, width=300, height=200)
            popup = folium.Popup(iframe, max_width=2650)

            marker = folium.Marker(
                location=[float(i[2].split(',')[0]), float(i[2].split(',')[1])],
                popup=popup,
                icon=folium.DivIcon(html=f"""<div><svg><polygon points="20, 20, 30, 0, 10, 0" fill="#00e600"></svg>
                                                            </div>"""))
            marker.add_to(marker_claster)

    def func_for_username(self, username):
        self.flag = True
        marker_claster = MarkerCluster().add_to(self.usernamers)

        con = sqlite3.connect('data_base/users_data.db')
        cur = con.cursor()
        result = cur.execute(f'SELECT * FROM Files WHERE username = "{username}"').fetchall()
        print(result)
        con.commit()
        for i in result:
            htm = f"""<h4>{i[2]}</h4>
                    <p>{i[5]}</p> """
            iframe = folium.IFrame(html=htm, width=200, height=150)
            popup = folium.Popup(iframe, max_width=2650)

            marker = folium.Marker(
                location=[float(i[3].split(',')[0]), float(i[3].split(',')[1])],
                popup=popup,
                tooltip=str(i[4]),
                icon=folium.DivIcon(html=f"""<div><svg><polygon points="20, 20, 30, 0, 10, 0" fill="#ff0000"></svg>
                                                            </div>"""))
            marker.add_to(marker_claster)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Entering()
    ex.show()
    sys.exit(app.exec())

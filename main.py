import sqlite3
import io
import folium
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from folium.plugins import MarkerCluster
from PyQt5 import uic, QtCore, QtWidgets
from testing import Test1_form
from authorisation import Another_autharisation
from PyQt5.Qt import *
import math
from folium.plugins import Geocoder
# подключение используемых библиотек

# глобальная переменная для координат по отрисовки небольшой интерактивной шестиугольной карты России
SPISOK_COORDS = [120, 180, 180, 70, 297, 150, 30, 242, 110, 20, 265, 200, 40, 370, 130, 20, 393, 165,
                         14, 380, 190, 80, 48, 145, 70, 7, 229,
                         40, 80, 215, 11, 98, 184, 50, -35, 168, 30, -20, 118, 26, -58, 124, 30, 116, 112]

# класс для отрисовки шестиугольников
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

# создание интерактивного поля внутри формы, задание параметров шестиугольников
class GraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        # self.resize(500, 500)
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

# класс для отображения формы с главным меню
class Entering(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/mainform2.ui', self)
        self.setWindowTitle('Главное меню')

        # добавление поля для картинки шестиугольной России
        self.view = GraphicsView()

        # надпись "Добро пожаловать.."
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

        # параметры связанные с кнопкой "тест" и её подписью
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
        self.label_test.setText('Узнайте, какой отдых вам необходим и какое направление лучше выбрать.')

        # параметры связанные с кнопкой "войти" и её подписью
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

        # параметры связанные с кнопкой "карта" и её подписью
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

        # подключение функций после нажатия на кнопку
        self.pushButton.clicked.connect(self.testing)
        self.pushButton_3.clicked.connect(self.parol)
        self.pushButton_2.clicked.connect(self.maining)

        # добавление в форму всех кнопок
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.label)
        vbox.addWidget(self.pushButton_3)
        vbox.addWidget(self.label_enter)
        vbox.addWidget(self.pushButton)
        vbox.addWidget(self.label_test)
        vbox.addWidget(self.pushButton_2)
        vbox.addWidget(self.label_map)
        vbox.addWidget(self.view)

    def testing(self):
        # переход к классу тестирования в файле testing.py
        self.main_forms = Test1_form()
        self.main_forms.show()
        self.close()

    def parol(self):
        # переход к классу авторизации в файле authorisation.py
        self.parols = Another_autharisation()
        self.close()
        self.parols.show()

    def maining(self):
        # переход к классу с открытием карты
        self.main_for = MyApp()
        self.close()
        self.main_for.show()


# класс по работе с картой (одна из основных функций)
class MyApp(QWidget):
    def __init__(self, show_museums=False, show_sanatories=False, show_seas=False, show_mountains=False, username=None):
        super().__init__()
        self.setWindowTitle('Карта')
        self.name_label = QLabel(self)
        self.name_label.setText("")
        self.name_label.move(10, 10)
        self.window_width, self.window_height = 760, 545
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
        # обработка окна при закрытии
        if self.flag:
            from authorisation import User_inside
            self.main_for = User_inside()
            self.main_for.show()
        else:
            self.main_for = Entering()
            self.main_for.show()
        event.accept()

    def basdan(self):
        # сборка информации из дб
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
        # маркеры с горными курортами
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
        # маркеры с санаториями
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
        # маркеры с музеями
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
        # маркеры с морями
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
        # маркеры с пользовательскими заметками, если авторизован)
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

import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect,QPropertyAnimation,QThread,pyqtSignal,Qt,QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
import paho.mqtt.client as paho
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import matplotlib
import time
import datetime as dt
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
from ui_form import Ui_MainWindow
broker = "localhost"
value=0
class thread(QThread):
    progress = pyqtSignal(int)
    def run(self):
        global value
        def on_message(client, userdata, message):
            time.sleep(1)
            ##print("received message =", str(message.payload.decode("utf-8")))
            self.value=str(message.payload.decode("utf-8"))
            self.progress.emit(int(message.payload.decode("utf-8")))
        print("connecting to broker ", broker)
        print("subscribing ")
        client1 = paho.Client("TEMP")
        client1.connect(broker,port=1883)  # connect
        client1.on_message = on_message
        while True:
            client1.loop_start()
            client1.subscribe("heater/globaltemp")
            time.sleep(1)
            """client.disconnect() #disconnect"""
            client1.loop_stop()  # stop loop
class mail(QThread):
    def run(self):
        self.asd=MyApp()
        mails = []
        for index in range(self.asd.ui.listWidget.count()):
            mails.append(self.asd.ui.listWidget.item(index).text())
        print(self.asd.ui.listWidget.item(0).text())
        for i in mails:
            mesaj = MIMEMultipart()
            mesaj["From"] = "selcuksmtp1@gmail.com"
            mesaj["To"] = i
            mesaj["Subject"] = "IOT Reporter"
            yazi = self.asd.report()
            mesaj_govdesi = MIMEText(yazi, "plain")
            mesaj.attach(mesaj_govdesi)
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("selcuksmtp1@gmail.com",
                       "29Qazxsw29.")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("Mail başarıyla gönderildi....")
            mail.close()
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=8, height=15, dpi=20):
        fig = Figure(figsize=(11, 5), dpi=dpi, facecolor="#374A54")
        FigureCanvasQTAgg.__init__(self, fig)
        FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)
        self.axes = fig.add_subplot(111)
        self.axes.set_facecolor("silver")
        self.axes.patch.set_facecolor("silver")
        self.axes.set_position([0.04, 0.13,0.95,0.81])
        super(MplCanvas, self).__init__(fig)
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.sqlitecon()
        self.window_width ,self.window_height=1200,800
        self.setMinimumSize(self.window_width,self.window_height)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.xs = []
        self.ys = []
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.ui.verticalLayout_3.addWidget(self.toolbar)
        self.ui.verticalLayout_3.addWidget(self.canvas)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.animation)
        self.ui.frame_7.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.ui.pushButton.hide()

        self.timer=QTimer()
        self.thread = thread()
        self.thread.progress.connect(self.update_plot)
        self.thread.start()

        self.ui.pushButton_4.clicked.connect(self.exportdata)
        self.ui.pushButton_3.clicked.connect(lambda :self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.pushButton_5.clicked.connect(lambda :self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pushButton_6.clicked.connect(self.add)
        self.ui.pushButton_7.clicked.connect(self.remove)
        self.show()
    def report(self):
        liste=list()
        time=list()
        self.cursor.execute("Select * from temperature1 where hour=? ",(dt.datetime.now().strftime('%H'),))
        data=self.cursor.fetchall()
        for i in (data):
            liste.append(i[0])
            time.append(i[1])
        return ("Average Temp Last one hour:"+str(round(sum(liste)/len(liste),3))+" C"+"\n"+
              "Minumum temperature last hour:"+str(min(liste))+" C"+ " Time : "+time[liste.index(min(liste))]+"\n"+
              "Maximum temperature last hour:"+str(max(liste))+" C"+ " Time :"+time[liste.index(max(liste))])
    def sendmailreport(self,i):
            print(i)
            mesaj = MIMEMultipart()
            mesaj["From"] = "selcuksmtp1@gmail.com"
            mesaj["To"] = i
            mesaj["Subject"] = "IOT Reporter"
            yazi = self.report()
            mesaj_govdesi = MIMEText(yazi, "plain")
            mesaj.attach(mesaj_govdesi)
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("selcuksmtp1@gmail.com",
                       "29Qazxsw29.")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("Mail başarıyla gönderildi....")
            mail.close()
    def sqlitecon(self):
        self.con=sqlite3.connect("record.db")
        self.cursor=self.con.cursor()
        sorgu="Create Table If not exists temperature1(temp INT,date TEXT,hour INT,minute TEXT)"
        self.cursor.execute(sorgu)
    def add(self):
        if self.ui.radioButton.isChecked()==True:
            mail=self.ui.textEdit.toPlainText()
            self.ui.listWidget.addItem(mail+"   Set Time:30 min")
            self.timer30min=QTimer(self)
            self.timer30min.timeout.connect(lambda :self.sendmailreport(str(mail)))
            self.timer30min.start(120000)
        if self.ui.radioButton_2.isChecked()==True:
            self.timer60min=QTimer(self)
            mail = self.ui.textEdit.toPlainText()
            self.ui.listWidget.addItem(mail+"   Set Time:60 min")
            self.timer60min.timeout.connect(lambda :self.sendmailreport(str(mail)))
            self.timer60min.start(60000)
            print("1Dk")
        self.ui.textEdit.clear()
    def remove(self):
        textlist=self.ui.listWidget.selectedItems()[0].text()
        time=(textlist.split(" ")[4])
        time=time[5:9]
        if int(time)==30:
            print("Stopped!30 min")
            self.timer30min.stop()
        if int(time) == 60:
            print("Stopped! 60 min")
            self.timer60min.stop()
        index = (self.ui.listWidget.currentRow())
        self.ui.listWidget.takeItem(index)
    def blink(self):
        self.ui.frame_8.setStyleSheet("QFrame{border:8px solid rgb(48,50,62);color:#FFF;padding-left:20px;padding-right:20px;background-color:rgb(34,36,40)}")
    def update_plot(self, val):
        temp_c = val
        self.cursor.execute("INSERT INTO temperature1 (temp, date,hour) VALUES(?,?,?)",
                            (val,dt.datetime.now().strftime('%d.%m.%Y  %H:%M:%S'),dt.datetime.now().strftime('%H')))
        self.con.commit()
        if val:
            self.ui.frame_8.setStyleSheet("""QFrame{border:8px solid rgb(85,170,255);color:#FFF;padding-left:20px;padding-right:20px;background-color:rgb(34,36,40);}""" )
        self.timer.start(500)
        self.timer.timeout.connect(self.blink)
        self.xs.append(dt.datetime.now().strftime('%H:%M:%S'))
        self.ui.label_5.setText(str(temp_c)+" ° C")
        self.ui.label_6.setText("Last update:" + dt.datetime.now().strftime('%d.%m.%Y  %H:%M:%S'))
        self.ys.append(temp_c)
        self.xs = self.xs[-10:]
        self.ys = self.ys[-10:]
        self.canvas.axes.cla()
        self.canvas.axes.set_xlabel("Time")
        self.canvas.axes.set_ylabel("Temperature")
        self.canvas.axes.grid(color='gray', linestyle='dashed')
        self.canvas.axes.plot(self.xs, self.ys, 'r')
        self.canvas.draw()
    def animation(self):
        currentwidth=self.ui.frame_7.width()
        self.animation=QPropertyAnimation(self.ui.frame_7,b'geometry')
        self.animation.setDuration(800)
        self.animation.setStartValue(QRect(0,0,0,800))
        self.animation.setEndValue(QRect(0,0,200,800))
        self.ui.pushButton_2.hide()
        self.ui.pushButton.show()
        self.animation.start()
    def exportdata(self):
        with open("logdata","w") as file:
            self.cursor.execute("Select * from temperature1")
            data=self.cursor.fetchall()
            file.write(" TEMP         DATETİME")
            file.write("\n--------------------------------")
            for i in data:
                file.writelines("\n"+str(i[0])+" °C----->"+str(i[1])+"\n")
        self.show_dialog()
    def show_dialog(self):
        msg = QMessageBox(self)
        msg.setText("Export success!")
        msg.setWindowTitle("EXPORT DATA")
        msg.setIcon(QMessageBox.Warning)
        msg.window_width, msg.window_height = 400,200
        msg.setMinimumSize(msg.window_width, msg.window_height)
        msg.exec_()
    def close(self):
        self.animation=QPropertyAnimation(self.ui.frame_7,b'geometry')
        self.animation.setDuration(800)
        self.animation.setStartValue(QRect(0,0,200,800))
        self.animation.setEndValue(QRect(0,0,0,800))
        self.ui.pushButton.hide()
        self.ui.pushButton_2.show()
        self.animation.start()
app=QApplication(sys.argv)
myapp=MyApp()
sys.exit(app.exec_())
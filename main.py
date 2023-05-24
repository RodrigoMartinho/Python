import sys
import time

from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton, QLineEdit, QLabel, QProgressBar

class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)

        self.lblvalor1 = QLabel(self)
        self.lblvalor1.setText("Valor 1")
        self.lblvalor1.move(10, 5)

        self.txtvalor1 = QLineEdit(self)
        self.txtvalor1.move(10, 20)

        self.lblvalor2 = QLabel(self)
        self.lblvalor2.setText("Valor 2")
        self.lblvalor2.move(10, 40)

        self.txtvalor2 = QLineEdit(self)
        self.txtvalor2.move(10, 55)

        self.lblresultado = QLabel(self)
        self.lblresultado.setText("Resultado")
        self.lblresultado.move(10, 75)

        self.txtresultado = QLineEdit(self)
        self.txtresultado.move(10, 90)

        #botão calcular
        self.btncalcular = QPushButton(self)
        self.btncalcular.setText("Calcular")

        self.btncalcular.move(10, 115)
        self.btncalcular.clicked.connect(self.calcular)

        # botão barra de progresso
        self.btnprogresso = QPushButton(self)
        self.btnprogresso.setText("Progresso")

        self.btnprogresso.move(100, 115)
        self.btnprogresso.clicked.connect(self.startprogress)

        # botão de mensagem
        self.btnmensagem = QPushButton(self)
        self.btnmensagem.setText("Olá Mundo")

        self.btnmensagem.move(200, 115)
        self.btnmensagem.clicked.connect(self.mensagem)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 140, 300, 25)

        self.setMinimumHeight(100)
        self.setMinimumWidth(150)
    def calcular(self):
        self.txtresultado.setText("{:,}".format(int(self.txtvalor1.text()) + int(self.txtvalor2.text())))

    def mensagem(self):
        msg = QMessageBox()
        msg.setIcon(msg.Information)
        msg.setWindowTitle("Mensagem")
        msg.setText("Olá Mundo! ")

        msg.exec()

    def startprogress(self):
        for startVal in range(1,101):
            time.sleep(0.07)
            self.progress_bar.setValue(startVal)

class principal(QWidget, ):
    def __init__(self, parent=None):
        super(principal, self).__init__(parent)

        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(320, 200)

        self.startPrincipal()

    def startPrincipal(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("Primeiro projeto!")
        # self.setCentralWidget(self.Window)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = principal()

    sys.exit(app.exec_())
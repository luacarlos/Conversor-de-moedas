import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from trader_virtual import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.pushButton_comprarMoeda.clicked.connect(self.compra)
        self.ui.pushButton_venderMoeda.clicked.connect(self.vender)

    def compra(self):
        valor = self.ui.lineEdit_comprar_vendaMoeda.text()
        moeda = self.ui.comprar_vendaMoeda.currentText()
        saldo = self.ui.Titulo_saldo.text()[15:]
        if saldo <= 0 or saldo<valor:
            self.ui.label_acao.setText("Você não possui saldo suficiente para comprar outra moeda")
        else:
            if moeda == "USD":
                
                
            elif moeda == "EUR":

            elif moeda == "JPY":

            elif moeda == "ARS":

    def vender(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
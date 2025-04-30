import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ConversorDeMoedas import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_converter.clicked.connect(self.Conversao)

    def Conversao(self):
        num = int(self.ui.lineEdit_inicial.text())
        moeda_atual = self.ui.comboBox_conversor.currentText()
        moeda_converter = self.ui.comboBox_converter.currentText()

        conversao = 0

        if moeda_atual == "USD":
            if moeda_converter == "EUR":
                simbolo = "€"
                conversao = num * 0.87805
            elif moeda_converter == "JPY":
                simbolo = "¥"
                conversao = num * 142.32
            elif moeda_converter == "BRL":
                simbolo = "R$"
                conversao = num * 5.63315
            elif moeda_converter == "ARS":
                simbolo = "AR$"
                conversao = num * 1175.00

        elif moeda_atual == "EUR":
            if moeda_converter == "USD":
                simbolo = "$"
                conversao = num * 1.1372
            elif moeda_converter == "JPY":
                simbolo = "¥"
                conversao = num * 163.32
            elif moeda_converter == "BRL":
                simbolo = "R$"
                conversao = num * 6.19915
            elif moeda_converter == "ARS":
                simbolo = "AR$"
                conversao = num * 1343.36

        elif moeda_atual == "JPY":
            if moeda_converter == "USD":
                simbolo = "$"
                conversao = num * 0.00696
            elif moeda_converter == "EUR":
                simbolo = "€"
                conversao = num * 0.00612
            elif moeda_converter == "BRL":
                simbolo = "R$"
                conversao = num * 0.03978
            elif moeda_converter == "ARS":
                simbolo = "AR$"
                conversao = num * 8.11376

        elif moeda_atual == "BRL":
            if moeda_converter == "USD":
                simbolo = "$"
                conversao = num * 0.17685
            elif moeda_converter == "EUR":
                simbolo = "€"
                conversao = num * 0.1613
            elif moeda_converter == "JPY":
                simbolo = "¥"
                conversao = num * 25.13
            elif moeda_converter == "ARS":
                simbolo = "AR$"
                conversao = num * 204.00

        elif moeda_atual == "ARS":
            if moeda_converter == "USD":
                simbolo = "$"
                conversao = num * 0.00085
            elif moeda_converter == "EUR":
                simbolo = "€"
                conversao = num * 0.00075
            elif moeda_converter == "JPY":
                simbolo = "¥"
                conversao = num * 0.1232
            elif moeda_converter == "BRL":
                simbolo = "R$"
                conversao = num * 0.0049



        if moeda_converter == moeda_atual:
            self.ui.label_resultado.setText("As moedas selecionadas são iguais")
        elif conversao is not None:
            self.ui.label_resultado.setText(f'A conversão de {num} de {moeda_atual} para {moeda_converter} é (ou aproximadamente): {simbolo} {conversao:.2f}')
        else:
            self.ui.label_resultado.setText("Conversão inválida ou não suportada.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())





#converta: 1 dollar para euro, 1 dolar para iene japones, 1 dollar para real, 1 dollar para peso argentino 
#converta: 1 euro para dollar, 1 euro para iene japones, 1 euro para real, 1 euro para peso argentino 
#converta: 1 iene japones para dollar, 1 iene japones para euro, 1 iene japones para real, 1 iene japones para peso argentino 
#converta: 1 real para dollar, 1 real para euro, 1 real para iene japones, 1 real para peso argentino 
#converta: 1 peso argentino para dollar, 1 peso argentino para euro, 1 peso argentino para iene japones, 1 peso argentino para real
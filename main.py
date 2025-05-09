import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Conversor import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Trocar.clicked.connect(self.Trocar)
        self.ui.pushButton_Converter.clicked.connect(self.Conversao)

    def Trocar(self):
        moeda_Valor = self.ui.comboBox_Valor.currentText()
        moeda_Conversao = self.ui.comboBox_Conversao.currentText()
        
        index_valor = self.ui.comboBox_Conversao.findText(moeda_Valor)
        index_conv = self.ui.comboBox_Valor.findText(moeda_Conversao)

        self.ui.comboBox_Valor.setItemText(index_valor,moeda_Conversao)
        self.ui.comboBox_Valor.setItemText(index_conv,moeda_Valor)

        self.ui.comboBox_Conversao.setItemText(index_conv,moeda_Valor)
        self.ui.comboBox_Conversao.setItemText(index_valor,moeda_Conversao)

        


    def Conversao(self):
        try:
            moeda_Valor = self.ui.comboBox_Valor.currentText()
            moeda_Conversao = self.ui.comboBox_Conversao.currentText()
            
            if moeda_Conversao == moeda_Valor:
                self.ui.label_alerta.setStyleSheet("background-color: white; border-radius:15px;")

                self.ui.label_alerta.setText("As moedas selecionadas são iguais")
            
            else:
                self.ui.label_alerta.setText("")
                self.ui.label_alerta.setStyleSheet("background-color: transparent;")

                valor = self.ui.lineEdit_valor.text()

                if ',' in valor:
                    count=0
                    valor_format=''
                    for i in valor:
                        if i ==',':
                            valor_format+='.'
                        else:
                            valor_format+=i
                        count+=1
                    
                valor = float(valor_format)

                conversao = 0
                
                if moeda_Valor == "USD":
                    if moeda_Conversao == "EUR":
                        simbolo = "€"
                        conversao = valor * 0.87805
                    elif moeda_Conversao == "JPY":
                        simbolo = "¥"
                        conversao = valor * 142.32
                    elif moeda_Conversao == "BRL":
                        simbolo = "R$"
                        conversao = valor * 5.63315
                    elif moeda_Conversao == "ARS":
                        simbolo = "AR$"
                        conversao = valor * 1175.00

                elif moeda_Valor == "EUR":
                    if moeda_Conversao == "USD":
                        simbolo = "$"
                        conversao = valor * 1.1372
                    elif moeda_Conversao == "JPY":
                        simbolo = "¥"
                        conversao = valor * 163.32
                    elif moeda_Conversao == "BRL":
                        simbolo = "R$"
                        conversao = valor * 6.19915
                    elif moeda_Conversao == "ARS":
                        simbolo = "AR$"
                        conversao = valor * 1343.36

                elif moeda_Valor == "JPY":
                    if moeda_Conversao == "USD":
                        simbolo = "$"
                        conversao = valor * 0.00696
                    elif moeda_Conversao == "EUR":
                        simbolo = "€"
                        conversao = valor * 0.00612
                    elif moeda_Conversao == "BRL":
                        simbolo = "R$"
                        conversao = valor * 0.03978
                    elif moeda_Conversao == "ARS":
                        simbolo = "AR$"
                        conversao = valor * 8.11376

                elif moeda_Valor == "BRL":
                    if moeda_Conversao == "USD":
                        simbolo = "$"
                        conversao = valor * 0.17685
                    elif moeda_Conversao == "EUR":
                        simbolo = "€"
                        conversao = valor * 0.1613
                    elif moeda_Conversao == "JPY":
                        simbolo = "¥"
                        conversao = valor * 25.13
                    elif moeda_Conversao == "ARS":
                        simbolo = "AR$"
                        conversao = valor * 204.00

                elif moeda_Valor == "ARS":
                    if moeda_Conversao == "USD":
                        simbolo = "$"
                        conversao = valor * 0.00085
                    elif moeda_Conversao == "EUR":
                        simbolo = "€"
                        conversao = valor * 0.00075
                    elif moeda_Conversao == "JPY":
                        simbolo = "¥"
                        conversao = valor * 0.1232
                    elif moeda_Conversao == "BRL":
                        simbolo = "R$"
                        conversao = valor * 0.0049
                
                self.ui.label_saida.setText(f"{simbolo}{conversao:.2f}")
        except ValueError:
            self.ui.label_alerta.setStyleSheet("background-color: white; border-radius:15px;")
            self.ui.label_alerta.setText("Conversão inválida ou não suportada.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
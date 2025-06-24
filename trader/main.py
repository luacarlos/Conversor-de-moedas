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
        else:
            valor = float(self.ui.lineEdit_comprar_vendaMoeda.text())

        
        if ',' in saldo:
            count=0
            saldo_format=''
            for i in saldo:
                if i ==',':
                    saldo_format+='.'
                else:
                    saldo_format+=i
                count+=1
            saldo = float(saldo_format)
        else:
            saldo = float(self.ui.Titulo_saldo.text()[15:])

        if saldo <= 0:
            self.ui.label_acao.setText("Você não possui saldo suficiente para comprar outra moeda")

        else:
            # if moeda == "USD":
            #     conversao = valor * 5.63315

            # elif moeda == "EUR":
            #     conversao = valor * 6.19915
    
            # elif moeda == "JPY":
            #     conversao = valor * 0.03978

            # elif moeda == "ARS":
            #     conversao = valor * 0.0049

            if moeda == "USD":
                conversao = valor * 5.54
                if saldo<conversao:
                    self.ui.label_acao.setText("Você não possui saldo suficiente para comprar este valor da moeda")
                else:
                    self.ui.label_carteiraUsd.setText(f"{self.ui.label_carteiraUsd.text()[0:6]}{(float(self.ui.label_carteiraUsd.text()[6:]) + valor):.2f}")
                    print(conversao)
                    self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo - conversao):.2f}')


            elif moeda == "EUR":
                conversao = valor * 6.41
                if saldo<conversao:
                    self.ui.label_acao.setText("Você não possui saldo suficiente para comprar este valor da moeda")
                else:
                    self.ui.label_carteiraEur.setText(f"{self.ui.label_carteiraEur.text()[0:6]}{(float(self.ui.label_carteiraEur.text()[6:]) + valor):.2f}")
                    print(conversao)
                    self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo - conversao):.2f}')
            
            elif moeda == "JPY":
                conversao = valor * 0.04
                if saldo<conversao:
                    self.ui.label_acao.setText("Você não possui saldo suficiente para comprar este valor da moeda")
                else:
                    self.ui.label_carteiraJpy.setText(f"{self.ui.label_carteiraJpy.text()[0:6]}{(float(self.ui.label_carteiraJpy.text()[6:]) + valor):.2f}")
                    print(conversao)
                    self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo - conversao):.2f}')
            
            elif moeda == "ARS":
                conversao = valor * 0.47
                if saldo<conversao:
                    self.ui.label_acao.setText("Você não possui saldo suficiente para comprar este valor da moeda")
                else:
                    self.ui.label_carteiraArs.setText(f"{self.ui.label_carteiraArs.text()[0:8]}{(float(self.ui.label_carteiraArs.text()[8:]) + valor):.2f}")
                    print(conversao)
                    self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo - conversao):.2f}')

    def vender(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
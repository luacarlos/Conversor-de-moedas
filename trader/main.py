import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from trader_virtual import Ui_MainWindow
from PyQt5.QtGui import QIcon

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        self.ui.pushButton_alterar_tema.setIcon(QIcon("assets/dark.png"))
        self.ui.pushButton_comprarMoeda.clicked.connect(self.compra)
        self.ui.pushButton_venderMoeda.clicked.connect(self.vender)
        self.ui.pushButton_alterar_tema.clicked.connect(self.alterarTema)
        self.tema = True
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

        if moeda == "USD":
            conversao = valor * 5.54
            if float(self.ui.label_carteiraUsd.text()[6:]) < valor:
                self.ui.label_acao.setText("Você não possui este valor na carteira")
            else:
                self.ui.label_carteiraUsd.setText(f"{self.ui.label_carteiraUsd.text()[0:6]}{(float(self.ui.label_carteiraUsd.text()[6:]) - valor):.2f}")
                print(conversao)
                self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo + conversao):.2f}')

        elif moeda == "EUR":
            conversao = valor * 6.41
            if float(self.ui.label_carteiraEur.text()[6:]) < valor:
                self.ui.label_acao.setText("Você não possui este valor na carteira")
            else:
                self.ui.label_carteiraEur.setText(f"{self.ui.label_carteiraEur.text()[0:6]}{(float(self.ui.label_carteiraEur.text()[6:]) - valor):.2f}")
                print(conversao)
                self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo + conversao):.2f}')

        elif moeda == "JPY":
            conversao = valor * 0.04
            if float(self.ui.label_carteiraJpy.text()[6:]) < valor:
                self.ui.label_acao.setText("Você não possui este valor na carteira")
            else:
                self.ui.label_carteiraJpy.setText(f"{self.ui.label_carteiraJpy.text()[0:6]}{(float(self.ui.label_carteiraJpy.text()[6:]) - valor):.2f}")
                print(conversao)
                self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo + conversao):.2f}')

        elif moeda == "ARS":
            conversao = valor * 0.47
            if float(self.ui.label_carteiraArs.text()[8:]) < valor:
                self.ui.label_acao.setText("Você não possui este valor na carteira")
            else:
                self.ui.label_carteiraArs.setText(f"{self.ui.label_carteiraArs.text()[0:8]}{(float(self.ui.label_carteiraArs.text()[8:]) - valor):.2f}")
                print(conversao)
                self.ui.Titulo_saldo.setText(f'{self.ui.Titulo_saldo.text()[0:15]}{(saldo + conversao):.2f}')
    
    def alterarTema(self):
        if self.tema:
            self.ui.pushButton_alterar_tema.setIcon(QIcon("assets/light.png"))
            self.tema = False
            
            self.setStyleSheet("background-color: #161817;")
            
            self.ui.label.setStyleSheet("background-color: #1c1d1c; border: 1.5px solid #303030; border-radius: 4px;")
            self.ui.label_6.setStyleSheet("background-color: #1c1d1c; border: 1.5px solid #303030; border-radius: 4px;")
            self.ui.label_11.setStyleSheet("background-color: #1c1d1c; border: 1.5px solid #303030; border-radius: 4px;")
            self.ui.label_12.setStyleSheet("background-color: #1c1d1c; border: 1.5px solid #303030; border-radius: 4px;")

            self.ui.pushButton_comprarMoeda.setStyleSheet('background-color: #242223; color: white; border: 1.5px solid #303030; border-radius: 4px;')
            self.ui.pushButton_venderMoeda.setStyleSheet('background-color: #242223; color: white; border: 1.5px solid #303030; border-radius: 4px;')

            self.ui.label_carteiraArs.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_carteiraEur.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_carteiraJpy.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_carteiraUsd.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_cotacaoArs.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_cotacaoEur.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_cotacaoJpy.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_cotacaoUsd.setStyleSheet('color: white; background-color: transparent;')

            self.ui.Titulo_acao.setStyleSheet('color: white; background-color: transparent;')
            self.ui.Titulo_carteira.setStyleSheet('color: white; background-color: transparent;')
            self.ui.Titulo_cotacaoAtual.setStyleSheet('color: white; background-color: transparent;')
            self.ui.Titulo_saldo.setStyleSheet('color: white; background-color: transparent;')
            self.ui.label_acao.setStyleSheet("background-color: transparent; color: white;")

            self.ui.lineEdit_comprar_vendaMoeda.setStyleSheet('color: white; border-radius: 5px; border: 1.5px solid white; padding: 10px;')
            self.ui.comprar_vendaMoeda.setStyleSheet('border: 1.5px solid white; border-radius: 5px; color: white;')

        else:
            self.ui.pushButton_alterar_tema.setIcon(QIcon("assets/dark.png"))
            self.tema=True

            self.setStyleSheet("background-color: rgb(248, 244, 238);")
            
            self.ui.label.setStyleSheet("background-color: rgb(255, 251, 243); border: 2px solid rgb(207, 204, 201); border-radius: 4px;")
            self.ui.label_6.setStyleSheet("background-color: rgb(255, 251, 243); border: 2px solid rgb(207, 204, 201); border-radius: 4px;")
            self.ui.label_11.setStyleSheet("background-color: rgb(255, 251, 243); border: 2px solid rgb(207, 204, 201); border-radius: 4px;")
            self.ui.label_12.setStyleSheet("background-color: rgb(255, 251, 243); border: 2px solid rgb(207, 204, 201); border-radius: 4px;")

            self.ui.pushButton_comprarMoeda.setStyleSheet('background-color: transparent; border: 1.5px solid rgb(207, 204, 201); border-radius: 4px;')
            self.ui.pushButton_venderMoeda.setStyleSheet('background-color: transparent; border: 1.5px solid rgb(207, 204, 201); border-radius: 4px;')

            self.ui.label_carteiraArs.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_carteiraEur.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_carteiraJpy.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_carteiraUsd.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_cotacaoArs.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_cotacaoEur.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_cotacaoJpy.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_cotacaoUsd.setStyleSheet('color: black; background-color: transparent;')
            self.ui.label_acao.setStyleSheet("background-color: transparent; color: black;")

            self.ui.Titulo_acao.setStyleSheet('color: black; background-color: transparent;')
            self.ui.Titulo_carteira.setStyleSheet('color: black; background-color: transparent;')
            self.ui.Titulo_cotacaoAtual.setStyleSheet('color: black; background-color: transparent;')
            self.ui.Titulo_saldo.setStyleSheet('color: black; background-color: transparent;')

            self.ui.lineEdit_comprar_vendaMoeda.setStyleSheet('border-radius: 5px; border: 1.5px solid black; padding: 10px;')
            self.ui.comprar_vendaMoeda.setStyleSheet('border: 1.5px solid black; border-radius: 5px;')


        print(self.tema)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
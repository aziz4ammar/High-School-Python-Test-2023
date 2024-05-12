from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from pickle import dump,load

def calcul():
    ch1=w.a.text()
    ch2=w.b.text()
    if ch1=="" or ch2=="" :
        QMessageBox.critical(w,"Erreur","a or b is still clear")
    else:
        k=float(ch1);m=float(ch2)
        if not (2<=k<=20)or not(2<=m<=20):
            QMessageBox.critical(w,"Erreur","verif your numbers")
        else:
            f=open("file.dat","ab")
            e={}
            e["A"]=k
            e["B"]=m
            e["N"]=""
            e["Methode"]=""
            e["Valeur"]=""
            dump(e,f)
            f.close()
def afficher():
    f=open("file.dat","rb")
    i=0
    w.tw.setRowCount(0)
    fin=False
    while fin==False:
        try:
            e=load(f)
            w.tw.insertRow(i)
            w.tw.setItem(i,0,QTableWidgetItem(str(e["A"])))
            w.tw.setItem(i,1,QTableWidgetItem(str(e["B"])))
            w.tw.setItem(i,2,QTableWidgetItem(str(e["N"])))
            w.tw.setItem(i,3,QTableWidgetItem(str(e["Methode"])))
            w.tw.setItem(i,4,QTableWidgetItem(str(e["Valeur"])))
            i+=1
        except:
            fin=True
    f.close() 

app=QApplication([])
w=loadUi("untitled.ui")
w.c.clicked.connect(calcul)
w.aff.clicked.connect(afficher)
w.show()
app.exec()
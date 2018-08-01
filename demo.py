from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton,QMessageBox
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.filename = "C:/py_qt/data.txt"
        self.initUI()
        
    def initUI(self):
    
        self.cb1 = QCheckBox('全选',self)
        self.cb2 = QCheckBox('Option1',self)
        self.cb3 = QCheckBox('Option2',self)
        self.cb4 = QCheckBox('Option3',self)
        self.cb5 = QCheckBox('Option4',self)
        self.cb6 = QCheckBox('Option5',self)
        self.cb7 = QCheckBox('Option6',self)
        self.cb8 = QCheckBox('Option7',self)
        self.cb9 = QCheckBox('Option8',self)
        self.cb10 = QCheckBox('Option9',self)
        self.cb11 = QCheckBox('Option10',self)
        self.cb12 = QCheckBox('Option11',self)
        self.cb13 = QCheckBox('Option12',self)
       
        
        
        bt = QPushButton('保存',self)
        
        self.resize(300,200)
        self.setWindowTitle('Yasuhara')
        
        self.cb1.move(20, 20)
        self.cb2.move(20, 50)
        self.cb3.move(20, 80)
        self.cb4.move(20, 110)
        self.cb5.move(20, 140)
        self.cb6.move(100, 50)
        self.cb7.move(100, 80)
        self.cb8.move(100, 110)
        self.cb9.move(100, 140)
        self.cb10.move(180, 50)
        self.cb11.move(180, 80)
        self.cb12.move(180, 110)
        self.cb13.move(180, 140)
        bt.move(200,170)
        
        self.cb1.stateChanged.connect(self.changecb1)
        self.cb2.stateChanged.connect(self.changecb2)
        self.cb3.stateChanged.connect(self.changecb2)
        self.cb4.stateChanged.connect(self.changecb2)
        self.cb5.stateChanged.connect(self.changecb2)
        self.cb6.stateChanged.connect(self.changecb2)
        self.cb7.stateChanged.connect(self.changecb2)
        self.cb8.stateChanged.connect(self.changecb2)
        self.cb9.stateChanged.connect(self.changecb2)
        self.cb10.stateChanged.connect(self.changecb2)
        self.cb11.stateChanged.connect(self.changecb2)
        self.cb12.stateChanged.connect(self.changecb2)
        self.cb13.stateChanged.connect(self.changecb2)
        bt.clicked.connect(self.go)
        
        self.show()
        
    def go(self):
        write2 = self.cb2.isChecked()
        write3 = self.cb3.isChecked()
        write4 = self.cb4.isChecked()
        write5 = self.cb5.isChecked()
        write6 = self.cb6.isChecked()
        write7 = self.cb7.isChecked()
        write8 = self.cb8.isChecked()
        write9 = self.cb9.isChecked()
        write10 = self.cb10.isChecked()
        write11 = self.cb11.isChecked()
        write12 = self.cb12.isChecked()
        write13 = self.cb13.isChecked()
        f = open(self.filename, 'w')
        f.write("%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d\n" %(write2,write3,write4,write5,write6,write7,write8,write9,write10,write11,write12,write13))
        f.close()
        # if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
        #     f = open(self.filename, 'w')
        #     f.write("1\n1\n1\n")
        #     f.close()
        # elif self.cb2.isChecked() and self.cb3.isChecked():
        #     QMessageBox.information(self,'I Love U','你是我的！')
        # elif self.cb2.isChecked() and self.cb4.isChecked():
        #     QMessageBox.information(self,'I Love U','你是宝贝！')
        # elif self.cb3.isChecked() and self.cb4.isChecked():
        #     QMessageBox.information(self,'I Love U','我的宝贝！')
        # elif self.cb2.isChecked():
        #     QMessageBox.information(self,'I Love U','你是！')
        # elif self.cb3.isChecked():
        #     QMessageBox.information(self,'I Love U','我的！')
        # elif self.cb4.isChecked():
        #     QMessageBox.information(self,'I Love U','宝贝！')
        # else:
        #     QMessageBox.information(self,'I Love U','貌似你没有勾选啊！')

    def changecb1(self):
        if self.cb1.checkState() == Qt.Checked:
            self.cb2.setChecked(True)
            self.cb3.setChecked(True)
            self.cb4.setChecked(True)
            self.cb5.setChecked(True)
            self.cb6.setChecked(True)
            self.cb7.setChecked(True)
            self.cb8.setChecked(True)
            self.cb9.setChecked(True)
            self.cb10.setChecked(True)
            self.cb11.setChecked(True)
            self.cb12.setChecked(True)
            self.cb13.setChecked(True)
        elif self.cb1.checkState() == Qt.Unchecked:
            self.cb2.setChecked(False)
            self.cb3.setChecked(False)
            self.cb4.setChecked(False)
            self.cb5.setChecked(False)
            self.cb6.setChecked(False)
            self.cb7.setChecked(False)
            self.cb8.setChecked(False)
            self.cb9.setChecked(False)
            self.cb10.setChecked(False)
            self.cb11.setChecked(False)
            self.cb12.setChecked(False)
            self.cb13.setChecked(False)
    def changecb2(self):
        pass
        # if self.cb2.isChecked() and self.cb3.isChecked() and self.cb4.isChecked():
        #     self.cb1.setCheckState(Qt.Checked)
        # elif self.cb2.isChecked() or self.cb3.isChecked() or self.cb4.isChecked():
        #     self.cb1.setTristate()
        #     self.cb1.setCheckState(Qt.PartiallyChecked)
        # else:
        #     self.cb1.setTristate(False)
        #     self.cb1.setCheckState(Qt.Unchecked)

    def closeEvent(self, event): #重写closeEvent函数
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

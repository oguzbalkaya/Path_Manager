from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os, glob

from ui.mainwindow import Ui_MainWindow
from ui.neworedit import Ui_Form


class EditNew(QWidget):
    saveSignal = Signal(str)
    editSignal = Signal(str,int)

    def isThere(self,newItem, pathList):
        if newItem in pathList:
            return 1
        return 0

    def searchFile(self,filename):
        files = glob.glob(filename)
        if len(files):
            print(files)
            return True
        return False

    def __init__(self, pathList,status):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.pathList = pathList
        self.status = status

    def cancel(self):
        print("cancel")
        self.close()

    def save(self):
        pathName = self.ui.lineEdit.text()
        if self.isThere(pathName, self.pathList):
            QMessageBox.information(self, "Information", "{} has already been added.".format(pathName), QMessageBox.Ok)
        elif not self.searchFile(pathName):
            QMessageBox.information(self, "Information", "Invalid path : {}.\n\nPlease write a valid path.".format(pathName), QMessageBox.Ok)
        else:
            if(self.status==-1): #new
                self.saveSignal.emit(pathName)
                self.close()
            else: #edit
                self.editSignal.emit(pathName,self.status)
                self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pathFilePath = os.environ.get("HOME") + "/.pathList"
        self.pathList = self.pathToList(self.pathFilePath)
        self.readPath()
        self.ui.newButton.clicked.connect(self.new)
        self.ui.editButton.clicked.connect(self.edit)
        self.ui.deleteButton.clicked.connect(self.delete)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.actionAbout.triggered.connect(self.about)
        self.isChanged = False
        self.lastItem = len(self.pathList)

    def about(self):
        QMessageBox.information(self, "About The Application",
                                "Oğuz BALKAYA\n"
                                "oguz.balkaya@gmail.com\n"
                                "https://www.linkedin.com/in/oguz-balkaya/\n"
                                "https://github.com/oguzbalkaya/Path_Manager", QMessageBox.Ok)

    def readPath(self):
        for i in range(0, len(self.pathList)):
            self.ui.listWidget.insertItem(i, self.pathList[i])
            if i < len(os.environ.get("PATH").split(":")):
                self.ui.listWidget.item(i).setForeground(QColor('#ff0000'))
                self.ui.listWidget.item(i).setFlags(Qt.NoItemFlags)
            else:
                self.ui.listWidget.item(i).setForeground(QColor('#008000'))

    def pathToList(self, filePath):
        path = os.environ.get("PATH")
        path = path.split(":")
        with open(filePath, "r+") as file:
            for r in file:
                path.append(r.replace("\n", ""))
        return path

    def newPath(self, path):
        self.isChanged = True
        self.ui.listWidget.addItem(path)
        self.pathList.append(path)


    def editPath(self, path, index):
        self.isChanged = True
        self.ui.listWidget.item(index).setForeground(QColor('#000000'))
        self.ui.listWidget.item(index).setText(path)
        self.pathList[index]=path



    def new(self):
        self.new_window = EditNew(self.pathList,-1)
        self.new_window.saveSignal.connect(self.newPath)
        self.new_window.show()

    def edit(self):
        if len(self.ui.listWidget.selectedIndexes()) != 0:
            self.new_window = EditNew(self.pathList, self.ui.listWidget.selectedIndexes()[0].row())
            print(self.ui.listWidget.selectedIndexes()[0].row())
            self.new_window.ui.lineEdit.setText(
                self.ui.listWidget.item(self.ui.listWidget.selectedIndexes()[0].row()).text())
            self.new_window.editSignal.connect(self.editPath)
            self.new_window.show()

    def delete(self):
        if len(self.ui.listWidget.selectedIndexes()):
            self.isChanged = True
            self.pathList.pop(self.ui.listWidget.selectedIndexes()[0].row())
            self.ui.listWidget.takeItem(self.ui.listWidget.selectedIndexes()[0].row())

    def save(self):
        if self.isChanged:
            print(self.pathList)
            self.isChanged = False
            for j in range(self.lastItem,len(self.pathList)):
                self.ui.listWidget.item(j).setForeground(QColor('#008000'))
            with open(self.pathFilePath, "w+") as file:
                for i in range(len(os.environ.get("PATH").split(":")), len(self.pathList)):
                    file.write(self.pathList[i] + "\n")


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()

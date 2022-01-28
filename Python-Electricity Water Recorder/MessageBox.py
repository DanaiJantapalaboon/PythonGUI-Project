from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sqlite3

#MessageBox
#Help --> About Menubar#
def showAbout():
    msg = QMessageBox()
    msg.setWindowTitle("About")
    msg.setText("Electricity-Water Bills Monthly Record V1.00\nProgramming by Danai J.\n------------------------------------\nPython version 3.9.1\nSQLite3 Database\nPyQT5 version 5.15.2\nmatplotlib version 3.4.2\nnumpy version 1.10.2")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()


#Message Box Exit
def showExit():
    msg = QMessageBox()
    msg.setWindowTitle("Exit")
    msg.setText("Do you want to Exit ?")
    msg.setIcon(QMessageBox.Question)
    choiceYes = msg.addButton("Yes", QMessageBox.ActionRole)
    choiceNo = msg.addButton("No", QMessageBox.RejectRole)
    msg.setDefaultButton(choiceNo)
    x = msg.exec_()
    if msg.clickedButton() == choiceYes:
        QApplication.quit()
        #exit()
        #app.quit()


#Message Clear Data
def clearData():
    msg = QMessageBox()
    msg.setWindowTitle("Clear History")
    msg.setText("Do you want to clear all data ? (The data will be lost)")
    msg.setIcon(QMessageBox.Question)
    choiceYes = msg.addButton("Yes", QMessageBox.ActionRole)
    choiceNo = msg.addButton("No", QMessageBox.RejectRole)
    msg.setDefaultButton(choiceNo)
    x = msg.exec_()
    if msg.clickedButton() == choiceYes:
        connection = sqlite3.connect("db/myDB.db")
        query = "DELETE FROM elecWater"
        connection.execute(query)
        connection.commit()
        connection.close()


#Message กรณีเปิดผิดไฟล์ (ไปเปิด db อันอื่น)
def wrongTable():
    msg = QMessageBox()
    msg.setWindowTitle("Warning")
    msg.setText("Wrong Database Table, Please Try Again")
    msg.setIcon(QMessageBox.Warning)
    x = msg.exec_()


#Message กรณีกดปุ่ม Chart แล้วไม่มีข้อมูลในตาราง
def emptyTable():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("No Data In Table, Please Open Database Or Record The Data")
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()


#Message กรณี Export Excel ไม่มีข้อมูลในตาราง
def noData():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("Cannot export to excel with no data!")
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()


#Message กรณี input ที่ไม่ใช่ int
def wrongInput():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("Please Input Number Only")
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()


#for v1.00
#Message Create Database
def backupDB():
    msg = QMessageBox()
    msg.setWindowTitle("Information")
    msg.setText("Database is Backuped!")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
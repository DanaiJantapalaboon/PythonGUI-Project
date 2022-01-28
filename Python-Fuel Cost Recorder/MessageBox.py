from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sqlite3

#MessageBox
#Help --> About Menubar#
def showAbout():
    msg = QMessageBox()
    msg.setWindowTitle("About")
    msg.setText("Fuel Management v1.01\nProgramming by Danai J.\n---------------------------\nPython version 3.9.1\nSQLite3 Database")
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
        #app.quit()

#Message no Data (use in datamgr.py)
def noData():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("ไม่มีข้อมูลในตาราง")
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()

#Message Create Database
def backupDB():
    msg = QMessageBox()
    msg.setWindowTitle("Information")
    msg.setText("Database is Backuped!")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()

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
        query = "DELETE FROM FuelManagement"
        connection.execute(query)
        connection.commit()
        connection.close()
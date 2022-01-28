from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sqlite3

#MessageBox
#Help --> About Menubar#
def showAbout():
    msg = QMessageBox()
    msg.setWindowTitle("About")
    msg.setText("Basic Translator English-Thai V1.01\nProgramming by Danai J.\n------------------------------------\nPython version 3.9.1\nGoogleTranslate API\nSQLite3 Database\nPyQT5 GUI")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
#END##########################################################################################################

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
#END##########################################################################################################


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
        connection = sqlite3.connect("db/defaultDB.db")
        query = "DELETE FROM History"
        connection.execute(query)
        connection.commit()
        connection.close()
#END##########################################################################################################


#Message กรณีที่ไม่มีความหมาย
def noMeaning():
    msg = QMessageBox()
    msg.setWindowTitle("Warning")
    msg.setText("Please input the correct words, try again!")
    msg.setIcon(QMessageBox.Warning)
    x = msg.exec_()
#END##########################################################################################################


#Message กรณีที่ไม่มีความหมาย
def noInternet():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("You have no input or no internet connection, Please try again!")
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()
#END##########################################################################################################


#Message กรณี Export Excel ไม่มีข้อมูลในตาราง
def noData():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("Cannot export to excel with no data!")
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()
#END##########################################################################################################



#for v1.00
#Message Create Database
def backupDB():
    msg = QMessageBox()
    msg.setWindowTitle("Information")
    msg.setText("Database is Backup!")
    msg.setIcon(QMessageBox.Information)
    x = msg.exec_()
#END##########################################################################################################

"""
#for v1.00
#Message กรณี Export Excel ไม่มีข้อมูลในตาราง
def noInput():
    msg = QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText("No input value, Please try again!")
    msg.setIcon(QMessageBox.Critical)
    x = msg.exec_()
#END##########################################################################################################
"""
import sys
import json
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTabWidget, QTextBrowser, QMessageBox
from PyQt6.QtCore import Qt
from openpyxl import Workbook
 
class friedchicken:
    def __init__(self, package, taste, price, origin, brand):
        #定義建構子，物件屬性
        self.package = package  #包裝
        self.taste = taste  #口味
        self.price = price  #價格
        self.origin = origin  #產地
        self.brand = brand  #名字

    def display_info(self):   #顯示結果
        return f"{self.brand} - package: {self.package}, taste: {self.taste}, price: ${self.price} ,origin: {self.origin} "

    def set_discount(self, discount_percent):   #設定折扣
        self.price=self.price * (1-discount_percent/100) 
        return f"{self.brand}-已使用折扣囉! New price: ${self.price}"   
 
    def change_taste(self, new_taste):     #變換口味
        self.taste= new_taste
        return f"{self.brand} - 口味換成 {new_taste} "
    
#創建4個炸雞物件
chicken01=friedchicken("一盒","海苔",150,"USA","1號餐")
chicken02=friedchicken("一桶","胡椒",200,"America","2號餐")
chicken03=friedchicken("一包","原味",80,"Mexico","3號餐")
chicken04=friedchicken("一籃","起士",250,"Taiwan","4號餐")

#呼叫物件
print(chicken01.display_info())
print(chicken02.set_discount(15)) 
print(chicken03.change_taste("海苔"))
print(chicken04.display_info())
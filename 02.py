import sys
import json
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTabWidget, QTextBrowser, QMessageBox
from PyQt6.QtCore import Qt
from openpyxl import Workbook

class Stust_Beverageshop:
    def __init__(self, name, seniority,work_hours):
        #定義建構子，物件屬性
        self.name = name  
        self.seniority = seniority   
        self.work_hours= work_hours
    def query_name(self):   
        return f"店名:{self.name}"
    def query_seniority(self):
        return f"年資:{self.seniority} 年"
    def query_work_hours(self):
        return f"本月工時:{self.work_hours} 小時"
    def calculate_salary(self):
        return f"預估月薪:{self.work_hours * hourly_rate}"
    def increase_work_hours(self,additional_hours):
        self.work_hours += additional_hours
        return f"工時時數增加 {additional_hours} 小時"
    def increase_seniority(self,additional_years):
        self.seniority +=additional_hours
        return f"年資增加 {additional_years} 年"
class Colddrink(Stust_Beverageshop):
     def __init__(self, name, seniority,work_hours,cold_type):
        #定義建構子，物件屬性
       super().__init__(name,seniority,work_hours)
       self.cold_type = cold_type  
class Hotdrink(Stust_Beverageshop):
     def __init__(self, name,seniority,work_hours,hot_type):
        #定義建構子，物件屬性
        super().__init__(name,seniority,work_hours)
        self.hot_type = hot_type  
#創立物件
drink_shop=Stust_Beverageshop("南台資工飲料店",3,120)
cold_drink=Colddrink("冷飲店",2,100,"氣泡水")
hot_drink=Hotdrink("熱飲店",1,80,"拿鐵")
#查詢資訊
print(drink_shop.query_name())
print(cold_drink.query_seniority())
print(hot_drink.query_work_hours())
#增加工時、年資
print(cold_drink.increase_work_hours(10))
print(hot_drink.increase_seniority(1))
#計算月薪
print(Stust_Beverageshop.calculate_monthly_salary())

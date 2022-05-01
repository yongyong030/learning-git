import openpyxl as op
import datetime
import os

##os.environ.setdefault("", "daytrading_data.settings")

path = r"C:\Users\jhr21\Desktop\경제"
wb = op.load_workbook(path + "\트레이딩 양식.xlsx")
path_save=r"C:\Users\jhr21\Desktop\Project_A"





now=datetime.datetime.now()
s_now=now.strftime('%Y.%m.%d_%H.%M.%S')

wb.save(path_save+"\\"+s_now+"_daytrading.xlsx")
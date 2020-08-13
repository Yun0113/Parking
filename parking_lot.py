# -*- coding: utf-8 -*-
import time
 
# 最大停车数
max_car = 100
# 当前停车数,初始为0
cur_car = 0
# 当前停车列表,初始设置为空
car_list = []
time.asctime()
 
class car(object):
 """定义一个车类包括 车主人名 车牌 开始停放时间"""
 
 def __init__(self, plate_number, starttime, carname):
  super(car, self).__init__()
  self.plate_number = plate_number
  self.starttime = starttime
  self.carname = carname
 
 def get_plate_number(self):
  return self.plate_number
 
 def get_starttime(self):
  return self.starttime
 
 def get_carname(self):
  return self.carname
 
 
if __name__ == '__main__':
 while True:
  print("-------------欢迎来到-停车管理系统---------")
  choice = input("请选则需要的功能 1,停车 2,取车 ,3.退出")
  print("********************************************")
  if choice == '1':
   carname = input("请输入你的名字:")
   plate_number = int(input("请输入你的车牌:"))
   starttime = time.time() # 记录当前时间
   carname = car(plate_number, starttime, carname, ) # 作为停车票
   car_list.append(carname) # 将汽车对象存入停车列表
   # print(len(car_list)) 测试用
   print("请拿好您的停车票：车牌号为%s的%s车主停车 当前时间%s" % (plate_number,carname.get_carname(),time.ctime()))
  elif choice == '2':
   # 第一步先查询汽车是否存在,如果不存在建议其联系管理员
   print("请出示您的停车票")
   plate_numbers = int(input("请输入你的车牌:"))
   for i in car_list:
    if plate_numbers == i.get_plate_number():
     print("车牌号为%s的车主%s欢迎取车,开车注意安全" % (plate_number,carname.get_carname()))
     car_list.remove(i)
    else:
     print("你的停车票号码不对,不能取车,如果有问题请联系管理员")
     break
  else:
   break
 print("感谢您的使用,再见")
import pandas as pd
import csv
import class_lab as cls


robot = cls.Robo(pd.read_csv('count.csv'))   #csvファイルを読み込む

robot.firstac()

robot.recom()

robot.quest()

robot.lastac()

robot.data.to_csv('count.csv',index=False)  #csvファイルに書き込む 

robot.data = pd.read_csv('count.csv')

print(robot.data)                         #csvファイルのデータを出力する
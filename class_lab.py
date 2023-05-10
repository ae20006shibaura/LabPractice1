import torch

import pandas as pd

class Robo:
    def __init__(self,data):
        self.data=data
        self.i_name='none'
        self.count=-1

    def firstac(self):
       print("こんにちは私はロボット受付です。あなたの名前は?")
       self.i_name = input()
    
    def recom(self):
         for index in self.data.iterrows():
             self.count=self.count+1
             sh_name=self.data.iloc[self.count,0]
             print(self.i_name +"さん。"+ sh_name +"がおすすめです")
             print(self.i_name +"さんは好きですか はい/いいえ") 
             check1 = input()
             if check1 == 'はい':
                 self.data.iloc[self.count,1]=self.data.iloc[self.count,1]+1
                 check1 = 'none'
    
    def quest(self):
        print(self.i_name+"さん。どこのレストランが好きですか")
        nsh_name = input()
        
        check = self.data[self.data['NAME'] == nsh_name]  
        if check.empty == True:                          
            self.data = self.data.append({'NAME': nsh_name,'COUNT': 1},ignore_index=True)
           
            

    def lastac(self):
        print(self.i_name + "さん、良い一日を") 
        self.data = self.data.sort_values('COUNT',ascending=False)





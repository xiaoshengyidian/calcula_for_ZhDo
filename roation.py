import csv
import pandas as pd
import re

g=10.0
#单位为国际单位
m_fama=0.05
M_pan=0.247
M_huan=0.204
R=0.02#并不是我实际实验时的半径
D=0.01#实际实验时的偏心距
def for_J(B_a:float,B_d:float):
    fenzi=m_fama*R*(g-R*B_a)
    fenmu=B_a-B_d
    res=fenzi/fenmu
    return res

def for_B(o1:float,t1:float,o2:float,t2:float):
    fenzi=2*(o2*t1-o1*t2)
    fenmu=t1*t2*(t2-t1)
    res=fenzi/fenmu
    return res

#第一组的转动惯量
list1_J=[]
#第一组的加速数据，待输入
list1a_t1=[]
list1a_t2=[]
list1a_o1=[]
list1a_o2=[]
Ba1=[]
#第一组的减速数据，待输入
list1d_t1=[]
list1d_t2=[]
list1d_o1=[]
list1d_o2=[]
Bd1=[]


#第二组的转动惯量
list2_J=[]
#第二组的加速数据，待输入
list2a_t1=[]
list2a_t2=[]
list2a_o1=[]
list2a_o2=[]
Ba2=[]
#第二组的减速数据，待输入
list2d_t1=[]
list2d_t2=[]
list2d_o1=[]
list2d_o2=[]
Bd2=[]

#第三组的转动惯量
list3_J=[]
#第三组的加速数据，待输入
list3a_t1=[]
list3a_t2=[]
list3a_o1=[]
list3a_o2=[]
Ba3=[]
#第三组的减速数据，待输入
list3d_t1=[]
list3d_t2=[]
list3d_o1=[]
list3d_o2=[]
Bd3=[]

BioaTou=[['实验序号'],['1'],['2'],['3'],['4'],['5']]
with open("第一组_普通_加速.csv", mode='w', newline='',encoding='utf-8') as file:  
    writer = csv.writer(file)  
    writer.writerows(BioaTou) 
print("done1!")

#进行第一组加速计算
for i in range(5):
    t1=list1a_t1[i]
    t2=list1a_t2[i]
    o1=list1a_o1[i]
    o2=list1a_o2[i]
    Ba_temp=for_B(o1,t1,o2,t2)
    Ba1.append(Ba_temp)
#进行第一组减速计算
for i in range(5):
    t1=list1d_t1[i]
    t2=list1d_t2[i]
    o1=list1d_o1[i]
    o2=list1d_o2[i]
    Bd_temp=for_B(o1,t1,o2,t2)
    Bd1.append(Bd_temp)
#进行第一组的转动惯量计算
for i in range(5):
    b_a=Ba1[i]
    b_d=Bd1[i]
    J_temp=for_J(b_a,b_d)
    list1_J.append(J_temp)

#进行数据的输出
df1=pd.read_csv('第一组_普通_加速.csv')
df1["第一组的的转动惯量"]=list1_J
df1.to_csv('第一组_普通_加速.csv',index=False)
print("done2!")
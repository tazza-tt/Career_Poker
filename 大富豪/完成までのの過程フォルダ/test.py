flag=True 
flag2=True 
s=1
t=1
print(flag == False  and s==1)
print(flag2==False and t==1)
if not (flag == False  and s==1) or (flag2==False and t==1)  :
    print("OK")


a="08"
b="1"
print(int(a)+int(b))


player2= [['10', '♦'], ['09', '♠'], ['joker', 'joker'], ['06', '♥'], ['06', '♦'], ['joker', 'joker'], ['07', '♣'], ['12', '♦'], ['08', '♦'], ['03', '♦'], ['Two', '♣'], ['One', '♣'], ['11', '♣']]
CP_choose_card=[]
try :
   only_num=[]
   for i in range(len(player2)) :
      only_num.append(player2[i][0])
         #８があったら８を出す処理
   eight_index = [p for p, x in enumerate(only_num) if x == "08" ]
   print(eight_index)
   CP_choose_card.append(player2[eight_index[0]])
except  Exception as e :
   CP_choose_card=[]
   pass
print(only_num)
print(CP_choose_card)



"""print("rrrr")"""

a=1
b=2
c=1
d=4 
if a != b != c != d :
    print("OKOKOK")

list_onzon_suuji_with_index_pea_3mai=[[['数字'], [8, 9, 10]]]
print(list_onzon_suuji_with_index_pea_3mai[0][-1][0])




a=1
b=2
c=3
listA=[]
if c >0 :
    listA.append(a)
    listA.append(b)
    listA.append(c)
print(listA)


import random 
a=random.randint(1,1)
print(a)

sikou_kaisuu=10
if 11 <= sikou_kaisuu <= 20 : 
    print("ok")


field_card=[[[2, "♠"]],[[2, "♠"]]]
print(field_card[-1][-1][-1])

list_only_num=['joker', 'One', '05', '05', '08', '07', '13', '09', '10', '06', '13', '07', '03']
ookisa_tehuda=0
for i in range(len(list_only_num)) : 
     if list_only_num[i]=="One" :
       ookisa_tehuda=ookisa_tehuda+1
     elif list_only_num[i]=="Two" :
          ookisa_tehuda=ookisa_tehuda+2
     elif list_only_num[i]=="joker" :
          ookisa_tehuda=ookisa_tehuda+0 
     else:
          ookisa_tehuda=ookisa_tehuda+int(list_only_num[i])
average_tehuda=(ookisa_tehuda/len(list_only_num))
print(average_tehuda)




a=[1,2,3,34,4,5,65,6,4,2,1]
a.remove(1)
print(a)


list_only_num=["joker","aaa"]
print(list_only_num.index("joker"))

a=[]
b=["a"]
c=["c"]
# a.append(["a"],["b"])
print(a)


a=["a",2,3,4,1,"a",3,4,1,1]
num = [i for i, x in enumerate(a) if x == "a"]
print(num)

top_field_card=[[["joker","joker"]]]
print(top_field_card[-1][-1][-1])

#関数内のの名前は同じじゃなくていいのか。
def A (choose_card) :
   print(choose_card)
CP_choose_card=1
A(CP_choose_card)


a=2
b=3
del a , b
a=3
b=4
print(a)
print(b)

Junni=1
def R() :
   global Akun,Junni
   Junni+=1
   Akun=Junni
def S() :
   global Akun,Junni
   Junni+=1
   Akun=Junni
R()
S()
print(Akun)




jyunni=10000
#BのaaaをAに持っていくためには、変数aaaをグローバル変数として定義する必要があり
def A():
    global aaa,jyunni,AA,BB
#     print(aaa)
    AA=jyunni

def B():
    global aaa,jyunni,AA,BB
    aaa = 1
    BB=jyunni
    jyunni+=1
#     print(jyunni)
    A()
B()
print(BB)
print(AA)



listA=[]
print(len(listA))

import random
print(random.randint(1,4))

three="03"
four="04"
five="05"
six="06"
seven="07"
eight="08"
nine="09"
ten="10"
eleven="11"
twelve="12"
thirteen="13"
#UNICODE的に1と2だけ大文字
one="One"
two="Two"
joker="joker" 
player1=[[two, "♠"], [four, "♦"], [eleven, "♥"], [one, "♦"], [eleven, "♠"], [joker, joker], [one, "♠"], [twelve, "♦"], [eleven, "♠"], [two, "♣"], [eight, "♥"], [six, "♣"], [seven, "♣"]]
print((random.choice(player1)))

#出した枚数が１～４枚の書く場合について、同じ数字なのかどうかをチェックする。ただし、jokerについても考慮する。
joker="joker"
choose_card=[['one', '♠'], ["one", "♠"],["one", "♠"],["one", "♠"]]
if (choose_card==1 )or (len(choose_card)==2 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2]))) \
 or (len(choose_card)==3 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2])))))) \
 or (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]) or ( (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
   or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
   or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])))))))) :
   print("ok")

choose_card=[['two', '♠'], ["two", "♠"],["one", "♠"],[joker, joker]]
if (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
   or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
   or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]))))):
   print("ok2")


a = [["joker", 'joker'], ["joker", 'joker'], ["joker", 'joker']]
count_joker = a.count(["joker", 'joker'])
print(count_joker)

a = [["joker", 2], ["joker", 3], ["joker", 4]]
count_joker = a.count(["joker"])
print(count_joker)

choose_card=[['Two', '♠'], ['Two', '♣']]
print((choose_card[-1][-2]==choose_card[-2][-2]))

three="03"
four="04"
five="05"
six="06"
seven="07"
eight="08"
nine="09"
ten="10"
eleven="11"
twelve="12"
thirteen="13"
#UNICODE的に1と2だけ大文字
one="One"
two="Two"
joker="joker" 
#下記Teruになって大小の比較ができる。革命時とイレブンバックの時はFalseで処理するようにすればいいし。
print("09"<"10"<"11"<"12"<"13"<"One"<"Two"<"joker")
print(three<four<five<six<seven<eight<nine<ten<eleven<twelve<thirteen<one<two<joker)

print(("13"<"One"<"Two"<"joker"))
print("---------------")
#UNICODEで等式がすべて成り立つように、かつ数字が一目でわかるようにするのは無理だ。→すうじにするしかない
"three"<"four"<"five"<"six"<"seven"<"eight"<"nine"<"ten"<"eleven"<"twelve"<"thirteen"<"one"<"two"<"joker"
print("Three"<"fOur")
print("fOur"<"FIVE")
print("Five"<"Six")
print("Six"<"seven")
print("seven"<"eight")
print("eight"<"nine")
print("nine"<"ten")
print("ten"<"eleven")
print("eleven"<"twelve")
print("twelve"<"thirteen")
print("thirteen"<"one")
print("one"<"two")
print("two"<"joker")


#UNICODE
four="four"
eleven="eleven"
four<eleven
print(four<eleven)


player1=[['two', '♠'], ['four', '♦'], ['seven', '♥'], ['one', '♦'], ['nine', '♠'], ['joker', 'joker'], ['one', '♠'], ['two', '♦'], ['eleven', '♠'], ['two', '♣'], ['eight', '♥'], ['six', '♣'], ['seven', '♣']]
a=player1[2]
print(a)
print(player1.index(a))
player1.pop(player1.index(a))
print(player1)


for i in range(7) :
    print(i)

list=[[1,2,3,4],[5,6,7,8,9]]
print(len(list[-1]))

# a=input("数字を入力してください:") 
# print(a)

flag=False
if flag==False : 
     for i in range(30) : 
      can_num_card=i    
      if can_num_card%6==0 :
           print(str(can_num_card)+"６の倍数")
      elif can_num_card%4==0 :
           print(str(can_num_card)+"４の倍数")
      else :
           print(str(can_num_card)+"該当なし")
             
field_card=[[[1,"♥"]],[[4,"♥"]]]
print(field_card[-1])
print(field_card[-1][-1])
print(field_card[-1][-1][-1])
print(field_card[-2])

top_field_card=[[1,"♥"]]
print(top_field_card[-1])
print(top_field_card[-1][-1])

field_card=[[[1,"♥"],[1,"♠"]],[[2,"♥"],[2,"♠"]]]
top_field_card=[[2,"♥"],[2,"♠"]]
print(top_field_card[-1])
print(top_field_card[-1][-1])
print(top_field_card[-2][-1])
# print(field_card[-1][-1][-1])

top_field_card=[[2,"♥"],["joker","joker"]]
print(("joker"or "A") in top_field_card[-1])

top_field_card.clear()
print(top_field_card)

# str(1)="a"
"one" < "two"
print("one"<"two")

field_card=[[["eleven","♥"],["eleven","♥"],["eleven","♥"]],[["joker","joker"],["eleven","♥"],["eleven","♥"]],[["eleven","♥"],["eleven","♥"],["eleven","♥"]]]
print(field_card.count("eleven"))
N=0
for i in range (54) :
   try :
    for k in range(4) :
      if field_card[i][k].count("eleven") : 
         N=N+1
   except :
      pass
print(N)

can_num_card=4
for i in range(can_num_card) :
   print(str(i)+"回目")


field_card=[]
def finish_turn (select_card) :
     field_card.append(select_card)
finish_turn([[2,"♥"],["joker","joker"]])
print(field_card)
num_field_card=len(field_card[-1]) 
print(num_field_card)

player1=[['two', '♠'], ['four', '♦'], ['seven', '♥'], ['one', '♦'], ['nine', '♠'], ['joker', 'joker'], ['one', '♠'], ['two', '♦'], ['eleven', '♠'], ['two', '♣'], ['eight', '♥'], ['six', '♣'], ['seven', '♣']]
for i in range(3) :
   print(player1[i][0]+player1[i][1])

# a=input("okと入力して")
# print(a=="ok")

# if True :
#    try :
#        a="test"
#    except :
#       pass
# print(a)

a=input("数字を入力してください")
int_a=int(a)

# #デッキの作成_N01
# num=["1","2","3","4","5","6","7","8","9","10","11","12","13","joker"]
# mark=["♥","♣","♦","♠"]
# # card=num[0]+mark[0]
# deck=[]
# for i in range(13) :
#     deck.append(num[i]+mark[0])
#     deck.append(num[i]+mark[1])
#     deck.append(num[i]+mark[2])
#     deck.append(num[i]+mark[3])
# deck.append(num[13]) #joker
# deck.append(num[13])
# print(deck)
# print(len(deck))
# #カードの評価をしづらいため没。大小比較で数字はintにしたいし、ルール的にも記号と分けたい。

#デッキの作成NO2 OK　これで行くーーーーーーーーーーーーーーーーーーー
# card1=[1,"♠"]
#数字はstrで表記する。３が最弱で２が一番強くするため
num=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen"]
"three"<"four"<"five"<"six"<"seven"<"eight"<"nine"<"ten"<"eleven"<"twelve"<"thirteen"<"one"<"two"<"joker"
mark=["♥","♣","♦","♠"]
deck=[]
# card.append(num[0])
# card.append(mark[0])
# print(card)
for i in range(13) :
    for k in range(4) :
        card=[]
        card.append(num[i])
        card.append(mark[k])
        deck.append(card)
deck.append(["joker","joker"])
deck.append(["joker","joker"])
print(deck)
print(len(deck))

#カードをデッキからplayer１に１３枚ランダムに配る。ーーーーーーーーーーーーーーーーー
import random
player1=[]

#deckから取り出したカードをdeckから削除したい、だから取り出したカードがデッキから何番目の要素なのかを追いたい。
#()popでもいい気がするけど。

#下記処理だと、 繰り返ししていくと例えば後半で５０の数字が[49]番目に入っているわけではないのでエラー起きるから没。
# try_num=[]
# for i in range (1,55) :
#     try_num.append(i)
# for i in range(13) : 
#      #deckの何番目のカードを取り出すか。
#      Num=random.choice(try_num)
#      del try_num[Num-1]
#      print(try_num)
#      print(Num)
#      card=deck[Num-1]  #0番目、１番目と数えるため
#      del deck[Num-1]
#      print(deck)#取り出したカードがdeckから消えているか確認
#      print(card)
#      #Num番目の数字がdeck[]の数字とマークあっていればOK
#      player1.append(card)
# print(player1)

# カードを適当に選んでplayer1に渡す。デッキからそのカードを消す。１３回繰り返すーーーーーーーーーーーーーー
# カードを選ぶ
for i in range(13) :
     card=random.choice(deck)
     print(card)
     # 何番目の要素か
     index=deck.index(card)
     print(index)
     # その要素を消す
     del deck[index]
     print(deck)
     player1.append(card)
print(player1)

#player2に１３枚カードを渡す。
player2=[]
for i in range(13) :
     card=random.choice(deck)
     index=deck.index(card)
     del deck[index]
     player2.append(card)
print(player2)

#player3に14枚カードを渡す。
player3=[]
for i in range(14) :
     card=random.choice(deck)
     index=deck.index(card)
     del deck[index]
     player3.append(card)
print(player3)

#player4に１4枚カードを渡す。
player4=[]
for i in range(14) :
     card=random.choice(deck)
     index=deck.index(card)
     del deck[index]
     player4.append(card)
print(player4)

print(deck)

#フィールド（場に出てる）カードを読み取る。----------------------------------------------------------------
# ここで、フィールドにどういう縛りが発生しているかを識別して、手札を出す時にそのルールを持ち込む。
field_card=[]
kakumei=1 #通常時１。kakumei=2nのとき革命中にすればいい。

def finish_turn(demo) : #でもで用意。手札出した後の処理につかう。
     pass

#（１）カードが何枚出てるか。また、４枚以上出た場合は革命が発動するとする。
# fieldには[]で格納している。例えば、2を3枚出したら、field=[ [[1,♠],[1,♣],[1,♥]] ]となり、len(field[0])=3となる。３枚出ていることがわかる。
num_field_card=len(field_card[-1]) #最後に格納されている数字でいい。
if num_field_card==1 :
     can_num_card=1
if num_field_card==2 :
     can_num_card=2
if num_field_card==3 :
     can_num_card=3
if num_field_card==4 :
     can_num_card=4
     kakumei=kakumei+1 #革命。あとで2%==0かどうかで偶数、奇数判別して2nが革命中とする。
if num_field_card==5 :
     can_num_card=5
     kakumei=kakumei+1 #革命
if num_field_card==6 :
     can_num_card=6
     kakumei=kakumei+1 #革命
if num_field_card==0 : #何もない状態
     can_num_card >= 0

#(2)マークの縛りがあるかどうか。num_field_cardが１枚以上のときは前後のマークの合致判断。さらに２枚以上のときは出されたカードが全部同じマークかの合致判断。
if can_num_card==1 :
     #field_card=[[[1,♥]],[[4,♥]]]という想定
     try :#初手の場合はpre_field_cardがないため。
          top_field_card=field_card[-1] #[[1,♥]]
          pre_field_card=field_card[-2] #[[4,♥]]
          if top_field_card[-1][-1] == pre_field_card[-1][-1] :
               shibari=1 #縛りあり
          else :
               shibari=0 #縛りなし
     except :
         pass
if can_num_card == 2 :#２枚場にカードがあるとき。出されたカードが全部同じマーク or 前に出されたカードのマークの種類と数と先頭のそれが同じどうかのチェック。(joker注意)
     #field_card=[[[1,♥],[1,♠]],[[2,♥],[2,♠]]]
     top_field_card=field_card[-1] #[[2,♥],[2,♠]]
     # pre_field_card=field_card[-2] #[[1,♥],[1,♠]]
     #出されたカードがすべて同じマーク
     if top_field_card[-1][-1] == top_field_card[-2][-1] : #[2,♥]と[2,♠]のマークが同じかどうかの判断
           shibari=1 #縛りあり
     #jokerがあるかどうかの判断。Trueだったらelifが機能する。
     elif "joker" in top_field_card[-1] or "joker" in top_field_card[-2] :
          shibari=1  #縛りあり
     else :
          shibari=0 #縛りなし

     #前に出されたカードのマークの種類と数と先頭のそれが同じ . [[[1,♥],[1,♠]],[[2,♥],[2,♠]]]
     #一手目の時はpre_field_cardがないのでエラー起きるので回避する。
     try:
          pre_field_card=field_card[-2] #[[1,♥],[1,♠]]
          if (top_field_card[-1][-1] == pre_field_card[-1][-1] or top_field_card[-1][-1] == pre_field_card[-2][-1]) \
          and (top_field_card[-2][-1] == pre_field_card[-1][-1] or top_field_card[-2][-1] == pre_field_card[-2][-1]) :
               shibari=1 #縛りあり
          #２枚だしてそのうちの１枚がjokerでかつもう一枚がその前のカードのどちらかとマークが一緒だった場合は縛りとなる。
          elif ("joker" in top_field_card[-1] or "joker" in top_field_card[-2]) and \
               ((top_field_card[-1][-1] or top_field_card[-2][-1]) in pre_field_card[-1] or (top_field_card[-1][-1] or top_field_card[-2][-1]) in pre_field_card[-2]) :
               shibari=1 #縛りあり
          else :
               shibari=0 #縛り無し
     except :
         pass
#★要追加記述↓★3枚、4枚、5枚についても記述する。（６枚はjokerが２枚使われていることになるので存在しえない）

#（３）8を出したら８流し。最大６枚出すパターンがあるため、すべての通りについて８があったら８流しをするようにする。
#例)top_field_card=[["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"]]
try :
     if ("eight" in top_field_card[-1]) :             
          top_field_card.clear() 
          #イレブンバックも解除
          eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
except :
     pass
try :
     if ("eight" in top_field_card[-2]) :             
          top_field_card.clear() 
          #イレブンバックも解除
          eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
except :
     pass
try :
     if ("eight" in top_field_card[-3]) :             
          top_field_card.clear() 
          #イレブンバックも解除
          eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
except :
     pass
try :
     if ("eight" in top_field_card[-4]) :             
          top_field_card.clear() 
          #イレブンバックも解除
          eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
except :
     pass
try :
     if ("eight" in top_field_card[-5]) :             
          top_field_card.clear() 
          #イレブンバックも解除
          eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
except :
     pass
try :
     if ("eight" in top_field_card[-6]) :             
          top_field_card.clear() 
          #イレブンバックも解除
          eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
except :
     pass

#(4)イレブンバック。場に出ている１１の数で判断。通常時がeleven_back=0 奇数のときイレブンバックが発動
#field_card=[[["eleven","♥"],["eleven","♥"],["eleven","♥"]],[["joker","joker"],["eleven","♥"],["eleven","♥"]],[["eleven","♥"],["eleven","♥"],["eleven","♥"]]]
kazu_field_eleven=0
#iターン数のセットだけカードがでていて、それぞれはk枚のセットであるということ。総当たり
for i in range (54) :
   try :
    for k in range(can_num_card) :#場に、ひとりひとりが何枚のカードを出しているか。(top_field_cardは何枚のカードか)
      if field_card[i][k].count("eleven") : 
         kazu_field_eleven+=1
   except :
      pass
if kazu_field_eleven %2 != 0 :
     eleven_back=1 #イレブンバック発動中
else :
     eleven_bacK=0 #kazu_eleven_backが偶数のとき、イレブンバックは発動していない

#(5)数字の大きさの評価と、イレブンバック。　革命中（kakumei=偶数の時）は逆になる。
#手札を出すときの出せるカードはTrueの時に出せるという風にすればよい。
if kakumei%2 != 0 : #奇数のとき。通常時
     if  eleven_back==0 : #イレブンバック起きてない
       "three"<"four"<"five"<"six"<"seven"<"eight"<"nine"<"ten"<"eleven"<"twelve"<"thirteen"<"one"<"two"<"joker"
     elif eleven_back==1 : #イレブンバック中
       "two"<"one"<"thirteen"<"twelve"<"eleven"<"ten"<"nine"<"eight"<"seven"<"six"<"five"<"four"<"three"<"joker"
elif kakumei%2 == 0 : #革命中
     if  eleven_back==0 : #イレブンバック起きてない
       "two"<"one"<"thirteen"<"twelve"<"eleven"<"ten"<"nine"<"eight"<"seven"<"six"<"five"<"four"<"three"<"joker"
     elif eleven_back==1 : #イレブンバックが起きているとき
       "three"<"four"<"five"<"six"<"seven"<"eight"<"nine"<"ten"<"eleven"<"twelve"<"thirteen"<"one"<"two"<"joker"
#★★上記を関数にして毎回呼び出して、毎回評価定義する。
"""
（例）
#field_card=[]
# def finish_turn (select_card) :
#      field_card.append(select_card)
# finish_turn([[2,"♥"],["joker","joker"]])
# print(field_card)"""



#PCの手札を選択するための関 数 ↓-------------------------------------------------------
#縛り的にも枚数的にも数の評価的にも出せるカードがどうかを判別→出せる（TRUE）なら条件処理（finish_card)次のプレイヤーへ					
#（１）数字の大小の評価。上記finish_cardで条件分岐によって数字の大きさが評価されているので、それに則って手札を出したときにＴｒｕｅなのかを判断する。
#下で選んだカード（choose_card）が出せるのか判断
def daseruka_hanndann(choose_card) :
    global flag
    if field_card != [] :#フィールドにすでにカードが出ている状態。
        pre_field_card=field_card[-1] #[[1,"♠"]] 先頭に出ているカード
        #ここの判別はルール関数で革命中かイレブンバック中か否かで全通り数字の大小を定義している。どのパターンでも>,<で評価できるようにしている。基本大きいもの(>)をだせていればいい。
        hannbetu=choose_card[-1][-2] > pre_field_card[-1][-2] #今回階段で出すのはなしだからどれか一枚だけの数字の評価で十分
    
    #判別（数の大小）がTrueか、フィールドにカードが出ていない場合は無条件で出せるため。
    if (hannbetu == True) or (field_card==[]) :
         print("そのカードは出せます。カードを出しました")
         flag=True
         #次のプレイヤーにかかる条件をルール関数で定義しなおす。
         finish_turn(choose_card) 

    else : #数字の大小の評価、Falseの場合　。
         print("そのカードは出せません。もう一度選んでください。")
         flag=False #また手札を出すところのループから抜け出していない。


# 自分の手札を選ぶ。自分が出すときだけ使う関数。
flag = False
your_tehuda=[]
while flag==False :
    tt=0
    for i in range(15) : 
       try :
          your_tehuda.append(player1[i][0]+player1[i][1])
          tt+=1
       except :
             pass   
             flag=True    
    print("あなたの手札は ",your_tehuda)
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    for i in range(tt) :
      print(i,":",your_tehuda[i]) #プレイヤーに選んでもらうためにわかりやすく手札を表示。半角数字によって何を出すかを判断させる。
    choose_card=[]#daseruka_hanbetu関数のために[[],[].[]]の形にしないといけないため・
    try :
       choice1=input("1枚目出すカードを選んでください(半角数字)パスならpassを入力") #10：eight♥で10を入力したら８♥を出したことになる。
       #passの場合は自分の手札選びを中断させてCPのターンにする処理を書かないと
       choose_card.append(player1[choice1])
       choice2=input("２枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
       if choice2 != "ok" : #２枚目を出すという意思表示
         choose_card.append(player1[choice2])
         choice3=input("３枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
         if choice3 != "ok" :
             choose_card.append(player1[choice3])
             choice4=input("４枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
             if choice4 != "ok" :
                choose_card.append(player1[choice4])
                choice5=input("５枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
                if choice5 != "ok" :
                    choose_card.append(player1[choice5])
                    choice6=input("６枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
                    if choice6 != "ok" :
                        choose_card.append(player1[choice6])
       else : 
           # このchoose_cardは([[2,"♥"],["joker","joker"]]な感じになってるはず。daseruka_handann関数で出せるかどうかを判断する。
           print("あなたが選んだカードは、",choose_card,"です。") 
           daseruka_hanndann(choose_card)


    except :
        daseruka_hanndann(choose_card)
        pass
        #変な入力になったら、そのままdaseruka_hannbetu()でエラー起こさせればいいか。出せない手札を選択したらflag=Falseのままでずっと続くはず。
#-----------------------------------------------------------



# 自分の手札から手札を選択する。手札を出す＝field_card[]に[[],[]]というリスト型で格納するということ---------------------------------
flag=False
if flag==False :
     your_card=input("出すカードを選んでください：") 
     # 出せる枚数の分岐（条件は上記fieldより持ち込む）条件に該当しない数字はその時の選択の時は、リストからその要素から消すか？
     if can_num_card==1 :
          #縛りのルールの有無。
          if shibari==1 :
               print("縛りあり")
          elif shibari==0 :
               print("縛りなし")



     elif can_num_card==2 :
          pass
     elif can_num_card==3 :
          pass
     elif can_num_card==4 :
          pass 
     elif can_num_card==5 :
          pass
     elif can_num_card==6 :
          pass
     else :
          can_num_card==0




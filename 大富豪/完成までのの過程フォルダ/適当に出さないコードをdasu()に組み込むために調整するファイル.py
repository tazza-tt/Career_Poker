import random

#【変数の定義】----------------------------------------------------------------------------------------------------------
field_card=[]
kakumei=1#奇数で通常時、偶数で革命中
shibari=0 #０で縛りなし、１で縛りあり
eleven_back=0#偶数で通常時、奇数でイレブンバック中
pass_kosuu=0 #パスが３つになったらfield_card.clear()をする
jyunni=1 #順位。抜けるたびに＋１していく。
agatteru_ninnzuu=0 #上がってる人数に合わせて、pass_kosuuが１～３でフィールドリセットされるかを判断するため。
agatteruka_p1=0
agatteruka_p2=0
agatteruka_p3=0
agatteruka_p4=0
p1_agari=False #上がったらTrueにしてplayer1＿dasuの処理を止めるため
p2_agari=False
p3_agari=False
p4_agari=False
eight_nagasi=False #8流ししたら次回も自分のターンにするようにするため
#------------------------------------------------------------------------------------------------------------------------


#【手札を配る】----------------------------------------------------------------------------------------------------------
#文字の大小を比較するに当たって fourとかは UNICODEで比較されてる可能性あり
# だからUNICODE対策で1桁には数字0をたした。１はOneみたいに大文字にしてjokerを一番大きくなるように定義しておく。2,も同様。
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
#下記Trueになって大小の比較ができる。革命時とイレブンバックの時はFalseで処理するようにすればいいし。
# print(three<four<five<six<seven<eight<nine<ten<eleven<twelve<thirteen<one<two<joker)
#→True.問題なし


#全通りのカードの組み合わせを作る。
num=[one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen]
mark=["♥","♣","♦","♠"]
deck=[]
for i in range(13) :
    for k in range(4) : 
        card=[]
        card.append(num[i])
        card.append(mark[k])
        deck.append(card)
#jokerについてはマークないので手動で入れる。
deck.append([joker,joker])
deck.append([joker,joker])
print(deck)
print("")
print("デッキを",len(deck),"枚作成。これからカードを配ります。")
print("")

#カードをデッキからplayerにランダムに配る。----------------------------------
#player1に13枚カードを渡す。
import random
player1=[]
for i in range(13) :
     card=random.choice(deck)
     index=deck.index(card)
     del deck[index]
     player1.append(card)

#player2に13枚カードを渡す。
player2=[]
for i in range(13) :
     card=random.choice(deck)
     index=deck.index(card)
     del deck[index]
     player2.append(card)

#player3に14枚カードを渡す。
player3=[]
for i in range(14) :
     card=random.choice(deck)
     index=deck.index(card)
     del deck[index]
     player3.append(card)

#player4に１4枚カードを渡す。
player4=[]
for i in range(14) :
     card=random.choice(deck)
     index=deck.index(card)
     del deck[index]
     player4.append(card)

#それぞれにきちんと手札がわたってるか確認する。
print("あなたの手札は",player1)
print("player2の手札は",player2)
print("player3の手札は",player3)
print("player4の手札は",player4)
print("")
print("★ ★ ★ ★--------ゲーム開始--------★ ★ ★ ★")
print("")


def player2_check_kakumei() :
      global can_kakumei ,joker_maisuu,list_only_num,onzon_suuji,list_kakumei_onzon_suuji_with_index,list_tyouhuku_husegu,average_tehuda
      joker_maisuu=0
      can_kakumei=False
      list_only_num=[]
      onzon_suuji=[]
      list_kakumei_onzon_suuji_with_index=[]
      list_tyouhuku_husegu=[]
      #4枚以上でないと革命ができないため
      #フィールドカードが４枚の時、or フィールドカードが０枚の時に発動する。
      if len(player2)>=4 :
          list_tyouhuku_husegu=[]
          for i in range(len(player2)) :
               if (joker in player2[i]) :
                    joker_maisuu+=1
                #数字だけのリストをつくり、同じ数字の枚数を数えやすくした
               list_only_num.append(player2[i][0])
          print(list_only_num)
          if joker_maisuu==0 :
               onzon_suuji=[]
               for i in range(len(player2)) :
                    print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
                    if  list_only_num.count(list_only_num[i]) ==4 :
                         print(list_only_num[i],"を使って革命ができます")
                         num_index = [k for k, x in enumerate(list_only_num) if x == list_only_num[i]]
                         #該当するキーとなる数字は温存する数字としてキープしたいから把握しておく.
                         #何回も同じ数字が検出されて重複するのを防ぐために、list_tyouhuku_huseguを作った。また,onzon_suujiで判断してしまうと、余計な文字も一緒に格納されてしまうので回避した。
                         if ((list_only_num[i] not  in onzon_suuji) and ( list_only_num[i] not  in list_tyouhuku_husegu)): 
                                #重複を防ぐために一回リセットする。appendする前にリセット
                                onzon_suuji=[]
                                list_tyouhuku_husegu.append(list_only_num[i])
                                onzon_suuji.append(list_only_num[i])
                                listA=[]
                                listA.append(onzon_suuji)
                                listA.append(num_index)
                                #[[['03'], [0, 1, 2, 3]]]のようになる。03という数字を使うのであれば[0, 1, 2, 3]のインデックスの手札を出させればいい。
                                list_kakumei_onzon_suuji_with_index.append(listA)
                          #Cpが革命するかはここのcan_kakumeiで判断する。手札の数値の平均値が６以下に
                         can_kakumei = True

                         
          if joker_maisuu==1 :
               onzon_suuji=[]
               for i in range(len(player2)) :
                    print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
                    if  list_only_num.count(list_only_num[i]) >= 3 :
                         print(list_only_num[i],"を使って革命ができます")
                         num_index = [k for k, x in enumerate(list_only_num) if x == list_only_num[i]]
                         #jokerを使うからjokerのインデクスを入れる。
                         num_index.append(list_only_num.index('joker'))
                         #該当するキーとなる数字は温存する数字としてキープしたいから把握しておく。
                         if ((list_only_num[i] not  in onzon_suuji) and ( list_only_num[i] not  in list_tyouhuku_husegu)) : 
                                #重複を防ぐために一回リセットする。appendする前にリセット
                                onzon_suuji=[]
                                list_tyouhuku_husegu.append(list_only_num[i])
                                onzon_suuji.append(list_only_num[i])
                                listA=[]
                                listA.append(onzon_suuji)
                                listA.append(num_index)
                                #[[['03'], [0, 1, 2, 3]]]のようになる。03という数字を使うのであれば[0, 1, 2, 3]のインデックスの手札を出させればいい。
                                list_kakumei_onzon_suuji_with_index.append(listA)
                         can_kakumei = True
          if joker_maisuu==2 :
               onzon_suuji=[]
               for i in range(len(player2)) :
                    print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
                    #joker2枚あった時にjoker2枚あるが、ほかのカードが２枚あった場合は省かないといけない。
                    if  (list_only_num.count(list_only_num[i]) >= 2 and (list_only_num[i] != joker)  ) :
                         print(list_only_num[i],"を使って革命ができます")
                         num_index = [k for k, x in enumerate(list_only_num) if x == list_only_num[i]]
                     
                     #消したら、ループが崩れてエラー起きる。（消さないと同じ数字が重複して検出されちゃうからどうにかしたいのに。）
                     #     list_only_num = [item for item in list_only_num if item != list_only_num[i]]
                     #     print(list_only_num) 
          
                         #jokerは確定で２つあるから２つインデックスを抽出してappendする。
                         joker_index = [l for l, x in enumerate(list_only_num) if x == "joker"]
                         num_index.append(joker_index[0])
                         num_index.append(joker_index[1])
                         #該当するキーとなる数字は温存する数字としてキープしたいから把握しておく。
                         if ((list_only_num[i] not  in onzon_suuji) and (list_only_num[i] not  in list_tyouhuku_husegu)) : 
                                #重複を防ぐために一回リセットする。appendする前にリセット
                                onzon_suuji=[]
                                list_tyouhuku_husegu.append(list_only_num[i])
                                onzon_suuji.append(list_only_num[i])
                                listA=[]
                                listA.append(onzon_suuji)
                                listA.append(num_index)
                                #[[['03'], [0, 1, 2, 3]]]のようになる。03という数字を使うのであれば[0, 1, 2, 3]のインデックスの手札を出させればいい。
                                list_kakumei_onzon_suuji_with_index.append(listA)
                         can_kakumei = True

               #ここに該当する数字はなるべく使わないようにする。
               print(list_kakumei_onzon_suuji_with_index)

               #手札の平均値が7以下のとき、革命を行うようにしたい。
               #手札で"One"=1とか定義して、sum(list)でもいいんだけど、定義でバグる箇所出てくるからifで場合分けして手札の大きさを足していく。
               ookisa_tehuda=0
               for i in range(len(list_only_num)) :
                    #Oneは１として足す
                    if list_only_num[i]=="One" :
                      ookisa_tehuda=ookisa_tehuda+1
                    elif list_only_num[i]=="Two" :
                         ookisa_tehuda=ookisa_tehuda+2
                    #jokerは最強カードのため０として足す。
                    elif list_only_num[i]=="joker" :
                         ookisa_tehuda=ookisa_tehuda+0 
                    else:
                         ookisa_tehuda=ookisa_tehuda+int(list_only_num[i])
               #手札の大きさの平均値。手札の平均値が７よりちいさかったら革命してしまおう。２が最強だから相対的な数字の大きさにするべきだけど、目をつむっておく。(するとしたら各+2すればよいか？)
               average_tehuda=(ookisa_tehuda/len(list_only_num))
               if (can_kakumei==True) and (average_tehuda <= 7) :
                     #その手札を出す
                     #print(list_kakumei_onzon_suuji_with_index)の部分
                     print("革命をします")
                     pass
         #can_kakumeiがTrueかどうかが重要。上で、４枚同じ数字あればTrueになるようにしている。
          

# player2_check_kakumei()
# print(list_kakumei_onzon_suuji_with_index)

# if ((shibari==0) and (len(field_card[-1])==1)) :
#     list_daseru_mark=[]
#     #フィールドカードのマークを抽出
#     field_mark=field_card[-1][-1][-1]
#     for i in range(len(player2)) :
#          tehuda_mark_syutoku=player2[i][-1]
#          #同じマークだった場合
#          if field_mark == tehuda_mark_syutoku :
#               kazu=player2[i][-2]
#               sono_mark_index=i
#               listA=[]
#               listA.append(kazu)
#               listA.append(sono_mark_index)
#               list_daseru_mark.append(listA)
#      #出す処理を書く.適当に出せるインデックスを出すようにする。
#      #list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
     
# #同じマーク→　[[(数字の大きさ),(そのカードを出すためのインデックス)]]という形で抽出される
# print("フィールドには",field_mark,"が出ています。そのマークで出せる候補の数字とインデックスは",list_daseru_mark,"です。")

player2= [['09', '♣'], ['05', '♠'], ['One', '♥'], ['11', '♣'], ['joker', 'joker'], ['joker', 'joker'], ['12', '♥'], ['09', '♦'], ['03', '♣'], ['11', '♥'], ['11', '♣'], ['07', '♦'], ['Two', '♦']]

def check_pea_player2() :
          global  list_onzon_suuji_with_index_pea_3mai,list_onzon_suuji_with_index_pea_2mai,joker_index_3mai,joker_index_2mai
          # can_kakumei=False
          list_only_num=[]
          onzon_suuji=[]
          joker_maisuu=0
          onzon_suuji_pea_3mai=[]
          list_onzon_suuji_with_index_pea_3mai=[]
          list_onzon_suuji_with_index_pea_2mai=[]
          joker_index_3mai=[]
          joker_index_2mai=[]
          list_tyouhuku_husegu=[]
          tt=0

          for i in range(len(player2)) :
               list_only_num.append(player2[i][0])
          #2枚以上じゃないとペアができないため。
          if len(list_only_num) >= 2 :
               
               for i in range(len(list_only_num)) :
                    if (joker in player2[i] ) :
                       joker_maisuu+=1
               print("jokerの枚数は",joker_maisuu,"枚です。")

               #joker枚数が２枚の時
               if joker_maisuu == 2 :
               #joker_index=[2,3]２，３とあと一枚好きな数字出せば３枚のペアができる。
                  joker_index_3mai= [n for n, x in enumerate(list_only_num) if x == joker]
                  print(joker_index_3mai,"の要素を使ってあと一枚だせば３枚のペアをだせます。")

                  #jokerを使わないで２枚、３枚出せるものを抽出する。 
                  for i in range(len(player2)) :
                         onzon_suuji=[]
                         print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
                         #jokerなしで純粋な同じ数３枚 .ただしそのカードがjokerではないとする。 
                         if (list_only_num.count(list_only_num[i]) == 3  and (list_only_num[i] != joker)):
                              onzon_suuji.append(list_only_num[i])
                              #ループのため、重複で同じ数字を入れるのを防ぐため。
                              if (list_only_num[i] not in list_tyouhuku_husegu) :
                                   list_tyouhuku_husegu.append(list_only_num[i])
                                   listA=[]
                                   num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
                                   listA.append(onzon_suuji)
                                   listA.append(num)
                                   #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
                                   list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
                         #jokerなしで純粋に同じ数字が２枚ある場合。ただしそのカードがjokerではないとする。
                         if  (list_only_num.count(list_only_num[i]) == 2 and (list_only_num[i] != joker)) :
                              onzon_suuji.append(list_only_num[i])
                              if (list_only_num[i] not in list_tyouhuku_husegu) :
                                   list_tyouhuku_husegu.append(list_only_num[i])
                                   listA=[]
                                   num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
                                   listA.append(onzon_suuji)
                                   listA.append(num)
                                   #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
                                   list_onzon_suuji_with_index_pea_2mai.append(listA)



               #joker枚数が１枚のとき
               if joker_maisuu == 1 :
                    num_index_joker=list_only_num.index(joker)
                    for i in range(len(player2)) :
                         #ここでonzon_suujiをリセットしておかないと、重複してはいってしまう。
                         onzon_suuji=[]
                         print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
                         #joker1枚、ペア２枚。それを使った３枚のペアの作り方を抽出する。
                         #list_onzon_suuji_with_index_pea_3mai=[[One],[2,3,4]]とかで抽出するのがゴール

                         if list_only_num.count(list_only_num[i])==2 :
                              onzon_suuji.append(list_only_num[i])
                              #tyouhuku_huseguで一度入った数字は入れないようにする。
                              if (list_only_num[i] not in  list_tyouhuku_husegu) :
                                   list_tyouhuku_husegu.append(list_only_num[i])
                                   print(list_only_num[i],"とjoker使って3枚のペアが作れます。")
                                   print(list_only_num[i],"を使って2枚のペアが作れます。（jokerは使わない）")
                                   listA=[]
                                   #jokerを使わない2枚ペア用
                                   listB=[]
                                   #listB用。
                                   num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
                                   #listA用。同じやつつかってるとバグるからnum_2として分ける。
                                   num_2= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]

                                   #jokerを含めないインデックスだけ先にlistBにapendしておく必要がある。３枚ペアと２枚ペアで区別するために。
                                   listB.append(onzon_suuji)
                                   listB.append(num)

                                   #jokerを含めたインデックス.3枚ペア用.jokerのインデックスをいれる
                                   num_2.append(num_index_joker)
                                   listA.append(onzon_suuji)
                                   listA.append(num_2)

                                   #jokerをいれた３枚のペアのためのインデックス
                                   list_onzon_suuji_with_index_pea_3mai.append(listA)
                                   #jokerを入れないで純粋な２枚のペアのためのインデックス
                                   list_onzon_suuji_with_index_pea_2mai.append(listB)

                                   print(list_onzon_suuji_with_index_pea_3mai)
                                   print(list_onzon_suuji_with_index_pea_2mai)

                         #３枚同じカードがある場合。→　1枚のjokerと３枚の同じカードだから革命のほうでも拾えてるか。そのときどうせ革命優先するんだから必要ないか
                         #  if list_only_num.count(list_only_num[i])==3 :
                              
                         #joker1枚と数字１枚のとき、２ペアができる。
                         if list_only_num.count(joker)==1 :
                         #jokerのインデックスのみ。これとあと1枚好きな数字出せば、２ペアができる。
                            tt=tt+1
                         #一回しか処理されないようにした
                         if tt == 1 :
                              joker_index_2mai.append(num_index_joker) 
               
               #jokerの枚数が０のとき
               if joker_maisuu== 0 :
                    for i in range(len(player2)) :
                         onzon_suuji=[]
                         print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
                         #jokerなしで純粋な同じ数所３枚
                         if list_only_num.count(list_only_num[i]) == 3 :
                              onzon_suuji.append(list_only_num[i])
                              #ループのため、重複で同じ数字を入れるのを防ぐため。
                              if (list_only_num[i] not in list_tyouhuku_husegu) :
                                   list_tyouhuku_husegu.append(list_only_num[i])
                                   listA=[]
                                   num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
                                   listA.append(onzon_suuji)
                                   listA.append(num)
                                   #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
                                   list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
                         #jokerなしで純粋に同じ数字が２枚ある場合。
                         if  list_only_num.count(list_only_num[i]) == 2 :
                              onzon_suuji.append(list_only_num[i])
                              if (list_only_num[i] not in list_tyouhuku_husegu) :
                                   list_tyouhuku_husegu.append(list_only_num[i])
                                   listA=[]
                                   num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
                                   listA.append(onzon_suuji)
                                   listA.append(num)
                                   #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
                                   list_onzon_suuji_with_index_pea_2mai.append(listA)
          print("ジョーカー2枚のインデックスは",joker_index_3mai)
          #ジョーカー2枚のインデックスは []
          print("ジョーカー１枚のインデックスは",joker_index_2mai)
          #ジョーカー１枚のインデックスは [12, 12, 12]
          print("3枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_3mai)
          #3枚のペアを出せるその数字とインデックスは [[['11'], [3, 9, 10]]]
          print("ジョーカーを使わず2枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_2mai)
          #ジョーカーを使わず2枚のペアを出せるその数字とインデックスは [[['09'], [0, 7]]]




check_pea_player2()
print(list_onzon_suuji_with_index_pea_2mai)


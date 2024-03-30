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
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


#【手札を出した後の読み込み処理→その条件が次プレイヤーに引き継がれる】ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

def finish_turn (select_card) :
     field_card.append(select_card) #関数処理はここだけで下記はただ評価するだけか。
     #一番最後にだしたカードを取得。枚数とその内訳を取得している。
     top_field_card=field_card[-1]

     global kakumei ,shibari,eleven_back,pass_kosuu,my_turn,eight_nagasi

     #（１）カードが何枚出てるか。また、４枚以上出た場合は革命が発動するとする。
     # fieldには[]で格納している。例えば、2を3枚出したら、field=[ [[1,♠],[1,♣],[1,♥]] ]となり、len(field[0])=3となる。３枚出ていることがわかる。
     num_field_card=len(field_card[-1]) #最後に格納されている数字でいい。
     if num_field_card==1 :
          can_num_card=1
          print("次ターンで1枚だけだしてください")
     if num_field_card==2 :
          can_num_card=2
          print("次ターンで2枚出してください")
     if num_field_card==3 :
          print("次ターンで3枚出してください")
          can_num_card=3
     if num_field_card==4 :
          print("次ターンで4枚出してください")
          can_num_card=4
          kakumei=kakumei+1 #革命。あとで2%==0かどうかで偶数、奇数判別して2nが革命中とする。
     if num_field_card==5 :
          print("次ターンで5枚出してください")
          can_num_card=5
          kakumei=kakumei+1 #革命
     if num_field_card==6 :
          print("次ターンで6枚出してください")
          can_num_card=6
          kakumei=kakumei+1 #革命
     if num_field_card==0 : #何もない状態
          print("次ターンでは好きな枚数出せます")
          can_num_card >= 0

     #(2)マークの縛りがあるかどうか。num_field_cardが１枚以上のときは前後のマークの合致判断。さらに２枚以上のときは出されたカードが全部同じマークかの合致判断。
     if can_num_card==1 :
          try :#初手の場合はpre_field_cardがないため。
               #field_card=[[[1,♥]],[[4,♥]]]という想定
               top_field_card=field_card[-1] #[[1,♥]]
               pre_field_card=field_card[-2] #[[4,♥]]
               #先頭のカードと、出したカードが同じマークかどうか
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
          elif joker in top_field_card[-1] or joker in top_field_card[-2] :
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
               elif (joker in top_field_card[-1] or joker in top_field_card[-2]) and \
                    ((top_field_card[-1][-1] or top_field_card[-2][-1]) in pre_field_card[-1] or (top_field_card[-1][-1] or top_field_card[-2][-1]) in pre_field_card[-2]) :
                    shibari=1 #縛りあり
               else :
                    shibari=0 #縛り無し
          except :
              pass
     #★要追加記述↓★3枚、4枚、5枚についても記述する。（６枚はjokerが２枚使われていることになるので存在しえない）

     #（３）8を出したら８流し。最大６枚出すパターンがあるため、すべての通りについて８があったら８流しをするようにする。
     #[[eight,""],[eight,""]]で２枚出した時２回「8流し発動」してしまうから、orで１枚目もしくは２枚目に出てた時に１回だけ表示されるようにする。
     try : #８を２枚出しした時に備える。
         if ((eight in top_field_card[-1]) or (eight in top_field_card[-2])) :  
             print("")  
             print("8流し発動!")         
             field_card.clear() 
             #イレブンバックも縛りも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
             shibari=0
             #８流し関数をTrueにすることでまたplayer〇_dasu()が機能してまた自分がカードを出せるようにする。
             eight_nagasi=True
     except :
         pass
     #2枚目に[eight,""]があった時。
    #  try :
    #      if (eight in top_field_card[-2]) :
    #          print("")
    #          print("8流し発動!")             
    #          field_card.clear() 
    #          #イレブンバックも縛りも解除
    #          eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
    #          shibari=0
    #          #８流し関数をTrueにすることでまたplayer〇_dasu()が機能してまた自分がカードを出せるようにする。
    #          eight_nagasi=True
    #  except :
    #      pass
    #3枚目に出ていた時
     try :
         if (eight in top_field_card[-3]) :   
             print("")  
             print("8流し発動!")        
             field_card.clear() 
             #イレブンバックも縛りも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
             shibari=0
             #８流し関数をTrueにすることでまたplayer〇_dasu()が機能してまた自分がカードを出せるようにする。
             eight_nagasi=True
     except :
         pass
     try :
         if (eight in top_field_card[-4]) :  
             print("")   
             print("8流し発動!")        
             field_card.clear() 
             #イレブンバックも縛りも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
             shibari=0
             #８流し関数をTrueにすることでまたplayer〇_dasu()が機能してまた自分がカードを出せるようにする。
             eight_nagasi=True
     except :
         pass
     try :
         if (eight in top_field_card[-5]) :    
             print("")
             print("8流し発動!")         
             field_card.clear() 
             #イレブンバックも縛りも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
             shibari=0
             #８流し関数をTrueにすることでまたplayer〇_dasu()が機能してまた自分がカードを出せるようにする。
             eight_nagasi=True
     except :
         pass
     try :
         if (eight in top_field_card[-6]) :
             print("")
             print("8流し発動!")             
             field_card.clear() 
             #イレブンバックも縛りも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
             shibari=0
             #８流し関数をTrueにすることでまたplayer〇_dasu()が機能してまた自分がカードを出せるようにする。
             eight_nagasi=True
     except :
         pass

     #(4)イレブンバック。場に出ている１１の数で判断。通常時がeleven_back=0 奇数のときイレブンバックが発動
     #field_card=[[[eleven,"♥"],[eleven,"♥"],[eleven,"♥"]],[[joker,joker],[eleven,"♥"],[eleven,"♥"]],[[eleven,"♥"],[eleven,"♥"],[eleven,"♥"]]]
     kazu_field_eleven=0
     #iターン数のセットだけカードがでていて、それぞれはk枚のセットであるということ。総当たり
     for i in range (54) :
        try :
         for k in range(can_num_card) :#場に、ひとりひとりが何枚のカードを出しているか。(top_field_cardは何枚のカードか)
           if field_card[i][k].count(eleven) : 
              kazu_field_eleven+=1
        except :
           pass
     if kazu_field_eleven %2 != 0 :
          eleven_back=1 #イレブンバック発動中
     else :
          eleven_bacK=0 #kazu_eleven_backが偶数のとき、イレブンバックは発動していない

     print("-------------------------------------------")
     print("")
     print("フィールドのカードは,",field_card)
     #自分のターンだけ出せるカードの詳細がprintされるようにした
     if my_turn==True :
        if shibari==0 :
            print("■マークの縛りはありません")
        if shibari==1 :
            print("■マークは縛られています")
        if kakumei %2 == 0 :
            print("■革命中です")
        if kakumei %2 != 0 :
            print("■革命中ではありません")
        if eleven_back == 0 :
            print("■イレブンバック中ではありません")
        if eleven_back == 1 :
            print("■イレブンバック中です")
     print("")
     print("-------------------------------------------")
     pass_kosuu=0


#【手札を出せるのかの判断】ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

#下のplayer〇_dasu()それぞれで選んだカード（choose_card）が出せるのか判断

#自分が出したカードがだせるのかの判断。出せなかったらもう一度player1_dasu()で出させる。
def daseruka_hanndann(choose_card) :
    #daseruka_hanndannにint_choice1等を送るためにはこっちにもグローバルをしておく必要があるみたい
    global int_choice1,int_choice2,int_choice3,int_choice4,int_choice5,int_choice6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,my_turn,eight_nagasi
    global flag 
    #自分のターンだけ出せるカードの詳細がfinish_turnでprintされるようにしたいから.TRueのとき表示される。
    my_turn=False
    #８流し関数はここで一回Falseに戻す。finish_turnでまたeight_nagasiのTrue、False判断するし。
    eight_nagasi=False

    # ここから下４行必要ないかも。
    # if len(field_card) != 0 :#フィールドにすでにカードが出ている状態。個数が0ではない場合 
    #     pre_field_card=field_card[-1] #[[1,"♠"]] 先頭に出ているカード
    #     #ここの判別はルール関数で革命中かイレブンバック中か否かで全通り数字の大小を定義している。どのパターンでも>,<で評価できるようにしている。基本大きいもの(>)をだせていればいい。
    #     hannbetu=choose_card[-1][-2] > pre_field_card[-1][-2] #今回階段で出すのはなしだからどれか一枚だけの数字の評価で十分
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
        #   print(field_card)    #問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            print("選んだカードの数字は",choose_card[-1][-2])
            print("場に出ているカードは",field_card[-1][-1][-2] )
            # print(choose_card[-1][-2] >field_card[-1][-1][-2]) #★ここがおかしい。Trueであってほしい eleven > fourでfalseになるのがおかしい。→UNICODE使ってる。解決済み         
            
            #★場に１枚しか出ていないとき。縛りだけ考える。----------------------------------------------------------------------------------------------------------
            if len(field_card[-1])==1 : #フィールドに１枚しかない場合。
               if shibari==1 : #縛りあり
                  if ((choose_card[-1][-1] ==field_card[-1][-1][-1]) or  ("joker" in choose_card[-1])) :#マークが同じじゃないといけない.それか出したカードがjoker
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。 
                            
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or ("joker" in choose_card[-1])) :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                             
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or ("joker" in choose_card[-1]))  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。
                  else :
                            print("そのカードは出せません。マークが違います。もう一度選んでください。")
                            print("---------------------------------------------")
                            flag=False #また手札を出すところのループから抜け出していない。                                            
               elif shibari== 0 :#縛りがない場合
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。 
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。
                            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                a=player1[int_choice1]
                                b=player1[int_choice2]
                                c=player1[int_choice3]
                                d=player1[int_choice4]
                                e=player1[int_choice5]
                                f=player1[int_choice6]
                            except Exception as e:
                                print("例外argsA:", e.args)
                                pass 
                            try :
                                player1.remove(a)
                                player1.remove(b)
                                player1.remove(c)
                                player1.remove(d)
                                player1.remove(e)
                                player1.remove(f)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player1,"です。")       
                            if len(player1)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                     
             #場に１枚のみでているところにカードを出す場合。縛りの有無で場合分け---------------------------------
            
            #２枚出しているとき。 出せないカード選択していたら出せませんってもうもう一度選ばされる。----------------------------------------------------------------------------------------
            if len(field_card[-1]) ==2 :           
                if (len(choose_card) == len(field_card[-1]) ==2) :
                    print("出すべき枚数はあってます。")
                    #出した２枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2])) :
                        print("そのペアは同じ数字できちんと出せています。")
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            # [['One', '♣'], ['joker', 'joker']]]　の[-1][-1][-2]から、絶対２枚だせなくなるため[-1][-2][-2]に勝っててもOKにする。
                            #choose_card[-1][-2]=jokerのとき大小の評価がバグるからそれは(choose_card[-1][-2] != 'joker')で排除。
                            if (((choose_card[-1][-2] >field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] >field_card[-1][-2][-2])and (choose_card[-1][-2] != 'joker')) ) :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] ) and (choose_card[-1][-2] != 'joker'))) :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (((choose_card[-1][-2] > field_card[-1][-1][-2] )and(choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] > field_card[-1][-2][-2] ) and (choose_card[-1][-2] != 'joker')))  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                

            #3枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==3 :           
                if (len(choose_card) == len(field_card[-1]) ==3) :
                    print("出すべき枚数はあってます。")
                    #出した3枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]))))) :  #★ここがエラー起きるかもしれない
                        print("そのペアは同じ数字できちんと出せています。")
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                                        

            #4枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==4 :           
                if (len(choose_card) == len(field_card[-1]) ==4) :
                    print("出すべき枚数はあってます。")
                    #出した4枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if  (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
                     or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
                     or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]))))) :  #★ここがエラー起きるかもしれない
                        print("そのペアは同じ数字できちんと出せています。")
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました。")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player1[int_choice1]
                                    b=player1[int_choice2]
                                    c=player1[int_choice3]
                                    d=player1[int_choice4]
                                    e=player1[int_choice5]
                                    f=player1[int_choice6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player1.remove(a)
                                    player1.remove(b)
                                    player1.remove(c)
                                    player1.remove(d)
                                    player1.remove(e)
                                    player1.remove(f)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player1,"です。")       
                                if len(player1)==0 :
                                    print("手札がなくなりました。あなたの抜けです。")
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                                            

 
       except Exception as e:
         print("例外args:C", e.args)
         print("そのカードは出せません。もう一度選んでください。")
         flag=False #また手札を出すところのループから抜け出していない。 
       
       # try :初手だから革命かどうかの場合は不要。
       if (len(field_card)==0) :          
          #複数枚だしているとき、それが同じ数字であればOK。もしくはjokerを含んでいれば。
          #1枚のとき、2枚の時,3枚のとき。４枚のとき
          #ジョーカーどうしで同じと認識にならないように、同じかどうかの判断時にjokerは外す。choose_card[-1][-2]==choose_card[-2][-2]!=joker
        if (len(choose_card)==1 )or (len(choose_card)==2 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2]))) \
         or (len(choose_card)==3 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2])))))) \
         or (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]) or ( (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
         or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
         or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])))))))) :

            print("そのカードは出せます。カードを出しました")
            #出したカードは手札から消す。
            #出したカードは手札から消す。
            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                a=player1[int_choice1]
                b=player1[int_choice2]
                c=player1[int_choice3]
                d=player1[int_choice4]
                e=player1[int_choice5]
                f=player1[int_choice6]
            except Exception as e:
                print("例外argD:", e.args)
                pass 
            try :
                player1.remove(a)
                player1.remove(b)
                player1.remove(c)
                player1.remove(d)
                player1.remove(e)
                player1.remove(f)
            except Exception as e:
                print("例外argsE:", e.args)
                pass                 
            print("カードを出した後のあなたの手札は",player1,"です。")
            if len(player1)==0 :
                print("手札がなくなりました。あなたの抜けです。")
            
            flag=True
            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
            finish_turn(choose_card)             
            # except :
            #      pass
        else :
         print("そのカードは出せません。もう一度選んでください。")
         print("---------------------------------------------")
         flag=False #また手札を出すところのループから抜け出していない。 
        

    except Exception as e: #数字の大小の評価、Falseの場合　。
        print("例外argsF:", e.args)
        print("そのカードは出せません。もう一度選んでください。")
        flag=False #また手札を出すところのループから抜け出していない。

#CP1用の関数。player2として、手札等を関数を書き換えないといけないので、それぞれの関数をCP3まで３作るって感じかな。
def daseruka_hanndann_CP1(choose_card) :
    global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player2,my_turn,player3,player4,eight_nagasi
    global flag 
    #自分のターンだけ出せるカードの詳細がfinish_turnでprintされるようにしたいから.TRueのとき表示される。
    #player3もplayer4もあがってたら次のターンが自分のターンのため
    if ((len(player3)==0) and (len(player4)==0)) :
       my_turn=True
    else :
        my_turn=False
    #８流し関数はここで一回Falseに戻す。finish_turnでまたeight_nagasiのTrue、False判断するし。
    eight_nagasi=False
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
          # print("フィールドのカードは",field_card)#問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            
            #★場に１枚しか出ていないとき。縛りだけ考える。----------------------------------------------------------------------------------------------------------
            if len(field_card[-1])==1 : #フィールドに１枚しかない場合。
               if shibari==1 : #縛りあり
                  if ((choose_card[-1][-1] ==field_card[-1][-1][-1] ) or ("joker" in choose_card[-1])) :#マークが同じじゃないといけない.それかjokerは出したとき。
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            #出したカードは手札から消す。
                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。 
                            
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
               
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
               elif shibari== 0 :#縛りがない場合
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                print(e.args)
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。 
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2]) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(CP_card_2)
                                player2.remove(CP_card_3)
                                player2.remove(CP_card_4)
                                player2.remove(CP_card_5)
                                player2.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                                     
             #場に１枚のみでているところにカードを出す場合。縛りの有無で場合分け---------------------------------
            
            #２枚出しているとき。 出せないカード選択していたら出せませんってもうもう一度選ばされる。----------------------------------------------------------------------------------------
            if len(field_card[-1]) ==2 :           
                if (len(choose_card) == len(field_card[-1]) ==2) :
                    #出した２枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2])) :
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            # [['One', '♣'], ['joker', 'joker']]]　の[-1][-1][-2]から、絶対２枚だせなくなるため[-1][-2][-2]に勝っててもOKにする。
                            if (((choose_card[-1][-2] >field_card[-1][-1][-2] ) and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] >field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] )and (choose_card[-1][-2] != 'joker')) ) :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')) ) :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (((choose_card[-1][-2] > field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] > field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                

            #3枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==3 :           
                if (len(choose_card) == len(field_card[-1]) ==3) :
                    #出した3枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]))))) :  #★ここがエラー起きるかもしれない
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                                        

            #4枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==4 :           
                if (len(choose_card) == len(field_card[-1]) ==4) :
                    #出した4枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if  (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
                     or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
                     or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]))))) :  #★ここがエラー起きるかもしれない
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[CP_card_2]
                                    c=player2[CP_card_3]
                                    d=player2[CP_card_4]
                                    e=player2[CP_card_5]
                                    f=player2[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(CP_card_2)
                                    player2.remove(CP_card_3)
                                    player2.remove(CP_card_4)
                                    player2.remove(CP_card_5)
                                    player2.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
         
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                            
       except Exception as e:
         flag=False #また手札を出すところのループから抜け出していない。 
       
       # try :初手だから革命かどうかの場合は不要。
       if ((len(field_card)==0) and (eight_nagasi==False)) :          
          #複数枚だしているとき、それが同じ数字であればOK。もしくはjokerを含んでいれば。
          #1枚のとき、2枚の時,3枚のとき。４枚のとき
          #ジョーカーどうしで同じと認識にならないように、同じかどうかの判断時にjokerは外す。choose_card[-1][-2]==choose_card[-2][-2]!=joker
        if (len(choose_card)==1 )or (len(choose_card)==2 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2]))) \
         or (len(choose_card)==3 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2])))))) \
         or (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]) or ( (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
         or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
         or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])))))))) :

            #出したカードは手札から消す。
            #出したカードは手札から消す。
            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                a=player2[CP_card_1]
                b=player2[CP_card_2]
                c=player2[CP_card_3]
                d=player2[CP_card_4]
                e=player2[CP_card_5]
                f=player2[CP_card_6]
            except Exception as e:
                pass 
            try :
                player2.remove(CP_card_1)
                player2.remove(CP_card_2)
                player2.remove(CP_card_3)
                player2.remove(CP_card_4)
                player2.remove(CP_card_5)
                player2.remove(CP_card_6)
            except Exception as e:
                pass 
            flag=True
            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
            print(choose_card,"を出しました。")
            finish_turn(choose_card)             
        else :
         flag=False #また手札を出すところのループから抜け出していない。 
    except Exception as e: #数字の大小の評価、Falseの場合　。
        flag=False #また手札を出すところのループから抜け出していない。

#CPのplayer3用の関数
def daseruka_hanndann_CP2(choose_card) :
    global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player3,my_turn,player4,eight_nagasi
    global flag 
    #自分のターンだけ出せるカードの詳細がfinish_turnでprintされるようにしたいから.TRueのとき表示される。
    #player3が上がってたら次のたーんが自分のターンのため。
    if len(player4)==0 :
      my_turn=True
    else :
        my_turn=False
    #８流し関数はここで一回Falseに戻す。finish_turnでまたeight_nagasiのTrue、False判断するし。
    eight_nagasi=False
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
          # print("フィールドのカードは",field_card)#問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            
            #★場に１枚しか出ていないとき。縛りだけ考える。----------------------------------------------------------------------------------------------------------
            if len(field_card[-1])==1 : #フィールドに１枚しかない場合。
               if shibari==1 : #縛りあり
                  if ((choose_card[-1][-1] ==field_card[-1][-1][-1] ) or ("joker" in choose_card[-1])) :#マークが同じじゃないといけない. それかjokerを出したとき
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            #出したカードは手札から消す。
                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。 
                            
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
               
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
               elif shibari== 0 :#縛りがない場合
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :

                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。 
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる.
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(CP_card_2)
                                player3.remove(CP_card_3)
                                player3.remove(CP_card_4)
                                player3.remove(CP_card_5)
                                player3.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                                     
             #場に１枚のみでているところにカードを出す場合。縛りの有無で場合分け---------------------------------
            
            #２枚出しているとき。 出せないカード選択していたら出せませんってもうもう一度選ばされる。----------------------------------------------------------------------------------------
            if len(field_card[-1]) ==2 :           
                if (len(choose_card) == len(field_card[-1]) ==2) :
                    #出した２枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2])) :
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (((choose_card[-1][-2] >field_card[-1][-1][-2] )and(choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] >field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and(choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (((choose_card[-1][-2] > field_card[-1][-1][-2] )and (choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] > field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                

            #3枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==3 :           
                if (len(choose_card) == len(field_card[-1]) ==3) :
                    #出した3枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]))))) :  #★ここがエラー起きるかもしれない
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                                        

            #4枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==4 :           
                if (len(choose_card) == len(field_card[-1]) ==4) :
                    #出した4枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if  (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
                     or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
                     or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]))))) :  #★ここがエラー起きるかもしれない
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[CP_card_2]
                                    c=player3[CP_card_3]
                                    d=player3[CP_card_4]
                                    e=player3[CP_card_5]
                                    f=player3[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(CP_card_2)
                                    player3.remove(CP_card_3)
                                    player3.remove(CP_card_4)
                                    player3.remove(CP_card_5)
                                    player3.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                            

 
       except Exception as e:
         flag=False #また手札を出すところのループから抜け出していない。 
       
       # try :初手だから革命かどうかの場合は不要。
       #８流しした後（eight_nagasi=True)のとき、ここも反応して重複しまうのでeight_nagasi=Falseのときだけ反応するようにする。
       if ((len(field_card)==0) and (eight_nagasi==False)) :          
          #複数枚だしているとき、それが同じ数字であればOK。もしくはjokerを含んでいれば。
          #1枚のとき、2枚の時,3枚のとき。４枚のとき
          #ジョーカーどうしで同じと認識にならないように、同じかどうかの判断時にjokerは外す。choose_card[-1][-2]==choose_card[-2][-2]!=joker
        if (len(choose_card)==1 )or (len(choose_card)==2 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2]))) \
         or (len(choose_card)==3 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2])))))) \
         or (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]) or ( (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
         or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
         or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])))))))) :

            #出したカードは手札から消す。
            #出したカードは手札から消す。
            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                a=player3[CP_card_1]
                b=player3[CP_card_2]
                c=player3[CP_card_3]
                d=player3[CP_card_4]
                e=player3[CP_card_5]
                f=player3[CP_card_6]
            except Exception as e:
                pass 
            try :
                player3.remove(CP_card_1)
                player3.remove(CP_card_2)
                player3.remove(CP_card_3)
                player3.remove(CP_card_4)
                player3.remove(CP_card_5)
                player3.remove(CP_card_6)
            except Exception as e:
                pass             
            flag=True
            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
            print(choose_card,"を出しました。")
            finish_turn(choose_card)             
            # except :
            #      pass
        else :
         flag=False #また手札を出すところのループから抜け出していない。 
        

    except Exception as e: #数字の大小の評価、Falseの場合　。
        flag=False #また手札を出すところのループから抜け出していない。

#CPのplayer4用の関数
def daseruka_hanndann_CP3(choose_card) :
    global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,my_turn,eight_nagasi
    global flag 
    #自分のターンだけ出せるカードの詳細がfinish_turnでprintされるようにしたいから.TRueのとき表示される。
    my_turn=True
    #８流し関数はここで一回Falseに戻す。finish_turnでまたeight_nagasiのTrue、False判断するし。
    eight_nagasi=False
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
          # print("フィールドのカードは",field_card)#問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            
            #★場に１枚しか出ていないとき。縛りだけ考える。----------------------------------------------------------------------------------------------------------
            if len(field_card[-1])==1 : #フィールドに１枚しかない場合。
               if shibari==1 : #縛りあり
                  if ((choose_card[-1][-1] ==field_card[-1][-1][-1] ) or ("joker" in choose_card[-1])) :#マークが同じじゃないといけない.それかjokerを出したとき。
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            #出したカードは手札から消す。
                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。 
                            
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
               
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
               elif shibari== 0 :#縛りがない場合
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                        #イレブンバック中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :

                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。 
                    elif kakumei%2 == 0 : #革命中
                      if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                        #革命中でもjokerは出せる。
                        if ((choose_card[-1][-2] < field_card[-1][-1][-2] ) or  ("joker" in choose_card[-1]))  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                             
                      elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                        if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(CP_card_2)
                                player4.remove(CP_card_3)
                                player4.remove(CP_card_4)
                                player4.remove(CP_card_5)
                                player4.remove(CP_card_6)
                            except Exception as e:
                                pass                        
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            print(choose_card,"を出しました。")
                            finish_turn(choose_card)
                        else :
                                flag=False #また手札を出すところのループから抜け出していない。                                     
             #場に１枚のみでているところにカードを出す場合。縛りの有無で場合分け---------------------------------
            
            #２枚出しているとき。 出せないカード選択していたら出せませんってもうもう一度選ばされる。----------------------------------------------------------------------------------------
            if len(field_card[-1]) ==2 :           
                if (len(choose_card) == len(field_card[-1]) ==2) :
                    #出した２枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2])) :
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (((choose_card[-1][-2] >field_card[-1][-1][-2] )and(choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] >field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and(choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (((choose_card[-1][-2] < field_card[-1][-1][-2] )and(choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] < field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (((choose_card[-1][-2] > field_card[-1][-1][-2] )and(choose_card[-1][-2] != 'joker')) or ((choose_card[-1][-2] > field_card[-1][-2][-2] )and(choose_card[-1][-2] != 'joker')))  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                

            #3枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==3 :           
                if (len(choose_card) == len(field_card[-1]) ==3) :
                    #出した3枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]))))) :  #★ここがエラー起きるかもしれない
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                                        

            #4枚出しているときーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
            if len(field_card[-1]) ==4 :           
                if (len(choose_card) == len(field_card[-1]) ==4) :
                    #出した4枚が同じ数字かチェック. 例えば2 2 とか2 joker 、joker 2のどれかを満たしていればいい。
                    if  (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
                     or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
                     or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]))))) :  #★ここがエラー起きるかもしれない
                        #数字の大きさのチェック

                        if kakumei%2 != 0 : #奇数のとき。通常時    
                          if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #イレブンバック中 大小を逆にすればいい。
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                        elif kakumei%2 == 0 : #革命中
                          if  eleven_back==0 : #イレブンバック起きてない。大小を<むきにする
                            if (choose_card[-1][-2] < field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                
                          elif eleven_back==1 : #革命時のイレブンバック中. 普通通り
                            if (choose_card[-1][-2] > field_card[-1][-1][-2] )  :
   
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[CP_card_2]
                                    c=player4[CP_card_3]
                                    d=player4[CP_card_4]
                                    e=player4[CP_card_5]
                                    f=player4[CP_card_6]
                                except Exception as e:
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(CP_card_2)
                                    player4.remove(CP_card_3)
                                    player4.remove(CP_card_4)
                                    player4.remove(CP_card_5)
                                    player4.remove(CP_card_6)
                                except Exception as e:   
                                    pass                 
       
                                flag=True
                                #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                                print(choose_card,"を出しました。")
                                finish_turn(choose_card)
                            else :
                                flag=False #また手札を出すところのループから抜け出していない。                                            

 
       except Exception as e:
         flag=False #また手札を出すところのループから抜け出していない。 
       
       # try :初手だから革命かどうかの場合は不要。
       if ((len(field_card)==0) and (eight_nagasi==False)) :          
          #複数枚だしているとき、それが同じ数字であればOK。もしくはjokerを含んでいれば。
          #1枚のとき、2枚の時,3枚のとき。４枚のとき
          #ジョーカーどうしで同じと認識にならないように、同じかどうかの判断時にjokerは外す。choose_card[-1][-2]==choose_card[-2][-2]!=joker
        if (len(choose_card)==1 )or (len(choose_card)==2 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (joker in choose_card[-1])  or (joker in choose_card[-2]))) \
         or (len(choose_card)==3 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card.count([joker,joker])==2) or ((choose_card.count([joker,joker])==1 and ((choose_card[-1][-2]==choose_card[-2][-2]) or (choose_card[-1][-2]==choose_card[-3][-2]) or (choose_card[-2][-2]==choose_card[-3][-2])))))) \
         or (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2]) or ( (len(choose_card)==4 and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])\
         or ((choose_card.count([joker,joker])==2) and ((choose_card[-1][-2]==choose_card[-2][-2]!=joker) or (choose_card[-1][-2]==choose_card[-3][-2]!=joker) or (choose_card[-1][-2]==choose_card[-4][-2]!=joker) or (choose_card[-2][-2]==choose_card[-3][-2]!=joker) or (choose_card[-2][-2]==choose_card[-4][-2]!=joker) or (choose_card[-3][-2]==choose_card[-4][-2]!=joker))  ) \
         or ((choose_card.count([joker,joker])==1) and ((choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-3][-2]) or (choose_card[-1][-2]==choose_card[-2][-2]==choose_card[-4][-2]) or (choose_card[-2][-2]==choose_card[-3][-2]==choose_card[-4][-2])))))))) :

            #出したカードは手札から消す。
            #出したカードは手札から消す。
            try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                a=player4[CP_card_1]
                b=player4[CP_card_2]
                c=player4[CP_card_3]
                d=player4[CP_card_4]
                e=player4[CP_card_5]
                f=player4[CP_card_6]
            except Exception as e:
                pass 
            try :
                player4.remove(CP_card_1)
                player4.remove(CP_card_2)
                player4.remove(CP_card_3)
                player4.remove(CP_card_4)
                player4.remove(CP_card_5)
                player4.remove(CP_card_6)
            except Exception as e:
                pass 
            
            flag=True
            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
            print(choose_card,"を出しました。")
            finish_turn(choose_card)             
            # except :
            #      pass
        else :
         flag=False #また手札を出すところのループから抜け出していない。 
        
    except Exception as e: #数字の大小の評価、Falseの場合　。
        flag=False #また手札を出すところのループから抜け出していない。



#【CPが革命をするべきかを判断する関数】-------------------------------------------------------------------------------------------------

def player2_check_kakumei() :
      global can_kakumei ,joker_maisuu,list_only_num,onzon_suuji,list_kakumei_onzon_suuji_with_index,list_tyouhuku_husegu,average_tehuda,do_kakumei
      joker_maisuu=0
      can_kakumei=False
      list_only_num=[]
      onzon_suuji=[]
      list_kakumei_onzon_suuji_with_index=[]
      list_tyouhuku_husegu=[]
      do_kakumei=False
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
                          #CPが革命するかはここのcan_kakumeiで判断する。手札の数値の平均値が６以下に
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
          print(average_tehuda)
          if (can_kakumei==True) and (average_tehuda <= 7) :
                #その手札を出す
                #print(list_kakumei_onzon_suuji_with_index)の部分
                do_kakumei=True
                pass
          #do_kakumeiがTrueかどうかが重要。上で、４枚同じ数字で、手札の大きさの平均値が７以下になればTrueになるようにしている。


def player3_check_kakumei() :
      global can_kakumei ,joker_maisuu,list_only_num,onzon_suuji,list_kakumei_onzon_suuji_with_index,list_tyouhuku_husegu,average_tehuda,do_kakumei
      joker_maisuu=0
      can_kakumei=False
      list_only_num=[]
      onzon_suuji=[]
      list_kakumei_onzon_suuji_with_index=[]
      list_tyouhuku_husegu=[]
      do_kakumei=False
      #4枚以上でないと革命ができないため
      #フィールドカードが４枚の時、or フィールドカードが０枚の時に発動する。
      if len(player3)>=4 :
          list_tyouhuku_husegu=[]
          for i in range(len(player3)) :
               if (joker in player3[i]) :
                    joker_maisuu+=1
                #数字だけのリストをつくり、同じ数字の枚数を数えやすくした
               list_only_num.append(player3[i][0])
          print(list_only_num)
          if joker_maisuu==0 :
               onzon_suuji=[]
               for i in range(len(player3)) :
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
                          #CPが革命するかはここのcan_kakumeiで判断する。手札の数値の平均値が６以下に
                         can_kakumei = True

                         
          if joker_maisuu==1 :
               onzon_suuji=[]
               for i in range(len(player3)) :
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
               for i in range(len(player3)) :
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
          print(average_tehuda)
          if (can_kakumei==True) and (average_tehuda <= 7) :
                #その手札を出す
                #print(list_kakumei_onzon_suuji_with_index)の部分
                do_kakumei=True
                pass
          #can_kakumeiがTrueかどうかが重要。上で、４枚同じ数字あればTrueになるようにしている。


def player4_check_kakumei() :
      global can_kakumei ,joker_maisuu,list_only_num,onzon_suuji,list_kakumei_onzon_suuji_with_index,list_tyouhuku_husegu,average_tehuda,do_kakumei
      joker_maisuu=0
      can_kakumei=False
      list_only_num=[]
      onzon_suuji=[]
      list_kakumei_onzon_suuji_with_index=[]
      list_tyouhuku_husegu=[]
      do_kakumei=False
      #4枚以上でないと革命ができないため
      #フィールドカードが４枚の時、or フィールドカードが０枚の時に発動する。
      if len(player4)>=4 :
          list_tyouhuku_husegu=[]
          for i in range(len(player4)) :
               if (joker in player4[i]) :
                    joker_maisuu+=1
                #数字だけのリストをつくり、同じ数字の枚数を数えやすくした
               list_only_num.append(player4[i][0])
          print(list_only_num)
          if joker_maisuu==0 :
               onzon_suuji=[]
               for i in range(len(player4)) :
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
                          #CPが革命するかはここのcan_kakumeiで判断する。手札の数値の平均値が６以下に
                         can_kakumei = True

                         
          if joker_maisuu==1 :
               onzon_suuji=[]
               for i in range(len(player4)) :
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
               for i in range(len(player4)) :
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
          print(average_tehuda)
          if (can_kakumei==True) and (average_tehuda <= 7) :
                #その手札を出す
                #print(list_kakumei_onzon_suuji_with_index)の部分
                do_kakumei=True
                pass
          #can_kakumeiがTrueかどうかが重要。上で、４枚同じ数字あればTrueになるようにしている。

#-------------------------------------------------------------------------------------------------


#CPと自分が手札を出す関数----------------------------------------------------------------------------------------------------------------------------------------------------
#★player2=daseruka_hanndann_CP1 用の手札を出す関数。ここがAIで強化するべきところ。課題の部分
#今回のは適当に枚数に応じて選択するようにして、それが出せる（True）になるまで繰り返す。
#ただし、５，６枚出しはなし。関数つくってないから。

def player1_dasu() :
 #daseruka_hanndannにint_choice1等を送るためにはこっちにもグローバルをしておく必要があるみたい
 global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,int_choice1,int_choice2,int_choice3,int_choice4,int_choice5,int_choice6,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
 flag = False
 your_tehuda=[]
 tehuda_hyouji_syori=False
 reset=True
 while flag==False :
    tt=0
    if tehuda_hyouji_syori==False :
     for i in range(15) : 
       try :
          your_tehuda.append(player1[i][0]+player1[i][1])
          tt+=1
          # 何回も選びなおすと毎回足されてしまうから一回きりにするため。
          tehuda_hyouji_syori=True
       except Exception as e :
             # print("例外argsG(無視していいエラー。15回繰り返した分だけエラー出る。):", e.args)
             flag=True 
             pass      
    print("あなたの手札は ",your_tehuda)
    print("フィールドのカードは",field_card,"です。")
    if len(your_tehuda)==0 :
        print("あなたの手札はありません。上がってます。")
        flag=True
        agatteruka_p1+=1
        #上がったらplayer1_dasu関数の処理を止めるため
        p1_agari=True
        #ここ繰り返しだから、一回しかプラスされないようにした。
        if agatteruka_p1==1 :
           #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
           agatteru_ninnzuu+=1
           #順位の確定（一回しか処理されないはず）
           p1_jyunni=jyunni
           jyunni+=1
           field_card.clear()
           #リセットするときに縛り等はリセットする
           shibari=0
           eleven_back=0
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    for i in range(tt) :
      print(i,":",your_tehuda[i]) #プレイヤーに選んでもらうためにわかりやすく手札を表示。半角数字によって何を出すかを判断させる。
    choose_card=[]#daseruka_hanbetu関数のために[[],[].[]]の形にしないといけないため・
    try :
       choice1=input("1枚目出すカードを選んでください(半角数字)パスならpassを入力") #10：eight♥で10を入力したら８♥を出したことになる。
       if choice1 == "pass"  :
           print("あなたはパスを選びました。相手のターンに回します")
           pass_kosuu+=1  #パスが３つになったらfield_card.clear()をする
            #あがっている人数に合わせて(agatteru_ninnzuu)、パスが１～３つたまったらフィールドカードのリセット
           if agatteru_ninnzuu==3 :
                if pass_kosuu==1 :
                  print("全員パスなのでフィールドカードをリセットします。")
                  eleven_back=0 
                  shibari=0
                  field_card.clear()
                  pass_kosuu=0
                  reset=False
           if agatteru_ninnzuu==2 :
                if pass_kosuu==1 :
                  print("全員パスなのでフィールドカードをリセットします。")
                  eleven_back=0 
                  shibari=0
                  field_card.clear()
                  pass_kosuu=0
                  reset=False
           if agatteru_ninnzuu==1 :
                if pass_kosuu==2 :
                  print("全員パスなのでフィールドカードをリセットします。")
                  eleven_back=0 
                  shibari=0
                  field_card.clear()
                  pass_kosuu=0 
                  reset=False
           if agatteru_ninnzuu==0 :
                if pass_kosuu==3 :
                  print("全員パスなのでフィールドカードをリセットします。")
                  eleven_back=0 
                  shibari=0
                  field_card.clear()
                  pass_kosuu=0 
                  reset=False
           flag=True
        
       else    : #passを選ばなかった場合
            try :
             int_choice1=int(choice1)
             #passの場合は自分の手札選びを中断させてCPのターンにする処理を書かないと
             print(player1[int_choice1],"を選びました。")
             choose_card.append(player1[int_choice1])
             choice2=input("２枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
             if choice2 != "ok" : #２枚目を出すという意思表示
              int_choice2=int(choice2)
              print(player1[int_choice2],"を選びました。")
              choose_card.append(player1[int_choice2])
              choice3=input("３枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
              if choice3 != "ok" :
                  int_choice3=int(choice3)
                  print(player1[int_choice3],"を選びました。")
                  choose_card.append(player1[int_choice3])
                  choice4=input("４枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
                  if choice4 != "ok" :
                     int_choice4=int(choice4)
                     print(player1[int_choice4],"を選びました。")
                     choose_card.append(player1[int_choice4])
                     choice5=input("５枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
                     if choice5 != "ok" :
                         int_choice5=int(choice5)
                         print(player1[int_choice5],"を選びました。")
                         choose_card.append(player1[int_choice5])
                         choice6=input("６枚目出すカードを選んでください(半角数字)これ以上出さないならokを入力")
                         if choice6 != "ok" :
                             int_choice6=int(choice6)
                             print(player1[int_choice6],"を選びました。")
                             choose_card.append(player1[int_choice6])
            
             # このchoose_cardは([[2,"♥"],[joker,joker]]な感じになってるはず。daseruka_handann関数で出せるかどうかを判断する。
             print("あなたが選んだカードは、",choose_card,"です。") 
             daseruka_hanndann(choose_card)
            except Exception as e :
                print("例外argsXX:", e.args)
                print("出せません。もう一度えらんでください")
                pass

    except Exception as e :
        print("例外argsH:", e.args)
        daseruka_hanndann(choose_card)
        pass
        #変な入力になったら、そのままdaseruka_hannbetu()でエラー起こさせればいいか。出せない手札を選択したらflag=Falseのままでずっと続くはず。

#【player2,daseruka_hanndann_CP1】
def player2_dasu() : 
 global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
 flag = False
 sikou_kaisuu=0
 #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
 reset=True
 while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    #毎回choose_cardはリセットしないとバグる
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
        agatteruka_p2+=1
        p2_agari=True
        #ここ繰り返しだから、一回しかプラスされないようにした。
        if agatteruka_p2==1 :
           #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
           agatteru_ninnzuu+=1
           #順位の確定（一回しか処理されないはず）
           p2_jyunni=jyunni
           jyunni+=1
           field_card.clear()
           #リセットするときに縛り等はリセットする
           shibari=0
           eleven_back=0
           
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          #１枚しかでていないとき。
          if len(field_card[0])==1 :
              #------------------------------------------------------------------------------------------
              #★CPを強くするための処理２：１枚ずつしかカード出さない時、かつ、まだ縛りがない場合、積極的に縛りを作りに来る！！
              #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
              if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
                list_daseru_mark=[]
                #フィールドカードのマークを抽出
                field_mark=field_card[-1][-1][-1] #でているカードの♥とか♣とか取得している。
                for i in range(len(player2)) :
                    #手札に同じマークがあるかを確認
                    tehuda_mark_syutoku=player2[i][-1]
                    #同じマークだった場合
                    if field_mark == tehuda_mark_syutoku :
                        #その同じマークの数字を取得
                        kazu=player2[i][-2]
                        #その同じマークの手札のインデックスの取得
                        sono_mark_index=i
                        listA=[]
                        listA.append(kazu)
                        listA.append(sono_mark_index)
                        list_daseru_mark.append(listA)
                # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]のようになるはず。[数字,インデックス]
                try :
                  #同じマークの手札のインデックスだけを抽出するためのリスト
                  onaji_mark_dasu_card=[]
                  for i in range(len(list_daseru_mark)) : 
                      #出せるカードのインデックスを全部入れる
                      onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
                  #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
                  CP_card_1=player2[random.choice(onaji_mark_dasu_card)]
                  #そのカードを出す
                  CP_choose_card.append(CP_card_1)
                  #出せるか判断
                  daseruka_hanndann_CP1(CP_choose_card)
                except :
                    #もし手札に小さいカードがでていても、手札に同じマークがなければ出せないから10回トライして出せないなら同じマークで出すことをあきらめる。
                    pass

              #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
              #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
              #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
              if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
                        CP_card_1=(random.choice(player2))
                        CP_choose_card.append(CP_card_1)
                        daseruka_hanndann_CP1(CP_choose_card)
                #------------------------------------------------------------------------------------------
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              CP_choose_card.append(CP_card_3)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              CP_choose_card.append(CP_card_3)
              CP_choose_card.append(CP_card_4)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #10000回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==10000 :
               print("player2はパスしました")
               flag=True
               pass_kosuu+=1    
               #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
               if agatteru_ninnzuu==3 :
                 if pass_kosuu==1 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False
               if agatteru_ninnzuu==2 :
                 if pass_kosuu==1 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False
               if agatteru_ninnzuu==1 :
                 if pass_kosuu==2 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False 
               if agatteru_ninnzuu==0 :
                 if pass_kosuu==3 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0     
                    reset=False        
         # if len(field_card)==5 :
         #     CP_card_1=(random.choice(player2))
         #     CP_card_2=(random.choice(player2))
         #     CP_card_3=(random.choice(player2))
         #     CP_card_4=(random.choice(player2))
         #     CP_card_5=(random.choice(player2))
         #     daseruka_hanndann_CP1(CP_choose_card)
         # if len(field_card)==6 :
         #     CP_card_1=(random.choice(player2))
         #     CP_card_2=(random.choice(player2))
         #     CP_card_3=(random.choice(player2))
         #     CP_card_4=(random.choice(player2))
         #     CP_card_5=(random.choice(player2))
         #     CP_card_6=(random.choice(player2))
         #     daseruka_hanndann_CP1(CP_choose_card)

    #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

    if ((len(field_card)== 0) and (reset==True)) :
        #上で一回試行回数１００００になってる可能性あるから０にする
        sikou_kaisuu=0
        while flag==False :
           #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
           #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


           #下記player2_check_kakumei()はplayer2が革命できる手札をもってるかどうか、また、player2の手札的に革命をするべきかどうかを判断する
           player2_check_kakumei()
           sikou_kaisuu+=1
           #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
           if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
                print(list_kakumei_onzon_suuji_with_index)
                #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
                CP_card_1=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
                CP_card_2=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
                CP_card_3=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
                CP_card_4=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
                CP_choose_card.append(CP_card_1)
                CP_choose_card.append(CP_card_2)
                CP_choose_card.append(CP_card_3)
                CP_choose_card.append(CP_card_4)
                daseruka_hanndann_CP1(CP_choose_card)

           #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。
           elif  sikou_kaisuu >= 10 :
                CP_choose_card=[]
                CP_syote_maisuu=random.randint(1,4)
                # print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
                try :
                    if CP_syote_maisuu==1 :
                        CP_card_1=(random.choice(player2))
                        CP_choose_card.append(CP_card_1)
                        daseruka_hanndann_CP1(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==2 :
                        CP_card_1=(random.choice(player2))
                        CP_card_2=(random.choice(player2))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        daseruka_hanndann_CP1(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==3 :
                        CP_card_1=(random.choice(player2))
                        CP_card_2=(random.choice(player2))
                        CP_card_3=(random.choice(player2))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        CP_choose_card.append(CP_card_3)
                        daseruka_hanndann_CP1(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==4 :
                        CP_card_1=(random.choice(player2))
                        CP_card_2=(random.choice(player2))
                        CP_card_3=(random.choice(player2))
                        CP_card_4=(random.choice(player2))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        CP_choose_card.append(CP_card_3)
                        CP_choose_card.append(CP_card_4)
                        daseruka_hanndann_CP1(CP_choose_card)
                except Exception as e  :
                    print(e.args)
                    pass
                #10000回手札選び失敗したらパスするようにした。
                sikou_kaisuu+=1
                if sikou_kaisuu==10000 :
                    print("player2はパスしましたよ。")
                    #パスが３つたまったらフィールドカードのリセット
                    pass_kosuu+=1
                    if agatteru_ninnzuu==3 :
                        if pass_kosuu==1 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0
                            reset=False
                    if agatteru_ninnzuu==2 :
                        if pass_kosuu==1 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0
                            reset=False
                    if agatteru_ninnzuu==1 :
                        if pass_kosuu==2 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0 
                            reset=False
                    if agatteru_ninnzuu==0 :
                        if pass_kosuu==3 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0    
                            reset=False   
                    flag=True
                # if CP_syote_maisuu==5 :
                #     CP_card_1=(random.choice(player2))
                #     CP_card_2=(random.choice(player2))
                #     CP_card_3=(random.choice(player2))
                #     CP_card_4=(random.choice(player2))
                #     CP_card_5=(random.choice(player2))
                #     daseruka_hanndann_CP1(CP_choose_card)
                # if CP_syote_maisuu==6 :
                #     CP_card_1=(random.choice(player2))
                #     CP_card_2=(random.choice(player2))
                #     CP_card_3=(random.choice(player2))
                #     CP_card_4=(random.choice(player2))
                #     CP_card_5=(random.choice(player2))
                #     CP_card_6=(random.choice(player2))
                #     daseruka_hanndann_CP1(CP_choose_card)

#【player3,daseruka_hanndann_CP2】
def player3_dasu() : 
 global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
 flag = False
 sikou_kaisuu=0
 #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
 reset=True
 while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
        agatteruka_p3+=1
        p3_agari=True
        #ここ繰り返しだから、一回しかプラスされないようにした。
        if agatteruka_p3==1 :
           #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
           agatteru_ninnzuu+=1
           #順位の確定（一回しか処理されないはず）
           p3_jyunni=jyunni
           jyunni+=1
           field_card.clear()
           #リセットするときに縛り等はリセットする
           shibari=0
           eleven_back=0
           
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          #１枚しかでていないとき。
          if len(field_card[0])==1 :
              #★CPを強くするための処理２：１枚ずつしかカード出さない時、かつ、まだ縛りがない場合、積極的に縛りを作りに来る！！
              #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
              if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
                list_daseru_mark=[]
                #フィールドカードのマークを抽出
                field_mark=field_card[-1][-1][-1]
                for i in range(len(player3)) :
                    tehuda_mark_syutoku=player3[i][-1]
                    #同じマークだった場合
                    if field_mark == tehuda_mark_syutoku :
                        kazu=player3[i][-2]
                        sono_mark_index=i
                        listA=[]
                        listA.append(kazu)
                        listA.append(sono_mark_index)
                        list_daseru_mark.append(listA)
                # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
                try :
                  onaji_mark_dasu_card=[]
                  for i in range(len(list_daseru_mark)) : 
                      onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
                  #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
                  CP_card_1=player3[random.choice(onaji_mark_dasu_card)]
                  CP_choose_card.append(CP_card_1)
                  daseruka_hanndann_CP2(CP_choose_card)
                except :
                    print("ここがパスになってます")
                    pass

              #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
              #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
              #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
              if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
                        CP_card_1=(random.choice(player3))
                        CP_choose_card.append(CP_card_1)
                        daseruka_hanndann_CP2(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player3))
              CP_card_2=(random.choice(player3))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              daseruka_hanndann_CP2(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player3))
              CP_card_2=(random.choice(player3))
              CP_card_3=(random.choice(player3))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              CP_choose_card.append(CP_card_3)
              daseruka_hanndann_CP2(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player3))
              CP_card_2=(random.choice(player3))
              CP_card_3=(random.choice(player3))
              CP_card_4=(random.choice(player3))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              CP_choose_card.append(CP_card_3)
              CP_choose_card.append(CP_card_4)
              daseruka_hanndann_CP2(CP_choose_card)
         except :
             pass
         #10000回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==10000 :
               print("player3はパスしました")
               flag=True
               pass_kosuu+=1    
               #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
               if agatteru_ninnzuu==3 :
                 if pass_kosuu==1 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False
               if agatteru_ninnzuu==2 :
                 if pass_kosuu==1 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False
               if agatteru_ninnzuu==1 :
                 if pass_kosuu==2 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False 
               if agatteru_ninnzuu==0 :
                 if pass_kosuu==3 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0     
                    reset=False        
         # if len(field_card)==5 :
         #     CP_card_1=(random.choice(player3))
         #     CP_card_2=(random.choice(player3))
         #     CP_card_3=(random.choice(player3))
         #     CP_card_4=(random.choice(player3))
         #     CP_card_5=(random.choice(player3))
         #     daseruka_hanndann_CP1(CP_choose_card)
         # if len(field_card)==6 :
         #     CP_card_1=(random.choice(player3))
         #     CP_card_2=(random.choice(player3))
         #     CP_card_3=(random.choice(player3))
         #     CP_card_4=(random.choice(player3))
         #     CP_card_5=(random.choice(player3))
         #     CP_card_6=(random.choice(player3))
         #     daseruka_hanndann_CP1(CP_choose_card)

    #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

    if ((len(field_card)== 0) and (reset==True)) :
        #上で一回試行回数１００００になってる可能性あるから０にする
        sikou_kaisuu=0
        while flag==False :
           #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
           #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


           #下記player3_check_kakumei()はplayer3が革命できる手札をもってるかどうか、また、player3の手札的に革命をするべきかどうかを判断する
           player3_check_kakumei()
           sikou_kaisuu+=1
           #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
           if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
                print(list_kakumei_onzon_suuji_with_index)
                #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
                CP_card_1=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
                CP_card_2=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
                CP_card_3=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
                CP_card_4=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
                CP_choose_card.append(CP_card_1)
                CP_choose_card.append(CP_card_2)
                CP_choose_card.append(CP_card_3)
                CP_choose_card.append(CP_card_4)
                daseruka_hanndann_CP2(CP_choose_card)
                
           #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。
           elif  sikou_kaisuu >= 10 :
                CP_choose_card=[]
                CP_syote_maisuu=random.randint(1,4)
                # print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
                try :
                    if CP_syote_maisuu==1 :
                        CP_card_1=(random.choice(player3))
                        CP_choose_card.append(CP_card_1)
                        daseruka_hanndann_CP2(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==2 :
                        CP_card_1=(random.choice(player3))
                        CP_card_2=(random.choice(player3))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        daseruka_hanndann_CP2(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==3 :
                        CP_card_1=(random.choice(player3))
                        CP_card_2=(random.choice(player3))
                        CP_card_3=(random.choice(player3))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        CP_choose_card.append(CP_card_3)
                        daseruka_hanndann_CP2(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==4 :
                        CP_card_1=(random.choice(player3))
                        CP_card_2=(random.choice(player3))
                        CP_card_3=(random.choice(player3))
                        CP_card_4=(random.choice(player3))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        CP_choose_card.append(CP_card_3)
                        CP_choose_card.append(CP_card_4)
                        daseruka_hanndann_CP2(CP_choose_card)
                except Exception as e  :
                    print(e.args)
                    pass
                #10000回手札選び失敗したらパスするようにした。
                sikou_kaisuu+=1
                if sikou_kaisuu==10000 :
                    print("player3はパスしましたよ。")
                    #パスが３つたまったらフィールドカードのリセット
                    pass_kosuu+=1
                    if agatteru_ninnzuu==3 :
                        if pass_kosuu==1 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0
                            reset=False
                    if agatteru_ninnzuu==2 :
                        if pass_kosuu==1 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0
                            reset=False
                    if agatteru_ninnzuu==1 :
                        if pass_kosuu==2 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0 
                            reset=False
                    if agatteru_ninnzuu==0 :
                        if pass_kosuu==3 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0    
                            reset=False   
                    flag=True
                # if CP_syote_maisuu==5 :
                #     CP_card_1=(random.choice(player3))
                #     CP_card_2=(random.choice(player3))
                #     CP_card_3=(random.choice(player3))
                #     CP_card_4=(random.choice(player3))
                #     CP_card_5=(random.choice(player3))
                #     daseruka_hanndann_CP1(CP_choose_card)
                # if CP_syote_maisuu==6 :
                #     CP_card_1=(random.choice(player3))
                #     CP_card_2=(random.choice(player3))
                #     CP_card_3=(random.choice(player3))
                #     CP_card_4=(random.choice(player3))
                #     CP_card_5=(random.choice(player3))
                #     CP_card_6=(random.choice(player3))
                #     daseruka_hanndann_CP1(CP_choose_card)

#【player4,daseruka_hanndann_CP3】
def player4_dasu() : 
 global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
 flag = False
 sikou_kaisuu=0
 #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
 reset=True
 while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player4)==0 :
        print("player4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
        agatteruka_p4+=1
        p4_agari=True
        #ここ繰り返しだから、一回しかプラスされないようにした。
        if agatteruka_p4==1 :
           #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
           agatteru_ninnzuu+=1
           #順位の確定（一回しか処理されないはず）
           p4_jyunni=jyunni
           jyunni+=1
           field_card.clear()
           #リセットするときに縛り等はリセットする
           shibari=0
           eleven_back=0
           
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          #１枚しかでていないとき。
          if len(field_card[0])==1 :
              #------------------------------------------------------------------------------------------
              #★CPを強くするための処理２：１枚ずつしかカード出さない時、かつ、まだ縛りがない場合、積極的に縛りを作りに来る！！
              #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
              if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
                list_daseru_mark=[]
                #フィールドカードのマークを抽出
                field_mark=field_card[-1][-1][-1]
                for i in range(len(player4)) :
                    tehuda_mark_syutoku=player4[i][-1]
                    #同じマークだった場合
                    if field_mark == tehuda_mark_syutoku :
                        kazu=player4[i][-2]
                        sono_mark_index=i
                        listA=[]
                        listA.append(kazu)
                        listA.append(sono_mark_index)
                        list_daseru_mark.append(listA)
                # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
                try :
                  onaji_mark_dasu_card=[]
                  for i in range(len(list_daseru_mark)) : 
                      onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
                  #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
                  CP_card_1=player4[random.choice(onaji_mark_dasu_card)]
                  CP_choose_card.append(CP_card_1)
                  daseruka_hanndann_CP3(CP_choose_card)
                except :
                    print("ここがパスになってます")
                    pass

              #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
              #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
              #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
              if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
                        CP_card_1=(random.choice(player4))
                        CP_choose_card.append(CP_card_1)
                        daseruka_hanndann_CP3(CP_choose_card)
                #------------------------------------------------------------------------------------------
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player4))
              CP_card_2=(random.choice(player4))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              daseruka_hanndann_CP3(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player4))
              CP_card_2=(random.choice(player4))
              CP_card_3=(random.choice(player4))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              CP_choose_card.append(CP_card_3)
              daseruka_hanndann_CP3(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player4))
              CP_card_2=(random.choice(player4))
              CP_card_3=(random.choice(player4))
              CP_card_4=(random.choice(player4))
              CP_choose_card.append(CP_card_1)
              CP_choose_card.append(CP_card_2)
              CP_choose_card.append(CP_card_3)
              CP_choose_card.append(CP_card_4)
              daseruka_hanndann_CP3(CP_choose_card)
         except :
             pass
         #10000回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==10000 :
               print("player4はパスしました")
               flag=True
               pass_kosuu+=1    
               #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
               if agatteru_ninnzuu==3 :
                 if pass_kosuu==1 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False
               if agatteru_ninnzuu==2 :
                 if pass_kosuu==1 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False
               if agatteru_ninnzuu==1 :
                 if pass_kosuu==2 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0
                    reset=False 
               if agatteru_ninnzuu==0 :
                 if pass_kosuu==3 :
                    print("全員パスなのでフィールドカードをリセットします。")
                    eleven_back=0 
                    shibari=0
                    field_card.clear()
                    pass_kosuu=0     
                    reset=False        
         # if len(field_card)==5 :
         #     CP_card_1=(random.choice(player4))
         #     CP_card_2=(random.choice(player4))
         #     CP_card_3=(random.choice(player4))
         #     CP_card_4=(random.choice(player4))
         #     CP_card_5=(random.choice(player4))
         #     daseruka_hanndann_CP1(CP_choose_card)
         # if len(field_card)==6 :
         #     CP_card_1=(random.choice(player4))
         #     CP_card_2=(random.choice(player4))
         #     CP_card_3=(random.choice(player4))
         #     CP_card_4=(random.choice(player4))
         #     CP_card_5=(random.choice(player4))
         #     CP_card_6=(random.choice(player4))
         #     daseruka_hanndann_CP1(CP_choose_card)

    #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

    if ((len(field_card)== 0) and (reset==True)) :
        #上で一回試行回数１００００になってる可能性あるから０にする
        sikou_kaisuu=0
        while flag==False :
           #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
           #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


           #下記player4_check_kakumei()はplayer4が革命できる手札をもってるかどうか、また、player4の手札的に革命をするべきかどうかを判断する
           player4_check_kakumei()
           sikou_kaisuu+=1
           #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
           if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
                print(list_kakumei_onzon_suuji_with_index)
                #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
                CP_card_1=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
                CP_card_2=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
                CP_card_3=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
                CP_card_4=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
                CP_choose_card.append(CP_card_1)
                CP_choose_card.append(CP_card_2)
                CP_choose_card.append(CP_card_3)
                CP_choose_card.append(CP_card_4)
                daseruka_hanndann_CP3(CP_choose_card)
                
           #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。
           elif  sikou_kaisuu >= 10 :
                CP_choose_card=[]
                CP_syote_maisuu=random.randint(1,4)
                # print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
                try :
                    if CP_syote_maisuu==1 :
                        CP_card_1=(random.choice(player4))
                        CP_choose_card.append(CP_card_1)
                        daseruka_hanndann_CP3(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==2 :
                        CP_card_1=(random.choice(player4))
                        CP_card_2=(random.choice(player4))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        daseruka_hanndann_CP3(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==3 :
                        CP_card_1=(random.choice(player4))
                        CP_card_2=(random.choice(player4))
                        CP_card_3=(random.choice(player4))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        CP_choose_card.append(CP_card_3)
                        daseruka_hanndann_CP3(CP_choose_card)
                except Exception as e :
                    print(e.args)
                    pass
                try :
                    if CP_syote_maisuu==4 :
                        CP_card_1=(random.choice(player4))
                        CP_card_2=(random.choice(player4))
                        CP_card_3=(random.choice(player4))
                        CP_card_4=(random.choice(player4))
                        CP_choose_card.append(CP_card_1)
                        CP_choose_card.append(CP_card_2)
                        CP_choose_card.append(CP_card_3)
                        CP_choose_card.append(CP_card_4)
                        daseruka_hanndann_CP3(CP_choose_card)
                except Exception as e  :
                    print(e.args)
                    pass
                #10000回手札選び失敗したらパスするようにした。
                sikou_kaisuu+=1
                if sikou_kaisuu==10000 :
                    print("player4はパスしましたよ。")
                    #パスが３つたまったらフィールドカードのリセット
                    pass_kosuu+=1
                    if agatteru_ninnzuu==3 :
                        if pass_kosuu==1 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0
                            reset=False
                    if agatteru_ninnzuu==2 :
                        if pass_kosuu==1 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0
                            reset=False
                    if agatteru_ninnzuu==1 :
                        if pass_kosuu==2 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0 
                            reset=False
                    if agatteru_ninnzuu==0 :
                        if pass_kosuu==3 :
                            print("全員パスなのでフィールドカードをリセットします。")
                            eleven_back=0 
                            shibari=0
                            field_card.clear()
                            pass_kosuu=0    
                            reset=False   
                    flag=True
                # if CP_syote_maisuu==5 :
                #     CP_card_1=(random.choice(player4))
                #     CP_card_2=(random.choice(player4))
                #     CP_card_3=(random.choice(player4))
                #     CP_card_4=(random.choice(player4))
                #     CP_card_5=(random.choice(player4))
                #     daseruka_hanndann_CP1(CP_choose_card)
                # if CP_syote_maisuu==6 :
                #     CP_card_1=(random.choice(player4))
                #     CP_card_2=(random.choice(player4))
                #     CP_card_3=(random.choice(player4))
                #     CP_card_4=(random.choice(player4))
                #     CP_card_5=(random.choice(player4))
                #     CP_card_6=(random.choice(player4))
                #     daseruka_hanndann_CP1(CP_choose_card)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#【延々と手札を出していく処理】------------------------------------------------------------------------------------------------------------------------------------------

syoubu=False
while syoubu==False  :
    global p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni

    #手札が０になるまでそれぞれ繰り返し。手札が０枚になったらp1_agari等がTrueになるからそのプレイヤーの関数は動かなくなる。
    if p1_agari==False :
     player1_dasu()
     #8流しをしたらもう一回次のターン出せる
     if eight_nagasi==True :
         player1_dasu()
    if p2_agari==False :  
     print("player2のターン")
     player2_dasu()
     if eight_nagasi==True :
          player2_dasu()
    if p3_agari==False :
     print("player3のターン")
     player3_dasu()
     if eight_nagasi==True : 
          player3_dasu()
    if p4_agari==False :
     print("player4のターン")
     player4_dasu()
     if eight_nagasi==True :
          player4_dasu()

    #上がってる人数が４人になるまで続ける。
    if agatteru_ninnzuu==4 :
        syoubu=True
        #【結果発表】------------------------------------------------------------------------------------------------------------------------------------------
        print("")
        print("勝負がつきました")
        print("")
        print("あなたの順位は",p1_jyunni,"位です")
        print("player2の順位は",p2_jyunni,"位です")
        print("player3の順位は",p3_jyunni,"位です")
        print("player4の順位は",p4_jyunni,"位です")        
        print("")

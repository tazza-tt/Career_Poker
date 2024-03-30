field_card=[]
kakumei=1
shibari=0 
eleven_back=0
pass_kosuu=0 #パスが３つになったらfield_card.clear()をする

#文字の大小を比較するに当たって fourとかは UNICODEで比較される--------------
# だからUNICODE対策で数字0をたした。１はOneと大文字にしてjokerを一番大きくなるように定義しておく
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
print(three<four<five<six<seven<eight<nine<ten<eleven<twelve<thirteen<one<two<joker)
#----------------------------------------------------------


player1=[[two, "♠"], [four, "♦"], [seven, "♥"], [one, "♦"], [ten, "♠"], [joker, joker], [one, "♠"], [twelve, "♦"], [eleven, "♠"], [two, "♣"], [eight, "♥"], [six, "♣"], [seven, "♣"]]

def finish_turn (select_card) :
     field_card.append(select_card) #関数処理はここだけで下記はただ評価するだけか。
     top_field_card=field_card[-1]

     global kakumei ,shibari,eleven_back

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
          try :#初手の場合はpre_field_cardがないため。
               #field_card=[[[1,♥]],[[4,♥]]]という想定
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
     try :
         if (eight in top_field_card[-1]) :             
             top_field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-2]) :             
             top_field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-3]) :             
             top_field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-4]) :             
             top_field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-5]) :             
             top_field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-6]) :             
             top_field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
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
     if shibari==0 :
         print("■縛りはありません")
     if shibari==1 :
         print("■縛られています")
     if kakumei %2 == 0 :
         print("■革命中です")
     if kakumei %2 != 0 :
         print("■革命中ではありません")
     if eleven_back == 0 :
         print("■イレブンバック中ではありません")
     if eleven_back == 1 :
         print("■イレブンバック中です")
     print("フィールドのカードは,",field_card)
     print("-------------------------------------------")

#下で選んだカード（choose_card）が出せるのか判断
def daseruka_hanndann(choose_card) :
    global int_choice1,int_choice2,int_choice3,int_choice4,int_choice5,int_choice6,your_tehuda
    global flag 

    # ここ必要ないかも。
    # if len(field_card) != 0 :#フィールドにすでにカードが出ている状態。個数が0ではない場合 
    #     pre_field_card=field_card[-1] #[[1,"♠"]] 先頭に出ているカード
    #     #ここの判別はルール関数で革命中かイレブンバック中か否かで全通り数字の大小を定義している。どのパターンでも>,<で評価できるようにしている。基本大きいもの(>)をだせていればいい。
    #     hannbetu=choose_card[-1][-2] > pre_field_card[-1][-2] #今回階段で出すのはなしだからどれか一枚だけの数字の評価で十分
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
          print(field_card)#問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            print("選んだカードの数字は",choose_card[-1][-2])
            print("場に出ているカードは",field_card[-1][-1][-2] )
            print(choose_card[-1][-2] >field_card[-1][-1][-2]) #★ここがおかしい。Trueであってほしい eleven > fourでfalseになるのがおかしい。→UNICODE使ってる。         

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


       except Exception as e:
         print("例外args:C", e.args)
         print("そのカードは出せません。もう一度選んでください。")
         flag=False #また手札を出すところのループから抜け出していない。 
       
       # try :初手だから革命かどうかの場合は不要。
       if (len(field_card)==0) :
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

    except Exception as e: #数字の大小の評価、Falseの場合　。
         print("例外argsF:", e.args)
         print("そのカードは出せません。もう一度選んでください。")
         flag=False #また手札を出すところのループから抜け出していない。

#自分の手札を選ぶ。自分が出すときだけ使う関数。
flag = False
your_tehuda=[]
tehuda_hyouji_syori=False
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
             print("例外argsG(無視していいエラー。15回繰り返した分だけエラー出る。):", e.args)
             flag=True 
             pass      
    print("あなたの手札は ",your_tehuda)
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    for i in range(tt) :
      print(i,":",your_tehuda[i]) #プレイヤーに選んでもらうためにわかりやすく手札を表示。半角数字によって何を出すかを判断させる。
    choose_card=[]#daseruka_hanbetu関数のために[[],[].[]]の形にしないといけないため・
    try :
       choice1=input("1枚目出すカードを選んでください(半角数字)パスならpassを入力") #10：eight♥で10を入力したら８♥を出したことになる。
       if choice1 == "pass"  :
           print("あなたはパスを選びました。相手のターンに回します")
           pass_kosuu+=1  #パスが３つになったらfield_card.clear()をする
        
       else    : #passを選ばなかった場合
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
        print("例外argsH:", e.args)
        daseruka_hanndann(choose_card)
        pass
        #変な入力になったら、そのままdaseruka_hannbetu()でエラー起こさせればいいか。出せない手札を選択したらflag=Falseのままでずっと続くはず。

flag = False
your_tehuda=[]
tehuda_hyouji_syori=False
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
             print("例外argsI（無視していいエラー。15回繰り返した分だけエラー出る。）:", e.args)
             flag=True 
             pass      
    print("あなたの手札は ",your_tehuda)
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    for i in range(tt) :
      print(i,":",your_tehuda[i]) #プレイヤーに選んでもらうためにわかりやすく手札を表示。半角数字によって何を出すかを判断させる。
    choose_card=[]#daseruka_hanbetu関数のために[[],[].[]]の形にしないといけないため・
    try :
       choice1=input("1枚目出すカードを選んでください(半角数字)パスならpassを入力") #10：eight♥で10を入力したら８♥を出したことになる。
       if choice1 == "pass"  :
           print("あなたはパスを選びました。相手のターンに回します")
           pass_kosuu+=1  #パスが３つになったらfield_card.clear()をする
        
       else    : #passを選ばなかった場合
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
        print("例外argsJ:", e.args)
        daseruka_hanndann(choose_card)
        pass
        #変な入力になったら、そのままdaseruka_hannbetu()でエラー起こさせればいいか。出せない手札を選択したらflag=Falseのままでずっと続くはず。

 
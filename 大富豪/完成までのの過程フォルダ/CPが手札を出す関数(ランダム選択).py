import random

field_card=[]
kakumei=1
shibari=0 
eleven_back=0
pass_kosuu=0 #パスが３つになったらfield_card.clear()をする
jyunni=1 #順位。抜けるたびに＋１していく。

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

# field_card=[[[four, "♦"]]]

def finish_turn (select_card) :
     field_card.append(select_card) #関数処理はここだけで下記はただ評価するだけか。
     top_field_card=field_card[-1]

     global kakumei ,shibari,eleven_back,pass_kosuu

     #（１）カードが何枚出てるか。また、４枚以上出た場合は革命が発動するとする。
     # fieldには[]で格納している。例えば、2を3枚出したら、field=[ [[1,♠],[1,♣],[1,♥]] ]となり、len(field[0])=3となる。３枚出ていることがわかる。
     num_field_card=len(field_card[-1]) #最後に格納されている数字でいい。
     if num_field_card==1 :
          can_num_card=1
          print("1枚だけ出せます")
     if num_field_card==2 :
          can_num_card=2
          print("2枚出してください")
     if num_field_card==3 :
          print("3枚出してください")
          can_num_card=3
     if num_field_card==4 :
          print("4枚出してください")
          can_num_card=4
          kakumei=kakumei+1 #革命。あとで2%==0かどうかで偶数、奇数判別して2nが革命中とする。
     if num_field_card==5 :
          print("5枚出せます")
          can_num_card=5
          kakumei=kakumei+1 #革命
     if num_field_card==6 :
          print("6枚出せます")
          can_num_card=6
          kakumei=kakumei+1 #革命
     if num_field_card==0 : #何もない状態
          print("好きな枚数出せます")
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
             field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-2]) :             
             field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-3]) :             
             field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-4]) :             
             field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-5]) :             
             field_card.clear() 
             #イレブンバックも解除
             eleven_back=0 #０すなわち偶数のときは、イレブンバックをしていない状況。
     except :
         pass
     try :
         if (eight in top_field_card[-6]) :             
             field_card.clear() 
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
         print("■マークの縛りはありません")
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
     pass_kosuu=0

#CP1用の関数。player2として、手札等を関数を書き換えないといけないので、それぞれの関数をCP3まで３作るって感じかな。
def daseruka_hanndann_CP1(choose_card) :
    global CP_card_1,cp_card_2,cp_card_3,cp_card_4,cp_card_5,cp_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player2
    global flag 
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
          print("フィールドのカードは",field_card)#問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            print("選んだカードの数字は",choose_card[-1][-2])
            print("場に出ているカードは",field_card[-1][-1][-2] )
            # print(choose_card[-1][-2] >field_card[-1][-1][-2]) #★ここがおかしい。Trueであってほしい eleven > fourでfalseになるのがおかしい。→UNICODE使ってる。解決済み         
            
            #★場に１枚しか出ていないとき。縛りだけ考える。----------------------------------------------------------------------------------------------------------
            if len(field_card[-1])==1 : #フィールドに１枚しかない場合。
               if shibari==1 : #縛りあり
                  if (choose_card[-1][-1] ==field_card[-1][-1][-1] ) :#マークが同じじゃないといけない
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
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
                            print("そのカードは出せます。カードを出しました。。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
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
                            print("そのカードは出せます。カードを出しました。。。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
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
                            print("そのカードは出せます。カードを出しました")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                             
               elif shibari== 0 :#縛りがない場合
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました.")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
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
                            print("そのカードは出せます。カードを出しました..")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
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
                            print("そのカードは出せます。カードを出しました...")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
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
                            print("そのカードは出せます。カードを出しました!")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player2.remove(CP_card_1)
                                player2.remove(cp_card_2)
                                player2.remove(cp_card_3)
                                player2.remove(cp_card_4)
                                player2.remove(cp_card_5)
                                player2.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player2,"です。")       
                            if len(player2)==0 :
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
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました!!")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                                    a=player2[CP_card_1]
                                    b=player2[cp_card_2]
                                    c=player2[cp_card_3]
                                    d=player2[cp_card_4]
                                    e=player2[cp_card_5]
                                    f=player2[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player2.remove(CP_card_1)
                                    player2.remove(cp_card_2)
                                    player2.remove(cp_card_3)
                                    player2.remove(cp_card_4)
                                    player2.remove(cp_card_5)
                                    player2.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player2,"です。")       
                                if len(player2)==0 :
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
                a=player2[CP_card_1]
                b=player2[cp_card_2]
                c=player2[cp_card_3]
                d=player2[cp_card_4]
                e=player2[cp_card_5]
                f=player2[cp_card_6]
            except Exception as e:
                print("例外argD:", e.args)
                pass 
            try :
                player2.remove(CP_card_1)
                player2.remove(cp_card_2)
                player2.remove(cp_card_3)
                player2.remove(cp_card_4)
                player2.remove(cp_card_5)
                player2.remove(cp_card_6)
            except Exception as e:
                print("例外argsE:", e.args)
                pass                 
            print("カードを出した後のあなたの手札は",player2,"です。")
            if len(player2)==0 :
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

#CPのplayer3用の関数
def daseruka_hanndann_CP2(choose_card) :
    global CP_card_1,cp_card_2,cp_card_3,cp_card_4,cp_card_5,cp_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player3
    global flag 
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
          print("フィールドのカードは",field_card)#問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            print("選んだカードの数字は",choose_card[-1][-2])
            print("場に出ているカードは",field_card[-1][-1][-2] )
            # print(choose_card[-1][-2] >field_card[-1][-1][-2]) #★ここがおかしい。Trueであってほしい eleven > fourでfalseになるのがおかしい。→UNICODE使ってる。解決済み         
            
            #★場に１枚しか出ていないとき。縛りだけ考える。----------------------------------------------------------------------------------------------------------
            if len(field_card[-1])==1 : #フィールドに１枚しかない場合。
               if shibari==1 : #縛りあり
                  if (choose_card[-1][-1] ==field_card[-1][-1][-1] ) :#マークが同じじゃないといけない
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
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
                            print("そのカードは出せます。カードを出しました。。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
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
                            print("そのカードは出せます。カードを出しました。。。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
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
                            print("そのカードは出せます。カードを出しました")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                             
               elif shibari== 0 :#縛りがない場合
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました.")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
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
                            print("そのカードは出せます。カードを出しました..")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
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
                            print("そのカードは出せます。カードを出しました...")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
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
                            print("そのカードは出せます。カードを出しました!")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player3.remove(CP_card_1)
                                player3.remove(cp_card_2)
                                player3.remove(cp_card_3)
                                player3.remove(cp_card_4)
                                player3.remove(cp_card_5)
                                player3.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player3,"です。")       
                            if len(player3)==0 :
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
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました!!")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                                    a=player3[CP_card_1]
                                    b=player3[cp_card_2]
                                    c=player3[cp_card_3]
                                    d=player3[cp_card_4]
                                    e=player3[cp_card_5]
                                    f=player3[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player3.remove(CP_card_1)
                                    player3.remove(cp_card_2)
                                    player3.remove(cp_card_3)
                                    player3.remove(cp_card_4)
                                    player3.remove(cp_card_5)
                                    player3.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player3,"です。")       
                                if len(player3)==0 :
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
                a=player3[CP_card_1]
                b=player3[cp_card_2]
                c=player3[cp_card_3]
                d=player3[cp_card_4]
                e=player3[cp_card_5]
                f=player3[cp_card_6]
            except Exception as e:
                print("例外argD:", e.args)
                pass 
            try :
                player3.remove(CP_card_1)
                player3.remove(cp_card_2)
                player3.remove(cp_card_3)
                player3.remove(cp_card_4)
                player3.remove(cp_card_5)
                player3.remove(cp_card_6)
            except Exception as e:
                print("例外argsE:", e.args)
                pass                 
            print("カードを出した後のあなたの手札は",player3,"です。")
            if len(player3)==0 :
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

#CPのplayer4用の関数
def daseruka_hanndann_CP3(choose_card) :
    global CP_card_1,cp_card_2,cp_card_3,cp_card_4,cp_card_5,cp_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4
    global flag 
        
    try : #フィールドにすでにカードがでている状態と、出ていない状態それぞれに出せるかの判断を数字評価している。
       try :#field_card[-1][-1][-2]とlen(field_card)==0は同時には成立しえないからどっちかが機能するはず。
          print("フィールドのカードは",field_card)#問題なく、前回の出したカードが引き継がれているのを確認した。
          if (len(field_card) != 0) :
            print("選んだカードの数字は",choose_card[-1][-2])
            print("場に出ているカードは",field_card[-1][-1][-2] )
            # print(choose_card[-1][-2] >field_card[-1][-1][-2]) #★ここがおかしい。Trueであってほしい eleven > fourでfalseになるのがおかしい。→UNICODE使ってる。解決済み         
            
            #★場に１枚しか出ていないとき。縛りだけ考える。----------------------------------------------------------------------------------------------------------
            if len(field_card[-1])==1 : #フィールドに１枚しかない場合。
               if shibari==1 : #縛りあり
                  if (choose_card[-1][-1] ==field_card[-1][-1][-1] ) :#マークが同じじゃないといけない
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました。")
                            #出したカードは手札から消す。
                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
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
                            print("そのカードは出せます。カードを出しました。。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
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
                            print("そのカードは出せます。カードを出しました。。。")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
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
                            print("そのカードは出せます。カードを出しました")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
                                print("手札がなくなりました。あなたの抜けです。")
                            flag=True
                            #次のプレイヤーにかかる条件をルール関数で定義しなおす。
                            finish_turn(choose_card)
                        else :
                                print("そのカードは出せません。もう一度選んでください。")
                                print("---------------------------------------------")
                                flag=False #また手札を出すところのループから抜け出していない。                             
               elif shibari== 0 :#縛りがない場合
                    if kakumei%2 != 0 : #奇数のとき。通常時    
                      if  eleven_back==0 : #イレブンバック起きてない。大小Trueかの判断
                        if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                            print("そのカードは出せます。カードを出しました.")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
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
                            print("そのカードは出せます。カードを出しました..")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
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
                            print("そのカードは出せます。カードを出しました...")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
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
                            print("そのカードは出せます。カードを出しました!")
                            #出したカードは手札から消す。
                            #出したカードは手札から消す。

                            try :
                                player4.remove(CP_card_1)
                                player4.remove(cp_card_2)
                                player4.remove(cp_card_3)
                                player4.remove(cp_card_4)
                                player4.remove(cp_card_5)
                                player4.remove(cp_card_6)
                            except Exception as e:
                                print("例外argsB:", e.args)
                                pass                 
                            print("カードを出した後のあなたの手札は",player4,"です。")       
                            if len(player4)==0 :
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
                            if (choose_card[-1][-2] >field_card[-1][-1][-2] )  :
                                print("そのカードは出せます。カードを出しました!!")
                                #出したカードは手札から消す。
                                #出したカードは手札から消す。
                                try :#出したカードを特定。a=[1,♥]のような形。消す前に特定しないとインデックスがずれるので先に定義しておく。
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                                    a=player4[CP_card_1]
                                    b=player4[cp_card_2]
                                    c=player4[cp_card_3]
                                    d=player4[cp_card_4]
                                    e=player4[cp_card_5]
                                    f=player4[cp_card_6]
                                except Exception as e:
                                    print("例外argsA:", e.args)
                                    pass 
                                try :
                                    player4.remove(CP_card_1)
                                    player4.remove(cp_card_2)
                                    player4.remove(cp_card_3)
                                    player4.remove(cp_card_4)
                                    player4.remove(cp_card_5)
                                    player4.remove(cp_card_6)
                                except Exception as e:
                                    print("例外argsB:", e.args)
                                    pass                 
                                print("カードを出した後のあなたの手札は",player4,"です。")       
                                if len(player4)==0 :
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
                a=player4[CP_card_1]
                b=player4[cp_card_2]
                c=player4[cp_card_3]
                d=player4[cp_card_4]
                e=player4[cp_card_5]
                f=player4[cp_card_6]
            except Exception as e:
                print("例外argD:", e.args)
                pass 
            try :
                player4.remove(CP_card_1)
                player4.remove(cp_card_2)
                player4.remove(cp_card_3)
                player4.remove(cp_card_4)
                player4.remove(cp_card_5)
                player4.remove(cp_card_6)
            except Exception as e:
                print("例外argsE:", e.args)
                pass                 
            print("カードを出した後のあなたの手札は",player4,"です。")
            if len(player4)==0 :
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


#CPが手札を出す関数------------------------------------------------------------------------------

player2=[[two, "♠"], [four, "♦"], [eleven, "♥"], [one, "♦"], [eleven, "♠"], [joker, joker], [one, "♠"], [twelve, "♦"], [eleven, "♠"], [two, "♣"], [eight, "♥"], [six, "♣"], [seven, "♣"]]
player3=[[two, "♠"], [four, "♦"], [eleven, "♥"], [one, "♦"], [eleven, "♠"], [joker, joker], [one, "♠"], [twelve, "♦"], [eleven, "♠"], [two, "♣"], [eight, "♥"], [six, "♣"], [seven, "♣"]]
player4=[[two, "♠"], [four, "♦"], [eleven, "♥"], [one, "♦"], [eleven, "♠"], [joker, joker], [one, "♠"], [twelve, "♦"], [eleven, "♠"], [two, "♣"], [eight, "♥"], [six, "♣"], [seven, "♣"]]

#★player2=daseruka_hanndann_CP1 用の手札を出す関数。ここがAIで強化するべきところ。課題の部分----------------------------------------
#今回のは適当に枚数に応じて選択するようにして、それが出せる（True）になるまで繰り返す。
#ただし、５，６枚出しはなし。関数つくってないから。

#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)

#1ターンの終了-------------------------------------------------------------------
#【以下繰り返し】






















#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
#【player2,daseruka_hanndann_CP1】
flag = False
sikou_kaisuu=0
while flag==False : 
    print("player2のターン")
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    if len(player2)==0 :
        print("player2は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :
         #上がってたら手札なくてエラー起きるため
         try :
          if len(field_card[0])==1 :
              CP_card_1=(random.choice(player2))
              CP_choose_card.append(CP_card_1)
              daseruka_hanndann_CP1(CP_choose_card)
         except :
          pass
         #8でfield_card=[]になった後にエラー起きるからtryにしておく。
         try :
          if len(field_card[0])==2 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==3 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         try :
          if len(field_card[0])==4 :
              CP_card_1=(random.choice(player2))
              CP_card_2=(random.choice(player2))
              CP_card_3=(random.choice(player2))
              CP_card_4=(random.choice(player2))
              daseruka_hanndann_CP1(CP_choose_card)
         except :
             pass
         #20回手札選び失敗したらパスするようにした。
         sikou_kaisuu+=1
         if sikou_kaisuu==20 :
               print("player2はパスしました。")
               flag=True
               pass_kosuu+=1
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   #リセットするときに縛りとイレブンバックも解除する。
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player2))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player2))
                CP_card_2=(random.choice(player2))
                CP_card_3=(random.choice(player2))
                CP_card_4=(random.choice(player2))
                daseruka_hanndann_CP1(CP_choose_card)
           except :
               pass
           #20回手札選び失敗したらパスするようにした。
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player2はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
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
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player3のターン")
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(player3)==0 :
        print("player3は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True
    if len(field_card) != 0 :
           try :
            if len(field_card[0])==1 :
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
               daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if len(field_card[0])==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if len(field_card)==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if len(field_card)==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player3))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player3))
                CP_card_2=(random.choice(player3))
                CP_card_3=(random.choice(player3))
                CP_card_4=(random.choice(player3))
                daseruka_hanndann_CP2(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               print("player3はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               pass_kosuu+=1
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0               
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player3))
           #     CP_card_2=(random.choice(player3))
           #     CP_card_3=(random.choice(player3))
           #     CP_card_4=(random.choice(player3))
           #     CP_card_5=(random.choice(player3))
           #     CP_card_6=(random.choice(player3))
           #     daseruka_hanndann_CP2(CP_choose_card)
        
#【player4,daseruka_hanndann_CP3】
flag = False
sikou_kaisuu=0
while flag==False : 
    flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
    CP_choose_card=[]
    print("player4のターン")
    if len(player4)==0 :
        print("playe4は上がりました。")
        #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
        flag=True 
    #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
    if len(field_card) != 0 :    
          try :
           if len(field_card[0])==1 :
               CP_card_1=(random.choice(player4))
               CP_choose_card.append(CP_card_1)
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==2 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==3 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          try :
           if len(field_card[0])==4 :
               CP_card_1=(random.choice(player4))
               CP_card_2=(random.choice(player4))
               CP_card_3=(random.choice(player4))
               CP_card_4=(random.choice(player4))
               daseruka_hanndann_CP3(CP_choose_card)
          except :
              pass
          sikou_kaisuu+=1
          if sikou_kaisuu == 20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   eleven_back=0 
                   shibari=0
                   field_card.clear()
                   pass_kosuu=0
               flag=True
          # if len(field_card)==5 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          # if len(field_card)==6 :
          #     CP_card_1=(random.choice(player4))
          #     CP_card_2=(random.choice(player4))
          #     CP_card_3=(random.choice(player4))
          #     CP_card_4=(random.choice(player4))
          #     CP_card_5=(random.choice(player4))
          #     CP_card_6=(random.choice(player4))
          #     daseruka_hanndann_CP3(CP_choose_card)
          #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
    if len(field_card)== 0 :
        while flag==False :
           CP_syote_maisuu=random.randint(1,4)
           print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
           try :
            if CP_syote_maisuu==1 :
                CP_card_1=(random.choice(player4))
                CP_choose_card.append(CP_card_1)
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           #len(field_card[0])という書き方ではないのが、手札０で上がってる場合はエラー起きるのでtryする。
           try :
            if CP_syote_maisuu==2 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==3 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           try :
            if CP_syote_maisuu==4 :
                CP_card_1=(random.choice(player4))
                CP_card_2=(random.choice(player4))
                CP_card_3=(random.choice(player4))
                CP_card_4=(random.choice(player4))
                daseruka_hanndann_CP3(CP_choose_card)
           except :
               pass
           sikou_kaisuu+=1
           if sikou_kaisuu==20 :
               pass_kosuu+=1
               print("player4はパスしました。")
               #パスが３つたまったらフィールドカードのリセット
               if pass_kosuu==3 :
                   print("全員パスなのでフィールドカードをリセットします。")
                   field_card.clear()
                   pass_kosuu=0
               flag=True
           # if CP_syote_maisuu==5 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)
           # if CP_syote_maisuu==6 :
           #     CP_card_1=(random.choice(player4))
           #     CP_card_2=(random.choice(player4))
           #     CP_card_3=(random.choice(player4))
           #     CP_card_4=(random.choice(player4))
           #     CP_card_5=(random.choice(player4))
           #     CP_card_6=(random.choice(player4))
           #     daseruka_hanndann_CP3(CP_choose_card)


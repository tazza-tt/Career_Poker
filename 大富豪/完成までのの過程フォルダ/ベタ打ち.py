# def player2_dasu() : 
#  global CP_card_1,cp_card_2,cp_card_3,cp_card_4,cp_card_5,cp_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     #毎回choose_cardはリセットしないとバグる
#     CP_choose_card=[]
#     if len(player2)==0 :
#         print("player2は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p2+=1
#         p2_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p2==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p2_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #------------------------------------------------------------------------------------------
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
#               if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
#                 list_daseru_mark=[]
#                 #フィールドカードのマークを抽出
#                 field_mark=field_card[-1][-1][-1]
#                 for i in range(len(player2)) :
#                     tehuda_mark_syutoku=player2[i][-1]
#                     #同じマークだった場合
#                     if field_mark == tehuda_mark_syutoku :
#                         kazu=player2[i][-2]
#                         sono_mark_index=i
#                         listA=[]
#                         listA.append(kazu)
#                         listA.append(sono_mark_index)
#                         list_daseru_mark.append(listA)
#                 # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                 try :
#                   onaji_mark_dasu_card=[]
#                   for i in range(len(list_daseru_mark)) : 
#                       onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                   #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                   CP_card_1=player2[random.choice(onaji_mark_dasu_card)]
#                   CP_choose_card.append(CP_card_1)
#                   daseruka_hanndann_CP1(CP_choose_card)
#                 except :
#                     print("ここがパスになってます")
#                     pass

#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#               if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player2))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                 #------------------------------------------------------------------------------------------
#          except :
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               CP_card_1=(random.choice(player2))
#               CP_card_2=(random.choice(player2))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               daseruka_hanndann_CP1(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               CP_card_1=(random.choice(player2))
#               CP_card_2=(random.choice(player2))
#               CP_card_3=(random.choice(player2))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               CP_choose_card.append(CP_card_3)
#               daseruka_hanndann_CP1(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               CP_card_1=(random.choice(player2))
#               CP_card_2=(random.choice(player2))
#               CP_card_3=(random.choice(player2))
#               CP_card_4=(random.choice(player2))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               CP_choose_card.append(CP_card_3)
#               CP_choose_card.append(CP_card_4)
#               daseruka_hanndann_CP1(CP_choose_card)
#          except :
#              pass
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player2はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     CP_card_6=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player2_check_kakumei()はplayer2が革命できる手札をもってるかどうか、また、player2の手札的に革命をするべきかどうかを判断する
#            player2_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 print(list_kakumei_onzon_suuji_with_index)
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP1(CP_choose_card)

#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。
#            elif  sikou_kaisuu >= 10 :
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player2))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         CP_card_1=(random.choice(player2))
#                         CP_card_2=(random.choice(player2))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         CP_card_1=(random.choice(player2))
#                         CP_card_2=(random.choice(player2))
#                         CP_card_3=(random.choice(player2))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         CP_card_1=(random.choice(player2))
#                         CP_card_2=(random.choice(player2))
#                         CP_card_3=(random.choice(player2))
#                         CP_card_4=(random.choice(player2))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         CP_choose_card.append(CP_card_4)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e  :
#                     print(e.args)
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1
#                 if sikou_kaisuu==10000 :
#                     print("player2はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     CP_card_6=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)

# def player3_dasu() : 
#  global CP_card_1,cp_card_2,cp_card_3,cp_card_4,cp_card_5,cp_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     CP_choose_card=[]
#     if len(player3)==0 :
#         print("player3は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p3+=1
#         p3_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p3==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p3_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
#               if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
#                 list_daseru_mark=[]
#                 #フィールドカードのマークを抽出
#                 field_mark=field_card[-1][-1][-1]
#                 for i in range(len(player3)) :
#                     tehuda_mark_syutoku=player3[i][-1]
#                     #同じマークだった場合
#                     if field_mark == tehuda_mark_syutoku :
#                         kazu=player3[i][-2]
#                         sono_mark_index=i
#                         listA=[]
#                         listA.append(kazu)
#                         listA.append(sono_mark_index)
#                         list_daseru_mark.append(listA)
#                 # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                 try :
#                   onaji_mark_dasu_card=[]
#                   for i in range(len(list_daseru_mark)) : 
#                       onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                   #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                   CP_card_1=player3[random.choice(onaji_mark_dasu_card)]
#                   CP_choose_card.append(CP_card_1)
#                   daseruka_hanndann_CP2(CP_choose_card)
#                 except :
#                     print("ここがパスになってます")
#                     pass

#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#               if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP2(CP_choose_card)
#          except :
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               CP_card_1=(random.choice(player3))
#               CP_card_2=(random.choice(player3))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               daseruka_hanndann_CP2(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               CP_card_1=(random.choice(player3))
#               CP_card_2=(random.choice(player3))
#               CP_card_3=(random.choice(player3))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               CP_choose_card.append(CP_card_3)
#               daseruka_hanndann_CP2(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               CP_card_1=(random.choice(player3))
#               CP_card_2=(random.choice(player3))
#               CP_card_3=(random.choice(player3))
#               CP_card_4=(random.choice(player3))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               CP_choose_card.append(CP_card_3)
#               CP_choose_card.append(CP_card_4)
#               daseruka_hanndann_CP2(CP_choose_card)
#          except :
#              pass
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player3はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player3))
#          #     CP_card_2=(random.choice(player3))
#          #     CP_card_3=(random.choice(player3))
#          #     CP_card_4=(random.choice(player3))
#          #     CP_card_5=(random.choice(player3))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player3))
#          #     CP_card_2=(random.choice(player3))
#          #     CP_card_3=(random.choice(player3))
#          #     CP_card_4=(random.choice(player3))
#          #     CP_card_5=(random.choice(player3))
#          #     CP_card_6=(random.choice(player3))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player3_check_kakumei()はplayer3が革命できる手札をもってるかどうか、また、player3の手札的に革命をするべきかどうかを判断する
#            player3_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 print(list_kakumei_onzon_suuji_with_index)
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP2(CP_choose_card)
                
#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。
#            elif  sikou_kaisuu >= 10 :
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player3が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         CP_card_1=(random.choice(player3))
#                         CP_card_2=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         CP_card_1=(random.choice(player3))
#                         CP_card_2=(random.choice(player3))
#                         CP_card_3=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         CP_card_1=(random.choice(player3))
#                         CP_card_2=(random.choice(player3))
#                         CP_card_3=(random.choice(player3))
#                         CP_card_4=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         CP_choose_card.append(CP_card_4)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e  :
#                     print(e.args)
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1
#                 if sikou_kaisuu==10000 :
#                     print("player3はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player3))
#                 #     CP_card_2=(random.choice(player3))
#                 #     CP_card_3=(random.choice(player3))
#                 #     CP_card_4=(random.choice(player3))
#                 #     CP_card_5=(random.choice(player3))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player3))
#                 #     CP_card_2=(random.choice(player3))
#                 #     CP_card_3=(random.choice(player3))
#                 #     CP_card_4=(random.choice(player3))
#                 #     CP_card_5=(random.choice(player3))
#                 #     CP_card_6=(random.choice(player3))
#                 #     daseruka_hanndann_CP1(CP_choose_card)

# def player4_dasu() : 
#  global CP_card_1,cp_card_2,cp_card_3,cp_card_4,cp_card_5,cp_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     CP_choose_card=[]
#     if len(player4)==0 :
#         print("player4は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p4+=1
#         p4_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p4==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p4_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #------------------------------------------------------------------------------------------
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
#               if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
#                 list_daseru_mark=[]
#                 #フィールドカードのマークを抽出
#                 field_mark=field_card[-1][-1][-1]
#                 for i in range(len(player4)) :
#                     tehuda_mark_syutoku=player4[i][-1]
#                     #同じマークだった場合
#                     if field_mark == tehuda_mark_syutoku :
#                         kazu=player4[i][-2]
#                         sono_mark_index=i
#                         listA=[]
#                         listA.append(kazu)
#                         listA.append(sono_mark_index)
#                         list_daseru_mark.append(listA)
#                 # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                 try :
#                   onaji_mark_dasu_card=[]
#                   for i in range(len(list_daseru_mark)) : 
#                       onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                   #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                   CP_card_1=player4[random.choice(onaji_mark_dasu_card)]
#                   CP_choose_card.append(CP_card_1)
#                   daseruka_hanndann_CP3(CP_choose_card)
#                 except :
#                     print("ここがパスになってます")
#                     pass

#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#               if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 #------------------------------------------------------------------------------------------
#          except :
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               CP_card_1=(random.choice(player4))
#               CP_card_2=(random.choice(player4))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               daseruka_hanndann_CP3(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               CP_card_1=(random.choice(player4))
#               CP_card_2=(random.choice(player4))
#               CP_card_3=(random.choice(player4))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               CP_choose_card.append(CP_card_3)
#               daseruka_hanndann_CP3(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               CP_card_1=(random.choice(player4))
#               CP_card_2=(random.choice(player4))
#               CP_card_3=(random.choice(player4))
#               CP_card_4=(random.choice(player4))
#               CP_choose_card.append(CP_card_1)
#               CP_choose_card.append(CP_card_2)
#               CP_choose_card.append(CP_card_3)
#               CP_choose_card.append(CP_card_4)
#               daseruka_hanndann_CP3(CP_choose_card)
#          except :
#              pass
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player4はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player4))
#          #     CP_card_2=(random.choice(player4))
#          #     CP_card_3=(random.choice(player4))
#          #     CP_card_4=(random.choice(player4))
#          #     CP_card_5=(random.choice(player4))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player4))
#          #     CP_card_2=(random.choice(player4))
#          #     CP_card_3=(random.choice(player4))
#          #     CP_card_4=(random.choice(player4))
#          #     CP_card_5=(random.choice(player4))
#          #     CP_card_6=(random.choice(player4))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player4_check_kakumei()はplayer4が革命できる手札をもってるかどうか、また、player4の手札的に革命をするべきかどうかを判断する
#            player4_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 print(list_kakumei_onzon_suuji_with_index)
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP3(CP_choose_card)
                
#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。
#            elif  sikou_kaisuu >= 10 :
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player4が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         CP_card_1=(random.choice(player4))
#                         CP_card_2=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         CP_card_1=(random.choice(player4))
#                         CP_card_2=(random.choice(player4))
#                         CP_card_3=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         CP_card_1=(random.choice(player4))
#                         CP_card_2=(random.choice(player4))
#                         CP_card_3=(random.choice(player4))
#                         CP_card_4=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         CP_choose_card.append(CP_card_4)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e  :
#                     print(e.args)
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1
#                 if sikou_kaisuu==10000 :
#                     print("player4はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player4))
#                 #     CP_card_2=(random.choice(player4))
#                 #     CP_card_3=(random.choice(player4))
#                 #     CP_card_4=(random.choice(player4))
#                 #     CP_card_5=(random.choice(player4))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player4))
#                 #     CP_card_2=(random.choice(player4))
#                 #     CP_card_3=(random.choice(player4))
#                 #     CP_card_4=(random.choice(player4))
#                 #     CP_card_5=(random.choice(player4))
#                 #     CP_card_6=(random.choice(player4))
#                 #     daseruka_hanndann_CP1(CP_choose_card)

# def check_pea_player2() :
#           global  list_onzon_suuji_with_index_pea_3mai,list_onzon_suuji_with_index_pea_2mai,joker_index_3mai,joker_index_2mai
#           # can_kakumei=False
#           list_only_num=[]
#           onzon_suuji=[]
#           joker_maisuu=0
#           onzon_suuji_pea_3mai=[]
#           list_onzon_suuji_with_index_pea_3mai=[]
#           list_onzon_suuji_with_index_pea_2mai=[]
#           joker_index_3mai=[]
#           joker_index_2mai=[]
#           list_tyouhuku_husegu=[]
#           tt=0

#           for i in range(len(player2)) :
#                list_only_num.append(player2[i][0])
#           #2枚以上じゃないとペアができないため。
#           if len(list_only_num) >= 2 :
               
#                for i in range(len(list_only_num)) :
#                     if (joker in player2[i] ) :
#                        joker_maisuu+=1
#                print("jokerの枚数は",joker_maisuu,"枚です。")

#                #joker枚数が２枚の時
#                if joker_maisuu == 2 :
#                #joker_index=[2,3]２，３とあと一枚好きな数字出せば３枚のペアができる。
#                   joker_index_3mai= [n for n, x in enumerate(list_only_num) if x == joker]
#                   print(joker_index_3mai,"の要素を使ってあと一枚だせば３枚のペアをだせます。")

#                   #jokerを使わないで２枚、３枚出せるものを抽出する。 
#                   for i in range(len(player2)) :
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #jokerなしで純粋な同じ数３枚 .ただしそのカードがjokerではないとする。 
#                          if (list_only_num.count(list_only_num[i]) == 3  and (list_only_num[i] != joker)):
#                               onzon_suuji.append(list_only_num[i])
#                               #ループのため、重複で同じ数字を入れるのを防ぐため。
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
#                          #jokerなしで純粋に同じ数字が２枚ある場合。ただしそのカードがjokerではないとする。
#                          if  (list_only_num.count(list_only_num[i]) == 2 and (list_only_num[i] != joker)) :
#                               onzon_suuji.append(list_only_num[i])
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
#                                    list_onzon_suuji_with_index_pea_2mai.append(listA)



#                #joker枚数が１枚のとき
#                if joker_maisuu == 1 :
#                     num_index_joker=list_only_num.index(joker)
#                     for i in range(len(player2)) :
#                          #ここでonzon_suujiをリセットしておかないと、重複してはいってしまう。
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #joker1枚、ペア２枚。それを使った３枚のペアの作り方を抽出する。
#                          #list_onzon_suuji_with_index_pea_3mai=[[One],[2,3,4]]とかで抽出するのがゴール

#                          if list_only_num.count(list_only_num[i])==2 :
#                               onzon_suuji.append(list_only_num[i])
#                               #tyouhuku_huseguで一度入った数字は入れないようにする。
#                               if (list_only_num[i] not in  list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    print(list_only_num[i],"とjoker使って3枚のペアが作れます。")
#                                    print(list_only_num[i],"を使って2枚のペアが作れます。（jokerは使わない）")
#                                    listA=[]
#                                    #jokerを使わない2枚ペア用
#                                    listB=[]
#                                    #listB用。
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    #listA用。同じやつつかってるとバグるからnum_2として分ける。
#                                    num_2= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]

#                                    #jokerを含めないインデックスだけ先にlistBにapendしておく必要がある。３枚ペアと２枚ペアで区別するために。
#                                    listB.append(onzon_suuji)
#                                    listB.append(num)

#                                    #jokerを含めたインデックス.3枚ペア用.jokerのインデックスをいれる
#                                    num_2.append(num_index_joker)
#                                    listA.append(onzon_suuji)
#                                    listA.append(num_2)

#                                    #jokerをいれた３枚のペアのためのインデックス
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
#                                    #jokerを入れないで純粋な２枚のペアのためのインデックス
#                                    list_onzon_suuji_with_index_pea_2mai.append(listB)

#                                    print(list_onzon_suuji_with_index_pea_3mai)
#                                    print(list_onzon_suuji_with_index_pea_2mai)

#                          #３枚同じカードがある場合。→　1枚のjokerと３枚の同じカードだから革命のほうでも拾えてるか。そのときどうせ革命優先するんだから必要ないか
#                          #  if list_only_num.count(list_only_num[i])==3 :
                              
#                          #joker1枚と数字１枚のとき、２ペアができる。
#                          if list_only_num.count(joker)==1 :
#                          #jokerのインデックスのみ。これとあと1枚好きな数字出せば、２ペアができる。
#                             tt=tt+1
#                          #一回しか処理されないようにした
#                          if tt == 1 :
#                               joker_index_2mai.append(num_index_joker) 
               
#                #jokerの枚数が０のとき
#                if joker_maisuu== 0 :
#                     for i in range(len(player2)) :
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #jokerなしで純粋な同じ数所３枚
#                          if list_only_num.count(list_only_num[i]) == 3 :
#                               onzon_suuji.append(list_only_num[i])
#                               #ループのため、重複で同じ数字を入れるのを防ぐため。
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
#                          #jokerなしで純粋に同じ数字が２枚ある場合。
#                          if  list_only_num.count(list_only_num[i]) == 2 :
#                               onzon_suuji.append(list_only_num[i])
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
#                                    list_onzon_suuji_with_index_pea_2mai.append(listA)
#           print("ジョーカー2枚のインデックスは",joker_index_3mai)
#           #ジョーカー2枚のインデックスは []
#           print("ジョーカー１枚のインデックスは",joker_index_2mai)
#           #ジョーカー１枚のインデックスは [12, 12, 12]
#           print("3枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_3mai)
#           #3枚のペアを出せるその数字とインデックスは [[['11'], [3, 9, 10]]]
#           print("ジョーカーを使わず2枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_2mai)
#           #ジョーカーを使わず2枚のペアを出せるその数字とインデックスは [[['09'], [0, 7]]]

# def check_pea_player3() :
#           global  list_onzon_suuji_with_index_pea_3mai,list_onzon_suuji_with_index_pea_2mai,joker_index_3mai,joker_index_2mai
#           # can_kakumei=False
#           list_only_num=[]
#           onzon_suuji=[]
#           joker_maisuu=0
#           onzon_suuji_pea_3mai=[]
#           list_onzon_suuji_with_index_pea_3mai=[]
#           list_onzon_suuji_with_index_pea_2mai=[]
#           joker_index_3mai=[]
#           joker_index_2mai=[]
#           list_tyouhuku_husegu=[]
#           tt=0

#           for i in range(len(player3)) :
#                list_only_num.append(player3[i][0])
#           #2枚以上じゃないとペアができないため。
#           if len(list_only_num) >= 2 :
               
#                for i in range(len(list_only_num)) :
#                     if (joker in player3[i] ) :
#                        joker_maisuu+=1
#                print("jokerの枚数は",joker_maisuu,"枚です。")

#                #joker枚数が２枚の時
#                if joker_maisuu == 2 :
#                #joker_index=[2,3]２，３とあと一枚好きな数字出せば３枚のペアができる。
#                   joker_index_3mai= [n for n, x in enumerate(list_only_num) if x == joker]
#                   print(joker_index_3mai,"の要素を使ってあと一枚だせば３枚のペアをだせます。")

#                   #jokerを使わないで２枚、３枚出せるものを抽出する。 
#                   for i in range(len(player3)) :
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #jokerなしで純粋な同じ数３枚 .ただしそのカードがjokerではないとする。 
#                          if (list_only_num.count(list_only_num[i]) == 3  and (list_only_num[i] != joker)):
#                               onzon_suuji.append(list_only_num[i])
#                               #ループのため、重複で同じ数字を入れるのを防ぐため。
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
#                          #jokerなしで純粋に同じ数字が２枚ある場合。ただしそのカードがjokerではないとする。
#                          if  (list_only_num.count(list_only_num[i]) == 2 and (list_only_num[i] != joker)) :
#                               onzon_suuji.append(list_only_num[i])
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
#                                    list_onzon_suuji_with_index_pea_2mai.append(listA)



#                #joker枚数が１枚のとき
#                if joker_maisuu == 1 :
#                     num_index_joker=list_only_num.index(joker)
#                     for i in range(len(player3)) :
#                          #ここでonzon_suujiをリセットしておかないと、重複してはいってしまう。
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #joker1枚、ペア２枚。それを使った３枚のペアの作り方を抽出する。
#                          #list_onzon_suuji_with_index_pea_3mai=[[One],[2,3,4]]とかで抽出するのがゴール

#                          if list_only_num.count(list_only_num[i])==2 :
#                               onzon_suuji.append(list_only_num[i])
#                               #tyouhuku_huseguで一度入った数字は入れないようにする。
#                               if (list_only_num[i] not in  list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    print(list_only_num[i],"とjoker使って3枚のペアが作れます。")
#                                    print(list_only_num[i],"を使って2枚のペアが作れます。（jokerは使わない）")
#                                    listA=[]
#                                    #jokerを使わない2枚ペア用
#                                    listB=[]
#                                    #listB用。
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    #listA用。同じやつつかってるとバグるからnum_2として分ける。
#                                    num_2= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]

#                                    #jokerを含めないインデックスだけ先にlistBにapendしておく必要がある。３枚ペアと２枚ペアで区別するために。
#                                    listB.append(onzon_suuji)
#                                    listB.append(num)

#                                    #jokerを含めたインデックス.3枚ペア用.jokerのインデックスをいれる
#                                    num_2.append(num_index_joker)
#                                    listA.append(onzon_suuji)
#                                    listA.append(num_2)

#                                    #jokerをいれた３枚のペアのためのインデックス
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
#                                    #jokerを入れないで純粋な２枚のペアのためのインデックス
#                                    list_onzon_suuji_with_index_pea_2mai.append(listB)

#                                    print(list_onzon_suuji_with_index_pea_3mai)
#                                    print(list_onzon_suuji_with_index_pea_2mai)

#                          #３枚同じカードがある場合。→　1枚のjokerと３枚の同じカードだから革命のほうでも拾えてるか。そのときどうせ革命優先するんだから必要ないか
#                          #  if list_only_num.count(list_only_num[i])==3 :
                              
#                          #joker1枚と数字１枚のとき、２ペアができる。
#                          if list_only_num.count(joker)==1 :
#                          #jokerのインデックスのみ。これとあと1枚好きな数字出せば、２ペアができる。
#                             tt=tt+1
#                          #一回しか処理されないようにした
#                          if tt == 1 :
#                               joker_index_2mai.append(num_index_joker) 
               
#                #jokerの枚数が０のとき
#                if joker_maisuu== 0 :
#                     for i in range(len(player3)) :
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #jokerなしで純粋な同じ数所３枚
#                          if list_only_num.count(list_only_num[i]) == 3 :
#                               onzon_suuji.append(list_only_num[i])
#                               #ループのため、重複で同じ数字を入れるのを防ぐため。
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
#                          #jokerなしで純粋に同じ数字が２枚ある場合。
#                          if  list_only_num.count(list_only_num[i]) == 2 :
#                               onzon_suuji.append(list_only_num[i])
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
#                                    list_onzon_suuji_with_index_pea_2mai.append(listA)
#           print("ジョーカー2枚のインデックスは",joker_index_3mai)
#           #ジョーカー2枚のインデックスは []
#           print("ジョーカー１枚のインデックスは",joker_index_2mai)
#           #ジョーカー１枚のインデックスは [12, 12, 12]
#           print("3枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_3mai)
#           #3枚のペアを出せるその数字とインデックスは [[['11'], [3, 9, 10]]]
#           print("ジョーカーを使わず2枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_2mai)
#           #ジョーカーを使わず2枚のペアを出せるその数字とインデックスは [[['09'], [0, 7]]]

# def check_pea_player4() :
#           global  list_onzon_suuji_with_index_pea_3mai,list_onzon_suuji_with_index_pea_2mai,joker_index_3mai,joker_index_2mai
#           # can_kakumei=False
#           list_only_num=[]
#           onzon_suuji=[]
#           joker_maisuu=0
#           onzon_suuji_pea_3mai=[]
#           list_onzon_suuji_with_index_pea_3mai=[]
#           list_onzon_suuji_with_index_pea_2mai=[]
#           joker_index_3mai=[]
#           joker_index_2mai=[]
#           list_tyouhuku_husegu=[]
#           tt=0

#           for i in range(len(player4)) :
#                list_only_num.append(player4[i][0])
#           #2枚以上じゃないとペアができないため。
#           if len(list_only_num) >= 2 :
               
#                for i in range(len(list_only_num)) :
#                     if (joker in player4[i] ) :
#                        joker_maisuu+=1
#                print("jokerの枚数は",joker_maisuu,"枚です。")

#                #joker枚数が２枚の時
#                if joker_maisuu == 2 :
#                #joker_index=[2,3]２，３とあと一枚好きな数字出せば３枚のペアができる。
#                   joker_index_3mai= [n for n, x in enumerate(list_only_num) if x == joker]
#                   print(joker_index_3mai,"の要素を使ってあと一枚だせば３枚のペアをだせます。")

#                   #jokerを使わないで２枚、３枚出せるものを抽出する。 
#                   for i in range(len(player4)) :
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #jokerなしで純粋な同じ数３枚 .ただしそのカードがjokerではないとする。 
#                          if (list_only_num.count(list_only_num[i]) == 3  and (list_only_num[i] != joker)):
#                               onzon_suuji.append(list_only_num[i])
#                               #ループのため、重複で同じ数字を入れるのを防ぐため。
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
#                          #jokerなしで純粋に同じ数字が２枚ある場合。ただしそのカードがjokerではないとする。
#                          if  (list_only_num.count(list_only_num[i]) == 2 and (list_only_num[i] != joker)) :
#                               onzon_suuji.append(list_only_num[i])
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
#                                    list_onzon_suuji_with_index_pea_2mai.append(listA)



#                #joker枚数が１枚のとき
#                if joker_maisuu == 1 :
#                     num_index_joker=list_only_num.index(joker)
#                     for i in range(len(player4)) :
#                          #ここでonzon_suujiをリセットしておかないと、重複してはいってしまう。
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #joker1枚、ペア２枚。それを使った３枚のペアの作り方を抽出する。
#                          #list_onzon_suuji_with_index_pea_3mai=[[One],[2,3,4]]とかで抽出するのがゴール

#                          if list_only_num.count(list_only_num[i])==2 :
#                               onzon_suuji.append(list_only_num[i])
#                               #tyouhuku_huseguで一度入った数字は入れないようにする。
#                               if (list_only_num[i] not in  list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    print(list_only_num[i],"とjoker使って3枚のペアが作れます。")
#                                    print(list_only_num[i],"を使って2枚のペアが作れます。（jokerは使わない）")
#                                    listA=[]
#                                    #jokerを使わない2枚ペア用
#                                    listB=[]
#                                    #listB用。
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    #listA用。同じやつつかってるとバグるからnum_2として分ける。
#                                    num_2= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]

#                                    #jokerを含めないインデックスだけ先にlistBにapendしておく必要がある。３枚ペアと２枚ペアで区別するために。
#                                    listB.append(onzon_suuji)
#                                    listB.append(num)

#                                    #jokerを含めたインデックス.3枚ペア用.jokerのインデックスをいれる
#                                    num_2.append(num_index_joker)
#                                    listA.append(onzon_suuji)
#                                    listA.append(num_2)

#                                    #jokerをいれた３枚のペアのためのインデックス
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
#                                    #jokerを入れないで純粋な２枚のペアのためのインデックス
#                                    list_onzon_suuji_with_index_pea_2mai.append(listB)

#                                    print(list_onzon_suuji_with_index_pea_3mai)
#                                    print(list_onzon_suuji_with_index_pea_2mai)

#                          #３枚同じカードがある場合。→　1枚のjokerと３枚の同じカードだから革命のほうでも拾えてるか。そのときどうせ革命優先するんだから必要ないか
#                          #  if list_only_num.count(list_only_num[i])==3 :
                              
#                          #joker1枚と数字１枚のとき、２ペアができる。
#                          if list_only_num.count(joker)==1 :
#                          #jokerのインデックスのみ。これとあと1枚好きな数字出せば、２ペアができる。
#                             tt=tt+1
#                          #一回しか処理されないようにした
#                          if tt == 1 :
#                               joker_index_2mai.append(num_index_joker) 
               
#                #jokerの枚数が０のとき
#                if joker_maisuu== 0 :
#                     for i in range(len(player4)) :
#                          onzon_suuji=[]
#                          print(list_only_num[i],"が",list_only_num.count(list_only_num[i]),"個あります。")
#                          #jokerなしで純粋な同じ数所３枚
#                          if list_only_num.count(list_only_num[i]) == 3 :
#                               onzon_suuji.append(list_only_num[i])
#                               #ループのため、重複で同じ数字を入れるのを防ぐため。
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [m for m, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字３枚。[ [["one"],[2,3,4]] ]とかで入るはず。
#                                    list_onzon_suuji_with_index_pea_3mai.append(listA)
                         
#                          #jokerなしで純粋に同じ数字が２枚ある場合。
#                          if  list_only_num.count(list_only_num[i]) == 2 :
#                               onzon_suuji.append(list_only_num[i])
#                               if (list_only_num[i] not in list_tyouhuku_husegu) :
#                                    list_tyouhuku_husegu.append(list_only_num[i])
#                                    listA=[]
#                                    num= [o for o, x in enumerate(list_only_num) if x == list_only_num[i]]
#                                    listA.append(onzon_suuji)
#                                    listA.append(num)
#                                    #jokerなしで純粋な同じ数字２枚の数字とインデックスを抽出。[ [["One"],[2,3]]  ]
#                                    list_onzon_suuji_with_index_pea_2mai.append(listA)
#           print("ジョーカー2枚のインデックスは",joker_index_3mai)
#           #ジョーカー2枚のインデックスは []
#           print("ジョーカー１枚のインデックスは",joker_index_2mai)
#           #ジョーカー１枚のインデックスは [12, 12, 12]
#           print("3枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_3mai)
#           #3枚のペアを出せるその数字とインデックスは [[['11'], [3, 9, 10]]]
#           print("ジョーカーを使わず2枚のペアを出せるその数字とインデックスは",list_onzon_suuji_with_index_pea_2mai)
#           #ジョーカーを使わず2枚のペアを出せるその数字とインデックスは [[['09'], [0, 7]]]

# def player3_dasu() : 
#  global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     #毎回choose_cardはリセットしないとバグる
#     CP_choose_card=[]
#     if len(player3)==0 :
#         print("player3は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p3+=1
#         p3_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p3==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p3_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #------------------------------------------------------------------------------------------
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
#               if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
#                 list_daseru_mark=[]
#                 #フィールドカードのマークを抽出
#                 field_mark=field_card[-1][-1][-1]
#                 for i in range(len(player3)) :
#                     tehuda_mark_syutoku=player3[i][-1]
#                     #同じマークだった場合
#                     if field_mark == tehuda_mark_syutoku :
#                         kazu=player3[i][-2]
#                         sono_mark_index=i
#                         listA=[]
#                         listA.append(kazu)
#                         listA.append(sono_mark_index)
#                         list_daseru_mark.append(listA)
#                 # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                 try :
#                   onaji_mark_dasu_card=[]
#                   for i in range(len(list_daseru_mark)) : 
#                       onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                   #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                   CP_card_1=player3[random.choice(onaji_mark_dasu_card)]
#                   CP_choose_card.append(CP_card_1)
#                   daseruka_hanndann_CP2(CP_choose_card)
#                 except :
#                     print("ここがパスになってます")
#                     pass

#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#               if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 #------------------------------------------------------------------------------------------
#          except :
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               rand1=random.choice(player3)
#               CP_card_1=(rand1)
#               rand2=random.choice(player3)
#               CP_card_2=(rand2)
#               #まったく同じカードが選ばれないようにしたい
#               if rand1 != rand2 :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  daseruka_hanndann_CP2(CP_choose_card)
#                  #消しておかないと、のちのち定義したままになって余計な手札まで消してしまう。
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               rand1=random.choice(player3)
#               CP_card_1=(rand1)
#               rand2=random.choice(player3)
#               CP_card_2=(rand2)
#               rand3=random.choice(player3)
#               CP_card_3=(rand3)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  daseruka_hanndann_CP2(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               rand1=random.choice(player3)
#               CP_card_1=(rand1)
#               rand2=random.choice(player3)              
#               CP_card_2=(rand2)
#               rand3=random.choice(player3)
#               CP_card_3=(rand3)
#               rand4=random.choice(player3)
#               CP_card_4=(rand4)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  CP_choose_card.append(CP_card_4)
#                  daseruka_hanndann_CP2(CP_choose_card)
#          except :
#              pass
#          try :
#              del CP_card_1
#              del CP_card_2
#              del CP_card_3
#              del CP_card_4
#          except :
#             pass 
                 
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player2はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     CP_card_6=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player2_check_kakumei()はplayer2が革命できる手札をもってるかどうか、また、player2の手札的に革命をするべきかどうかを判断する
#            player3_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 print(list_kakumei_onzon_suuji_with_index)
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP2(CP_choose_card)

#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。

#            #----------------------------------------------------------------------------------------------------------------------------------------
           
#            #★Ａｉを強くするためなるべくペアで出すようにする。
#            #革命が第一で優先されるため、do_kakumeiがFalse1で革命ができないときに２枚以上のペアで出すようにする。
#            elif ((10 <= sikou_kaisuu <= 20) and (do_kakumei==False)) :
#                check_pea_player3()
#                CP_choose_card=[]
#                """
#                下記の順でカードを出そうとする。
#                ジョーカーを使って１枚つかって３枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_3mai=[[['数字'], [8, 9, 10]]] これで３枚のペアをだす    
#                ↓
#                ジョーカーを使わず2枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_2mai=[[['数字'], [0, 7]]] これで２枚のペアを出す  
#                ↓
#                ジョーカー2枚のインデックスは joker_index_3mai=[○, ○]。これでjokerを使って、3枚のペアをだす 
#                ↓
#                ジョーカー１枚のインデックスは joker_index_2mai=[○]。これでjokerを使って。2枚のペアをだす。  
#                """

#                #jokerを１枚つかって３枚のペアを出す。例：[[['数字'], [8, 9, 10]]]
#                try : 
#                    if flag==False :
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(list_onzon_suuji_with_index_pea_3mai))
#                         print("1111111111111111111111111")
#                         #出す数字はランダムに出すことにする。
#                         #１個ずれてindex error 起きるから、[rand-1]にしておかないと
#                         CP_card_1=player3[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][0]]
#                         CP_card_2=player3[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][1]]
#                         CP_card_3=player3[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][2]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                         #上記関数で出せる判断ならflag=Trueになってるはず。下の３つの関数が起動しないようにflagで処理を起こすかどうかを場合分けする。
#                except Exception as e :
#                     print(e.args)
#                     pass
               
#                #jokerを使わずに2枚のペアを出す。例：[[['数字'], [0, 7]]]
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if (flag==False) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
#                         print("222222222222222")
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(player3))
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player3[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][0]]
#                         CP_card_2=player3[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][1]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                except Exception as e :
#                     print(e.args)
#                     pass


#                #joker２枚を使って3枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    #(average_tehuda <= 7)なら、ここの処理はdo_kakuemeiがFalse前提なんだし、いくらjokerを温存してても革命はできないんだから、手札の平均数字が７以下ならjokerを使っちゃう。
#                    if ((flag==False) and (average_tehuda <= 7)) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
#                         print("333333333333333333333")
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player3[joker_index_3mai[0]]
#                         CP_card_2=player3[joker_index_3mai[1]]
#                         k=random.randint(1,len(player3))
#                         #joker２枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if ((k != joker_index_3mai[0]) and (k != joker_index_3mai[1])) : 
#                              CP_card_3=player3[joker_index_3mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              daseruka_hanndann_CP2(CP_choose_card)
#                except Exception as e :
#                     print(e.args)
#                     pass

#                #jokerを１枚使って2枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if ((flag==False) and (average_tehuda <= 7))  :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
#                         print("444444444444444444444444")
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player3[joker_index_2mai[0]]
#                         k=random.randint(1,len(player3))
#                         #joker1枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if (k != joker_index_2mai[1]) : 
#                              CP_card_2=player3[joker_index_2mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              daseruka_hanndann_CP2(CP_choose_card)
#                except Exception as e :
#                     print(e.args)
#                     pass              

#            #------------------------------------------------------------------------------

#            elif  sikou_kaisuu >= 20 :
#                 print("5555555555555555555555555")
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         rand1=random.choice(player3)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player3)
#                         CP_card_2=(rand2)
#                         #まったく同じカードが選択されないようにするため。
#                         if (rand1 != rand2) :
#                            CP_choose_card.append(CP_card_1)
#                            CP_choose_card.append(CP_card_2)
#                            daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         rand1=random.choice(player3)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player3)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player3)
#                         CP_card_3=(rand3)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)):                        
#                             CP_choose_card.append(CP_card_1)
#                             CP_choose_card.append(CP_card_2)
#                             CP_choose_card.append(CP_card_3)
#                             daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         rand1=random.choice(player3)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player3)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player3)
#                         CP_card_3=(rand3)
#                         rand4=random.choice(player3)
#                         CP_card_4=(rand4)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              CP_choose_card.append(CP_card_4)
#                              daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e  :
#                     print(e.args)
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1

#                 try :
#                     del CP_card_1
#                     del CP_card_2
#                     del CP_card_3
#                     del CP_card_4
#                 except :
#                     pass

#                 if sikou_kaisuu==10000 :
#                     print("player2はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True

#                     try :
#                         del CP_card_1
#                         del CP_card_2
#                         del CP_card_3
#                         del CP_card_4
#                     except :
#                         pass                    
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     CP_card_6=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
               
# def player4_dasu() : 
#  global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     #毎回choose_cardはリセットしないとバグる
#     CP_choose_card=[]
#     if len(player4)==0 :
#         print("player4は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p4+=1
#         p4_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p4==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p4_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #------------------------------------------------------------------------------------------
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
#               if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu<=10)) :
#                 list_daseru_mark=[]
#                 #フィールドカードのマークを抽出
#                 field_mark=field_card[-1][-1][-1]
#                 for i in range(len(player4)) :
#                     tehuda_mark_syutoku=player4[i][-1]
#                     #同じマークだった場合
#                     if field_mark == tehuda_mark_syutoku :
#                         kazu=player4[i][-2]
#                         sono_mark_index=i
#                         listA=[]
#                         listA.append(kazu)
#                         listA.append(sono_mark_index)
#                         list_daseru_mark.append(listA)
#                 # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                 try :
#                   onaji_mark_dasu_card=[]
#                   for i in range(len(list_daseru_mark)) : 
#                       onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                   #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                   CP_card_1=player4[random.choice(onaji_mark_dasu_card)]
#                   CP_choose_card.append(CP_card_1)
#                   daseruka_hanndann_CP3(CP_choose_card)
#                 except :
#                     print("ここがパスになってます")
#                     pass

#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#               if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 #------------------------------------------------------------------------------------------
#          except :
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               rand1=random.choice(player4)
#               CP_card_1=(rand1)
#               rand2=random.choice(player4)
#               CP_card_2=(rand2)
#               #まったく同じカードが選ばれないようにしたい
#               if rand1 != rand2 :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  daseruka_hanndann_CP3(CP_choose_card)
#                  #消しておかないと、のちのち定義したままになって余計な手札まで消してしまう。
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               rand1=random.choice(player4)
#               CP_card_1=(rand1)
#               rand2=random.choice(player4)
#               CP_card_2=(rand2)
#               rand3=random.choice(player4)
#               CP_card_3=(rand3)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  daseruka_hanndann_CP3(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               rand1=random.choice(player4)
#               CP_card_1=(rand1)
#               rand2=random.choice(player4)              
#               CP_card_2=(rand2)
#               rand3=random.choice(player4)
#               CP_card_3=(rand3)
#               rand4=random.choice(player4)
#               CP_card_4=(rand4)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  CP_choose_card.append(CP_card_4)
#                  daseruka_hanndann_CP3(CP_choose_card)
#          except :
#              pass
#          try :
#              del CP_card_1
#              del CP_card_2
#              del CP_card_3
#              del CP_card_4
#          except :
#             pass 
                 
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player2はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     CP_card_6=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player2_check_kakumei()はplayer2が革命できる手札をもってるかどうか、また、player2の手札的に革命をするべきかどうかを判断する
#            player4_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 print(list_kakumei_onzon_suuji_with_index)
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP3(CP_choose_card)

#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。

#            #----------------------------------------------------------------------------------------------------------------------------------------
           
#            #★Ａｉを強くするためなるべくペアで出すようにする。
#            #革命が第一で優先されるため、do_kakumeiがFalse1で革命ができないときに２枚以上のペアで出すようにする。
#            elif ((10 <= sikou_kaisuu <= 20) and (do_kakumei==False)) :
#                check_pea_player4()
#                CP_choose_card=[]
#                """
#                下記の順でカードを出そうとする。
#                ジョーカーを使って１枚つかって３枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_3mai=[[['数字'], [8, 9, 10]]] これで３枚のペアをだす    
#                ↓
#                ジョーカーを使わず2枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_2mai=[[['数字'], [0, 7]]] これで２枚のペアを出す  
#                ↓
#                ジョーカー2枚のインデックスは joker_index_3mai=[○, ○]。これでjokerを使って、3枚のペアをだす 
#                ↓
#                ジョーカー１枚のインデックスは joker_index_2mai=[○]。これでjokerを使って。2枚のペアをだす。  
#                """

#                #jokerを１枚つかって３枚のペアを出す。例：[[['数字'], [8, 9, 10]]]
#                try : 
#                    if flag==False :
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(list_onzon_suuji_with_index_pea_3mai))
#                         print("1111111111111111111111111")
#                         #出す数字はランダムに出すことにする。
#                         #１個ずれてindex error 起きるから、[rand-1]にしておかないと
#                         CP_card_1=player4[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][0]]
#                         CP_card_2=player4[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][1]]
#                         CP_card_3=player4[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][2]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                         #上記関数で出せる判断ならflag=Trueになってるはず。下の３つの関数が起動しないようにflagで処理を起こすかどうかを場合分けする。
#                except Exception as e :
#                     print(e.args)
#                     pass
               
#                #jokerを使わずに2枚のペアを出す。例：[[['数字'], [0, 7]]]
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if (flag==False) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
#                         print("222222222222222")
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(player4))
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player4[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][0]]
#                         CP_card_2=player4[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][1]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                except Exception as e :
#                     print(e.args)
#                     pass


#                #joker２枚を使って3枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    #(average_tehuda <= 7)なら、ここの処理はdo_kakuemeiがFalse前提なんだし、いくらjokerを温存してても革命はできないんだから、手札の平均数字が７以下ならjokerを使っちゃう。
#                    if ((flag==False) and (average_tehuda <= 7)) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
#                         print("333333333333333333333")
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player4[joker_index_3mai[0]]
#                         CP_card_2=player4[joker_index_3mai[1]]
#                         k=random.randint(1,len(player4))
#                         #joker２枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if ((k != joker_index_3mai[0]) and (k != joker_index_3mai[1])) : 
#                              CP_card_3=player4[joker_index_3mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              daseruka_hanndann_CP3(CP_choose_card)
#                except Exception as e :
#                     print(e.args)
#                     pass

#                #jokerを１枚使って2枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if ((flag==False) and (average_tehuda <= 7))  :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
#                         print("444444444444444444444444")
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player4[joker_index_2mai[0]]
#                         k=random.randint(1,len(player4))
#                         #joker1枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if (k != joker_index_2mai[1]) : 
#                              CP_card_2=player4[joker_index_2mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              daseruka_hanndann_CP3(CP_choose_card)
#                except Exception as e :
#                     print(e.args)
#                     pass              

#            #------------------------------------------------------------------------------

#            elif  sikou_kaisuu >= 20 :
#                 print("5555555555555555555555555")
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         rand1=random.choice(player4)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player4)
#                         CP_card_2=(rand2)
#                         #まったく同じカードが選択されないようにするため。
#                         if (rand1 != rand2) :
#                            CP_choose_card.append(CP_card_1)
#                            CP_choose_card.append(CP_card_2)
#                            daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         rand1=random.choice(player4)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player4)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player4)
#                         CP_card_3=(rand3)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)):                        
#                             CP_choose_card.append(CP_card_1)
#                             CP_choose_card.append(CP_card_2)
#                             CP_choose_card.append(CP_card_3)
#                             daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     print(e.args)
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         rand1=random.choice(player4)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player4)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player4)
#                         CP_card_3=(rand3)
#                         rand4=random.choice(player4)
#                         CP_card_4=(rand4)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              CP_choose_card.append(CP_card_4)
#                              daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e  :
#                     print(e.args)
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1

#                 try :
#                     del CP_card_1
#                     del CP_card_2
#                     del CP_card_3
#                     del CP_card_4
#                 except :
#                     pass

#                 if sikou_kaisuu==10000 :
#                     print("player2はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True

#                     try :
#                         del CP_card_1
#                         del CP_card_2
#                         del CP_card_3
#                         del CP_card_4
#                     except :
#                         pass                    
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     CP_card_6=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)

# def player2_dasu() : 
#  global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi,do_kakumei
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  #◎-------------------------------------------------------------------------------------------------
#  do_kakumei=False
#  #◎-------------------------------------------------------------------------------------------------
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     #毎回choose_cardはリセットしないとバグる
#     CP_choose_card=[]
#     if len(player2)==0 :
#         print("player2は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p2+=1
#         p2_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p2==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p2_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #------------------------------------------------------------------------------------------
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
# #----------------------------------------------------------------------------------
#              #★８切をしてから革命をするための処理。もし革命できる手札をもっていて、革命するべき手札であれば、８切り→革命をさせる。
#              #試行回数０回目のときのみ判断させればじゅうぶん。
#              if sikou_kaisuu == 0 : 
#               #革命できるか、革命するべき手札かを判断。
#               player2_check_kakumei()
#               if (do_kakumei == True) :
#                 try :
#                     only_num=[]
#                     for i in range(len(player2)) :
#                         only_num.append(player2[i][0])
#                          #８があったら８を出す処理
#                     eight_index = [p for p, x in enumerate(only_num) if x == "08" ]
#                     CP_card_1=player2[eight_index[0]]
#                     CP_choose_card.append(player2[eight_index[0]])
#                     daseruka_hanndann_CP1(CP_choose_card)
#                 except :
#                     CP_choose_card=[]
#                     pass
#                 #上記で８流しでフィールドのカードのリセット。ここでのリセットは
#                 # eight_nagasi==False                       

# #----------------------------------------------------------------------------------


#              try :
#                 if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu >= 1) and (sikou_kaisuu<=10) and (flag==False) ) :
#                     list_daseru_mark=[]
#                     #フィールドカードのマークを抽出
#                     field_mark=field_card[-1][-1][-1]
#                     for i in range(len(player2)) :
#                         tehuda_mark_syutoku=player2[i][-1]
#                         #同じマークだった場合
#                         if field_mark == tehuda_mark_syutoku :
#                             kazu=player2[i][-2]
#                             sono_mark_index=i
#                             listA=[]
#                             listA.append(kazu)
#                             listA.append(sono_mark_index)
#                             list_daseru_mark.append(listA)
#                     # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                     try :
#                      onaji_mark_dasu_card=[]
#                      for i in range(len(list_daseru_mark)) : 
#                          onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                      #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                      CP_card_1=player2[random.choice(onaji_mark_dasu_card)]
#                      CP_choose_card.append(CP_card_1)
#                      daseruka_hanndann_CP1(CP_choose_card)
#                     except :
#                         pass
#              except :
#                   pass 
#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#              if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player2))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                 #------------------------------------------------------------------------------------------
#          except Exception as e  :
#           """print(e.args)"""
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               rand1=random.choice(player2)
#               CP_card_1=(rand1)
#               rand2=random.choice(player2)
#               CP_card_2=(rand2)
#               #まったく同じカードが選ばれないようにしたい
#               if rand1 != rand2 :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  daseruka_hanndann_CP1(CP_choose_card)
#                  #消しておかないと、のちのち定義したままになって余計な手札まで消してしまう。
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               rand1=random.choice(player2)
#               CP_card_1=(rand1)
#               rand2=random.choice(player2)
#               CP_card_2=(rand2)
#               rand3=random.choice(player2)
#               CP_card_3=(rand3)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  daseruka_hanndann_CP1(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               rand1=random.choice(player2)
#               CP_card_1=(rand1)
#               rand2=random.choice(player2)              
#               CP_card_2=(rand2)
#               rand3=random.choice(player2)
#               CP_card_3=(rand3)
#               rand4=random.choice(player2)
#               CP_card_4=(rand4)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  CP_choose_card.append(CP_card_4)
#                  daseruka_hanndann_CP1(CP_choose_card)
#          except :
#              pass
#          #試行回数ごとに選んだカードを消しておかないとdaseruka_hanndann()で余計なカードまで消してしまう。
#          try :
#              del CP_card_1
#              del CP_card_2
#              del CP_card_3
#              del CP_card_4
#          except :
#             pass 
                 
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player2はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     CP_card_6=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
        
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player2_check_kakumei()はplayer2が革命できる手札をもってるかどうか、また、player2の手札的に革命をするべきかどうかを判断する
#            player2_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 CP_choose_card=[]

# #------------------------------------------------------------------------------------------------------
#                 # try :
#                     # only_num=[]
#                     # for i in range(len(player2)) :
#                         # only_num.append(player2[i][0])
#                          #８があったら８を出す処理
#                     # eight_index = [p for p, x in enumerate(only_num) if x == eight ]
#                     # CP_choose_card.append(player2[eight_index[0]])
#                     # daseruka_hanndann_CP1(CP_choose_card)
#                 # except :
#                     # CP_choose_card=[]
#                     # pass
#                 #上記で８流しでフィールドのカードのリセット。ここでのリセットは
#                 # eight_nagasi==False        
# #------------------------------------------------------------------------------------------------------



#                 """print(list_kakumei_onzon_suuji_with_index)"""
                
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player2[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP1(CP_choose_card)

#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。

#            #----------------------------------------------------------------------------------------------------------------------------------------
           
#            #★Ａｉを強くするためなるべくペアで出すようにする。
#            #革命が第一で優先されるため、do_kakumeiがFalse1で革命ができないときに２枚以上のペアで出すようにする。
#            elif ((10 <= sikou_kaisuu <= 20) and (do_kakumei==False)) :
#                check_pea_player2()
#                CP_choose_card=[]
#                """
#                下記の順でカードを出そうとする。
#                ジョーカーを使って１枚つかって３枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_3mai=[[['数字'], [8, 9, 10]]] これで３枚のペアをだす    
#                ↓
#                ジョーカーを使わず2枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_2mai=[[['数字'], [0, 7]]] これで２枚のペアを出す  
#                ↓
#                ジョーカー2枚のインデックスは joker_index_3mai=[○, ○]。これでjokerを使って、3枚のペアをだす 
#                ↓
#                ジョーカー１枚のインデックスは joker_index_2mai=[○]。これでjokerを使って。2枚のペアをだす。  
#                """

#                #jokerを１枚つかって３枚のペアを出す。例：[[['数字'], [8, 9, 10]]]
#                try : 
#                    if flag==False :
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(list_onzon_suuji_with_index_pea_3mai))
                        
#                         #出す数字はランダムに出すことにする。
#                         #１個ずれてindex error 起きるから、[rand-1]にしておかないと
#                         CP_card_1=player2[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][0]]
#                         CP_card_2=player2[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][1]]
#                         CP_card_3=player2[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][2]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                         #上記関数で出せる判断ならflag=Trueになってるはず。下の３つの関数が起動しないようにflagで処理を起こすかどうかを場合分けする。
#                except Exception as e :
#                     """print(e.args)"""
#                     pass
               
#                #jokerを使わずに2枚のペアを出す。例：[[['数字'], [0, 7]]]
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if (flag==False) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(player2))
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player2[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][0]]
#                         CP_card_2=player2[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][1]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass


#                #joker２枚を使って3枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    #(average_tehuda <= 7)なら、ここの処理はdo_kakuemeiがFalse前提なんだし、いくらjokerを温存してても革命はできないんだから、手札の平均数字が７以下ならjokerを使っちゃう。
#                    if ((flag==False) and (average_tehuda <= 7)) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player2[joker_index_3mai[0]]
#                         CP_card_2=player2[joker_index_3mai[1]]
#                         k=random.randint(1,len(player2))
#                         #joker２枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if ((k != joker_index_3mai[0]) and (k != joker_index_3mai[1])) : 
#                              CP_card_3=player2[joker_index_3mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              daseruka_hanndann_CP1(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass

#                #jokerを１枚使って2枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if ((flag==False) and (average_tehuda <= 7))  :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player2[joker_index_2mai[0]]
#                         k=random.randint(1,len(player2))
#                         #joker1枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if (k != joker_index_2mai[1]) : 
#                              CP_card_2=player2[joker_index_2mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              daseruka_hanndann_CP1(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass              

#            #------------------------------------------------------------------------------

#            elif  sikou_kaisuu >= 20 :
                
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player2))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         rand1=random.choice(player2)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player2)
#                         CP_card_2=(rand2)
#                         #まったく同じカードが選択されないようにするため。
#                         if (rand1 != rand2) :
#                            CP_choose_card.append(CP_card_1)
#                            CP_choose_card.append(CP_card_2)
#                            daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         rand1=random.choice(player2)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player2)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player2)
#                         CP_card_3=(rand3)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)):                        
#                             CP_choose_card.append(CP_card_1)
#                             CP_choose_card.append(CP_card_2)
#                             CP_choose_card.append(CP_card_3)
#                             daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         rand1=random.choice(player2)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player2)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player2)
#                         CP_card_3=(rand3)
#                         rand4=random.choice(player2)
#                         CP_card_4=(rand4)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              CP_choose_card.append(CP_card_4)
#                              daseruka_hanndann_CP1(CP_choose_card)
#                 except Exception as e  :
#                     """print(e.args)"""
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1

#                 try :
#                     del CP_card_1
#                     del CP_card_2
#                     del CP_card_3
#                     del CP_card_4
#                 except :
#                     pass

#                 if sikou_kaisuu==10000 :
#                     print("player2はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True

#                     try :
#                         del CP_card_1
#                         del CP_card_2
#                         del CP_card_3
#                         del CP_card_4
#                     except :
#                         pass  

#                 #だされたカードが５枚、６枚の時は考えない。低確率すぎるので割愛。                  
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     CP_card_6=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)


# def player3_dasu() : 
#  global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi,do_kakumei
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  #◎-------------------------------------------------------------------------------------------------
#  do_kakumei=False
#  #◎-------------------------------------------------------------------------------------------------
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     #毎回choose_cardはリセットしないとバグる
#     CP_choose_card=[]
#     if len(player3)==0 :
#         print("player3は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p3+=1
#         p3_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p3==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p3_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #------------------------------------------------------------------------------------------
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
# #----------------------------------------------------------------------------------
#              #★８切をしてから革命をするための処理。もし革命できる手札をもっていて、革命するべき手札であれば、８切り→革命をさせる。
#              #試行回数０回目のときのみ判断させればじゅうぶん。
#              if sikou_kaisuu == 0 : 
#               #革命できるか、革命するべき手札かを判断。
#               player3_check_kakumei()
#               if (do_kakumei == True) :
#                 try :
#                     only_num=[]
#                     for i in range(len(player3)) :
#                         only_num.append(player3[i][0])
#                          #８があったら８を出す処理
#                     eight_index = [p for p, x in enumerate(only_num) if x == "08" ]
#                     CP_card_1=player3[eight_index[0]]
#                     CP_choose_card.append(player3[eight_index[0]])
#                     daseruka_hanndann_CP2(CP_choose_card)
#                 except :
#                     CP_choose_card=[]
#                     pass
#                 #上記で８流しでフィールドのカードのリセット。ここでのリセットは
#                 # eight_nagasi==False                       

# #----------------------------------------------------------------------------------


#              try :
#                 if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu >= 1) and (sikou_kaisuu<=10) and (flag==False) ) :
#                     list_daseru_mark=[]
#                     #フィールドカードのマークを抽出
#                     field_mark=field_card[-1][-1][-1]
#                     for i in range(len(player3)) :
#                         tehuda_mark_syutoku=player3[i][-1]
#                         #同じマークだった場合
#                         if field_mark == tehuda_mark_syutoku :
#                             kazu=player3[i][-2]
#                             sono_mark_index=i
#                             listA=[]
#                             listA.append(kazu)
#                             listA.append(sono_mark_index)
#                             list_daseru_mark.append(listA)
#                     # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                     try :
#                      onaji_mark_dasu_card=[]
#                      for i in range(len(list_daseru_mark)) : 
#                          onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                      #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                      CP_card_1=player3[random.choice(onaji_mark_dasu_card)]
#                      CP_choose_card.append(CP_card_1)
#                      daseruka_hanndann_CP2(CP_choose_card)
#                     except :
#                         pass
#              except :
#                   pass 
#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#              if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 #------------------------------------------------------------------------------------------
#          except Exception as e  :
#           """print(e.args)"""
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               rand1=random.choice(player3)
#               CP_card_1=(rand1)
#               rand2=random.choice(player3)
#               CP_card_2=(rand2)
#               #まったく同じカードが選ばれないようにしたい
#               if rand1 != rand2 :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  daseruka_hanndann_CP2(CP_choose_card)
#                  #消しておかないと、のちのち定義したままになって余計な手札まで消してしまう。
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               rand1=random.choice(player3)
#               CP_card_1=(rand1)
#               rand2=random.choice(player3)
#               CP_card_2=(rand2)
#               rand3=random.choice(player3)
#               CP_card_3=(rand3)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  daseruka_hanndann_CP2(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               rand1=random.choice(player3)
#               CP_card_1=(rand1)
#               rand2=random.choice(player3)              
#               CP_card_2=(rand2)
#               rand3=random.choice(player3)
#               CP_card_3=(rand3)
#               rand4=random.choice(player3)
#               CP_card_4=(rand4)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  CP_choose_card.append(CP_card_4)
#                  daseruka_hanndann_CP2(CP_choose_card)
#          except :
#              pass
#          #試行回数ごとに選んだカードを消しておかないとdaseruka_hanndann()で余計なカードまで消してしまう。
#          try :
#              del CP_card_1
#              del CP_card_2
#              del CP_card_3
#              del CP_card_4
#          except :
#             pass 
                 
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player3はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     CP_card_6=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
        
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player2_check_kakumei()はplayer2が革命できる手札をもってるかどうか、また、player2の手札的に革命をするべきかどうかを判断する
#            player3_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 CP_choose_card=[]

# #------------------------------------------------------------------------------------------------------
#                 # try :
#                     # only_num=[]
#                     # for i in range(len(player2)) :
#                         # only_num.append(player2[i][0])
#                          #８があったら８を出す処理
#                     # eight_index = [p for p, x in enumerate(only_num) if x == eight ]
#                     # CP_choose_card.append(player2[eight_index[0]])
#                     # daseruka_hanndann_CP1(CP_choose_card)
#                 # except :
#                     # CP_choose_card=[]
#                     # pass
#                 #上記で８流しでフィールドのカードのリセット。ここでのリセットは
#                 # eight_nagasi==False        
# #------------------------------------------------------------------------------------------------------



#                 """print(list_kakumei_onzon_suuji_with_index)"""
                
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player3[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP2(CP_choose_card)

#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。

#            #----------------------------------------------------------------------------------------------------------------------------------------
           
#            #★Ａｉを強くするためなるべくペアで出すようにする。
#            #革命が第一で優先されるため、do_kakumeiがFalse1で革命ができないときに２枚以上のペアで出すようにする。
#            elif ((10 <= sikou_kaisuu <= 20) and (do_kakumei==False)) :
#                check_pea_player3()
#                CP_choose_card=[]
#                """
#                下記の順でカードを出そうとする。
#                ジョーカーを使って１枚つかって３枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_3mai=[[['数字'], [8, 9, 10]]] これで３枚のペアをだす    
#                ↓
#                ジョーカーを使わず2枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_2mai=[[['数字'], [0, 7]]] これで２枚のペアを出す  
#                ↓
#                ジョーカー2枚のインデックスは joker_index_3mai=[○, ○]。これでjokerを使って、3枚のペアをだす 
#                ↓
#                ジョーカー１枚のインデックスは joker_index_2mai=[○]。これでjokerを使って。2枚のペアをだす。  
#                """

#                #jokerを１枚つかって３枚のペアを出す。例：[[['数字'], [8, 9, 10]]]
#                try : 
#                    if flag==False :
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(list_onzon_suuji_with_index_pea_3mai))
                        
#                         #出す数字はランダムに出すことにする。
#                         #１個ずれてindex error 起きるから、[rand-1]にしておかないと
#                         CP_card_1=player3[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][0]]
#                         CP_card_2=player3[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][1]]
#                         CP_card_3=player3[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][2]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                         #上記関数で出せる判断ならflag=Trueになってるはず。下の３つの関数が起動しないようにflagで処理を起こすかどうかを場合分けする。
#                except Exception as e :
#                     """print(e.args)"""
#                     pass
               
#                #jokerを使わずに2枚のペアを出す。例：[[['数字'], [0, 7]]]
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if (flag==False) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(player3))
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player3[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][0]]
#                         CP_card_2=player3[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][1]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass


#                #joker２枚を使って3枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    #(average_tehuda <= 7)なら、ここの処理はdo_kakuemeiがFalse前提なんだし、いくらjokerを温存してても革命はできないんだから、手札の平均数字が７以下ならjokerを使っちゃう。
#                    if ((flag==False) and (average_tehuda <= 7)) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player3[joker_index_3mai[0]]
#                         CP_card_2=player3[joker_index_3mai[1]]
#                         k=random.randint(1,len(player3))
#                         #joker２枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if ((k != joker_index_3mai[0]) and (k != joker_index_3mai[1])) : 
#                              CP_card_3=player3[joker_index_3mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              daseruka_hanndann_CP2(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass

#                #jokerを１枚使って2枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if ((flag==False) and (average_tehuda <= 7))  :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player3[joker_index_2mai[0]]
#                         k=random.randint(1,len(player3))
#                         #joker1枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if (k != joker_index_2mai[1]) : 
#                              CP_card_2=player3[joker_index_2mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              daseruka_hanndann_CP2(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass              

#            #------------------------------------------------------------------------------

#            elif  sikou_kaisuu >= 20 :
                
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player3))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         rand1=random.choice(player3)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player3)
#                         CP_card_2=(rand2)
#                         #まったく同じカードが選択されないようにするため。
#                         if (rand1 != rand2) :
#                            CP_choose_card.append(CP_card_1)
#                            CP_choose_card.append(CP_card_2)
#                            daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         rand1=random.choice(player3)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player3)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player3)
#                         CP_card_3=(rand3)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)):                        
#                             CP_choose_card.append(CP_card_1)
#                             CP_choose_card.append(CP_card_2)
#                             CP_choose_card.append(CP_card_3)
#                             daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         rand1=random.choice(player3)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player3)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player3)
#                         CP_card_3=(rand3)
#                         rand4=random.choice(player3)
#                         CP_card_4=(rand4)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              CP_choose_card.append(CP_card_4)
#                              daseruka_hanndann_CP2(CP_choose_card)
#                 except Exception as e  :
#                     """print(e.args)"""
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1

#                 try :
#                     del CP_card_1
#                     del CP_card_2
#                     del CP_card_3
#                     del CP_card_4
#                 except :
#                     pass

#                 if sikou_kaisuu==10000 :
#                     print("player3はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True

#                     try :
#                         del CP_card_1
#                         del CP_card_2
#                         del CP_card_3
#                         del CP_card_4
#                     except :
#                         pass  

#                 #だされたカードが５枚、６枚の時は考えない。低確率すぎるので割愛。                  
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     CP_card_6=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)


# def player4_dasu() : 
#  global CP_card_1,CP_card_2,CP_card_3,CP_card_4,CP_card_5,CP_card_6,your_tehuda,can_num_card,shibari,kakumei,eleven_back,player4,pass_kosuu,agatteru_ninnzuu,agatteruka_p1,agatteruka_p2,agatteruka_p3,agatteruka_p4,flag,p1_jyunni,p2_jyunni,p3_jyunni,p4_jyunni,jyunni,p1_agari,p2_agari,p3_agari,p4_agari,eight_nagasi,do_kakumei
#  flag = False
#  sikou_kaisuu=0
#  #下記関数内でパスが続いて、field_card.clearしたときに、len(field_card)==0が反応して誤作動を起こしてしまう。だからパス→フィールドリセット時にreset=Falseにして誤作動を防ぐ。
#  reset=True
#  #◎-------------------------------------------------------------------------------------------------
#  do_kakumei=False
#  #◎-------------------------------------------------------------------------------------------------
#  while flag==False : 
#     flag=False  #daseruka_hanbetuでTrueになるまで手札からカードを選ばせるため。
#     #毎回choose_cardはリセットしないとバグる
#     CP_choose_card=[]
#     if len(player4)==0 :
#         print("player4は上がりました。")
#         #繰り返しをしてsikou_kaisuu=20とならないようにTrueにしておく。
#         flag=True
#         agatteruka_p4+=1
#         p4_agari=True
#         #ここ繰り返しだから、一回しかプラスされないようにした。
#         if agatteruka_p4==1 :
#            #ここの人数に合わせてpass_kosuuにおうじてフィールドカードをリセットする。
#            agatteru_ninnzuu+=1
#            #順位の確定（一回しか処理されないはず）
#            p4_jyunni=jyunni
#            jyunni+=1
#            field_card.clear()
#            #リセットするときに縛り等はリセットする
#            shibari=0
#            eleven_back=0
           
#     #field_card=[]のとき、field_card[0]でエラー起きないように場合分け。
#     if len(field_card) != 0 :
#          #上がってたら手札なくてエラー起きるため
#          try :
#           #１枚しかでていないとき。
#           if len(field_card[0])==1 :
#               #------------------------------------------------------------------------------------------
#               #試行回数が１０回まで繰り返す。１０回繰り返してなければ、同じマークのカードは出せないということ。その時違うマークで１枚出せるよう下の処理へ行くため
# #----------------------------------------------------------------------------------
#              #★８切をしてから革命をするための処理。もし革命できる手札をもっていて、革命するべき手札であれば、８切り→革命をさせる。
#              #試行回数０回目のときのみ判断させればじゅうぶん。
#              if sikou_kaisuu == 0 : 
#               #革命できるか、革命するべき手札かを判断。
#               player4_check_kakumei()
#               if (do_kakumei == True) :
#                 try :
#                     only_num=[]
#                     for i in range(len(player4)) :
#                         only_num.append(player4[i][0])
#                          #８があったら８を出す処理
#                     eight_index = [p for p, x in enumerate(only_num) if x == "08" ]
#                     CP_card_1=player4[eight_index[0]]
#                     CP_choose_card.append(player4[eight_index[0]])
#                     daseruka_hanndann_CP3(CP_choose_card)
#                 except :
#                     CP_choose_card=[]
#                     pass
#                 #上記で８流しでフィールドのカードのリセット。ここでのリセットは
#                 # eight_nagasi==False                       

# #----------------------------------------------------------------------------------


#              try :
#                 if ((shibari==0) and (len(field_card[-1])==1) and (sikou_kaisuu >= 1) and (sikou_kaisuu<=10) and (flag==False) ) :
#                     list_daseru_mark=[]
#                     #フィールドカードのマークを抽出
#                     field_mark=field_card[-1][-1][-1]
#                     for i in range(len(player4)) :
#                         tehuda_mark_syutoku=player4[i][-1]
#                         #同じマークだった場合
#                         if field_mark == tehuda_mark_syutoku :
#                             kazu=player4[i][-2]
#                             sono_mark_index=i
#                             listA=[]
#                             listA.append(kazu)
#                             listA.append(sono_mark_index)
#                             list_daseru_mark.append(listA)
#                     # list_daseru_mark=[['03', 0], ['07', 4], ['04', 11]]
#                     try :
#                      onaji_mark_dasu_card=[]
#                      for i in range(len(list_daseru_mark)) : 
#                          onaji_mark_dasu_card.append(list_daseru_mark[i][-1])
#                      #ここで適当な数字のインデックス（同じマークの）を取得して、そのインデックスのplayer2のインデックスを出している処理
#                      CP_card_1=player4[random.choice(onaji_mark_dasu_card)]
#                      CP_choose_card.append(CP_card_1)
#                      daseruka_hanndann_CP3(CP_choose_card)
#                     except :
#                         pass
#              except :
#                   pass 
#               #１枚出しのターンの際、フィールドカードの戦闘がjokerのときなにも出せないようにする。1000回試行してパスになるはず。
#               #これをやらないとイレブンバック中にjoker出しても最弱カードとして認識されてそこからまた7とか3とか出されるようになってしまうため強制終了させる。
#               #試行回数が１１回以上の時は通常通りの、違うマークでもいいから、何か１枚カードを出す処理をする。
#              if ((field_card[-1][-1][-1] != "joker") and (sikou_kaisuu >= 11)) : #フィールドカードの先頭のカードにjokerがあるかどうか。
#                         CP_card_1=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 #------------------------------------------------------------------------------------------
#          except Exception as e  :
#           """print(e.args)"""
#           pass
#          #8でfield_card=[]になった後にエラー起きるからtryにしておく。
#          try :
#           if len(field_card[0])==2 :
#               rand1=random.choice(player4)
#               CP_card_1=(rand1)
#               rand2=random.choice(player4)
#               CP_card_2=(rand2)
#               #まったく同じカードが選ばれないようにしたい
#               if rand1 != rand2 :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  daseruka_hanndann_CP3(CP_choose_card)
                 
#          except :
#              pass
#          try :
#           if len(field_card[0])==3 :
#               rand1=random.choice(player4)
#               CP_card_1=(rand1)
#               rand2=random.choice(player4)
#               CP_card_2=(rand2)
#               rand3=random.choice(player4)
#               CP_card_3=(rand3)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  daseruka_hanndann_CP3(CP_choose_card)
#          except :
#              pass
#          try :
#           if len(field_card[0])==4 :
#               rand1=random.choice(player4)
#               CP_card_1=(rand1)
#               rand2=random.choice(player4)              
#               CP_card_2=(rand2)
#               rand3=random.choice(player4)
#               CP_card_3=(rand3)
#               rand4=random.choice(player4)
#               CP_card_4=(rand4)
#               #まったく同じカードが選ばれないようにしたい
#               if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                  CP_choose_card.append(CP_card_1)
#                  CP_choose_card.append(CP_card_2)
#                  CP_choose_card.append(CP_card_3)
#                  CP_choose_card.append(CP_card_4)
#                  daseruka_hanndann_CP3(CP_choose_card)
#          except :
#              pass
#          #試行回数ごとに選んだカードを消しておかないとdaseruka_hanndann()で余計なカードまで消してしまう。
#          try :
#              del CP_card_1
#              del CP_card_2
#              del CP_card_3
#              del CP_card_4
#          except :
#             pass 
                 
#          #10000回手札選び失敗したらパスするようにした。
#          sikou_kaisuu+=1
#          if sikou_kaisuu==10000 :
#                print("player4はパスしました")
#                flag=True
#                pass_kosuu+=1    
#                #あがっている人数に合わせて(agatteru_ninnzuu)、パスが３つたまったらフィールドカードのリセット
#                if agatteru_ninnzuu==3 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==2 :
#                  if pass_kosuu==1 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False
#                if agatteru_ninnzuu==1 :
#                  if pass_kosuu==2 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0
#                     reset=False 
#                if agatteru_ninnzuu==0 :
#                  if pass_kosuu==3 :
#                     print("全員パスなのでフィールドカードをリセットします。")
#                     eleven_back=0 
#                     shibari=0
#                     field_card.clear()
#                     pass_kosuu=0     
#                     reset=False        
#          # if len(field_card)==5 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)
#          # if len(field_card)==6 :
#          #     CP_card_1=(random.choice(player2))
#          #     CP_card_2=(random.choice(player2))
#          #     CP_card_3=(random.choice(player2))
#          #     CP_card_4=(random.choice(player2))
#          #     CP_card_5=(random.choice(player2))
#          #     CP_card_6=(random.choice(player2))
#          #     daseruka_hanndann_CP1(CP_choose_card)

#     #フィールドカードが０の時、何枚出すべきかを勝手に選ぶようにする。
#     #パス続きでフィールドリセットしたときにここが反応しないようにand (reset==True)を追加。

#     if ((len(field_card)== 0) and (reset==True)) :
#         #上で一回試行回数１００００になってる可能性あるから０にする
#         sikou_kaisuu=0
        
#         while flag==False :
#            #出せない判定食らうたびにCP_choose_cardは初期化しないと、field_card=[]のとき何も出せなくなる。
#            #フィールドカードが０の時、革命ができるチャンスかどうかを確かめる。


#            #下記player2_check_kakumei()はplayer2が革命できる手札をもってるかどうか、また、player2の手札的に革命をするべきかどうかを判断する
#            player4_check_kakumei()
#            sikou_kaisuu+=1
#            #do_kakumeiがTrueのとき、革命をするべき時。ただ、daseruka_hanndannCP1ではじかれたらループするので、試行回数は９回までにする。
#            if ((do_kakumei==True) and (sikou_kaisuu <=9)) :
#                 CP_choose_card=[]

# #------------------------------------------------------------------------------------------------------
#                 # try :
#                     # only_num=[]
#                     # for i in range(len(player2)) :
#                         # only_num.append(player2[i][0])
#                          #８があったら８を出す処理
#                     # eight_index = [p for p, x in enumerate(only_num) if x == eight ]
#                     # CP_choose_card.append(player2[eight_index[0]])
#                     # daseruka_hanndann_CP1(CP_choose_card)
#                 # except :
#                     # CP_choose_card=[]
#                     # pass
#                 #上記で８流しでフィールドのカードのリセット。ここでのリセットは
#                 # eight_nagasi==False        
# #------------------------------------------------------------------------------------------------------



#                 """print(list_kakumei_onzon_suuji_with_index)"""
                
#                 #list_kakumei_onzon_suuji_with_index[-1][-1][0] = [[['One'], [1, 3, 6, 5]], [['11'], [2, 4, 8, 5]]]のように抽出されてる。
#                 CP_card_1=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][0]])
#                 CP_card_2=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][1]])
#                 CP_card_3=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][2]])
#                 CP_card_4=(player4[list_kakumei_onzon_suuji_with_index[-1][-1][3]])
#                 CP_choose_card.append(CP_card_1)
#                 CP_choose_card.append(CP_card_2)
#                 CP_choose_card.append(CP_card_3)
#                 CP_choose_card.append(CP_card_4)
#                 daseruka_hanndann_CP3(CP_choose_card)

#            #革命をするべきではない、もしくは革命ができない場合は通常通り手札を10000回出す試行をする。

#            #----------------------------------------------------------------------------------------------------------------------------------------
           
#            #★Ａｉを強くするためなるべくペアで出すようにする。
#            #革命が第一で優先されるため、do_kakumeiがFalse1で革命ができないときに２枚以上のペアで出すようにする。
#            elif ((10 <= sikou_kaisuu <= 20) and (do_kakumei==False)) :
#                check_pea_player4()
#                CP_choose_card=[]
#                """
#                下記の順でカードを出そうとする。
#                ジョーカーを使って１枚つかって３枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_3mai=[[['数字'], [8, 9, 10]]] これで３枚のペアをだす    
#                ↓
#                ジョーカーを使わず2枚のペアを出せるその数字とインデックスは list_onzon_suuji_with_index_pea_2mai=[[['数字'], [0, 7]]] これで２枚のペアを出す  
#                ↓
#                ジョーカー2枚のインデックスは joker_index_3mai=[○, ○]。これでjokerを使って、3枚のペアをだす 
#                ↓
#                ジョーカー１枚のインデックスは joker_index_2mai=[○]。これでjokerを使って。2枚のペアをだす。  
#                """

#                #jokerを１枚つかって３枚のペアを出す。例：[[['数字'], [8, 9, 10]]]
#                try : 
#                    if flag==False :
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(list_onzon_suuji_with_index_pea_3mai))
                        
#                         #出す数字はランダムに出すことにする。
#                         #１個ずれてindex error 起きるから、[rand-1]にしておかないと
#                         CP_card_1=player4[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][0]]
#                         CP_card_2=player4[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][1]]
#                         CP_card_3=player4[ list_onzon_suuji_with_index_pea_3mai[rand-1][-1][2]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         CP_choose_card.append(CP_card_3)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                         #上記関数で出せる判断ならflag=Trueになってるはず。下の３つの関数が起動しないようにflagで処理を起こすかどうかを場合分けする。
#                except Exception as e :
#                     """print(e.args)"""
#                     pass
               
#                #jokerを使わずに2枚のペアを出す。例：[[['数字'], [0, 7]]]
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if (flag==False) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #list_onzon_suuji_with_index_pea_3maiの要素が何個あるかわからない＆どの数字をだすかはランダムで出すことにする。
#                         #len(list_onzon_suuji_with_index_pea_3mai)にしておけばout of rangeでエラーおきることはないはず。
#                         rand=random.randint(1,len(player4))
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player4[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][0]]
#                         CP_card_2=player4[ list_onzon_suuji_with_index_pea_2mai[rand-1][-1][1]]
#                         CP_choose_card.append(CP_card_1)
#                         CP_choose_card.append(CP_card_2)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass


#                #joker２枚を使って3枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    #(average_tehuda <= 7)なら、ここの処理はdo_kakuemeiがFalse前提なんだし、いくらjokerを温存してても革命はできないんだから、手札の平均数字が７以下ならjokerを使っちゃう。
#                    if ((flag==False) and (average_tehuda <= 7)) :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player4[joker_index_3mai[0]]
#                         CP_card_2=player4[joker_index_3mai[1]]
#                         k=random.randint(1,len(player4))
#                         #joker２枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if ((k != joker_index_3mai[0]) and (k != joker_index_3mai[1])) : 
#                              CP_card_3=player4[joker_index_3mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              daseruka_hanndann_CP3(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass

#                #jokerを１枚使って2枚のペアを出す
#                try : 
#                    #上記処理でうまくいかなかった場合に出す処理。
#                    if ((flag==False) and (average_tehuda <= 7))  :
#                         #上の処理がエラーの時、CP_choose_card=[] は一回空にしておく。
#                         CP_choose_card=[] 
                        
#                         #出す数字はランダムに出すことにする。
#                         CP_card_1=player4[joker_index_2mai[0]]
#                         k=random.randint(1,len(player4))
#                         #joker1枚と適当に出したカードｋが、jokerと同じインデックスのものを選ばないように、その場合は除外する必要がある。
#                         if (k != joker_index_2mai[1]) : 
#                              CP_card_2=player4[joker_index_2mai[k-1]]
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              daseruka_hanndann_CP3(CP_choose_card)
#                except Exception as e :
#                     """print(e.args)"""
#                     pass              

#            #------------------------------------------------------------------------------

#            elif  sikou_kaisuu >= 20 :
                
#                 CP_choose_card=[]
#                 CP_syote_maisuu=random.randint(1,4)
#                 # print("player2が",CP_syote_maisuu,"枚出す試みをしています。")
#                 try :
#                     if CP_syote_maisuu==1 :
#                         CP_card_1=(random.choice(player4))
#                         CP_choose_card.append(CP_card_1)
#                         daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==2 :
#                         rand1=random.choice(player4)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player4)
#                         CP_card_2=(rand2)
#                         #まったく同じカードが選択されないようにするため。
#                         if (rand1 != rand2) :
#                            CP_choose_card.append(CP_card_1)
#                            CP_choose_card.append(CP_card_2)
#                            daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==3 :
#                         rand1=random.choice(player4)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player4)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player4)
#                         CP_card_3=(rand3)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand2!=rand3)):                        
#                             CP_choose_card.append(CP_card_1)
#                             CP_choose_card.append(CP_card_2)
#                             CP_choose_card.append(CP_card_3)
#                             daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e :
#                     """print(e.args)"""
#                     pass
#                 try :
#                     if CP_syote_maisuu==4 :
#                         rand1=random.choice(player4)
#                         CP_card_1=(rand1)
#                         rand2=random.choice(player4)
#                         CP_card_2=(rand2)
#                         rand3=random.choice(player4)
#                         CP_card_3=(rand3)
#                         rand4=random.choice(player4)
#                         CP_card_4=(rand4)
#                         #まったく同じカードが選択されないようにするため。
#                         if ((rand1 != rand2) and (rand1!= rand3) and (rand1!=rand4) and (rand2 != rand3) and (rand2 != rand4) and (rand3 != rand4)  ) :
#                              CP_choose_card.append(CP_card_1)
#                              CP_choose_card.append(CP_card_2)
#                              CP_choose_card.append(CP_card_3)
#                              CP_choose_card.append(CP_card_4)
#                              daseruka_hanndann_CP3(CP_choose_card)
#                 except Exception as e  :
#                     """print(e.args)"""
#                     pass
#                 #10000回手札選び失敗したらパスするようにした。
#                 sikou_kaisuu+=1

#                 try :
#                     del CP_card_1
#                     del CP_card_2
#                     del CP_card_3
#                     del CP_card_4
#                 except :
#                     pass

#                 if sikou_kaisuu==10000 :
#                     print("player3はパスしましたよ。")
#                     #パスが３つたまったらフィールドカードのリセット
#                     pass_kosuu+=1
#                     if agatteru_ninnzuu==3 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==2 :
#                         if pass_kosuu==1 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0
#                             reset=False
#                     if agatteru_ninnzuu==1 :
#                         if pass_kosuu==2 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0 
#                             reset=False
#                     if agatteru_ninnzuu==0 :
#                         if pass_kosuu==3 :
#                             print("全員パスなのでフィールドカードをリセットします。")
#                             eleven_back=0 
#                             shibari=0
#                             field_card.clear()
#                             pass_kosuu=0    
#                             reset=False   
#                     flag=True

#                     try :
#                         del CP_card_1
#                         del CP_card_2
#                         del CP_card_3
#                         del CP_card_4
#                     except :
#                         pass  

#                 #だされたカードが５枚、６枚の時は考えない。低確率すぎるので割愛。                  
#                 # if CP_syote_maisuu==5 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)
#                 # if CP_syote_maisuu==6 :
#                 #     CP_card_1=(random.choice(player2))
#                 #     CP_card_2=(random.choice(player2))
#                 #     CP_card_3=(random.choice(player2))
#                 #     CP_card_4=(random.choice(player2))
#                 #     CP_card_5=(random.choice(player2))
#                 #     CP_card_6=(random.choice(player2))
#                 #     daseruka_hanndann_CP1(CP_choose_card)




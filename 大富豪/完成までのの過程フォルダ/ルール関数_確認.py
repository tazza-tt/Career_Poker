field_card=[]
kakumei=1
shibari=0 
eleven_back=0

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
     
     if shibari==0 :
         print("縛りはありません")
     if shibari==1 :
         print("縛られています")
     if kakumei %2 == 0 :
         print("革命中です")
     if kakumei %2 != 0 :
         print("革命中ではありません")
     if eleven_back == 0 :
         print("イレブンバック中ではありません")
     if eleven_back == 1 :
         print("イレブンバック中です")

finish_turn([["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"]])  
print(shibari) #０で縛りなし
print(kakumei) #偶数で革命
print(eleven_back) #０で通常

top_field_card=[["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"],["eleven","♠"]]
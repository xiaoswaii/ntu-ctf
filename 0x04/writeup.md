## [0x04]how2xss
一開始先嘗試 alert,利用 html case insensitive 的特性,用大寫 bypass 掉只能出現一個字元便可以 alert 了。於是便利用 iframe 去打到自己的 domain,在自己的 domain 寫好一個 script,這邊我是使用 webhook 的服務去看有哪些 request,script 放在自己的github 網址,一開始想要直接用 fetch 去 get request,然後把 cookie 和 url 一起request,但是發現這樣的話會有 cors 的問題,因此不能直接用 fetch 的方式。所以利用了 window name 的方法,先講一些變數 assign 到 window name,然後在塞 payload去執行 window name 裡面的 js script。比較 tricky 的地方是 domain name 太長的話就很難或是幾乎不可能繞過 waf,因此找到了 bitly 縮短網址的服務,而且可以 customize。

附上 script 所在的 github : https://github.com/xiaoswaii/xss

POW 則直接用了暴力 loop 去解。

`FLAG{babyxss_easy_peasy_yo}`

## [0x04]Cathub v2
一開始有利用用簡單的 sql injection 去 inject,後來發現有一些 waf 像是空格,semicolon,單引號之類的,空格可以利用%0b,%0c 等去 bypass 掉。先用boolean-based 去測試 `https://edu-ctf.csie.org:10159/video.php?vid=1` 這邊可以不被injection,測試可以之後。想使用 sqlmap 去測試出使用哪一種 DBMS,後來發現到有點難測。於是先用 order by 的方式去測試有幾個欄位,發現欄位是三個(先用 null 去測試,因為資料型態不一樣會有 error),而且這個時候影片就不會顯示了,再透過各個 DB 不同的 database version 的 function 去測試,發現中間的欄位是可以被在影片的名字原本的位置,透過這個 function,便可得知 DBMS 是 oracle。爬過一些資料後知道oracle 有一些 table 是放了每個 table 的資訊,還有每個 table 裡面的 column。另外可以配合 rownum 的使用選取欄位,但需要配合 subquery 的使用才能執行,便可以從user_table 去找出每一個table,於是在第六行找出一個叫做 `s3cret` 的 table_name,再利用 USER_TAB_COLUMNS 去找去每一個 column,於是在第 19 行找出`v3ry_s3cret_c0lumn` 這個欄位,直接 `select v3ry_s3cret_c0lumn from s3cret 便是 flag`。但是因為 css 把全部都變成 uppercase,因此需要看 html code 裡面的 flag 才是正確的。

`FLAG{hey___or@cle_d4tab4s3__inj3cti0n_i5____to0OoO0ooO0OO_e4sy!!!!!??}`
## [0x03] Unexploitable

這一題在戳網址底下的其他路徑時,會出現 Github 顯示的 error,於是便直接到 github 去利用 domain name(https://unexploitable.kaibro.tw/)做檢索,會發現到有一個 repo 叫做 `Bucharesti.github.io`,然後去看 commit,其中一個叫做 delete secret file,flag 就在裡面。

`FLAG{baby_recon_dont_forget_to_look_github_page}`

## [0x03] Safe R/W
一開始有要使用 race condition 的方式去做,但是不知道要如何施作,雖然設法跑到 include 檔案那行,於是寫了兩個 python 檔案,一個是違法的,在 c 的部分寫入 php 的語法(利用 array bypass 掉 strlen 的檢查),執行 system 相關的指令,另外一個則是輸入合法的字串,希望在判斷的時候會有 multi thread 的情況出現,判斷到合法字串,在include 的時候 include 到的是不合法的 php system 指令。結果成功,找到 flag 在根目錄的文件夾(flag_is_here)裡面。

`FLAG{w3lc0me_t0_th3_PHP_W0r1d}`
## [0x01] Back to the Future

利用ida pro 進行 decompile。然後找到main function 的位置,透過解讀程式,了解到會對 input 進行處理再對比到某個變數。而也花了不少時間在算 input,但是 input
實際上根本輸入不到。於是利用兩個 byte 變數進行 Xor,便可得到 flag。其中程式其實就只是要讓 input 在進行處理後先和某個byte 變數一樣,再對另一個 byte 變數進行 Xor。

`FLAG{PE_!S_EASY}`
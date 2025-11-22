# H1
H1
===
H2
---

**粗體** __粗體__  
*斜體* _斜體_  
***斜體兼粗體***  
~~刪除線~~  
正常^上標^  
正常~下標~  
++底線++  
==螢光標記==  

>縮排語法
>第一層(引用)
>>第二層
>>>第三層

--- 
上面是分隔線 這裡是一般內文  
&emsp;縮排1  
&ensp;縮排2  
&nbsp;縮排3  

行末按兩個空格=換行

1. 數字標號
2. 數字標號
3. 數字標號
- 其他標號
+ 其他標號
* 其他標號

- 無序清單
- 無序清單
    - 無序清單子清單
        - 無序清單子子清單

1. 有序清單
2. 有序清單
    1. 有序清單子清單
        1. 有序清單子子清單

名詞
: 解釋  
名詞
~ 定義  

`內容`  
<網址或mail>  
 [Tab] jo  
[Google][1]  
[Yahoo][2]  
[MSN][3]  
[1]: http://google.com/        
[2]: http://search.yahoo.com/  
[3]: http://search.msn.com/    

[顯示link](https://github.com/Yoyo-ace1110/-)  
![ 圖名 ](相對位置/圖片網址)  
[ ![圖片](相對位置/圖片網址) ](連結網址)

| 欄位1 | 欄位2 | 欄位3 |
| :-- | --: |:--:|
| 置左  | 置右 | 置中 |

 - [ ] uncheck
 - [x] check

\+ 顯示符號前加上一個\
\\ 像這樣

$$
\begin{align*}
y = y(x,t) &= A e^{i\theta} \\
&= A (\cos \theta + i \sin \theta) \\
&= A (\cos(kx - \omega t) + i \sin(kx - \omega t)) \\
&= A\cos(kx - \omega t) + i A\sin(kx - \omega t)  \\
&= A\cos \Big(\frac{2\pi}{\lambda}x - \frac{2\pi v}{\lambda} t \Big) + i A\sin \Big(\frac{2\pi}{\lambda}x - \frac{2\pi v}{\lambda} t \Big)  \\
&= A\cos \frac{2\pi}{\lambda} (x - v t) + i A\sin \frac{2\pi}{\lambda} (x - v t)
\end{align*}
$$

```py
print("這是程式碼 上方式標記語言(方便上色)")
```

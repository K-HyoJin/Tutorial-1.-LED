# Arduino example 1 
Tutorial 1. LED  \
LED가 3번 깜박이도록 제작

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함 

``` import time ```\
프로그램을 일정시간동안 지연시키기위해 time 모듈을 import함

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

``` board.get_pin('d:13:o')``` \
  -> 13번핀을 digital신호 출력핀으로 설정\
변수1 = 변수2.get_pin('**d or a** : **pin number** : **i or o** ') \
**d or a** : The type of the pin \
**pin number** : The number of the pin\
**i or o** : The mode of the pin 
 
```board.digital[13].write(1)```\
led가 연결된 13번 핀에 1을 입력시켜서 led를 켜도록 함

```board.digital[13].write(0)```\
led가 연결된 13번 핀에 0을 입력시켜서 led를 끄도록 함

```  time.sleep(1) ```\
1초동안 기다림

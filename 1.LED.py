from pyfirmata import Arduino,util
import time

#핀 모드 세팅
board = Arduino('COM8')
board.get_pin('d:13:o') # 13번 핀을 출력으로 설정

print("start")
for i in range(3):
    board.digital[13].write(0)
    time.sleep(1)
    board.digital[13].write(1)
    time.sleep(1)
print("fin")







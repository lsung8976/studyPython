#랜덤한 숫자를 만들기 위해 가져옵니다.
import random

#간단한 한글 리스트를 만듭니다.
hanguls = list("서연고성한중경건동홍국세")
#파일을 쓰기모드로 엽니다.

with open("info.txt", "w") as file:
    for i in range(1000):
        #랜덤한 값으로 변수를 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        #텍스트를 씁니다.
        file.write("{}, {}, {}\n".format(name, weight, height))

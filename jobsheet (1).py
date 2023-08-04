import random
from guess import TbkAngka

tebak=int(input('Tebak Angka : '))
jawab=random.randint(1-20)

jawaban1 = TbkAngka (tebak, jawab)

if jawaban1.process():
    print("YOU Win!!!")
else:
    print("You lose")    
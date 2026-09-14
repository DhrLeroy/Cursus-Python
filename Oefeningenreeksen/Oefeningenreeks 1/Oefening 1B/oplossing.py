import sys

for i in range(1,sys.maxsize):
    som = 0
    for deler in range(1,(i//2)+1):
        if i % deler == 0:
            som += deler
    if som == i:
        print(f"{i} is een perfect getal.")
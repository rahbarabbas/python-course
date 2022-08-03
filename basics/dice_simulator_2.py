from random import randint
win_count=0
lose_count=0

dice=['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣']

while True:
    input('Press enter to 🎲 roll a dice')
    out=randint(1,6)
    print(f'🎲=>{dice[out-1]}')
    if out==6:
        win_count+=1
    elif out!=6:
        win_count=0
    if out==1:
        lose_count+=1
    elif out!=1:
        lose_count=0
    if win_count==2:
        print('You win 👑')
        break
    elif lose_count==2:
        print('You lose 💀')
        break

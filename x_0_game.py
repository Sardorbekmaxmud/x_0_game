g = [1,2,3,4,5,6,7,8,9]

def short_print():
    print(f"""
                {g[0]} | {g[1]} | {g[2]}
                ---------
                {g[3]} | {g[4]} | {g[5]}
                ---------
                {g[6]} | {g[7]} | {g[8]}
        """)
short_print()

while True:
    while True:
        x = int(input("x: "))
        if len(g)<x:
            print("bunday katak yo'q")
            continue
        if g[x-1]=="O" or g[x-1]=='X':
            print("kiritib bo'lmaydi")
            continue
        else:
            g[x-1]="X"
            break
    short_print()

    if g[0]==g[1]==g[2] or g[3]==g[4]==g[5] or g[6]==g[7]==g[8] or g[0]==g[3]==g[6] or g[1]==g[4]==g[7] or g[2]==g[5]==g[8] or g[0]==g[4]==g[8] or g[2]==g[4]==g[6]:
        print("👉 X 👈 WIN. 🎉Congratulations🎉")
        break

    if g.count('X')>=5 or g.count('O')>=5:
        print("DROW")
        break
    while True:
        o = int(input("O: "))
        if len(g)<o:
            print("bunday katak yo'q")
            continue
        if g[o-1]=="O" or g[o-1]=='X':
            print("🙅‍♂️ kiritib bo'lmaydi!")
            continue
        else:
            g[o-1]="O"
            break
    short_print()

    if g[0]==g[1]==g[2] or g[3]==g[4]==g[5] or g[6]==g[7]==g[8] or g[0]==g[3]==g[6] or g[1]==g[4]==g[7] or g[2]==g[5]==g[8] or g[0]==g[4]==g[8] or g[2]==g[4]==g[6]:
        print("👉 O 👈 WIN. 🎉Congratulations🎉")
        break

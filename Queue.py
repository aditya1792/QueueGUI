'''
   QUEUE in Python
'''

def PUSH():
    global Q,f,r

    if(f == -1):
        f=0

    r+=1

    print('\n Enter a num : ')
    n = int(input())
    Q.insert(r, n)

def DISP():
    global Q,f,r

    if(Q == []):
        print('\n QUEUE IS EMPTY ')
    else:
        print('\n QUEUE : ')
        for i in range(f, r+1):
            print(Q[i])

def PEEK():
    global Q,f,r

    if(Q == []):
        print('\n QUEUE IS EMPTY ')
    else:
        print('\n PEEK = ', Q[f])


def POP():
    global Q,f,r

    if(Q == []):
        print('\n QUEUE IS EMPTY ')
    else:
        Q.pop(f)
        r -= 1

    if(r == -1):
        f = -1

Q=[]
f=-1
r=-1

while(True):
    print('\n'*4)
    print('1] PUSH ')
    print('2] DISP ')
    print('3] PEEK ')
    print('4] POP ')
    print('5] EXIT ')

    print('\n Enter your choice : ')
    choice = int(input())

    if(choice == 1):
        PUSH()
        DISP()
    elif(choice == 2):
        DISP()        
    elif(choice == 3):
        PEEK()
    elif(choice == 4):
        POP()
        DISP()
    elif(choice == 5):
        print('\n EXIT ')
        break
    else:
        print('\n INVALID INPUT')
        





    

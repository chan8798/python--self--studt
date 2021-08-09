#Generate Sudoku
import random


def create():
    global puzzle
    maxAttempts = 100 #stops the program after 100 attempts
    count = 9999
    solCount = 0
    
    while count > maxAttempts:
        solCount +=1
        # init array
        puzzle = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(0)
                #print row
            puzzle.append(row)
    
        for row in range(9):
            for col in range(9):
                thisRow=puzzle[row]
                thisCol=[]
                for h in range(9):
                    thisCol.append(puzzle[h][col]) 
    
                subCol = int(col/3)
                subRow = int(row/3)
                subMat = []
                
                for subR in range (3):
                    for subC in range (3):
                        subMat.append(puzzle[subRow*3 + subR][subCol*3 + subC])
                
                randVal = 0
                count = 0
                
                while randVal in thisRow or randVal in thisCol or randVal in subMat:
                    randVal = random.randint(1,9)
                    count+=1
                    if count > maxAttempts: 
                        break 
                
                puzzle[row][col] = randVal
                if count > maxAttempts: 
                    break
                
            if count > maxAttempts:
                break
    
    for r in puzzle: 
        print (r)
    answer=[]
    for i in range(len(puzzle)):
        answer.append(puzzle[i].copy())

#정답

def copy_answer():
    global answer
    answer=[]
    for i in range(len(puzzle)):
        answer.append(puzzle[i].copy())

create()
copy_answer()
#정답 보여주기
def show_answer():
    for i in answer:
        print(i)
        
    for i in range(9):
        for j in range(9):
            if answer[i][j]==0:
                solvesquare(52+50*i,101+51*j,'light gray')
            else:
                fillsquare(answer[i][j],52+50*i,101+51*j, 'light gray')
             
    for i in range(3):
        for j in range(3):
            if answer[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(answer[i][j],52+50*i,101+51*j,'gray')
    
    for i in range(6,9):
        for j in range(3):
            if answer[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(answer[i][j],52+50*i,101+51*j,'gray')
    
    for i in range(3):
        for j in range(6,9):
            if answer[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(answer[i][j],52+50*i,101+51*j,'gray')
    
    for i in range(6,9):
        for j in range(6,9):
            if answer[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(answer[i][j],52+50*i,101+51*j,'gray')
    for i in range(3,6):
        for j in range(3,6):
            if answer[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(answer[i][j],52+50*i,101+51*j,'gray')

#쉬움
def easy():
    for i in range(9):
        rn1=random.randint(0,8)
        rn2=random.randint(0,8)
        while rn1==rn2:
           rn2=random.randint(0,8)
        puzzle[i][rn1]=0
        puzzle[i][rn2]=0
    for i in puzzle:
        print(i)
    
def medium():
    for i in range(9):
        rn1=random.randint(0,8)
        rn2=random.randint(0,8)
        while rn1==rn2:
            rn2=random.randint(0,8)
        rn3=random.randint(0,8)
        while rn1==rn3 or rn2==rn3:
            rn3=random.randint(0,8)
        rn4=random.randint(0,8)
        while rn1==rn4 or rn2==rn4 or rn3==rn4:
            rn4=random.randint(0,8)
        puzzle[i][rn1]=0
        puzzle[i][rn2]=0
        puzzle[i][rn3]=0
        puzzle[i][rn4]=0
    for i in puzzle:
        print(i)
    
def hard():
    for i in range(9):
        rn1=random.randint(0,8)
        rn2=random.randint(0,8)
        while rn1==rn2:
            rn2=random.randint(0,8)
        rn3=random.randint(0,8)
        while rn1==rn3 or rn2==rn3:
            rn3=random.randint(0,8)
        rn4=random.randint(0,8)
        while rn1==rn4 or rn2==rn4 or rn3==rn4:
            rn4=random.randint(0,8)
        rn5=random.randint(0,8)
        while rn1==rn5 or rn2==rn5 or rn3==rn5 or rn4==rn5:
            rn5=random.randint(0,8)
        rn6=random.randint(0,8)
        while rn1==rn6 or rn2==rn6 or rn3==rn6 or rn4==rn6 or rn5==rn6:
            rn6=random.randint(0,8)
        puzzle[i][rn1]=0
        puzzle[i][rn2]=0
        puzzle[i][rn3]=0
        puzzle[i][rn4]=0
        puzzle[i][rn5]=0
        puzzle[i][rn6]=0
    for i in puzzle:
        print(i)
        
def hell():
    for i in range(9):
        rn1=random.randint(0,8)
        rn2=random.randint(0,8)
        while rn1==rn2:
            rn2=random.randint(0,8)
        rn3=random.randint(0,8)
        while rn1==rn3 or rn2==rn3:
            rn3=random.randint(0,8)
        rn4=random.randint(0,8)
        while rn1==rn4 or rn2==rn4 or rn3==rn4:
            rn4=random.randint(0,8)
        rn5=random.randint(0,8)
        while rn1==rn5 or rn2==rn5 or rn3==rn5 or rn4==rn5:
            rn5=random.randint(0,8)
        rn6=random.randint(0,8)
        while rn1==rn6 or rn2==rn6 or rn3==rn6 or rn4==rn6 or rn5==rn6:
            rn6=random.randint(0,8)
        rn7=random.randint(0,8)
        while rn1==rn7 or rn2==rn7 or rn3==rn7 or rn4==rn7 or rn5==rn7 or rn6==rn7:
            rn7=random.randint(0,8)
        rn8=random.randint(0,8)
        while rn1==rn8 or rn2==rn8 or rn3==rn8 or rn4==rn8 or rn5==rn8 or rn6==rn8 or rn7==rn8:
            rn8=random.randint(0,8)
        puzzle[i][rn1]=0
        puzzle[i][rn2]=0
        puzzle[i][rn3]=0
        puzzle[i][rn4]=0
        puzzle[i][rn5]=0
        puzzle[i][rn6]=0
        puzzle[i][rn7]=0
        puzzle[i][rn8]=0
    for i in puzzle:
        print(i)

print ('Choose Difficulty:')
print ('1. Easy')
print ('2. Medium')
print ('3. Hard')
print ('4. Hell')
b=input().upper()
if b=='EASY':
    easy()
elif b=='MEDIUM':
    medium()
elif b=='HARD':
    hard()
elif b=='HELL':
    hell()

#############################################################
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

a=Tk()
canvas = Canvas(a,width=680,height=620,background='gray85')
canvas.pack()

canvas.create_line(0,340,680,340,fill='black',width=1000)
canvas.create_line(600,130,600,350,fill='gray92',width=150)

#줄 긋기
lx=49
rx=502
ty=98
by=562
canvas.create_line(lx+152,ty,lx+152,by,fill='red',width=2)
canvas.create_line(lx+302,ty,lx+302,by,fill='red',width=2)
canvas.create_line(lx,ty+155,rx,ty+155,fill='red',width=2)
canvas.create_line(lx,ty+309,rx,ty+309,fill='red',width=2)
canvas.create_line(rx,ty-3,rx,by+3,fill='white',width=6)
canvas.create_line(lx,ty-3,lx,by+3,fill='white',width=6)
canvas.create_line(lx,ty,rx,ty,fill='white',width=6)
canvas.create_line(lx,by,rx,by,fill='white',width=6)



def fillsquare(puzzle,row,col,color='white'):
    lbl=ttk.Label(a,text=puzzle,width=2)
    lbl.config(font=('arial black',25,'bold',),background=color,foreground='Blue')
    lbl.config(borderwidth=3)
    lbl.place(x=row,y=col)
    lbl.config(anchor='center')

def solvesquare(row,col,color='white'):
    textbox=Text(a,width=2,height=1)
    textbox.config(font=('arial black',25,'bold'),background=color,foreground='black')
    textbox.tag_configure('center',justify='center')
    textbox.insert("1.0"," ")
    textbox.tag_add('center',1.0,'end')
    textbox.place(x=row,y=col)

def new():
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==0:
                solvesquare(52+50*i,101+51*j,'light gray')
            else:
                fillsquare(puzzle[i][j],52+50*i,101+51*j, 'light gray')
             
    for i in range(3):
        for j in range(3):
            if puzzle[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(puzzle[i][j],52+50*i,101+51*j,'gray')
    
    for i in range(6,9):
        for j in range(3):
            if puzzle[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(puzzle[i][j],52+50*i,101+51*j,'gray')
    
    for i in range(3):
        for j in range(6,9):
            if puzzle[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(puzzle[i][j],52+50*i,101+51*j,'gray')
    
    for i in range(6,9):
        for j in range(6,9):
            if puzzle[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(puzzle[i][j],52+50*i,101+51*j,'gray')
    for i in range(3,6):
        for j in range(3,6):
            if puzzle[i][j]==0:
                solvesquare(52+50*i,101+51*j,'gray')
            else:
                fillsquare(puzzle[i][j],52+50*i,101+51*j,'gray')
                
                
                

def close():
    a.destroy()

def createnew():
    if radVar.get()==1:
        create()
        copy_answer()
        easy()
        new()
    if radVar.get()==2:
        create()
        copy_answer()
        medium()
        new()
    if radVar.get()==3:
        create()
        copy_answer()
        hard()
        new()
    if radVar.get()==4:
        create()
        copy_answer()
        hell()
        new()

radVar=IntVar()
action1 = ttk.Radiobutton(a, text = "쉬움", variable=radVar, value = 1, command = createnew())  
action2 = ttk.Radiobutton(a, text = "중간", variable=radVar,value = 2,  command = createnew())  
action3 = ttk.Radiobutton(a, text = '어려움', variable=radVar,value=3, command = createnew())
action4 = ttk.Radiobutton(a, text = '아주 어려움', variable=radVar,value=4, command = createnew())

action1.place(x=550,y=190)
action2.place(x=550,y=210)
action3.place(x=550,y=230)
action4.place(x=550,y=250)

        
new()

#메뉴
bcreate=Button(a,text="새로 만들기",command=createnew)
bcreate.place(x=550,y=150)
bcreate.config(font=('굴림',11,'bold'))
bcreate.config(width=10)

ccreate=Button(a,text="정답",command=show_answer)
ccreate.place(x=550,y=310)
ccreate.config(font=('굴림',11,'bold'))
ccreate.config(width=10)

dcreate=Button(a,text="정답 체크",command='')
dcreate.place(x=550,y=280)
dcreate.config(font=('굴림',11,'bold'))
dcreate.config(width=10)

lbl=ttk.Label(a,text='Sudoku',width=33)
lbl.config(font=('굴림',25,'bold',),background='black',foreground='White')
lbl.config(borderwidth=3)
lbl.place(x=5,y=50)
lbl.config(anchor='center')

canvas.configure(background='white')
a.title("스도쿠 게임")
a.geometry('680x620+450+100')
a.mainloop()



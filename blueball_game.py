from tkinter import *
import tkinter.messagebox as t

root = Tk()
 
# Create Title
root.title(  "Put_the_ball_in bucket")

def red(event):
    global redball
    redball=PhotoImage(file="D:\\bball.png")
    redball1=can.create_image(event.x,event.y,image=redball)
    if((event.x>1 and event.x<203)and (event.y>330 and event.y<432)):
        release(event)
        print("1 if activated")
    if((event.x>900 and event.x<1412) and (event.y>390 and event.y<750)):
        release(event)
        print("2 if activated")
    if((event.x>876 and event.x<977) and (event.y==292)):
        release(event)
        print("3 if activated")
    if((event.x>856 and event.x<876) and (event.y>292 and event.y<307)):
        release(event)
        print("4 if activated")
    if((event.x>837 and event.x<856) and (event.y>307 and event.y<342)):
        print("5 is activated")
    if((event.x>843 and event.x<845) and (event.y>345 and event.y<493)):
        release(event)
        print("6 if activated")
    if((event.x>794 and event.x<843) and (event.y>493 and event.y<554)):
        release(event)
        print("7 if activated")
    if((event.x>648 and event.x<799) and (event.y==568)):
        release(event)
        print("8 if activated")
    if((event.x>599 and event.x<608) and (event.y>484 and event.y<537)):
        release(event)
        print("9 if activated")
    if ((event.x>608 and event.x<648) and (event.y>537 and event.y<568)):
        release(event)
        print("10 is activated")
    if((event.x>570 and event.x<592) and (event.y>420 and event.y<484)):
        release(event)
        print("11 if activated")
    if((event.x>552 and event.x<563) and (event.y>411 and event.y<420)):
        print("12 id activated")
    if((event.x>520 and event.x<552) and (event.y>386 and event.y<421)):
        release(event)
        print("13 if activated")
    if((event.x>382 and event.x<550) and (event.y==386)):
        release(event)
        print("14 if activated")
    if((event.x>327 and event.x<382) and (event.y>389 and event.y<392)):
        release(event)
        print("15 if activated")
    if((event.x>246 and event.x<327) and (event.y==398)):
        release(event)
        print("16 if activated")
    if((event.x>226 and event.x<246) and (event.y>394 and event.y<401)):
        release(event)
        print("17 if activated")
    if((event.x>199 and event.x<226) and (event.y>402 and event.y<434)):
        release(event)
        print("18 is activated")
    if((event.x==202) and (event.y>444 and event.y<554)):
        release(event)
        print("19 if activated")
    if((event.x>184 and event.x<202) and (event.y>573 and event.y<579)):
        release(event)
        print("20 if activated")
    if((event.x>164 and event.x<184) and (event.y>554 and event.y<573)):
        release(event)
        print("21 is activated")
    #above all are upside touch events
    if((event.x>910 and event.x<966) and event.y>=343 and event.y<=353):
        release(event)
        print("down wala touch  part1")
    if((event.x>896 and event.x<910) and (event.y>345 and event.y<529)):
        release(event)
        print("down wala touch part2")
    if((event.x>876 and event.x<896) and (event.y>529 and event.y<583)):
        release(event)
        print("down wala part 3")
    if((event.x>849 and event.x<876) and (event.y>583 and event.y<605)):
        release(event)
        print("down wala part 4")
    if((event.x>792 and event.x<849) and (event.y>605 and event.y<626)):
        release(event)
        print("down wala part 5")
    if((event.x>635 and event.x<801) and (event.y==623)):
        release(event)
        print("down wala part 6")
    if((event.x>576 and event.x<635) and (event.y>592 and event.y<623)):
        release(event)
        print("down wala part 7")
    if((event.x>576 and event.x<543) and (event.y>556 and event.y<623)):
        release(event)
        print("down wala part 8")
    if((event.x>530 and event.x<543) and (event.y>486 and event.y<556)):
        release(event)
        print("down wala part 9")
    if((event.x>504 and event.x<530) and (event.y>454 and event.y<486)):
        print("down wala part 10 ")
        release(event)
    if((event.x>379 and event.x<501) and (event.y>435 and event.y<454)):
        print("down wala part 11")
        release(event)
    if((event.x>329 and event.x<380) and (event.y>425 and event.y<449)):
        print("down part 12")
        release(event)
    if((event.x>252 and event.x<328) and (event.y==425)):
        print("down wala part 13")
        release(event)
    if((event.x>235 and event.x<252) and (event.y>429 and event.y<458)):
        print("down wala part 14")
        release(event)
    if((event.x==233) and (event.y>459 and event.y<562)):
        print("down wala part 15")
        release(event)
    if((event.x>212 and event.x<234) and (event.y>562 and event.y<592)):
        print("down wala part  16")
        release(event)
    if((event.x>193 and event.x<210) and (event.y>597 and event.y<611)):
        print("down wala part 17")
        release(event)
    if((event.x>166 and event.x<194) and (event.y>607 and event.y<614)):
        print("down wala part 18")
        release(event)
    
        
    
    
    
def funny(event):
    global phot01
    phot01=PhotoImage(file="D:\\pipe.png")
    my_can=can.create_image(event.x,event.y,image=phot01)

def release(event):
    can.delete("all")
    la=Label(can,text="Game Over ",font="TimesNewRoman 45 bold",fg="red")
    la.pack(pady=250,side="top")
    if((event.x>1 and event.x<203)and (event.y>330 and event.y<432) or ((event.x>900 and event.x<1412) and (event.y>390 and event.y<750))):
        l=Label(can,text="You crossed the danger line or going to cross it",font="TimesNewRoman 19 bold")
        l.pack(side="top")
    b1=Button(can,text="finish",fg="red",font="TimesNewRoman 19 bold",command=close)
    b1.pack(pady=2,side="top")
    
def close():
    root.destroy()

def function():
    instruction_window.destroy()
    
        
def instruction():
    ans=t.askyesno("Instructions","Have You Read The Instruction Before Playing?")
    if(ans==False):
        print("hello")
        global instruction_window
        instruction_window=Toplevel()
        instruction_window.title("Instructions")
        instruction_window.config(bg="black")
        instruction_window.geometry('2000x750')
        f1=Frame(instruction_window,bg="black")
        f1.pack(side="top")
        l1=Label(f1,text="Rules",font="TimesNewRoman 19 bold",bg="black",fg="red")
        l1.pack(side="top")

        l2=Label(f1,text="1)Your Ball should not cross or touch the danger lines(prohibited lines) in the game.\n\n2)following are the particular keys are given to particular balls.\n\n3)Once you release the key before puting ball in bucket you will lose the game.\n\n4)Follow the Directions for playing throughly."
                  ,fg="white",font="TimesNewRoman 15 bold",bg="black").pack(side="top")
        f2=Frame(instruction_window,bg="black")
        f2.pack(side="top")
        l3=Label(f1,text="Directions for playing(Controls)",font="TimesNewRoman 19 bold",bg="black",fg="red")
        l3.pack(side="top",pady=20)
        l2=Label(f1,text="1)For Red Ball - Continue Press 1(on keyboard) + Mouse Motion(Don't release untill putting ball in bucket)\n\n2)For Green Ball-Press 2 + Motion\n\n3)for YELLOW ball - press 3 + Motion\n\n4)for BLUE ball -press  4 + Motion.\n\n5)for BLACK ball -press 5 + Motion\n\n6)for Grey ball-press 6 + Motion\n\n7)for PINK ball-press 7 + Motion\n\n8)for Brown ball -press 8 +Motion"
                  ,fg="white",font="TimesNewRoman 15 bold",bg="black").pack(side="top")
        b1=Button(f2,text="Go to Game",fg="black",bg="yellow",command=function).pack(side="top")
        

def ss(event):
    print("hello")
    
    
  
    
# specify size
root.geometry("2000x750")
instruction()
f1=Frame(root,height=695,width=1350,)
f1.pack()
can=Canvas(f1,height=695,width=1350,) 
can.pack()
#can.bind('<Control-Motion>',fun)
phot01=PhotoImage(file="D:\\pipe.png")
my_can=can.create_image(580,495,image=phot01)
buc=PhotoImage(file="D:\\bucket.png")
bucket=can.create_image(115,640,image=buc)
plate=PhotoImage(file="D:\\plate.png")
plate1=can.create_image(610,200,image=plate)
redball=PhotoImage(file="D:\\bball.png")
redball1=can.create_image(606,190,image=redball)
ch=PhotoImage(file="D:\\chainleft.png")
c=can.create_image(-75,230,image=ch)
chrr=PhotoImage(file="D:\\rightchain.png")
cs=can.create_image(1275,255,image=chrr)
can.bind('<Control-Motion>',red)
root.bind('<KeyRelease-Control_R>',release)
root.bind('<KeyRelease-Control_L>',release)


#16 down wala
#18 part is activated
#down part 7
#resolve this




root.mainloop()

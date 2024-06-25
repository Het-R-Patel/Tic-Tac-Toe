from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Programmatic_tech - Tic tac Toe")
root.geometry("700x750+220+50")
root.config(background="#FFC7C7")
photo = PhotoImage(file = "graphics/plog.png")
root.iconphoto(False, photo)
root.resizable(0,0)

#x start
clicked=True
count=0

#image of reset
imgres=PhotoImage(file='graphics/res.png')
# images for simple
img1=PhotoImage(file='graphics/0s.png')
imgs=PhotoImage(file='graphics/s.png')
img3=PhotoImage(file='graphics/2s.png')
img4=PhotoImage(file='graphics/3s.png')
img5=PhotoImage(file='graphics/1s.png')
#image for x
img1x=PhotoImage(file='graphics/0x.png')
imgx=PhotoImage(file='graphics/x.png')
img3x=PhotoImage(file='graphics/2x.png')
img4x=PhotoImage(file='graphics/3x.png')
img5x=PhotoImage(file='graphics/1x.png')
#image for 0
img1o=PhotoImage(file='graphics/0o.png')
imgo=PhotoImage(file='graphics/o.png')
img3o=PhotoImage(file='graphics/2o.png')
img4o=PhotoImage(file='graphics/3o.png')
img5o=PhotoImage(file='graphics/1o.png')

#imges for horiz line X
img1xh=PhotoImage(file='graphics/1xh.png')
img2xh=PhotoImage(file='graphics/2xh.png')
img3xh=PhotoImage(file='graphics/3xh.png')
img4xh=PhotoImage(file='graphics/4xh.png')
img5xh=PhotoImage(file='graphics/5xh.png')
img6xh=PhotoImage(file='graphics/6xh.png')
img7xh=PhotoImage(file='graphics/7xh.png')
img8xh=PhotoImage(file='graphics/8xh.png')
img9xh=PhotoImage(file='graphics/9xh.png')

#imges for vertical line X
img1xv=PhotoImage(file='graphics/1xv.png')
img2xv=PhotoImage(file='graphics/2xv.png')
img3xv=PhotoImage(file='graphics/3xv.png')
img4xv=PhotoImage(file='graphics/4xv.png')
img5xv=PhotoImage(file='graphics/5xv.png')
img6xv=PhotoImage(file='graphics/6xv.png')
img7xv=PhotoImage(file='graphics/7xv.png')
img8xv=PhotoImage(file='graphics/8xv.png')
img9xv=PhotoImage(file='graphics/9xv.png')

#imges for cross left and right line X
img1cl=PhotoImage(file='graphics/1xcl.png')
img9cl=PhotoImage(file='graphics/9xvl.png')
img5cl=PhotoImage(file='graphics/5xcl.png')

img3cr=PhotoImage(file='graphics/3xcr.png')
img7cr=PhotoImage(file='graphics/7xcr.png')
img5cr=PhotoImage(file='graphics/5xcr.png')


#imges for horiz line O
img1oh=PhotoImage(file='graphics/1oh.png')
img2oh=PhotoImage(file='graphics/2oh.png')
img3oh=PhotoImage(file='graphics/3oh.png')
img4oh=PhotoImage(file='graphics/4oh.png')
img5oh=PhotoImage(file='graphics/5oh.png')
img6oh=PhotoImage(file='graphics/6oh.png')
img7oh=PhotoImage(file='graphics/7oh.png')
img8oh=PhotoImage(file='graphics/8oh.png')
img9oh=PhotoImage(file='graphics/9oh.png')

#imges for vertical line O
img1ov=PhotoImage(file='graphics/1ov.png')
img2ov=PhotoImage(file='graphics/2ov.png')
img3ov=PhotoImage(file='graphics/3ov.png')
img4ov=PhotoImage(file='graphics/6ov.png')
img5ov=PhotoImage(file='graphics/5ov.png')
img6ov=PhotoImage(file='graphics/4ov.png')
img7ov=PhotoImage(file='graphics/7ov.png')
img8ov=PhotoImage(file='graphics/8ov.png')
img9ov=PhotoImage(file='graphics/9ov.png')

#imges for cross left and right line O
img1ocl=PhotoImage(file='graphics/1ocr.png')
img9ocl=PhotoImage(file='graphics/9ocr.png')
img5ocl=PhotoImage(file='graphics/5ocr.png')

img3ocr=PhotoImage(file='graphics/3ocl.png')
img7ocr=PhotoImage(file='graphics/7ocl.png')
img5ocr=PhotoImage(file='graphics/5ocl.png')

#Buttons
#reset 
def reset():
    
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked= True
    count = 0
    b1=Button(root,text=" ",image=img1,overrelief=FLAT,relief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b1))
    b1.place(x=50,y=30)
    b2=Button(root,text=" ",image=imgs,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b2))
    b2.place(x=250,y=30)
    b3=Button(root,text=" ",image=img3,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b3))
    b3.place(x=450,y=30)

    b4=Button(root,text=" ",image=imgs,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b4))
    b4.place(x=50,y=230)
    b5=Button(root,text=" ",image=imgs,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b5))
    b5.place(x=250,y=230)
    b6=Button(root,text=" ",image=imgs,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b6))
    b6.place(x=450,y=230)

    b7=Button(root,text=" ",image=img4,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b7))
    b7.place(x=50,y=430)
    b8=Button(root,text=" ",image=imgs,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b8))
    b8.place(x=250,y=430)
    b9=Button(root,text=" ",image=img5,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=lambda: b_click(b9))
    b9.place(x=450,y=430)

    resetbtn=Button(root,text=" ",image=imgres,relief=FLAT,overrelief=FLAT,border=0,bg="#FFC7C7",
            activebackground="#FFC7C7",command=reset)
    resetbtn.place(x=240,y=650)
#disable all buttons 
def disabled():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# check for win
def checkifwon():
    global winner
    winner = False

# logic for x wins
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.configure(image=img1xh)
        b2.configure(image=img2xh)
        b3.configure(image=img3xh)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.configure(image=img4xh)
        b5.configure(image=img5xh)
        b6.configure(image=img6xh)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.configure(image=img7xh)
        b8.configure(image=img8xh)
        b9.configure(image=img9xh)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.configure(image=img1xv)
        b4.configure(image=img4xv)
        b7.configure(image=img7xv)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.configure(image=img2xv)
        b5.configure(image=img5xv)
        b8.configure(image=img8xv)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.configure(image=img3xv)
        b6.configure(image=img6xv)
        b9.configure(image=img9xv)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.configure(image=img1cl)
        b5.configure(image=img5cl)
        b9.configure(image=img9cl)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.configure(image=img3cr)
        b5.configure(image=img5cr)
        b7.configure(image=img7cr)
        winner = True
        disabled()
        labg=Label(root,text="X WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)


# logic for o wins


    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.configure(image=img1oh)
        b2.configure(image=img2oh)
        b3.configure(image=img3oh)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.configure(image=img4oh)
        b5.configure(image=img5oh)
        b6.configure(image=img6oh)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.configure(image=img7oh)
        b8.configure(image=img8oh)
        b9.configure(image=img9oh)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.configure(image=img1ov)
        b4.configure(image=img4ov)
        b7.configure(image=img7ov)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.configure(image=img2ov)
        b5.configure(image=img5ov)
        b8.configure(image=img8ov)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.configure(image=img3ov)
        b6.configure(image=img6ov)
        b9.configure(image=img9ov)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.configure(image=img1ocl)
        b5.configure(image=img5ocl)
        b9.configure(image=img9ocl)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.configure(image=img3ocr)
        b5.configure(image=img5ocr)
        b7.configure(image=img7ocr)
        winner = True
        disabled()
        labg=Label(root,text="O WINS \n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
# check for tie
    if count == 9 and winner == False:
        labg=Label(root,text="IT'S A TIE\n !!GAME OVER!!",border=0,font=("Times new roman",40),background="#7071E8",foreground="black")
        labg.place(x=150,y=260)
        disabled()


#buttons functions
def b_click(b):
    global clicked , count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked=False
        count +=1
   
      
        if b==b1:
            
            b1.configure(image=img1x)
        elif b==b2:
          
            b2.configure(image=imgx)
        elif b==b3:
           
            b3.configure(image=img4x)
        elif b==b4:
           
            b4.configure(image=imgx)
        elif b==b5:
            
            b5.configure(image=imgx)
        elif b==b6:
        
            b6.configure(image=imgx)
        elif b==b7:
         
            b7.configure(image=img3x)
        elif b==b8:
            
            b8.configure(image=imgx)
        elif b==b9:
       
            b9.configure(image=img5x)
        else:
            pass
        checkifwon()
        
    elif  b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked=True
        count +=1 

        
        if b==b1:
            
            b1.configure(image=img1o)
        elif b==b2:
            
            b2.configure(image=imgo)
        elif b==b3:
            
            b3.configure(image=img4o)
        elif b==b4:
            
            b4.configure(image=imgo)
        elif b==b5:
         
            b5.configure(image=imgo)
        elif b==b6:
         
            b6.configure(image=imgo)
        elif b==b7:
            
            b7.configure(image=img3o)
        elif b==b8:
           
            b8.configure(image=imgo)
        elif b==b9:
          
            b9.configure(image=img5o)
        else:
            pass
        checkifwon()
              
    else:
        messagebox.showerror("Tic Tac Toe","Please choose another box !!")
        


    

reset()
root.mainloop()
from tkinter import *
import time
from tkinter.scrolledtext import ScrolledText
import csv

root = Tk()
root.title("Typing Speed Test")

c = Canvas(root,height =600, width = 600,bg = 'yellow')
c.grid(rowspan=5,columnspan =5)


# Functions Definitions
#----------------------------------------------------------------------------------------QUIT----------------------------------------------------------------------------------------
def quit():
    quit_btn_text.set('Quiting...')
    time.sleep(1)
    root.destroy()



def click_on_space(event):
        if event.char == ' ':
          e.delete(0,END)
          counter.set(counter.get()+1)


#----------------------------------------------------------------------------------------START----------------------------------------------------------------------------------------
def start():
    top = Toplevel(root,height = 600,width = 600,bg = '#FFFDDE')
    top.title('Start!')
    t=ScrolledText(top,wrap = WORD,width = 50,height = 20)
    t.place(x=100,y=10)
    t.insert(INSERT,"Some Text")

    entry_label = Label(top,text = 'Write the text here!',bg = '#FFFDDE',font = (('Ariel'),10,'bold'))
    entry_label.place(x=250,y=480)

    global counter
    counter= IntVar()
    counter_label_num = Label(top, textvariable = counter, bg='#FFFDDE', font=(('Ariel'), 10, 'bold'))
    counter_label_num.place(x=250,y=450)
    counter_label_text = Label(top, text = "Counter: ", bg='#FFFDDE', font=(('Ariel'), 10, 'bold'))
    counter_label_text.place(x=190,y=450)


    text_file = open('test.txt','r')
    stuff = text_file.read()

    global e
    e = Entry(top,width = 40)
    e.place(x=180,y = 500)
    e.bind("<Key>",click_on_space)
    t.insert(END,stuff)
    t.config(state = DISABLED)


    text_file.close()



instruction_label =Label(root,text = "Welcome to the typing speed challenge!",font = (('SimSun'),16,'bold'),bg = 'yellow')
instruction_label.place (x=100,y = 50)

ready_label = Label(root,text = "Ready? press Click To Start!",font = (('SimSun'),14),bg = 'yellow',fg = 'black',pady=0)
ready_label.place(x = 160 , y =100)



# Button Definitions
start_btn_text = StringVar()
start_btn_text.set('Click To Start!')
start_btn = Button(root,textvariable =start_btn_text ,command = start,bg = 'white',padx =30 ,pady=10)
start_btn.place(x=80,y = 500)


quit_btn_text = StringVar()
quit_btn_text.set('Quit')
quit_btn = Button(root,textvariable =quit_btn_text ,bg = 'white',command = quit,padx=30,pady=10)
quit_btn.place(x=400,y = 500)

root.mainloop()
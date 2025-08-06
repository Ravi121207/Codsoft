import tkinter as tk

def exit():
    root.quit()
root=tk.Tk()
root.title("TO DO LIST")
root.geometry("800x500")
root.configure(bg="magenta")

lb=tk.Label(root,text="To Do List",font=("arial",25),bg="magenta")
lb.place(x=10,y=10)
en=tk.Entry(root,width=25,font=("arial",25),highlightthickness="3")
en.place(x=200,y=10)

lst=tk.Listbox(root,width=30,height=10,font=("arial",20),highlightthickness="3")
lst.place(x=200,y=70)

def add():
    task=en.get()
    lst.insert(tk.END,task)
    en.delete(0,tk.END)
 
def mark():
    selection=lst.curselection()
    if selection:
        pos = selection[0]
        text=lst.get(pos)
        lst.delete(pos)
        lst.insert(tk.END,f"{text} \u2713")
    else:
        print("No task selected to mark.")

def remove():
    selection = lst.curselection()
    if selection:
        pos = selection[0]
        lst.delete(pos)
    else:
        print("No task selected to remove.")


btn1=tk.Button(root,text="Add",font=("arial",15,"bold"),cursor="hand2",width=7,command=add)
btn1.place(x=200,y=420)

btn2=tk.Button(root,text="Mark",font=("arial",15,"bold"),cursor="hand2",width=7,command=mark)
btn2.place(x=320,y=420)

btn3=tk.Button(root,text="Remove",font=("arial",15,"bold"),cursor="hand2",width=7,command=remove)
btn3.place(x=440,y=420)

btn4=tk.Button(root,text="Exit",font=("arial",15,"bold"),cursor="hand2",width=7,command=exit)
btn4.place(x=564,y=420)

root.mainloop()
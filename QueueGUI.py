import tkinter as tk

def PUSH():
    global Q, f, r
    if f == -1:
        f = 0
    r += 1
    n = int(entry.get())
    Q.insert(r, n)
    entry.delete(0, tk.END)
    DISP()

def DISP():
    global Q, f, r
    if Q == []:
        queue_label.config(text='QUEUE IS EMPTY')
    else:
        queue_label.config(text='QUEUE:\n' + ' '.join(str(n) for n in Q[f:r+1]))

def PEEK():
    global Q, f
    if Q == []:
        queue_label.config(text='QUEUE IS EMPTY')
    else:
        queue_label.config(text='PEEK = ' + str(Q[f]))

def POP():
    global Q, f, r
    if Q == []:
        queue_label.config(text='QUEUE IS EMPTY')
    else:
        Q.pop(f)
        r -= 1
    if r == -1:
        f = -1
    DISP()

def exit_program():
    root.destroy()

Q = []
f = -1
r = -1

root = tk.Tk()
root.title("Queue Program")

# Set the background color or gradient
background_color = "orange"  # Light gray

root.configure(bg=background_color)

queue_label = tk.Label(root, text="")
queue_label.pack()

entry = tk.Entry(root)
entry.pack()

push_button = tk.Button(root, text="PUSH", bg="red", command=PUSH, width=10, height=2)
push_button.pack()

disp_button = tk.Button(root, text="DISP", bg="blue", command=DISP, width=10, height=2)
disp_button.pack()

peek_button = tk.Button(root, text="PEEK", bg="green", command=PEEK, width=10, height=2)
peek_button.pack()

pop_button = tk.Button(root, text="POP", bg="violet", command=POP, width=10, height=2)
pop_button.pack()

exit_button = tk.Button(root, text="EXIT", bg="orange", command=exit_program, width=10, height=2)
exit_button.pack()

root.mainloop()

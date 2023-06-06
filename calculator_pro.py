import tkinter as tk
from tkinter import messagebox

# TODO SIMPLIFY THE CODE
def insert_entry(text : str):
    entry_screen.insert(index='insert', string=text)

def get_entry():
    return entry_screen.get()

def fun_ce():
    entry_screen.delete(0, tk.END)

def fun_cl():
    entry = get_entry()
    new_entry = entry[0:-1]         # remove the last character entered

    fun_ce()        # clear the entry screen
    insert_entry(new_entry)
    
def fun_1():
    text = "1"
    insert_entry(text)

def fun_2():
    text = "2"
    insert_entry(text)

def fun_3():
    text = "3"
    insert_entry(text)

def fun_4():
    text = "4"
    insert_entry(text)

def fun_5():
    text = "5"
    insert_entry(text)

def fun_6():
    text = "6"
    insert_entry(text)

def fun_7():
    text = "7"
    insert_entry(text)

def fun_8():
    text = "8"
    insert_entry(text)

def fun_9():
    text = "9"
    insert_entry(text)

def fun_0():
    text = "0"
    insert_entry(text)

def fun_plus():
    text = "+"
    insert_entry(text)

def fun_minus():
    text = "-"
    insert_entry(text)

def fun_multiply():
    text = "*"
    insert_entry(text)

def fun_divide():
    text = "/"
    insert_entry(text)

def fun_equal():
    equation = get_entry()
    fun_ce()
    # evaluation the equation entered and give error for incorrect syntax
    try:
        answer = eval(equation)     
        insert_entry(answer)
    except Exception:
        messagebox.showerror("Error!", "SYNTAX ERROR")
        


if __name__ == '__main__':
    # INTERFACE

    main_window = tk.Tk()
    main_window.config(background='white')
    main_window.config(pady=20)
    main_window.geometry('440x440+500+100')
    main_window.resizable(False, False)
    main_window.title("Calculator Pro")
    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=10)
    main_window.columnconfigure(0, weight=1)
    # main_window.columnconfigure(0, weight=1)

    # entry screen
    entry_screen = tk.Entry(main_window, borderwidth=5, width=25, font=('FiraCode',20))
    entry_screen.grid(row=0, column=0)
    
    # buttons frame
    buttons_frame = tk.Frame(main_window, background='light blue', borderwidth=5)
    buttons_frame.grid(row=1, column=0)

    # buttons
    # row 0
    button_ce = tk.Button(buttons_frame, text='CE', width=5, font=("FiraCode", 20), command=fun_ce)
    button_ce.grid(row=0, column=0)
    button_cl = tk.Button(buttons_frame, text='CL', width=5, font=("FiraCode", 20), command=fun_cl)
    button_cl.grid(row=0, column=1)
    # row 1
    button_7 = tk.Button(buttons_frame, text='7', width=5, font=("FiraCode", 20), command=fun_7)
    button_7.grid(row=1, column=0)
    button_8 = tk.Button(buttons_frame, text='8', width=5, font=("FiraCode", 20), command=fun_8)
    button_8.grid(row=1, column=1)
    button_9 = tk.Button(buttons_frame, text='9', width=5, font=("FiraCode", 20), command=fun_9)
    button_9.grid(row=1, column=2)
    button_plus = tk.Button(buttons_frame, text='+', width=5, font=("FiraCode", 20), command=fun_plus)
    button_plus.grid(row=1, column=3)
    # row 2
    button_4 = tk.Button(buttons_frame, text='4', width=5, font=("FiraCode", 20), command=fun_4)
    button_4.grid(row=2, column=0)
    button_5 = tk.Button(buttons_frame, text='5', width=5, font=("FiraCode", 20), command=fun_5)
    button_5.grid(row=2, column=1)
    button_6 = tk.Button(buttons_frame, text='6', width=5, font=("FiraCode", 20), command=fun_6)
    button_6.grid(row=2, column=2)
    button_minus = tk.Button(buttons_frame, text='-', width=5, font=("FiraCode", 20), command=fun_minus)
    button_minus.grid(row=2, column=3)
    # row 3
    button_1 = tk.Button(buttons_frame, text='1', width=5, font=("FiraCode", 20), command=fun_1)
    button_1.grid(row=3, column=0)
    button_2 = tk.Button(buttons_frame, text='2', width=5, font=("FiraCode", 20), command=fun_2)
    button_2.grid(row=3, column=1)
    button_3 = tk.Button(buttons_frame, text='3', width=5, font=("FiraCode", 20), command=fun_3)
    button_3.grid(row=3, column=2)
    button_multiply = tk.Button(buttons_frame, text='*', width=5, font=("FiraCode", 20), command=fun_multiply)
    button_multiply.grid(row=3, column=3)
    # row 4
    button_0 = tk.Button(buttons_frame, text='0', width=5, font=("FiraCode", 20), command=fun_0)
    button_0.grid(row=4, column=0)
    button_equal = tk.Button(buttons_frame, text='=', width=5, font=("FiraCode", 20), command=fun_equal)
    button_equal.grid(row=4, column=1, columnspan=2, sticky='news')
    button_divide = tk.Button(buttons_frame, text='/', width=5, font=("FiraCode", 20), command=fun_divide)
    button_divide.grid(row=4, column=3)

    main_window.mainloop()
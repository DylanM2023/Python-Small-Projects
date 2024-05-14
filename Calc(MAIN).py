from tkinter import *

calculator = Tk()
calculator.geometry("600x800")
calculator.title("Calculator App")


def calc_screen():

    screen_frame = Frame(calculator)
    screen_frame.configure(
        width = "600", 
        height = "100", 
    )
    screen_frame.propagate(False)
    screen_frame.pack(side = TOP , pady = 10)

    display = Entry(
    screen_frame,
    font = ("Bold", 50))

    display.bind("<Key>", lambda a: "break") #stops users from entering in entry box

    display.pack(side=RIGHT)
    
    def disply_input(number):
        equation = display.get()
        if len(equation) >= 1:
            display.delete("0" , "end")
            equation += number
            display.insert(index=False , string = equation)
        else:
            display.insert(index = False , string=number)

    def clear_display():
        display.delete("0" , "end")

    def button_rows():

        
        button_r_1 = Frame()
        button_r_1.propagate(False)
        button_r_1.config(width=580 , height=135 , bg="Red")
        button_r_1.pack(side = TOP)

        button_r_2 = Frame()
        button_r_2.propagate(False)
        button_r_2.config(width=580 , height=135 , bg="white")
        button_r_2.pack(side =TOP)

        button_r_3 = Frame()
        button_r_3.propagate(False)
        button_r_3.config(width=580 , height=135 , bg="black")
        button_r_3.pack()

        button_r_4 = Frame()
        button_r_4.propagate(False)
        button_r_4.config(width=580 , height=135 , bg="yellow")
        button_r_4.pack()

        button_r_5 = Frame()
        button_r_5.propagate(False)
        button_r_5.config(width=580 , height=135 , bg="orange")
        button_r_5.pack()

        clear_button = Button(
            button_r_1,
            text="C",
            width=10,
            height=5,
            command = lambda: clear_display()
        )
        one_button = Button(
            button_r_2,
            text=" 1 ",
            width=10,
            height=5,
            font= ("Bold" , 15),
            command = lambda: disply_input("1")
        )
        two_button = Button(
            button_r_2,
            text=" 2 ",
            width=10,
            height=5,
            font= ("Bold" , 15),
            command = lambda: disply_input("2")

        )
        three_button = Button(
            button_r_2,
            text=" 3 ",
            width=10,
            height=5,
            font= ("Bold" , 15),
            command = lambda: disply_input("3")
        )
        four_button = Button(
            button_r_3,
            text=" 4 ",
            width=10,
            height=5,
            font= ("Bold" , 15),
            command = lambda: disply_input("4")
        )
        clear_button.pack(padx = "5" , pady = "5" , side=LEFT)
        one_button.pack(padx = "5" , pady = "5" , side=LEFT)
        two_button.pack(padx = "5" , pady = "5" , side=LEFT)
        three_button.pack(padx = "5" , pady = "5" , side=LEFT)
        four_button.pack(padx = "5" , pady = "5" , side=LEFT)

    button_rows()




calc_screen()


calculator.mainloop()


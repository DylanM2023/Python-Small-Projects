from tkinter import *

calculator = Tk()
calculator.geometry("470x790")
calculator.resizable(width=False , height=False)
calculator.title("Calculator App")
calculator.configure(bg="#222222")

def calculator_functions():
    def calc_ui():
        screen = Entry(
            width=500,
            font= ("Bold" , 50)
        )
        screen.pack(side=TOP , pady=10)
        screen.bind("<Key>", lambda a: "break")        


        def display_equation(character):
            user_input = screen.get()
            if len(user_input) >= 1:
                screen.delete("0" , "end")
                equation = user_input + character
                screen.insert(index=False , string = equation)
            else:
                screen.insert(index=False , string = character)

        def clear_screen():
            screen.delete("0" , "end")

        def solve():
            equation = screen.get()
            screen.delete("0" , "end")
            print(equation)

        def add_buttons():
            button_r_1 = Frame(
                width=550,
                height=135,
                bg="Red"
            )

            button_r_1.propagate(False)

            button_r_2 = Frame(
                width=550,
                height=135,
                bg="Blue"
            )

            button_r_2.propagate(False)

            button_r_3 = Frame(
                width=550,
                height=135,
                bg="Yellow"
            )

            button_r_3.propagate(False)

            button_r_4 = Frame(
                width=550,
                height=135,
                bg="Orange"
            )

            button_r_4.propagate(False)

            button_r_5 = Frame(
                width=550,
                height=135,
                bg="Purple"
            )

            button_r_5.propagate(False)

            clear_button = Button(
                button_r_1,
                width=5,
                height=2,
                text="C",
                font=("Bold",25),
                command= lambda: clear_screen()
            )

            one_button = Button(
                button_r_2,
                width=5,
                height=2,
                text="1",
                font=("Bold",25),
                command= lambda: display_equation("1")
            )

            two_button = Button(
                button_r_2,
                width=5,
                height=2,
                text="2",
                font=("Bold",25),
                command= lambda: display_equation("2")
            )

            three_button = Button(
                button_r_2,
                width=5,
                height=2,
                text="3",
                font=("Bold",25),
                command= lambda: display_equation("3")
            )

            multiply_button = Button(
                button_r_2,
                width=5,
                height=2,
                text="x",
                font=("Bold",25),
                command= lambda: display_equation("x")
            )

            four_button = Button(
                button_r_3,
                width=5,
                height=2,
                text="4",
                font=("Bold",25),
                command= lambda: display_equation("4")
            )

            five_button = Button(
                button_r_3,
                width=5,
                height=2,
                text="5",
                font=("Bold",25),
                command= lambda: display_equation("5")
            )

            six_button = Button(
                button_r_3,
                width=5,
                height=2,
                text="6",
                font=("Bold",25),
                command= lambda: display_equation("6")
            )

            subtract_button = Button(
                button_r_3,
                width=5,
                height=2,
                text="-",
                font=("Bold",25),
                command= lambda: display_equation("-")
            )

            seven_button = Button(
                button_r_4,
                width=5,
                height=2,
                text="7",
                font=("Bold",25),
                command= lambda: display_equation("7")
            )

            eight_button = Button(
                button_r_4,
                width=5,
                height=2,
                text="8",
                font=("Bold",25),
                command= lambda: display_equation("8")
            )

            nine_button = Button(
                button_r_4,
                width=5,
                height=2,
                text="9",
                font=("Bold",25),
                command= lambda: display_equation("9")
            )

            add_button = Button(
                button_r_4,
                width=5,
                height=2,
                text="+",
                font=("Bold",25),
                command= lambda: display_equation("+")
            )

            
            solve_button = Button(
                button_r_5,
                width=5,
                height=2,
                text="=",
                font=("Bold",25),
                command= lambda: solve()
            )


            button_r_1.pack()
            button_r_2.pack()
            button_r_3.pack()
            button_r_4.pack()
            button_r_5.pack()

            clear_button.pack(side=LEFT,padx=10)
            
            one_button.pack(side=LEFT , padx=10)
            two_button.pack(side=LEFT , padx=0)
            three_button.pack(side=LEFT , padx=10)
            multiply_button.pack(side=LEFT , padx=0)

            four_button.pack(side=LEFT , padx=10)
            five_button.pack(side=LEFT , padx=0)
            six_button.pack(side=LEFT , padx=10)
            subtract_button.pack(side=LEFT , padx=0)

            seven_button.pack(side=LEFT , padx=10)
            eight_button.pack(side=LEFT , padx=0)
            nine_button.pack(side=LEFT , padx=10)
            add_button.pack(side=LEFT , padx=0)

            solve_button.pack(side=RIGHT , padx=10)

        add_buttons()
    calc_ui()

calculator_functions()

calculator.mainloop()


equation_multiply = "5x20x2"
equation_subtract = "100-10"
equation_subtract_2 = "100-20-5"

def solve(equation):
    for i in equation:
        if i == "x":
            total = 1
            split_equation = equation.split("x")
            for i in range(len(split_equation)):
                total = total * int(split_equation[i])
            
        elif i == "-":
            total = 1
            split_equation = equation.split("-")
            print(split_equation)
            for i in range(len(split_equation)):
                total = total - int(split_equation[i])
        elif i == "+":
            print("not done")
    print(total)


solve(equation_multiply)
solve(equation_subtract)
solve(equation_subtract_2)
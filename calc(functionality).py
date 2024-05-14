equation_multiply = "5x20x2"
equation_subtract = "100-10"
equation_subtract_2 = "100-20-5"
equation_addition = "100+100"
equation_addition_2 = "100+100+100"
equation_division = "100÷5"
equation_division_2 = "100÷5÷2"

def solve(equation):
    for i in equation:
        if i == "x":
            split_equation = equation.split("x")
            total = int(split_equation[0])
            for i in range(len(split_equation)-1):
                total = total * int(split_equation[i+1])
            
        elif i == "-":
            split_equation = equation.split("-")
            total = int(split_equation[0])
            for i in range(len(split_equation)-1):
                total = total - int(split_equation[i+1])
        elif i == "+":
            split_equation = equation.split("+")
            total = int(split_equation[0])
            for i in range(len(split_equation)-1):
                total = total + int(split_equation[i+1])
        elif i == "÷":
            split_equation = equation.split("÷")
            total = int(split_equation[0])
            for i in range(len(split_equation)-1):
                total = total / int(split_equation[i+1])
    print(int(total))


solve(equation_multiply)
solve(equation_subtract)
solve(equation_subtract_2)
solve(equation_addition)
solve(equation_addition_2)
solve(equation_division)
solve(equation_division_2)
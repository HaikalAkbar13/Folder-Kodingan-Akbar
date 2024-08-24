def arithmetic_arranger(problems, show_answer = False):
    # store the result in list
    first_line = []
    second_line = []
    dashes_line = []
    results_line = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        # Make the condition for the errors    
        if operator != '+' and operator != '-':
            return("Error: Operator must be '+' or '-'.")
        elif not operand1.isdigit() or not operand2.isdigit():
            return("Error: Numbers must only contain digits.")
        elif len(operand1) > 4 or len(operand2) > 4:
            return("Error: Numbers cannot be more than four digits.")
        # condition for the right operators
        elif operator == '+':
            results = str(int(operand1) + int(operand2))
        elif operator == '-':
            results = str(int(operand1) - int(operand2))

        # set the width
        width = max(len(operand1), len(operand2)) + 2

        # appending the result on the list before
        first_line.append(operand1.rjust(width))
        second_line.append(operator + operand2.rjust(width -1)) 
        dashes_line.append('-' * width)
        results_line.append(results.rjust(width))

    if len(problems) > 5:
        return("Error: Too many problems.")
    elif show_answer == True:
        problems = (
            "    ".join(first_line) + "\n" +
            "    ".join(second_line) + "\n" +
            "    ".join(dashes_line) + "\n" +
            "    ".join(results_line)
        )
    else:
        problems = (
            "    ".join(first_line) + "\n" +
            "    ".join(second_line) + "\n" +
            "    ".join(dashes_line)
        )
    
    return problems

soal = ["32 + 8", "1 + 3801", "9999 + 9999", "523 - 49", "123 - 334"]

print(arithmetic_arranger(soal, True))
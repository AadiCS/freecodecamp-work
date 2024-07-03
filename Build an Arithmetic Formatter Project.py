def arithmetic_arranger(problems, show_answers=False):
#1length paramater 
    if len(problems) > 5:
        return "Error: Too many problems."
    
#2check for operator 
    operators = []
    for problem in problems:
        array = problem.split()
        operators.append(array[1])
    for operator in operators:
        if operator in ['*','/']:
            return "Error: Operator must be '+' or '-'."
#3 check for non digits 
    numbers = []
    for problem in problems:
        array = problem.split()
        numbers.append(array[0])
        numbers.append(array[2])
    for number in numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."
#4 check operand length
        elif len(number) > 4:
            return "Error: Numbers cannot be more than four digits."

#5 values 
    answers = []
    top_row = ''
    bottem_row = ''
    answer = ''
    dashes = ''

    for i in range(0, len(numbers), 2):
        pass
        num1 = int(numbers[i])
        num2 = int(numbers[i + 1])
        operator = operators[i // 2]

        if operator == '+':
            result = num1 + num2 
        else:
            result = num1 - num2
        answers.append(result)
      
#6 making problem rows 
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_row += numbers[i].rjust(space_width)
        bottem_row += operator + numbers[i + 1].rjust(space_width -1 )
        dashes += '-' * space_width
        

#7 spacing 
        if i != len(numbers) -2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            bottem_row += ' ' * 4
#8 formatting answers row
    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]),len(numbers[2 * i + 1])) + 2
        answer += str(answers[i]).rjust(space_width)
#9 spacing between answers 
        if i != len(answers) -1:
            answer += ' ' * 4
#10 final 
    if show_answers:
        arrange_problems = '\n'.join((top_row, bottem_row, dashes, answer))
    else:
        arrange_problems = '\n'.join((top_row, bottem_row, dashes,))
       



    
    

    return arrange_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 + 2", "45 + 43", "1223 + 49"],True)}')

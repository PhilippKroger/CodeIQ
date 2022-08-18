data = input().split()
# ( 2 + 5 ) * ( 3 - 1 / 1 ) + 4 / ( 2 + 1 * 2 )
error_1 = "The stack is empty. Therefore, the opening parenthesis is missing, i.e. expression is wrong"
error_2 = "The example is wrong"


# calculation function
def p(op, a, b):
    a = int(a) # str to int
    b = int(b) # str to int
    if op == "+": return b+a
    if op == "-": return b-a
    if op == "*": return b*a
    if op == "/": return b/a


stack_nums = []  # stack for operands
stack_operators = []  # stack for operators

i = 0  # counter
while i < len(data) or len(stack_operators) > 0:
    if data[i].isdigit():
        stack_nums.append(int(data[i]))
        i += 1
    elif data[i] in '+-':  # 1
        if len(stack_operators) == 0 or stack_operators[-1] == "(":
            stack_operators.append(data[i])
            i += 1
        elif stack_operators[-1] in '+-':
            stack_nums.append(p(stack_operators.pop(), stack_nums.pop(), stack_nums.pop()))
            stack_operators.append(data[i])
            i = i + 1
        elif stack_operators[-1] in '/*':
            stack_nums.append(p(stack_operators.pop(), stack_nums.pop(), stack_nums.pop()))

    elif data[i] in '/*':  # 1
        if len(stack_operators) == 0 or stack_operators[-1] == "(" or stack_operators[-1] in '+-':
            stack_operators.append(data[i])
            i = i + 1
        elif stack_operators[-1] in '/*':
            stack_nums.append(p(stack_operators.pop(), stack_nums.pop(), stack_nums.pop()))
            stack_operators.append(data[i])
            i = i + 1
    elif data[i] == "(":  # 1
        stack_operators.append(data[i])
        i = i + 1
    elif data[i] == ")":  # 1
        if len(stack_operators) == 0:
            print(error_1)
            break
        elif stack_operators[-1] == "(":
            stack_operators.pop()
            i = i + 1
        elif stack_operators[-1] in '+-/*':
            stack_nums.append(p(stack_operators.pop(), stack_nums.pop(), stack_nums.pop()))
    elif data[i]=="=":  # 1
        if len(stack_operators)==0:
            print(stack_nums.pop())
            break
        elif stack_operators[-1]=="(":
            print(error_2)
            break
        elif stack_operators[-1] in '+-/*':
            stack_nums.append(p(stack_operators.pop(), stack_nums.pop(), stack_nums.pop()))
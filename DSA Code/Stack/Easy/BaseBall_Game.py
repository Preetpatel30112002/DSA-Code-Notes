def calPoints(operations):
    stack = []
    for op in operations:
        match op:
            case '+':
                if len(stack)>=2:
                    stack.append(int(stack[0])+int(stack[1]))
            case 'D':
                if stack:
                    stack.append(int(stack[0])*2)
            case 'C':
                if stack:
                    stack.pop()
            case _:
                stack.append(int(op))

    return sum(stack)

if __name__ == "__main__":
    ops = ["5","2","C","D","+"]
    total = calPoints(ops)
    print(total)


while True :
    word = input()
    if word == ".":
        break
    
    stack_arr = []
    confirm = True

    for each_alpha in word :

        if each_alpha == "(" or each_alpha == "[" :
            stack_arr.append(each_alpha)
        elif each_alpha == ")" :
            if len(stack_arr) == 0 or stack_arr[-1] == "[":
                confirm = False
                break
            elif stack_arr[-1] == "(":
                stack_arr.pop()

        elif each_alpha == "]" :
            if len(stack_arr) == 0 or stack_arr[-1] == "(":
                confirm = False
                break
            elif stack_arr[-1] == "[":
                stack_arr.pop()
        
    if confirm == True and len(stack_arr) == 0 :
        print("yes")
    else:
        print("no")
    
    
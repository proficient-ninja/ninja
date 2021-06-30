def solution(participant, completion):
    dict_for_solution = {}
    
    for each in participant :
        if each in dict_for_solution :
            dict_for_solution[each] += 1
        else :
            dict_for_solution[each] = 1
            
    for each in completion :
        if each in dict_for_solution :
            dict_for_solution[each] -= 1
        if dict_for_solution[each] == 0 :
            del dict_for_solution[each]
    
    return list(dict_for_solution.keys())[0]

    
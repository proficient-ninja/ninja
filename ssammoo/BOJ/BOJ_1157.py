alpha = input().upper()

alpha_dict = {}

for each in alpha.upper() :
    if each in alpha_dict :
        alpha_dict[each] += 1
    else :
        alpha_dict[each] = 1

return_alpha = ""
max_num = 0

for each in alpha_dict :
    if alpha_dict[each] > max_num :
        max_num = alpha_dict[each]
        return_alpha = each
    elif alpha_dict[each] == max_num :
        return_alpha = "?"

print(return_alpha)
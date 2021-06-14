input_alpha = input()

cro_alpha = [
    "c=",
	"c-",
	"dz=",	
    "d-",
	"lj",
	"nj",
	"s=",
	"z="
    ]


for each in cro_alpha :
    alpha = input_alpha.find(each)
    if each in input_alpha :
        input_alpha = input_alpha.replace(each, "a")


print(len(input_alpha))


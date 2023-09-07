# This function make a christmas tree with the String ande the Size passed to parameter
def custom_christmas_tree(chars, n):
    amount = len(chars)
    tree = ""
    cord = 0

    for i in range(n):
        tree+=" "*(n-i-1)

        for j in range(i+1):
            if cord>amount-1:
                cord = 0

            tree+=chars[cord]+" "
            cord+=1

        tree+="\n"

    if n<=4:
        stick = 1
    else:
        stick = 2

    for i in range(0, stick):
        tree+=" "*int(n-1)+"|\n"        
        
    return tree


print(custom_christmas_tree("@!*", 7))
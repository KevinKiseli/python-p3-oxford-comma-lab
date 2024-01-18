

def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        
        return f"{', '.join(items[:-1])}, and {items[-1]}"


print(oxford_comma(["kiwi"]))  

print(oxford_comma(["kiwi", "durian"]))  

print(oxford_comma(["kiwi", "durian", "starfruit"]))  

print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"]))  

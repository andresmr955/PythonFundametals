def pyramid_sum(lower, upper, margin=1):
    blanks = "X" * margin
    print(blanks, lower, upper)

    if lower > upper:
        print(blanks)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4) 
        print(blanks, result)
        return result
    
pyramid_sum(1, 4)
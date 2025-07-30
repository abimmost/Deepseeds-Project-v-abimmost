## REVIEW OF ARRAYS: TEST

def array_calc(arrey, target):
    accumulator = 0
    avg = 0
    # for i in len(arrey):
    #     adder += arrey[i]
    for num in arrey:
        accumulator += num
    if target in arrey:
        status = "Seen"
    else:
        status = "Unseen"
    avg = float(accumulator/len(arrey))
    # return {"Status": status, "Average": avg} # Dictionaries
    return status, avg

n = int(input("Enter array length: "))

arrey = [int(input(f"Enter element {i}: ".format(i+1))) for i in range(n)]

target = int(input("Enter the number to find in the array: "))

target_status, average = array_calc(arrey, target)


# import the libs.
# json for storing results and time for the timeout. Delete it if you want the code to be faster (I don't recommend it).
import json, time

number = 0

# the loop.
while True:

    number = number + 1
    a = number
    steps = 0

    # the code of conjecture.
    while a!=1:
        steps = steps + 1
        if a % 2 == 0:
            a = a // 2
        else:
            a = (a * 3) + 1

        # interrupts the loop if the steps exceed 1 million attempts.
        if steps > 1000000:
            break
    
    # here we print the result in the output.
    print(f"There are {steps} steps to the number {number}.")

    # the json that stores the results.
    with open("number.json", encoding='utf-8') as f:
        data = json.load(f)
    data[number] = {}   
    data[number]["steps"] = steps
    with open("number.json","w", encoding='utf-8') as f:
        json.dump(data,f,indent=4,separators=(',',': '), ensure_ascii=False)
    
    # 0.5 second timeout.
    time.sleep(0.5)
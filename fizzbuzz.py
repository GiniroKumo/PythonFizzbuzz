count = 0
end = 100

while count <= end: #creates the loop as long as the number is 100 or less
    if count % 5 == 0 and count % 3 == 0: # four spaces, also making sure each is divisible
        print("Fizzbuzz")
    elif count % 5 == 0:
        print("Fizz")
    elif count % 3 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1    # makes sure the count increases by 1. has to be nestled INSIDE the while statement!
    

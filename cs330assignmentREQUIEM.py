import random

studentid = input("Enter your student ID: ")
unlock = studentid[-5:] + "1"
lock = studentid[-5:] + "4"

random_nums = input("Enter a string of numbers: ")

if unlock in random_nums:
    print("Unlocked")
elif lock in random_nums:
    print ("Locked")
else:
    print("Invalid")

def lockpicking():
    num_symbols = 0
    while True:    
        attempt = str(random.randint(0,9))
        for i in attempt:
            if unlock in attempt:
                return num_symbols
            else:
                num_symbols += 1
        return num_symbols

results = []
for i in range(10):
    results.append(lockpicking())

print("Minimum:", min(results))
print("Maximum:", max(results))
print("Average:", sum(results)/len(results))



#Try to estimate how long it would take (on the average) to break the lock if one has to wait one second to see 
# if the lock has unlocked or not. Assume the random number generator has an uniform distribution.
#Do the actual test: use some random number generator to generate the input string for the security device. 
# Count how many symbols (digits from 0 to 9) have been generated before the lock is unlocked. 
# Ignore the waiting time in this case and have the program run at full speed. Since you use random numbers you 
# will have to repet the test several times to obtain significant results; find the minimum, maximum and the average.



#

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

#########################
# infinite loop & break #
#########################
# stop a while loop after n amount of time
import time
timeout = time.time() + 5   # 5 seconds from now
counter = 0
while True:
   #counter += 1
    time.sleep(1)

    print("#{} do something at {}".format(counter,time.ctime()))

    if counter == 5 or time.time() > timeout:
        break



##########################
# user interactive break #
##########################
questions = [ "[read] what is your name? "
            , "[read] what is your favourite color? "
            , "[read] what is your quest ?"
            ]

n = 0

while True:
    a = input(questions[n])
    a = a.lower()
    if a == "q":
        break
    n = (n + 1) % 3
    if n == 0:
        print("[info] type key [Q] to quit.\n")

############
# continue #
############

# use continue in for-loop
for i in range(1, 10):
    if (i % 3) == 0:
        continue
    print(i)

# use continue for while-loop
i = 1
while i < 10:
    if (i % 3) == 0:
        i += 1
        continue
    print(i)
    i += 1


###############
# nested loop #
###############
# case sample 1
for i in range(1, 3):
    print("\n outer loop #{}".format(i))
    for letter in ["a", "b", "c"]:
        print("    inner loop {}".format(letter))


# case sample 2
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)


# case sample 3
while input('[read] y or n? ') != 'n':
    for i in range(1, 6):
        print(i)




#######
# EOF #
#######
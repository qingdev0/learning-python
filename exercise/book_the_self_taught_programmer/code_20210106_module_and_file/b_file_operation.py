import os

os.path.join(
    "c:",
    "Users",
    "a540619",
    "FILDBA",
    "TOOLKIT",
    "PYTK",
    "exercise",
    "book_the_self_taught_programmer",
)

#########
# write #
#########
# create, write and close file object at the end
file_object = open("test.txt", "w")
file_object.write("Hi from Python!")
file_object.close()


# create, write and auto-close file object
with open("test.txt", "w") as file_object:
    file_object.write("Hi from Ewan!")

########
# read #
########
my_list = list()
# there is only one read allowed in one open,
# so would better store read output in a variable or container
with open("test.txt", "r") as file_object:
    my_list.append(file_object.read())

print(my_list)


###################
# manage CSV file #
###################
import csv as _csv

# write sample
################
# with open("test.csv", "w") as csv_object:
with open("test.csv", "w", newline="") as csv_object:
    csv_data = _csv.writer(csv_object, delimiter=",")
    csv_data.writerow(["one", "two", "three"])
    csv_data.writerow(["four", "five", "six"])

# read sample (revision 1)
############################
with open("test.csv", "r") as csv_object:
    csv_data = _csv.reader(csv_object, delimiter=",")
    # print(csv_data)
    # output like: <_csv.reader object at 0x000001F5FFED8E18>
    for csv_list in csv_data:
        # check if row is empty
        if not (csv_list):
            continue
        print(csv_list)
        print(",".join(csv_list))

# read sample (revision 2)
############################
with open("test.csv", "r") as csv_object:
    csv_data = _csv.reader(csv_object, delimiter=",")
    csv_data = [row for row in csv_data if row]
    print(csv_data)
    for csv_list in csv_data:
        print(csv_list)
        print(",".join(csv_list))

# write practice
watch_list = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"],
]

with open("test.csv", "w", newline="") as csv_object:
    csv_data = _csv.writer(csv_object, delimiter=",")
    for each_list in watch_list:
        csv_data.writerow(each_list)


#######
# EOF #
#######

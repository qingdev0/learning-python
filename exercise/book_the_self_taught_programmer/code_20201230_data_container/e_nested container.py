# nested list 1/3: list element can be list

artist_list = []
rap = ["Kanye West", "Jay Z", "Eminem", "Nas"]
rock = ["Bob Dylan", "The Beatles", "Led Zeppelin"]
dj = ["Zeds Dead", "Tiesto"]


artist_list.append(rap)
artist_list.append(rock)
artist_list.append(dj)
print(artist_list)


rap = artist_list[0]
print(rap)


rap.append("Kendrick Lamar")
print(rap)
print(artist_list)



# nested list 2/3: list element can be tuple

location_list = list()

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

location_list.append(la)
location_list.append(chicago)

print(location_list)



# nested tuple 1/2: tuple element can be list

eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]

tuple_authors = (eights, nines)
print(tuple_authors)



dict_birthday = {"Hemingway": "7.21.1899", "Fitzgerald": "9.24.1896"}
# nested list 3/3: list element can be dictionary
my_list = [dict_birthday]
print(my_list)
# nested tuple 2/2: tuple element can be dictionary
my_tuple = (dict_birthday,)
print(my_tuple)


# netsted dictionary 1/1: dictionary element can be list, tuple, and dictionary

ny = {"locations": (40.7128, 74.0059)
     ,"celebs"   : ["W. Allen", "Jay Z", "K. Bacon"]
     ,"facts"    : {"state": "NY", "country": "America"}
     }

print(ny)


#######
# EOF #
#######
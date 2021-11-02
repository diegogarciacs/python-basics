####################################################
# CS 31, Prof. Muldrow
# Name: Diego Garcia
# Assignment: Project 3
# Due Date: 05/27/2021
# ####################################################
def main():
    file = open("tv_shows.txt", 'r')
    tvShow = {}
    line = file.readline()
    while line:
        key = line.rstrip('\n').upper()
        line = file.readline()
        ID = line.rstrip('\n')
        # start year if the digits are between 0 and 18, you must add 2000, otherwise add 1900
        year = int(ID[:2])
        if year < 19:
            year += 2000
        else:
            year += 1900
        # indicates number of seasons (1=ABC, 2=CBS, 3=NBC, 4=FOX))
        seasons = int(ID[2:4])
        seasons += year

        # indicates network
        network = int(ID[4:])
        if network == 1:
            network = "ABC"
        elif network == 2:
            network = "CBS"
        elif network == 3:
            network = "NBC"
        elif network == 4:
            network = "FOX"

        line = file.readline()
        actor1 = line.rstrip('\n')
        line = file.readline()
        actor2 = line.rstrip('\n')
        line = file.readline()
        actor3 = line.rstrip('\n')
        line = file.readline()
        actor4 = line.rstrip('\n')
        tvShow[key] = [year, seasons, network, actor1, actor2, actor3, actor4]
        line = file.readline()
    file.close()
    for key,value in tvShow.items(): # we can use two variables for keys and elements using .items()
        print(key, " aired from ", value[0], " to ", value[1], " on ", value[2], ".", sep='')
        # print(key, " aired from ", tvShow[key][0], " to ", tvShow[key][1], " on ", tvShow[key][2], ".", sep='')
        print("It starred ", tvShow[key][3], ", ", tvShow[key][4], ", ", tvShow[key][5], ", and ", tvShow[key][6], '.',
              sep='')
        print()


main()

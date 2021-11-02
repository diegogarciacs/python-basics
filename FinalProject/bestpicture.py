#
# matrix = ([0,0,0,0,0],[0,0,0,0,0])
# file = open('nums.txt','r')
# for x in range(2):
#     for y in range(5):
#         num = int(file.readline())
#         if num % 2 == 0:
#             matrix[x][y] = 3 * num + 1
#         else:
#             matrix[x][y] = num // 2 - 3
# print(matrix)
#
# list1 = [5,6,7,8,9,10,11,12,13,14]
# print(list1[:4])
# print(list1[-3:])
# print(list1[-5:-2])
# print(list1[3:6])
# print(list1[2:7:3])
# print()
# list2 = ['a','b','c','d','e','f','g','h','i','j']
# print(list2[:-3])
# print(list2[8:])
# print(list2[-8:-4])
# print(list2[5:9])
# print(list2[-2:-7:-2])
# print()
# set1= {1,2,3,4,5,6}
# set2 = {3,4,5,6,7,8}
# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# print(set1 ^ set2)
# print(set1 >= set2)

def main():
    file = open('bestpicture.txt', 'r')
    bestpicture = {}
    studio = {'UA': 'United Artists', 'WB': 'Warner Brothers', 'DW': 'Dreamworks', 'PM': 'Paramount'}
    line = file.readline()
    while line:
        title = line.rstrip('\n')
        info = file.readline().rstrip('\n')
        info = info.split()
        info.insert(2,studio.get(info[2]))
        del info[3]
        info[1] = f"{int(info[1]):,.2f}"
        bestpicture[title] = info
        line = file.readline()
    print(bestpicture)
    file.close()
    for key,value in bestpicture.items():
        print(key, ', released in ',value[0],' by ',value[2],' made $',value[1],'.',sep='')


main()

#Напишете програма која од листа на броеви (на пример, a=[5, 10, 15, 20]) ќе направи нова листа од само првиот и последниот елемент

def insertList():

    list = []
    print("Enter the list's elements: ")
    while True:
        element = input()
        if element == "":
            break
        list.append(element)
    return list


def newList(list):
    newList = [list[0], list[-1]]
    return newList

if __name__ == "__main__":
    list = insertList()
    newList = newList(list)
    print(newList)

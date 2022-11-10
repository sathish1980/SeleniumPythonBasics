def missing_numbers(num_list):
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))

def inbetweennumber(num_list):
    Listafter = []
    count=0
    listnewvall=missing_numbers(num_list)

    for x in range(0,len(listnewvall)):
        count=count+1
        #print(listnewvall[x])
        if (count == 1):
            Listafter.append("1-" + str(listnewvall[x] - 1))
            print("1-" + str(listnewvall[x] - 1))
        elif(count!=len(listnewvall)):
            if(str(listnewvall[x+1])!=str(listnewvall[x]+1)):
                Listafter.append(str(listnewvall[x-1])+"-" + str(listnewvall[x] - 1))
                print(str(listnewvall[x-1]+1)+"-" + str(listnewvall[x] - 1))


def newval(num_list):
    Listafter = []
    count = 0
    elsecount=0
    #listnewvall = missing_numbers(num_list)

    for x in range(0, len(num_list)):
        #print(num_list[x])
        if(num_list[x]+1==num_list[x+1]):
            count=count+1
        else:
            elsecount = elsecount+1
            if(count>=1 and elsecount==1):
                print("1-"+str(count))
                count = 0
            elif (count>=1 and elsecount>=2):
                print(str(num_list[x-count])+"-" + str(count))
                count = 0
                print(num_list[x])



#print(missing_numbers([1,2,3,5,6,7,9,25]))
#print(missing_numbers([10, 11, 12, 14, 17]))
print(newval([1,2,3,5,6,7,9,25]))
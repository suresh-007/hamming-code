"""Hamming code is used to verify wheather the sent data is equal to the received data using redundant bits"""
"""Using hamming code we are able to find error in only one bit"""

"""
output format:
Enter No.of bits:4
Enter No.of redundant bits:3
#######
Enter list to send
Enter value:0
Enter value:0
Enter value:1
Enter value:1
redundant bits here are:[1,0,0]
obtained list is :[1,0,0,0,0,1,1]

Enter bits"""
m = input("Enter No.of bits:")
r = input("Enter No.of redundant bits:")
n = int(m + r)
send = []
sqlist = []


def fun1():
    oglist = []
    redun = []
    for i in range(1, int(m) + 1):
        oglist.append(input("Enter value :"))

    # sqlist = [2 ** x for x in range(int(r))]
    for i in range(0, int(r)):
        sqlist.append(pow(2, i))

    """
    print("original list :")
    print(oglist)
    print("squares list  :")
    print(sqlist)
    print("length of oglist :")
    print(len(oglist))
    print("length of sqlist :")
    print(len(sqlist))
    """
    """
    def oglvalues():
        for i in oglist:
            yield i


    for i in oglvalues():
        print(i)
    """
    j = 0
    for i in range(1, int(n) + 1):
        if (i not in sqlist):
            if (j < int(m)):
                a = oglist[j]
                send.insert(i, int(a))
                j = j + 1
            else:
                break
        else:
            send.append(-1)

    notsq = []
    for i in range(1, len(send) + 1):
        if i not in sqlist:
            notsq.append(i)
    # print("List of non square values:")
    # print(notsq)

    # print("list to be send is :")
    # print(send)
    # print("Length of sendlist:")
    # print(len(send))
    count = 0
    for i in sqlist:
        for j in notsq:
            if i & j != 0:
                count = count + send[j - 1]
        if count % 2 == 0:
            redun.append(0)
            send[i - 1] = 0
        else:
            redun.append(1)
            send[i - 1] = 1
        count = 0

    print("redundant bits here are:{0}".format(redun))
    print("Obtained list is :{0}".format(send))
    return redun


print("#######")
print("Enter list of bit values:")
send1 = fun1()
send.clear()
print("Enter received bits")
recv1 = fun1()
print(send1)
print(recv1)
sum = 0
for i in range(0, len(send1)):
    if (send1[i] != recv1[i]):
        sum = sum + sqlist[i]
if sum > 0:
    print("Error is Found in POSITION :{0} of obtainedlist{1}".format(sum, send))
else:
    print("Error not found in the received data")

# print(send[sum-1])
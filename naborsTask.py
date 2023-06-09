# Compare 2 strings. But before that, find all spaces and delete the space
# and the element preceding the space
myStr1 = "abcc  d ae f"
myStr1 += 1000*"a"
myStr1 += 1000*" "
myStr2 = "abaf"
count = 0
for i in myStr1:
    if i == " ":
        count += 1
print(f"There are {count} spaces in myStr1:  {myStr1}")
# print("///////////////")
while count > 0:
    myIndex = myStr1.index(" ")
    # print("space index is: ", myIndex)
    myStr1 = myStr1[0: myIndex - 1] + myStr1[myIndex + 1::]
    # print(myStr1)
    count -= 1
if myStr1 == myStr2:
    print("/////////////////")
    print(True)
else:
    print(False)
    # print(f" << {myStr1} >> and << {myStr2} >> strings are  equal")
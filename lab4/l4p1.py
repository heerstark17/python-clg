list=[1,25,85,877,47,10]
ele=int(input("Enter element thst you want to search"))
for i in range(0,6):
    if ele==list[i]:
        print(ele,"iS present")
        break
else:
    print(ele,"Isn't present")

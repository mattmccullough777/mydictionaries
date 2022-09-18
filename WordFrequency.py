def main():
    infile = open("sometext.txt","r")

    txtfile = infile.read()

    txtfile = str(txtfile)


#make lower case and remove special characters like periods and commas

    txtfile = txtfile.replace(",","")
    txtfile = txtfile.replace(".","")
    txtfile = txtfile.replace("-"," ")
    txtfile = txtfile.lower()

#count occurances and make into dictionary

    counts = dict()
    words = txtfile.split()
    for x in words:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    print(counts)
        
    infile.close()

main()
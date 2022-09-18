def main():

    infile = open("info_security.txt","r")

    info = infile.read()

    outfile = open("encrypted.txt","w")

    info = str(info)

    codes = {"A": "~","a":"`","B":"!","b":"1","C":"@","c":"2","D":"#","d":"3","E":"$","e":"4","F":"%","f":"5","G":"^","g":"6","H":"&","h":"7","I":"*","i":"8","J":"(","j":"9","K":")","k":"0","L":"_","l":"-","M":"+","m":"=","N":"{","n":"[","O":"}","o":"]","P":"|","p":":","Q":";","q":"<","R":",","r":">","S":"?","s":".","T":"/","t":"A","U":"b","u":"C","V":"d","v":"e","W":"F","w":"f","X":"G","x":"H","Y":"I","y":"j","Z":"k","z":"L"}

    for letter, encrypted in codes.items():
        info = info.replace(letter, encrypted)

    outfile.write(info)

    infile.close()
    outfile.close()

main()
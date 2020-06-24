#put your directory below, I don't like inputting my directory everytime I run a program so this is why I am just leaving it like this
rpath = open("message.txt", "r").read()
smapr1 = [0]
smapr2 = []
let = ""
morse = ""
english = ""
morseINT = {
    "/":" ", " ":"", ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "----.":"9", "-----":"0", ".-.-.-":".", "--..--":",", "..--..":"?", ".----.":"\'", "-.--.":"(", "-.--.-":")", "-..-.":"/", ".-..-.":"\"", ".--.-.":"@", "-.-.--":"!", "...-..-":"$", "-.-.-.":";", "---...":":", ".-...":"&", "-....-":"-", "..--.-":"_", "-...-":"=", ".-.-.":"+", "\n":"", "":""
}
def Breaker(i):
    morse = ""
    let = ""
    for a in range(smapr1[i], smapr2[i]-1):
        morse += rpath[a]

    let = morseINT[morse]
    return let


wordcount = 1

for i in range(len(rpath)):
    if rpath[i] == " " or rpath[i] == "\n":
        smapr1.append(int(i+1))
        smapr2.append(int(i+1))
    else:
        continue

#finds length of final word
y = smapr1[len(smapr1)-1]
for i in range(smapr1[len(smapr1)-1], len(rpath)):
    y += 1
smapr2.append(y+1)
for i in range(len(smapr1)):
    english += Breaker(i)


# for i in range(len(smapr1)):
#     print(str(smapr1[i]) + "      " + str(smapr2[i]))
#me testing how format works, not realizing that this step was unnecessary, but it did work
#print("{}      {}".format(smapr1[len(smapr1)-1], smapr2[len(smapr2)-1]))
print(english)

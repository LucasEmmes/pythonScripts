#1)
#Her legger du inn navnet du bruker til input i equations
inputName = "OK"

#2)
#Her legger du inn navnet for output.
#Dersom det er mer komplisert output så er det gjerne greit å la denne være blank (da skipper koden å regne den ut)
outputName = ""

#3)
#Her er navnene du bruker for flipflops i equations. Pleier å være de samme i det fleste eksamener
flipflops = ["Q0", "Q1", "Q2"]


#4)
#Her fyller du inn equations for flipfloppene. PASS PÅ FORMATERING
#For AND bruker du mellomrom (" ")
#For OR bruker du mellomrom-+-mellomrom (" + ")
#Se under for eksempel fra eksamen desember 2016
D0 = "~Q2 ~Q1 ~Q0 OK + ~Q2 Q1 ~Q0 OK"
D1 = "~Q2 Q1 ~Q0 OK + ~Q2 ~Q1 Q0 OK"
D2 = "~Q2 Q1 Q0 OK"

#5)
#Output eq blir ignorert dersom outputNavn er tomt
output = "Q2 ~Q1 ~Q0"




#Når du er kommet hit er du ferdig å fylle inn og kan kjøre koden
equations = [D0, D1, D2, output]

def parse(truthEq):
    temp = truthEq.split(" + ")
    for i in range(len(temp)):
        temp[i] = temp[i].split(" ")
    return temp


for i in range(len(equations)):
    equations[i] = parse(equations[i])

def checkTruth(truthArray, valArr, inp):

    result = False
    
    for sec in truthArray:
        
        sectionResult = True
        for var in sec:
            if "~" in var:
                var = var[1:]
                if var in flipflops:
                    
                    index = flipflops.index(var)
                    sectionResult = sectionResult and not valArr[index]
                elif var == inputName:
                    sectionResult = sectionResult and not inp
            else:
                if var in flipflops:
                    index = flipflops.index(var)
                    sectionResult = sectionResult and valArr[index]
                elif var == inputName:
                    sectionResult = sectionResult and inp

        result = result or sectionResult

        
    if result:
        return 1
    else:
        return 0


def main():
    values = []
    for i in range(len(flipflops)):
        values.append([])
        for j in range(2**len(flipflops)):
            values[i].append(j//(2**i) % 2)

    for i in range(len(values[0])):
        print("Current: " + str(values[2][i]) + str(values[1][i]) + str(values[0][i]), end=" | ")
        print("Next " + inputName + ": " + str(checkTruth(equations[2], [values[0][i], values[1][i], values[2][i]], 1)) + str(checkTruth(equations[1], [values[0][i], values[1][i], values[2][i]], 1)) + str(checkTruth(equations[0], [values[0][i], values[1][i], values[2][i]], 1)), end=" | ")
        print("Next ~" + inputName + ": " + str(checkTruth(equations[2], [values[0][i], values[1][i], values[2][i]], 0)) + str(checkTruth(equations[1], [values[0][i], values[1][i], values[2][i]], 0)) + str(checkTruth(equations[0], [values[0][i], values[1][i], values[2][i]], 0)), end=" | ")
        if outputName != "":
            print(outputName + ": " + str(checkTruth(equations[3], [values[0][i], values[1][i], values[2][i]], 0)))
        else:
            print("")

main()

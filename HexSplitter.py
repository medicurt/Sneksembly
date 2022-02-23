#implement the class
#class hexSplitter

def hexRipper(file, out):
        out = []
        lines = file.readlines()
        i = 0
        for i in range(len(lines)):
                temp = []
                temp = lines[i].split(">:  ")
                if len(temp)>1:
                        out.append(temp[1])
                        i += 1

def print_asm(asm_array):
        for i in range(len(asm_array)):
                print(asm_array[i], end = "")

#add more translations

def asm_translate(inArray):
        i = 0
        for i in range(len(inArray)):
                inArray[i] = inArray[i].lstrip()
                fromto = []
                temp = []
                temp.append(inArray[i][0:5])
		#print(temp[0])
                temp.append(inArray[i][7:-1])
		#print(temp[1])
                fromto.append(temp[1].split(","))
		#print("temp and fromto")
		#print(temp)
		#print(fromto)
                fromto = fromto[0]
                if len(fromto)>1:
                        if temp[0]==("mov  "):
                                print("mov moves " + str(fromto[0]) + " to " + str(fromto[1]), end = "\n")
                        elif temp[0]==("lea  "):
                                print("lea loads the effective address of " + str(fromto[0]) + " into " + str(fromto[1]), end = "\n")
                        elif temp[0]==("movq "):
                                print("movq moves a quadword from " + str(fromto[0]) + "to " + str(fromto[1]), end = "\n")
                        elif temp[0]==("imul "):
                                print("imul multiplies an integer from " + str(fromto[0]) + "into " + str(fromto[1]), end ="\n")
                        elif temp[0]==("addl "):
                                print("addl adds a long from " + str(fromto[0]) + " to " + str(fromto[1]))
                        elif temp[0]==("cmpl "):
                                print("cmpl compares " + str(fromto[0]) +" and " + str(fromto[1]), end = "\n")
                        elif temp[0]==("xor  "):
                                if fromto[0] == fromto[1]:
                                        print("xor flushes the value at " + str(fromto[0]))

                        else:
                                print(str(inArray[i]), end = "")
                elif len(fromto) > 0:
                        if temp[0]==("jmp  "):
                                print("the execution jumps to the instructions at" + str(fromto[0]))
                else:
                        print(str(inArray[i]), end = "")

#accepts an array input for files, flushes the output array at the beginning
def processHex(inFiles, out):
        out = []
        final_out = []
        i = 0
        for i in range(len(inFiles)):
                hexRipper(inFiles[i], out)
                final_out.append(out)
        asm_translate(final_out)

                


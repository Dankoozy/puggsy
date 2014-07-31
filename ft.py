import time
import fivebit
import random
s = fivebit.Substitute()
a = s.sub("tree")
a = s.sub("bollix")
print(s.desub(a))



#Test routines
def teststr(lent=65536,low=26,high=128):
	a = ""	
	for i in range(lent): a = a + chr(random.randrange(low,high))
	return a


print("Compressing random string 65536 characters, range 26-128 Dictionary on...")
tstr = teststr()
starttime = time.time()
d = fivebit.compress(tstr)
print("Execution time: " + str(time.time() - starttime))

print("Decompressing random string 65536 characters, range 26-128 Dictionary on...")
starttime = time.time()
dec = fivebit.decompress(d)
print("Execution time: " + str(time.time() - starttime))
print( dec==tstr)

print("Compressing random string 65536 characters, range 26-128 Dictionary off...")
starttime = time.time()
nd = fivebit.compress(tstr,False)
print("Execution time: " + str(time.time() - starttime))


#Random lowercase words
print("\n\n\nGenerating 50000 lowercase random words..")
lst = []
for i in range(50000):	
	lst.append(teststr(random.randrange(1,15),97,122) + " ")

wordlist = "".join(lst)
print("Testing compression time with dictionary enabled")
starttime = time.time()
d = fivebit.compress(wordlist,True)
print("Execution time: " + str(time.time() - starttime))
print("Testing compression time with dictionary disabled")
starttime = time.time()
nd = fivebit.compress(wordlist,False)
print("Execution time: " + str(time.time() - starttime))
print("Testing decompression time..")
print("Uncompressed length: " + str(len(wordlist)) + " Dict compressed length: " + str(len(d)) + " Nodict compressed length: " + str(len(nd)) )

#Random dictionary words
lst = []
print("\n\n\nGenerating 50000 lowercase random dictionary words..")
for i in range(50000):	
	lst.append(fivebit.dic1024[random.randrange(1024)] + " ")

starttime = time.time()
fivebit.decompress(fivebit.compress("".join(lst)))
print("Execution time: " + str(time.time() - starttime))



#Random gobbledegook words
print("\n\n\nGenerating 50000 gobbledegook random words..")
lst = []
for i in range(50000):	
	lst.append(teststr(random.randrange(1,15),1,255) + " ")

wordlist = "".join(lst)
print("Testing compression time with dictionary enabled")
starttime = time.time()
d = fivebit.compress(wordlist,True)
print("Execution time: " + str(time.time() - starttime))
print("Testing compression time with dictionary disabled")
starttime = time.time()
nd = fivebit.compress(wordlist,False)
print("Execution time: " + str(time.time() - starttime))
print("Testing decompression time..")
starttime = time.time()
dec = fivebit.decompress(d)
print("Execution time: " + str(time.time() - starttime))
print("Uncompressed length: " + str(len(wordlist)) + " Dict compressed length: " + str(len(d)) + " Nodict compressed length: " + str(len(nd)) )
print( dec==wordlist)

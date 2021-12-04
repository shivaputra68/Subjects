import gc
import sys

i = 0
def create_cycle():
        collected = gc.collect()
        x = { }
        x[i+1] = x
        print (x)
	#print(id(x))
	#print(sys.getrefcount(x))
        collected = gc.collect()
        print (collected)
collected = gc.collect() 
print ("Garbage collector: collected %d objects." % (collected)) 

print ("Creating cycles...")
for i in range(0,10): 
	create_cycle() 

collected = gc.collect()
print ("Garbage collector: collected %d objects." % (collected) )
#print(sys.getrefcount(x))

import time
import sys

def bubble(A,n):
	for i in range(n):
		for j in range(n-i-1):
			if A[j] > A[j+1]:
				A[j],A[j+1]=A[j+1],A[j]

def insertionSort(arr,n):
    for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    j -= 1
            arr[j + 1] = key 
            
def selecSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i] 

def quick_sort(lo, hi, a):
    while((hi - lo) > 0):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i],a[j] = a[j],a[i]
                i += 1
        a[i],a[hi] = a[hi],a[i]
        if(i - lo <= hi - i):
            quick_sort(lo, i-1, a)
            lo = i+1
        else:
            quick_sort(i+1, hi, a)
            hi = i-1

#---------------Reading Increment numbers-----------------
# reading 10K Inc Numbers:
B10_i=[]
f=open("10k_inc","r")
for line in f.readlines():
    B10_i.append(int(line))
f.close()
n=len(B10_i)
I10_i=B10_i
S10_i=B10_i
Q10_i=B10_i

# reading 20K Inc Numbers:
B20_i=[]
f=open("20k_inc","r")
for line in f.readlines():
    B20_i.append(int(line))
f.close()
n=len(B20_i)
I20_i=B20_i
S20_i=B20_i
Q20_i=B20_i

# reading 50K Inc Numbers:
B50_i=[]
f=open("50k_inc","r")
for line in f.readlines():
    B50_i.append(int(line))
f.close()
n=len(B50_i)
I50_i=B50_i
S50_i=B50_i
Q50_i=B50_i

# reading 100K Inc Numbers:
B100_i=[]
f=open("100k_inc","r")
for line in f.readlines():
    B100_i.append(int(line))
f.close()
n=len(B100_i)
I100_i=B100_i
S100_i=B100_i
Q100_i=B100_i

#---------------Reading Decrement numbers-----------------
# reading 10K Dec Numbers:
B10_d=[]
f=open("10k_dec","r")
for line in f.readlines():
    B10_d.append(int(line))
f.close()
n=len(B10_d)
I10_d=B10_d
S10_d=B10_d
Q10_d=B10_d

# reading 20K Dec Numbers:
B20_d=[]
f=open("20k_dec","r")
for line in f.readlines():
    B20_d.append(int(line))
f.close()
n=len(B20_d)
I20_d=B20_d
S20_d=B20_d
Q20_d=B20_d

# reading 50K Dec Numbers:
B50_d=[]
f=open("50k_dec","r")
for line in f.readlines():
    B50_d.append(int(line))
f.close()
n=len(B50_d)
I50_d=B50_d
S50_d=B50_d
Q50_d=B50_d

# reading 100K Dec Numbers:
B100_d=[]
f=open("100k_dec","r")
for line in f.readlines():
    B100_d.append(int(line))
f.close()
n=len(B100_d)
I100_d=B100_d
S100_d=B100_d
Q100_d=B100_d

#---------------Reading Random numbers-----------------
# reading 10K Ran Numbers:
B10_r=[]
f=open("10k_ran","r")
for line in f.readlines():
    B10_r.append(int(line))
f.close()
n=len(B10_r)
I10_r=B10_r
S10_r=B10_r
Q10_r=B10_r

# reading 20K Ran Numbers:
B20_r=[]
f=open("20k_ran","r")
for line in f.readlines():
    B20_r.append(int(line))
f.close()
n=len(B20_r)
I20_r=B20_r
S20_r=B20_r
Q20_r=B20_r

# reading 50K Ran Numbers:
B50_r=[]
f=open("50k_ran","r")
for line in f.readlines():
    B50_r.append(int(line))
f.close()
n=len(B50_r)
I50_r=B50_r
S50_r=B50_r
Q50_r=B50_r

# reading 100K Ran Numbers:
B100_r=[]
f=open("100k_ran","r")
for line in f.readlines():
    B100_r.append(int(line))
f.close()
n=len(B100_r)
I100_r=B100_r
S100_r=B100_r
Q100_r=B100_r

print("1.Bubble \n2.Insertion \n3.Selection \n4.quick \nFor exit enter 999")
ch=1
sys.setrecursionlimit(10**9)
print(sys.getrecursionlimit())
while(ch!=999):
    print("Enter Choice:")        
    ch=int(input())
    if ch == 1: 
        #--------------- 10K Number -----------------
        start_time10_i=time.time()
        bubble(B10_i,len(B10_i))
        end_time10_i=time.time()
        print("done..")
        start_time10_d=time.time()
        bubble(B10_d,len(B10_d))
        end_time10_d=time.time()
        print("done..")

        start_time10_r=time.time()
        bubble(B10_r,len(B10_r))
        end_time10_r=time.time()
        print("10k done..")
        #--------------- 20K Number -----------------
        start_time20_i=time.time()
        bubble(B20_i,len(B20_i))
        end_time20_i=time.time()        
        print("done..")

        start_time20_d=time.time()
        bubble(B20_d,len(B20_d))
        end_time20_d=time.time()        
        print("done..")

        start_time20_r=time.time()
        bubble(B20_r,len(B20_r))
        end_time20_r=time.time()
        print("20k done..")

        #--------------- 50K Number -----------------
        start_time50_i=time.time()
        bubble(B50_i,len(B50_i))
        end_time50_i=time.time()        
        print("done..")

        start_time50_d=time.time()
        bubble(B50_d,len(B50_d))
        end_time50_d=time.time()        
        print("done..")

        start_time50_r=time.time()
        bubble(B50_r,len(B50_r))
        end_time50_r=time.time()
        print("50k done..")

        #--------------- 100K Number -----------------
        start_time100_i=time.time()
        bubble(B100_i,len(B100_i))
        end_time100_i=time.time()        
        print("done..")

        start_time100_d=time.time()
        bubble(B100_d,len(B100_d))
        end_time100_d=time.time()        
        print("done..")

        start_time100_r=time.time()
        bubble(B100_r,len(B100_r))
        end_time100_r=time.time()
        print("100k done..")

        print("-------------Bubble sort-----------")
        print("Execution time 10k_inc:",(end_time10_i-start_time10_i))
        print("Execution time 10k_dec:",(end_time10_d-start_time10_d))
        print("Execution time 10k_ran:",(end_time10_r-start_time10_r))
        print("Execution time 20k_inc:",(end_time20_i-start_time20_i))
        print("Execution time 20k_dec:",(end_time20_d-start_time20_d))
        print("Execution time 20k_ran:",(end_time20_r-start_time20_r))
        print("Execution time 50k_inc:",(end_time50_i-start_time50_i))
        print("Execution time 50k_dec:",(end_time50_d-start_time50_d))
        print("Execution time 50k_ran:",(end_time50_r-start_time50_r))
        print("Execution time 100k_inc:",(end_time100_i-start_time100_i))
        print("Execution time 100k_dec:",(end_time100_d-start_time100_d))
        print("Execution time 100k_ran:",(end_time100_r-start_time100_r))
     
    elif ch == 2:
        #--------------- 10K Number -----------------
        print(B10_i)
        istart_time10_i=time.time()
        insertionSort(B10_i,len(B10_i))
        iend_time10_i=time.time()        
        print("done..")
        istart_time10_d=time.time()
        insertionSort(B10_d,len(B10_d))
        iend_time10_d=time.time()        
        print("done..")

        istart_time10_r=time.time()
        insertionSort(B10_r,len(B10_r))
        iend_time10_r=time.time()
        print("10k done..")

        #--------------- 20K Number -----------------
        istart_time20_i=time.time()
        insertionSort(B20_i,len(B20_i))
        iend_time20_i=time.time()        
        print("done..")

        istart_time20_d=time.time()
        insertionSort(B20_d,len(B20_d))
        iend_time20_d=time.time()        
        print("done..")

        istart_time20_r=time.time()
        insertionSort(B20_r,len(B20_r))
        iend_time20_r=time.time()
        print("20k done..")

        #--------------- 50K Number -----------------
        istart_time50_i=time.time()
        insertionSort(B50_i,len(B50_i))
        iend_time50_i=time.time()        
        print("done..")

        istart_time50_d=time.time()
        insertionSort(B50_d,len(B50_d))
        iend_time50_d=time.time()        
        print("done..")

        istart_time50_r=time.time()
        insertionSort(B50_r,len(B50_r))
        iend_time50_r=time.time()
        print("50k done..")

        #--------------- 100K Number -----------------
        istart_time100_i=time.time()
        insertionSort(B100_i,len(B100_i))
        iend_time100_i=time.time()        
        print("done..")

        istart_time100_d=time.time()
        insertionSort(B100_d,len(B100_d))
        iend_time100_d=time.time()        
        print("done..")

        istart_time100_r=time.time()
        insertionSort(B100_r,len(B100_r))
        iend_time100_r=time.time()
        print("100k done..")

        print("-------------insertionSort sort-----------")
        print("Execution time 10k_inc:",(iend_time10_i-istart_time10_i))
        print("Execution time 10k_dec:",(iend_time10_d-istart_time10_d))
        print("Execution time 10k_ran:",(iend_time10_r-istart_time10_r))
        print("Execution time 20k_inc:",(iend_time20_i-istart_time20_i))
        print("Execution time 20k_dec:",(iend_time20_d-istart_time20_d))
        print("Execution time 20k_ran:",(iend_time20_r-istart_time20_r))
        print("Execution time 50k_inc:",(iend_time50_i-istart_time50_i))
        print("Execution time 50k_dec:",(iend_time50_d-istart_time50_d))
        print("Execution time 60k_ran:",(iend_time50_r-istart_time50_r))
        print("Execution time 100k_inc:",(iend_time100_i-istart_time100_i))
        print("Execution time 100k_dec:",(iend_time100_d-istart_time100_d))
        print("Execution time 100k_ran:",(iend_time100_r-istart_time100_r))
      
    elif ch == 3:
        #--------------- 10K Number -----------------
        sstart_time10_i=time.time()
        selecSort(B10_i)
        send_time10_i=time.time()        
        print("done..")

        sstart_time10_d=time.time()
        selecSort(B10_d)
        send_time10_d=time.time()        
        print("done..")

        sstart_time10_r=time.time()
        selecSort(B10_r)
        send_time10_r=time.time()
        print("10k done..")

        #--------------- 20K Number -----------------
        sstart_time20_i=time.time()
        selecSort(B20_i)
        send_time20_i=time.time()        
        print("done..")

        sstart_time20_d=time.time()
        selecSort(B20_d)
        send_time20_d=time.time()        
        print("done..")

        sstart_time20_r=time.time()
        selecSort(B20_r)
        send_time20_r=time.time()        
        print("20k done..")

        #--------------- 50K Number -----------------
        sstart_time50_i=time.time()
        selecSort(B50_i)
        send_time50_i=time.time()        
        print("done..")

        sstart_time50_d=time.time()
        selecSort(B50_d)
        send_time50_d=time.time()        
        print("done..")

        sstart_time50_r=time.time()
        selecSort(B50_r)
        send_time50_r=time.time()        
        print("50k done..")

        #--------------- 100K Number -----------------
        sstart_time100_i=time.time()
        selecSort(B100_i)
        send_time100_i=time.time()        
        print("done..")

        sstart_time100_d=time.time()
        selecSort(B100_d)
        send_time100_d=time.time()        
        print("done..")

        sstart_time100_r=time.time()
        selecSort(B100_r)
        send_time100_r=time.time()        
        print("100k done..")

        print("-------------selection sort-----------")
        print("Execution time 10k_inc:",(send_time10_i-sstart_time10_i))
        print("Execution time 10k_dec:",(send_time10_d-sstart_time10_d))
        print("Execution time 10k_ran:",(send_time10_r-sstart_time10_r))
        print("Execution time 20k_inc:",(send_time20_i-sstart_time20_i))
        print("Execution time 20k_dec:",(send_time20_d-sstart_time20_d))
        print("Execution time 20k_ran:",(send_time20_r-sstart_time20_r))
        print("Execution time 50k_inc:",(send_time50_i-sstart_time50_i))
        print("Execution time 50k_dec:",(send_time50_d-sstart_time50_d))
        print("Execution time 60k_ran:",(send_time50_r-sstart_time50_r))
        print("Execution time 100k_inc:",(send_time100_i-sstart_time100_i))
        print("Execution time 100k_dec:",(send_time100_d-sstart_time100_d))
        print("Execution time 100k_ran:",(send_time100_r-sstart_time100_r))

    elif ch == 4:
        #--------------- 10K Number -----------------
        qstart_time10_i=time.time()
        quick_sort(0,len(B10_i)-1,B10_i)
        qend_time10_i=time.time()
        qstart_time10_d=time.time()
        quick_sort(0,len(B10_d)-1,B10_d)
        qend_time10_d=time.time()
        qstart_time10_r=time.time()
        quick_sort(0,len(B10_r)-1,B10_r)
        qend_time10_r=time.time()        
        print("10k done..")

        #--------------- 20K Number -----------------
        qstart_time20_i=time.time()
        quick_sort(0,len(B20_i)-1,B20_i)
        qend_time20_i=time.time()
        qstart_time20_d=time.time()
        quick_sort(0,len(B20_d)-1,B20_d)
        qend_time20_d=time.time()
        qstart_time20_r=time.time()
        quick_sort(0,len(B20_r)-1,B20_r)
        qend_time20_r=time.time()        
        print("20k done..")

        #--------------- 50K Number -----------------
        qstart_time50_i=time.time()
        quick_sort(0,len(B50_i)-1,B50_i)
        qend_time50_i=time.time()
        qstart_time50_d=time.time()
        quick_sort(0,len(B50_d)-1,B50_d)
        qend_time50_d=time.time()
        qstart_time50_r=time.time()
        quick_sort(0,len(B50_r)-1,B50_r)
        qend_time50_r=time.time()        
        print("50k done..")

        #--------------- 100K Number -----------------
        qstart_time100_i=time.time()
        quick_sort(0,len(B100_i)-1,B100_i)
        qend_time100_i=time.time()
        qstart_time100_d=time.time()
        quick_sort(0,len(B100_d)-1,B100_d)
        qend_time100_d=time.time()
        qstart_time100_r=time.time()
        quick_sort(0,len(B100_r)-1,B100_r)
        qend_time100_r=time.time()        
        print("100k done..")

        print("-------------Quick sort-----------")
        print("Execution time 10k_inc:",(qend_time10_i-qstart_time10_i))
        print("Execution time 10k_dec:",(qend_time10_d-qstart_time10_d))
        print("Execution time 10k_ran:",(qend_time10_r-qstart_time10_r))
        print("Execution time 20k_inc:",(qend_time20_i-qstart_time20_i))
        print("Execution time 20k_dec:",(qend_time20_d-qstart_time20_d))
        print("Execution time 20k_ran:",(qend_time20_r-qstart_time20_r))
        print("Execution time 50k_inc:",(qend_time50_i-qstart_time50_i))
        print("Execution time 50k_dec:",(qend_time50_d-qstart_time50_d))
        print("Execution time 60k_ran:",(qend_time50_r-qstart_time50_r))
        print("Execution time 100k_inc:",(qend_time100_i-qstart_time100_i))
        print("Execution time 100k_dec:",(qend_time100_d-qstart_time100_d))
        print("Execution time 100k_ran:",(qend_time100_r-qstart_time100_r))

    else:
        print("Exited...")
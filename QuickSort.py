#Partiton Code Begin
#Last element of the array is set as pivot
# i is set as the index of the smaller element in the array given
def Create_Partition(Input_Array,Start_Index,End_Index):
	i=(Start_Index-1)
	pivot=Input_Array[End_Index]

#Start_Index denotes the starting index picked
#End_Index denotes the ending index picked

	for j in range(Start_Index,End_Index):

		if Input_Array[j]<=pivot:
			i=i+1
			Input_Array[i],Input_Array[j]=Input_Array[j],Input_Array[i]
	Input_Array[i+1],Input_Array[End_Index]=Input_Array[End_Index],Input_Array[i+1]
	return(i+1)

#Recursive quick sort function
#Start Index gets low value value of input
#End index gets high value of input
def Quick_Sort_Algo(Input_Array,Start_Index,End_Index):
	if Start_Index<End_Index:
		pi=Create_Partition(Input_Array,Start_Index,End_Index)

		Quick_Sort_Algo(Input_Array,Start_Index,pi-1)
		Quick_Sort_Algo(Input_Array,pi+1,End_Index)
#Quick sort code complete


#Input Array to verify the merge sort working
#Accepting inputs from command line by user
#data array contains the user input
data_array = list()
print("\nQUICK SORT")
Array_Size = int(input("Enter the number of elements you want sort:"))
print ('Enter numbers in array by pressing ENTER key after each element')

n=0
i=0
for i in range(Array_Size):
    n = int(input("Number:"))
    data_array.append(int(n))

print ('\nInput Array Given: ',data_array)

#calculating the start time and end time of quick sort
#calling quick sort by passing input array and size
start_time=time.clock()
Quick_Sort_Algo(data_array,0,Array_Size-1)
end_time=time.clock()-start_time
#once Sort is completed capturing the end time

print("\nOutput Array After Quick Sort:")
for i in range(Array_Size):
    print("%d" %data_array[i]),

print("\nTime Taken to Quick Sort the Numbers is: %s" %end_time)
#Code Complete
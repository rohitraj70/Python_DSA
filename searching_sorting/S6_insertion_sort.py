

def insertion_sort(arr):
    n = len(arr)

    for current in range(1,n):
        currentCard = arr[current]
        correctPosition = current-1 
        while correctPosition >=0:
            if(arr[correctPosition] < currentCard):
                break
            else:
                arr[correctPosition +1 ] = arr[correctPosition]
                correctPosition-=1
            arr[correctPosition + 1] = currentCard

    return arr


unsorted_list = [10,9,8,7,6,5,4,3,2,1]
sorted_list = insertion_sort(unsorted_list)
print("Sorted Elements :", sorted_list)
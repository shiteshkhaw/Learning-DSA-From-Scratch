def checker(arr,arr_size):
    even_count=0
    odd_count=0

    for i in range(arr_size):
        if (arr[i]%2)==0:
            even_count+=1
        else:
            odd_count+=1
    print("No of Even No In the given array is ",even_count)
    print("No of Odd No In the given array is ",odd_count)

arr=[2,3,4,5,6]
checker(arr,5)
#CodeByShiteshKhaw

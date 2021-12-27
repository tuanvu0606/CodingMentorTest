def check_pair_of_socks():
    # This is the first solution that I could make \
    # it contains 2 nested loops, first loop will iterate through the array, second loop
    # will iterate from the index of first loop till the end of the array
    # if it finds a matching sock, then turn both value at that index to be -1, out of the value range of ar[i] and will never be affecting the process.
    # after that increment the pair_count
    # as it finished the job, break the loop/
    # its the nested loop so the time complexity is On^2, not very good

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    pair_count = 0

    for i in range(0,len(ar)):
        print(ar)
        if ar[i] == -1:
            continue
        else:              
            for j in range (i + 1, len(ar)):
                if ar[j] == ar[i]:                    
                    ar[j] = -1
                    ar[i] = -1
                    pair_count += 1 
                    
                    print("paired")
                    break                      
    return pair_count


def check_pair_of_socks_v2():
    # This is the second solution which is faster with On^2 complexity, as 1 <= n <= 100 and 1<= ar[i] <= 100, we can define an array model_arr which has 101 element, the index will be the possible value of ar[i]
    # then we loop through ar[i], for each of the value we will increment the value of model_arr, which will be used later to calculate the pair_count
    # after that loop, we will loop again in model_arr, in each of the value, we divide it by 2 and add the rounded down integer to the pair_count.
    
    pair_count = 0
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    model_arr = [0] * 101

    for i in range(0, len(ar)):
        model_arr[ar[i]] += 1
    for j in range(0, len(model_arr)):
        pair_count = pair_count + model_arr[j]//2

    return pair_count

check_pair_of_socks_v2()
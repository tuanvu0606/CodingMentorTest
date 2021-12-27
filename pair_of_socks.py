def check_pair_of_socks():
    # get the number of items from the user 

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
    print(pair_count)


def check_pair_of_socks_v2():
    # get the number of items from the user 
    pair_count = 0
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    b = [0] * 101

    for i in range(0, len(ar)):
        b[ar[i]] += 1
    for j in range(0, len(b)):
        if b[j] > 0:
            pair_count = pair_count + b[j]/2

    print(b)
    print(pair_count)

check_pair_of_socks_v2()
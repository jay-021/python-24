def sum_of_oneD_arr(arr):
    sum = 0
    arr_new = []
    for i in range(0,len(arr)):
        sum += arr[i]
        # arr_new[i] = sum
        arr_new.append(sum)
        i += 1
    return arr_new

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(sum_of_oneD_arr(arr))
def get_merge_sorted_list(unsorted_list):
    if len(unsorted_list) == 1:     #base case for when the recursion should end as it needs to stop at 1 length
        return unsorted_list

    mid_point = int((len(unsorted_list))//2)        #gets middle element of the list

    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

   # half_a = divide_with_recursion(first_half)
    #half_b = divide_with_recursion(second_half)

    half_a = get_merge_sorted_list(first_half)
    half_b = get_merge_sorted_list(second_half)

    return sorted(half_a + half_b)

def merge_and_sort(first_half,second_half):
    x = 0
    y = 0
    ordered_list = []

    while x < len(first_half) and y < len(second_half):

        if first_half[x] < second_half[y]:
            ordered_list.append(first_half[x])
            x += 1
        else: 
            ordered_list.append(second_half[y])

    while x < len(first_half):
        ordered_list.append(first_half[x])
        x += 1

    while y < len(second_half):
        ordered_list.append(second_half[y])
        y += 1

    return ordered_list
    
       
if __name__ == "__main__":

    import random
    unordered_list = [] 
    for i in range(15):
        unordered_list.append(random.randint(0,50))

    print(f"The list of numbers in random order is {unordered_list}")

    ordered_list = get_merge_sorted_list(unordered_list)

    print(f"The list of numbers in order is {ordered_list}")

    print(f"There is something else I want to try out with this so don't be surprised with a random github message at 3am maybe")
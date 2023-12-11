"""--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?"""


import heapq


def load_input(input: list[str]) -> None:
    """
        Input:  a list of strings representing the lines of the input file

        Output: side effect on the lists created before.
                For seeds a list of lists of int will be used. i.e.:
                [[start, end], [start, end], [start, end] ...]
                For transformations a list of lists of tuples containing a 
                tuple of two int and an int will be used.
                maps[map[transformation((start, end), add)]]
                maps is the list that contains all the map;
                map are the lists that contain the transformations;
                transformation is a tuple composed of:
                    -   a tuple that indicates the interval where the 
                        transformation is applied
                    -   an int that indicates what number must be added (it can 
                        be negative, too) to apply the transformation at the 
                        values in the interval given by the tuple
    """
    s: list[int] = [ int(x) for x in input[0].split(':')[1].split() ]
    for i in range(0, len(s), 2):
        interval: list[int] = []
        interval.extend([s[i], s[i]+s[i+1]-1])
        heapq.heappush(seeds, interval)
    list_num: int = -1
    for line_num in range(1, len(input)):
        if input[line_num][0].isdigit():
            tmp_transformations_list: list[int] = []
            for number in input[line_num].split():
                tmp_transformations_list.append(int(number))
            aux_tuple: tuple[int, int] = (tmp_transformations_list[1], tmp_transformations_list[1]+tmp_transformations_list[2]-1)
            heapq.heappush(transformations[list_num], (aux_tuple, tmp_transformations_list[0]-tmp_transformations_list[1]))
        elif input[line_num][0].isalpha():
            transformations.append([])
            list_num += 1



def intersection(interval: list[int], transformation: tuple[int, int]) -> list[list[int]]:
    """
        Input:  interval:           a list of two integers representing an 
                                    interval fo values
                transformation:    a tuple of two integers representing an 
                                    interval of values
        
        Output: a list of tree lists containing two integers each.
                The first list represents the value of interval that are before 
                the values of transformation, so these values must be not 
                transformed.
                The second list represents the interval of value of interval 
                that are in the interval of transformation, so these values 
                must be transformed.
                The third list represents the interval of value of interval 
                that are after the values of transformations, so these values 
                must not be transformed.
    """
    if interval[1] < transformation[0]:
        return [interval, [], []]
    if interval[0] > transformation[1]:
        return [[], [], interval]
    res: list[list[int]] = [[], [], []]
    if interval[0] < transformation[0]:
        res[0] = [interval[0], transformation[0]-1]
        res[1].append(transformation[0])
    else:
        res[1].append(interval[0])
    if interval[1] > transformation[1]:
        res[2] = [transformation[1]+1, interval[1]]
        res[1].append(transformation[1])
    else:
        res[1].append(interval[1])
    return res



def interval_binary_search(interval: list[int], transformations_list: list[tuple[int, int]], lim_sx: int = 0, lim_dx: int = -1) -> int:
    """
        Input:  interval:               a list of two integers representing an 
                                        interval of values
                transformations_list:   a list of tuple of two integers, each 
                                        tuple represents an interval of value
                lim_sx:                 an integer representing the limit sx of 
                                        the transformations_list during the 
                                        binary search.
                lim_dx                  an integer representing the limit dx of 
                                        the transformations_list during the 
                                        binary search.
        
        Output: an integer representing index of transformations_list that 
                indicate the first interval of values that intersect the given 
                interval.
                -1 if no intervals in transformation_list intersect the given 
                interval.
    """
    if lim_dx == -1:
        lim_dx = len(transformations_list)-1
    if lim_dx == lim_sx:
        if intersection(interval, transformations_list[lim_sx])[1] == []:
            return -1
        return lim_sx
    index = int((lim_sx + lim_dx)/2)
    if transformations_list[index][1] < interval[0]:
        return interval_binary_search(interval, transformations_list, index+1, lim_dx)
    if transformations_list[index][0] > interval[1]:
        return interval_binary_search(interval, transformations_list, lim_sx, index)
    while index > 0:
        if intersection(interval, transformations_list[index-1])[1] != []:
            index -= 1
        else:
            break
    return index



def apply_transformation(interval: list[int], transformation: int) -> list[int]:
    return [interval[0]+transformation, interval[1]+transformation]



def merge_intervals(seeds: list[list[int]]) -> list[list[int]]:
    """
        Input:  a sorted list of intervals in the [start, end] form

        Output: a sorted list of intervals where the overlapping intervals of 
                the input list are merged
    """
    res: list[list[int]] = []
    while len(seeds) > 1:
        e1 = heapq.heappop(seeds)
        e2 = heapq.heappop(seeds)
        if e1[1] > e2[0]:
            heapq.heappush(seeds, [e1[0], max(e1[1], e2[1])])
            continue
        heapq.heappush(res, e1)
        heapq.heappush(seeds, e2)
    if len(seeds) == 1:
        aux = heapq.heappop(seeds)
        heapq.heappush(res, aux)
    return res





def elaborate(seeds: [list[list[int, int]]], transformations_lists: list[list[tuple[tuple[int, int], int]]], num_trans_list: int = 0) -> list[list[int]]:
    """
        Input:  seeds:                  list of intervals of values to transform
                transformations_lists:  lists of list of transformations. Lists 
                                        of transformations must be applied to 
                                        elements in seeds, in order. A 
                                        trasnformation is a 
                                        tuple[tuple[int, int], int] where the 
                                        first tuple says the range where the 
                                        transformation must be applied and the 
                                        last integer what number must be add to 
                                        do the transformation. The last number 
                                        can be positive or negative.
                num_trans_list: int     a number that says what list of 
                                        transformations to use.
        
        Output: a list of lists of two integers. Every list indicate a range of 
                values representing an interval
    """
    if num_trans_list == len(transformations_lists):
        return seeds
    elaborated_intervals: list[list[int]] = []
    trans_list: list[tuple[tuple[int, int], int]] = [ heapq.heappop(transformations_lists[num_trans_list]) for _ in range(len(transformations_lists[num_trans_list])) ]
    while len(seeds) > 0:
        interval = heapq.heappop(seeds)
        first_index: int = interval_binary_search(interval, [ x[0] for x in trans_list ])
        if first_index == -1:
            heapq.heappush(elaborated_intervals, interval)
            continue
        aux: list[list[int]] = intersection(interval, trans_list[first_index][0])
        if aux[0] != []:
            heapq.heappush(elaborated_intervals, aux[0])
        heapq.heappush(elaborated_intervals, apply_transformation(aux[1], trans_list[first_index][1]))
        if aux[2] != []:
            heapq.heappush(seeds, aux[2])
    return elaborate(merge_intervals(elaborated_intervals), transformations_lists, num_trans_list+1)







with open('day_05/input', 'r') as input:
#with open('day_05/test_input_1', 'r') as input:
    l = input.readlines()
seeds: list[list[int]] = []
transformations: list[list[tuple[tuple[int, int], int]]] = []
load_input(l)
res = elaborate(seeds, transformations)
print(min(min(res)))
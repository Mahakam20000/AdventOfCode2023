"""--- Part Two ---
As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

Time:      7  15   30
Distance:  9  40  200
...now instead means this:

Time:      71530
Distance:  940200
Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?"""



def elaborate(time: int, distance: int) -> int:
    """
        Input:  time and distance are two integers, time is the 
                time to complete the race, distance is the minimum 
                distance to travel to win the race
        
        Output: an integer representing the ways to beat the record
    """
    max: int
    i: int
    if time%2 == 0:
        max = time//2
        i = 1
        while max+1 <= time:
            if (max+i)*(max-i) > distance:
                i += 1
            else:
                break
        i = i*2-1
    else:
        max = time//2
        i = 1
        while max+i+1 <= time:
            if (max+i+1)*(max-i) > distance:
                i += 1
            else:
                break
        i *= 2
    return i




#with open('day_06/test_input_1', 'r') as f:
with open('day_06/input', 'r') as f:
    l = f.readlines()
time: int = int(l[0].split(':')[1].replace(" ", ""))
distance: int = int(l[1].split(':')[1].replace(" ", ""))
print(f"time: {time}\ndistance: {distance}")
res: int = elaborate(time, distance)
print(f"\n\nres: {res}")
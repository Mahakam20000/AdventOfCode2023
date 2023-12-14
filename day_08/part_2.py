"""--- Part Two ---
The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?"""


from math import lcm


def load_input(l: list[str]) -> tuple[str, dict[str, list[str]]]:
    """
        Load input in two variables:
            - instructions: a string that contains te instructions to navigate
            - nodes:        a dict that has the nodes' names as keys and their 
                            children as values
    """
    instructions: str = l[0].strip()
    nodes: dict[str, list[str]] = {}
    for i in range(2, len(l)):
        aux = l[i]
        nodes[aux.split('=')[0].strip()] = [aux.split('=')[1].split(',')[0][2:], aux.split('=')[1].split(',')[1].strip()[:-1]]
    return (instructions, nodes)



def find_loop_len(node: str) -> int:
    """
        Input:  a string representing a node

        Output: an int representing the number of steps needed to get the the 
                node that ends with "Z" when the instructions ends.
    """
    count: int = 0
    i: int = 0
    while i <= len(instructions):
        if i == len(instructions):
            if node.endswith("Z"):
                break
            i = 0
        if instructions[i] == "L":
            node = nodes.get(node)[0]
        if instructions[i] == "R":
            node = nodes.get(node)[1]
        count += 1
        i += 1
    return count




def elaborate() -> int:
    """
        Output: the number of steps to arrive at all nodes ending with "Z" 
                simultaneously, starting from all nodes ending with "A".
        Call find_loop_len to get, for every node that ends with "A", how many 
        instructions needs to reach the node that ends with "Z" at the given 
        condition, than find the least common multiple of those numbers.

        * means "use the value of this list as arguments"
    """
    nodes_list: list[str] = [ x for x in nodes.keys() if x.endswith("A") ]
    loops: list[int] = []
    for node in nodes_list:
        loops.append(find_loop_len(node))
    return lcm(*loops)



#with open('day_08/test_input_3', 'r') as f:
with open('day_08/input', 'r') as f:
    l = f.readlines()
instructions: str
nodes: dict[str, list[str]]
instructions, nodes = load_input(l)
steps: int = elaborate()
print(f"steps: {steps}")

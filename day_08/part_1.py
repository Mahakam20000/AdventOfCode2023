"""--- Day 8: Haunted Wasteland ---
You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?"""



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



def elaborate() -> int:
    """
        Navigate the tree. Nodes are saved in a dict because I can retrieve the 
        children in O(1)
        Iterative version, too much steps to use recursion.
    """
    i: int = 0
    count: int = 0
    node: str = "AAA"
    children: list[str] = nodes.get(node)
    while i <= len(instructions):
        if i == len(instructions):
            i = 0
            if node == "ZZZ":
                return count
        if instructions[i] == "L":
            node = children[0]
            children = nodes.get(children[0])
            count += 1
        else:
            node = children[1]
            children = nodes.get(children[1])
            count += 1
        i += 1
    return count



#with open('day_08/test_input_1', 'r') as f:
with open('day_08/input', 'r') as f:
    l = f.readlines()
instructions: str
nodes: dict[str, list[str]]
instructions, nodes = load_input(l)
steps: int = elaborate()
print(f"steps: {steps}")

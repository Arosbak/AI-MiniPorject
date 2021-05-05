"""
Breadth-first and Depth-first search solutions to the Missionaries and Cannibals problem
Created by Brian Bemman based in part on pseudo-code provided in Russell and Norvig (2010).

Three missionaries and three cannibals are on one side of a river along with a boat that can hold at most two people
and never none. Find a way to get everyone to the other side without ever leaving the missionaries on either
side outnumbered by the cannibals.

Problem formulation:

Represent the state of the world on the starting side of the river as a tuple, <m,c,b>, where
m is the number of missionaries,
c is the number of cannibals, and
b is the presence (or not) of the boat.
A solution is a sequence of actions that when applied to the state lead to the goal state of <0,0,0>. Actions are applied
to each state in an alternating manner of subtraction and addition, corresponding to the missionaries and cannibals either
leaving from or arriving at the starting side of the river, respectively. At no point can the state on either side of the river
result in (1) c < 0; c > 3; m < 0; m > 3 and (2) c > m where m is > 0.

initial state:              <3,3,1> i.e., 3 missionaries, 3 cannibals and boat on the starting side of the river
actions:                    <2,0,1>, <0,2,1>, <1,1,1>, <1,0,1>, <0,1,1>
transition model:           -(state, action), +(state, action) i.e., moving from one side to the other
goal test:                  whether or not the current state is the goal state of <0,0,0>
                            i.e., no missionaries, cannibals or boat on the starting side of the river
path cost:                  cost(p) i.e., number of nodes in path from start to n

"""




class Node:
    """A Node class with instance attributes suggested for use in search algorithms by Russell and Norvig (2010)."""
    # constructor for defining the instance attributes
    def __init__(self, state=None, parent=None, action=None, path_cost=0):
        self.state = state  # tuple
        self.parent = parent  # Node object
        self.action = action  # tuple; the action applied to the parent state that results in self.state
        self.path_cost = path_cost  # cost(p); equivalent to depth when each action has a cost of 1
        self.depth = 0  # level in search tree
        if parent:
            self.depth = parent.depth + 1



def depth_first_search(initial_state, goal_state):
    """Depth-first search algorithm first expands the deepest child node of a parent node at each level in search for a state which
  matches the specified goal state. In this implementation, a list is treated as a stack by always removing elements
  from the back and appending elements to the back. """

    if initial_state == goal_state:
        return construct_path(Node(initial_state), initial_state)
    frontier = [Node(initial_state)]  # queue
    reached = set()

    while frontier:
        parent = frontier.pop()
        for child in successors(parent):
            s = child.state
            if s == goal_state:
                return construct_path(child, initial_state)
            if s not in reached:
                reached.add(s)
                frontier.append(child)

    return [], []  # no solution found; return empty state and action paths


def successors(parent):
    """Generates a list of valid successor (i.e., child) nodes from a given parent. Valid successors are those having a
    state which does not violate the constraints of the problem formulation."""
    valid_successors = []
    # determine which of the possible actions applied to the parent state result in a valid child state
    for action in [(2, 0, 1), (0, 2, 1), (1, 1, 1), (1, 0, 1), (0, 1, 1)]:
        child_state = get_child_state(parent, action)
        if is_valid_state(child_state):
            valid_successors.append(Node(child_state, parent, action, parent.depth + 1))
    return valid_successors


def get_child_state(parent, action):
    """Transition model: Applies an action to a parent state to produce a child state."""
    if parent.state[2] == 1:  # boat is on the starting side of river
        child_state = (parent.state[0] - action[0], parent.state[1] - action[1], 0)
    else:
        child_state = (parent.state[0] + action[0], parent.state[1] + action[1], 1)
    return child_state



def is_valid_state(child_state):
    """Determines whether or not an action results in a valid state by considering its effect on both sides of the river.
    A state is valid if on both sides of the river, an action does not result in (1) there being fewer than zero missionaries
    and zero cannibals or more than 3 missionaries and 3 cannibals and (2) more cannibals than missionaries if there is
    at least one missionary. """
    # starting side of river
    if not (0 <= child_state[0] <= 3) or not (0 <= child_state[1] <= 3):
        return False
    if 0 < child_state[0] < child_state[1]:
        return False
    # ending side of river
    if not (0 <= 3 - child_state[0] <= 3) or not (0 <= 3 - child_state[1] <= 3):
        return False
    if 0 < 3 - child_state[0] < 3 - child_state[1]:
        return False
    return True


def construct_path(final_node, initial_state):
    """Constructs the path from the initial state to the goal state by working backwards through parents starting from
    the goal node. """
    state_path = []  # initialize a path to hold states which comprise a solution
    action_path = []  # initialize a path to hold actions which comprise a solution
    while final_node.state != initial_state:
        state_path.append(final_node.state)
        action_path.append(final_node.action)
        final_node = final_node.parent
    state_path.append(final_node.state)
    action_path.append(final_node.action)
    return state_path[::-1], action_path[::-1]  # return path from initial state to goal state


def main():
    initial_state = (3,3,1)
    goal_state = (0, 0, 0)
    print("Initial state:", initial_state, "Goal state:", goal_state)
    state_path, action_path = depth_first_search(initial_state, goal_state)
    print("Depth-first search results:")
    print("States:", state_path)
    print("Actions:", action_path)


if __name__ == '__main__':
    main()

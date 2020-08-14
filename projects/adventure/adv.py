from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Function to get the opposite direction of an input
def opposite_direction(direction):
    if direction == 'n':
        direction = 's'
    elif direction == 's':
        direction = 'n'
    elif direction == 'e':
        direction = 'w'
    elif direction == 'w':
        direction = 'e'
    
    return direction

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt" ##PASSED
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# traversal_path = ['n', 'n']
# This path contains cardinal directions
traversal_path = []

## This graph contains a record of all the rooms I've visited, and which exits I've explored
traversal_graph = {}

## Setting up the first entry in the traversal graph
## It needs to be pre-populated
traversal_graph[world.starting_room.id] = {}
possible_exits = world.starting_room.get_exits()
for item in possible_exits:
    traversal_graph[world.starting_room.id][item] = "?"

# my path of rooms
# this path contains the room ID
path = [world.starting_room.id]

while len(traversal_graph) < len(room_graph):
    room = path[-1]

    # add the current room to the graph if it's a new room
    # Populate the exits in the room with "?"
    if room not in traversal_graph:
        traversal_graph[player.current_room.id] = {}
        possible_exits = player.current_room.get_exits()
        for item in possible_exits:
            traversal_graph[player.current_room.id][item] = "?"

    #picks a random unexplored direction from the player's current room,
    random_direction = random.choice(player.current_room.get_exits())

    #ravels and logs that direction
    if traversal_graph[player.current_room.id][random_direction] is '?':      
 
        # save the name of the current (soon to be old) room
        old_room = player.current_room.id

        # Move in the random direction
        player.travel(random_direction)

        ## save the direction traveled
        traversal_path.append(random_direction)

        # save the name of the new room
        new_room = player.current_room.id

        #link the two rooms together in my graph
        traversal_graph[old_room][random_direction] = new_room

        #need to get opposite of random direction
        opposite = opposite_direction(random_direction)

        ## repeating the block of code above. I'm sure there's a better way to do this.
        if player.current_room.id not in traversal_graph:
            traversal_graph[player.current_room.id] = {}
            possible_exits = player.current_room.get_exits()
            for item in possible_exits:
                traversal_graph[player.current_room.id][item] = "?"
            traversal_graph[new_room][opposite] = old_room
        
        # Build the path of room IDs
        path.append(player.current_room.id)

    # now I just need to loop back to the last branch that was unexplored.
    if '?' not in traversal_graph[player.current_room.id].values():

        if len(path) > 1:
            # Get the most recently traveled direction from the 'path' list of rooms
            for key, value in traversal_graph[player.current_room.id].items():
                if value == path[-2]:
                    direction_key = key

            player.travel(direction_key)
            traversal_path.append(direction_key)
            # Each time you arrive in a room that's been explored, keep going back down the path you just traveled.
            path.pop()
        
        # If the len is 1, you are back at the starting room. The while loop continues.


#print(f'FINAL TRAVERSAL PATH: {traversal_path}')
#print(f'FINAL TRAVERSAL GRAPH: {traversal_graph}')

for key in traversal_graph:
    print(key, traversal_graph[key])




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)



from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt" ##PASSED
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk



### This passes the first test

# print(f"CURRENT ROOM ID: {player.current_room.id}")
# # traversal_path.append(player.current_room.id)
# print(f'GET EXITS {player.current_room.get_exits()}')
# player.travel('n')
# traversal_path.append('n')
# print(f"CURRENT ROOM ID: {player.current_room.id}")
# print(f'GET EXITS {player.current_room.get_exits()}')
# player.travel('n')
# traversal_path.append('n')
# print(f"CURRENT ROOM ID: {player.current_room.id}")
# print(f'GET EXITS {player.current_room.get_exits()}')


#To solve this path, you'll want to construct your own traversal graph.

# this is the sub- data structure
links_to_other_rooms = {}

## This is my "visited"
traversal_graph = {}


# traversal_path = ['n', 'n']
traversal_path = []

q = Queue()

#print(world.starting_room.id)
q.enqueue([world.starting_room.id])


def get_neighbors(room):
    return [0,1,2]
    



while q.size() > 0:

    print('~~~~~NEXT ITERATION~~~~~~')
    ## check current room
    current_room = player.current_room.id
    print(f'CURRENT ROOM: {current_room}')

    path = q.dequeue()
    most_recent_room = path[-1]

    # what exits are avaliable in this current room?
    exit_list = player.current_room.get_exits()

    for direction in exit_list:
        print(f"---> DIRECTION: {direction}")
        links_to_other_rooms[direction] = "?"  


    #BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.


    print(traversal_graph)

    # If an exit has been explored, you can put it in your BFS queue like normal.
    if most_recent_room not in traversal_graph:
        #Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. 
        # if item in most_recent_room == "?": ## This will need to be fixed
        #     ## update the links to other rooms
        #     pass
    
        traversal_graph[most_recent_room] = exit_list

        

        for next_room in get_neighbors(most_recent_room):
            new_path = path.copy()
            new_path.append(next_room)
            q.enqueue(new_path)
    
    #     #picks a random unexplored direction from the player's current room,
    random_direction = random.choice(player.current_room.get_exits())

    #     #  travels and logs that direction
    print(f'TRAVELING IN A "{random_direction.upper()}" DIRECTION')
    player.travel(random_direction)

    traversal_path = new_path
    traversal_path.append(random_direction)
    print(f'RUNNING TRAVERSAL PATH: {traversal_path}')

        

print(f'FINAL TRAVERSAL PATH: {traversal_path}')
print(f'FINAL TRAVERSAL GRAPH: {traversal_graph}')




    # print(f'EXIT LIST: {exit_list}')    
    # ## Populate the list with "?"
    # for direction in exit_list:
    #     print(f"---> DIRECTION: {direction}")
    #     links_to_other_rooms[direction] = "?"  

     ## updates the traversal graph
    # for item in traversal_graph:
    #     print(traversal_path[item])
    #     print(traversal_path[-1])
    #     if traversal_graph[item] == traversal_path[-1]:
    #         traversal_graph[item] = "THE ROOM PREVIOUS"
    
    # traversal_graph[player.current_room.id] = links_to_other_rooms


    
    













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

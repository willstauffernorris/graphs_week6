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

#print(opposite_direction('n'))

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt" ##PASSED
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# traversal_path = ['n', 'n']
traversal_path = []



## Setting up the first entry in the traversal graph
traversal_graph = {}

possible_exits = world.starting_room.get_exits()
#print(possible_exits)

traversal_graph[world.starting_room.id] = {}

for item in possible_exits:
    traversal_graph[world.starting_room.id][item] = "?"


#print(traversal_graph[0])


q = Queue()

q.enqueue([world.starting_room.id])


visited = traversal_graph

#while q.size() > 0:
while len(traversal_graph) < len(room_graph):
    print(f'RUNNING TRAVERSAL PATH: {traversal_path}')

    path = q.dequeue()

    room = path[-1]


    
    # add the current room to the graph if it's a new room
    if room not in traversal_graph:

        traversal_graph[player.current_room.id] = {}

        possible_exits = player.current_room.get_exits()

        for item in possible_exits:
            # if player.current_room.id is world.starting_room.id:
            traversal_graph[player.current_room.id][item] = "?"

    # print(player.current_room.id)


     #picks a random unexplored direction from the player's current room,
    random_direction = random.choice(player.current_room.get_exits())

    if traversal_graph[player.current_room.id][random_direction] is '?':
        #print("UNEXPLORED!")
    #  travels and logs that direction
    #print(f'TRAVELING IN A "{random_direction.upper()}" DIRECTION')

        # save the name of the current (soon to be old) room
        old_room = player.current_room.id
    
        player.travel(random_direction)
        ## save the direction traveled
        traversal_path.append(random_direction)

        # save the name of the new room
        new_room = player.current_room.id

        #link the two rooms together in my graph
        traversal_graph[old_room][random_direction] = new_room

        #need to get opposite of random direction
        opposite = opposite_direction(random_direction)
        # print(random_direction)
        # print(opposite)
        # print(traversal_graph[new])

        ## repeating the block of code above. I'm sure there's a better way to do this.
        if player.current_room.id not in traversal_graph:
            traversal_graph[player.current_room.id] = {}
            possible_exits = player.current_room.get_exits()
            for item in possible_exits:
                # if player.current_room.id is world.starting_room.id:
                traversal_graph[player.current_room.id][item] = "?"
            traversal_graph[new_room][opposite] = old_room
        
        new_path = path.copy()
        new_path.append(player.current_room.id)
        q.enqueue(new_path)
        print(f'NEW PATH: {new_path}')
        print(f'NEW PATH, NEW EXPLORATION')

        # now I just need to loop back to the last branch that was unexplored.
    if '?' not in traversal_graph[player.current_room.id].values():
        print("FUCK YA FOUND A DEAD END")
        #print(traversal_graph)

        # traversal_graph[player.current_room.id]

        # print(traversal_graph[player.current_room.id].values())

        #print(new_path[-2])

        if len(new_path) > 1:
            for key, value in traversal_graph[player.current_room.id].items():
                if value == new_path[-2]:
                    direction_key = key

            player.travel(direction_key)
            print(f'CURRENT ROOM {player.current_room.id}')
            traversal_path.append(direction_key)
            new_path = path.copy()
            new_path.pop()
            q.enqueue(new_path)
            print(f'NEW PATH: {new_path}')
            print(f'LEN OF PATH: {len(new_path)}')
        if len(new_path) == 1:
            print(f'CURRENT ROOM {player.current_room.id}')
            # for key, value in traversal_graph[player.current_room.id].items():
            #     if value == new_path[0]:
            #         direction_key = key
            
            # player.travel(direction_key)
            # print(f'CURRENT ROOM {player.current_room.id}')
            # traversal_path.append(direction_key)
            # new_path = path.copy()
            # # new_path.pop(-1)
            q.enqueue(new_path)
            print(f'NEW PATH: {new_path}')



        # else: # if len of newpath is 1
        #     for key, value in traversal_graph[player.current_room.id].items():
        #         if value == new_path[-2]:
        #             print(key)
        #     key = new_path[0]
        #     player.travel(key)

    print(traversal_graph)
    print(player.current_room.id)




print(f'FINAL TRAVERSAL PATH: {traversal_path}')
#print(f'FINAL TRAVERSAL GRAPH: {traversal_graph}')

for key in traversal_graph:
    print(key, traversal_graph[key])
























# # this is the sub- data structure
# links_to_other_rooms = {}

# ## This is my "visited"
# traversal_graph = {}

# # traversal_path = ['n', 'n']
# traversal_path = []

# q = Queue()

# print(world.starting_room.id)
# q.enqueue([world.starting_room.id])
    

# while q.size() > 0:

#     #print('~~~~~NEXT ITERATION~~~~~~')
#     ## check current room
#     current_room = player.current_room.id
#     print(f'CURRENT ROOM: {current_room}')

#     path = q.dequeue()
#     most_recent_room = path[-1]

#     # what exits are avaliable in this current room?
#     exit_list = player.current_room.get_exits()

#     neighors_list = [0,1,2]


#     ## Populate the list with "?"
#     # print(f'EXIT LIST: {exit_list}') 
#     # for direction in exit_list:
#     #     print(f"---> DIRECTION: {direction}")
#     #     links_to_other_rooms[direction] = "?"  


#     #BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.


#     print(traversal_graph)

#     # If an exit has been explored, you can put it in your BFS queue like normal.
#     if most_recent_room not in traversal_graph:
#         #Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. 
#         # if item in most_recent_room == "?": ## This will need to be fixed
#         #     ## update the links to other rooms
#         #     pass
    
#         traversal_graph[most_recent_room] = exit_list




#         for next_room in neighors_list:
#             new_path = path.copy()
#             new_path.append(next_room)
#             q.enqueue(new_path)
    
#     #     #picks a random unexplored direction from the player's current room,
#     random_direction = random.choice(player.current_room.get_exits())

#     #     #  travels and logs that direction
#     print(f'TRAVELING IN A "{random_direction.upper()}" DIRECTION')
#     player.travel(random_direction)

#     traversal_path = new_path
#     traversal_path.append(random_direction)
#     print(f'RUNNING TRAVERSAL GRAPH: {traversal_graph}')

        

# print(f'FINAL TRAVERSAL PATH: {traversal_path}')
# print(f'FINAL TRAVERSAL GRAPH: {traversal_graph}')










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

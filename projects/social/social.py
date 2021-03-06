import random


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


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"user {i}")

        # Create friendships
        # generate all possible friendship combinations
        possible_friendships = []

        # avoid duplicate by ensuring the first number < second number
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle friendships
        random.shuffle(possible_friendships)

        # create friendships for the first N pairs of the list
        # n -> num_users * avg_friendships // 2
        N = num_users * avg_friendships//2
        for i in range(N):
            friendship = possible_friendships[i]

            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)

    def get_neighbors(self, vertex_id):
        return self.friendships[vertex_id]


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
          ## key = friend ID
        ## value = path

        #visited will contain every user in the given user's network AND the shortest path between the two

        # !!!! IMPLEMENT ME
        ## do a depth first search or a breadth first search
        ## BREADTH FIRST
        q = Queue()

        q.enqueue([user_id])

        #print(self.get_neighbors(user_id))
        #print(user_id)

        visited = {}

        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]

            ## for each final node, save the path to the visited dictionary
            if vertex not in visited:
                visited[vertex] = path

                for next_vertex in self.get_neighbors(vertex):
                    new_path = path.copy()
                    new_path.append(next_vertex)
                    q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'FRIENDSHIPS: {sg.friendships}')
    connections = sg.get_all_social_paths(1)
    print(f'CONNECTIONS: {connections}')

    sg.populate_graph(100, 10)
    #print(f'100 USERS: {sg.friendships}')


# If you create 1000 users with an average of 5 random friends each
    sg.populate_graph(1000, 5)
    #print(f'1000 USERS: {sg.friendships}')
    connections = sg.get_all_social_paths(1)
    #print(f'CONNECTIONS: {connections}')

    #what percentage of other users will be in a particular user's extended social network?
    print(len(connections)) # 990 #992 #996 # 991
    ## almost 100% are in the extended social network. There are very few isolated users.


    #What is the average degree of separation between a user and those in his/her extended network?
    len_of_connections = []
    for key in connections:
        degrees_of_sep = (len(connections[key]))
        #print(len_of_connections)
        len_of_connections.append(degrees_of_sep)
    #print(len_of_connections)
    print(sum(len_of_connections)/len(len_of_connections))
    ## avg degrees of separation is 5 (ish)!





        #len_of_connections = len_of_connections.append(len(connections[key])
    #print(len_of_connections)



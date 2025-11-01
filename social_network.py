class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
       if friend not in self.friends and friend != self:
           self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
   
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends and friend != self:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network. Skipping...")

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. {person1_name} or {person2_name} doesn't exist!")
            return
        
        p1 = self.people[person1_name]
        p2 = self.people[person2_name]

        p1.add_friend(p2)
        p2.add_friend(p1)

    def print_network(self):
        print("\n--- Social Network Connections ---")
        for name, person in self.people.items():
            friends = ", ".join(friend.name for friend in person.friends) if person.friends else "No friends"
            print(f"{name} is friends with: {friends}")


# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    # Add 6 users
    for person in ["Alex", "Jordan", "Morgan", "Taylor", "Riley", "Casey"]:
        network.add_person(person)

    # Test duplicate person
    network.add_person("Alex")

    # Add 8 friendships (non-linear)
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Morgan")
    network.add_friendship("Morgan", "Taylor")
    network.add_friendship("Jordan", "Riley")
    network.add_friendship("Riley", "Alex")
    network.add_friendship("Casey", "Morgan")
    network.add_friendship("Casey", "Riley")

    # Test nonexistent user
    network.add_friendship("Alex", "Sam")

    network.print_network()
# Design memo:
# Why is a graph the right structure to represent a social network?
# A graph is the best strucuture for a social network because it allows for nodes to be connecte to other edges in any direction. 
# Graphs typically represent real-world networks where mutual friendships can have various connections. 
# Helping to further understand the connection between others.

# Why wouldn’t a list or tree work as well for this?
# A list or tree wouldn't work as well for this because they have strict parent-child relationships and no cycles.
# In social networks, theres no "parent" and users can connect more freely. A tree would restreict connections. 
# A list can only store users in a single sequence, and it does not represent relationships between them. List wouldn't show who is connected.

# What performance or structural trade-offs did you notice when adding friends or printing the network?
# Checking for duplicate friendships. Since each person stores their friends in a list, the program has to look through the existing list to avoid
# re-adding friends. Printing increases runtime since the network goes through every person and then through each of their friends. 
# A set or hash map could make lookups faster but using lists performs well for mid-sized graphs.
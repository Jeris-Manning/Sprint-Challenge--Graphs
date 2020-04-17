from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

wizard = Player(world.starting_room)



def a_wandering_wizards_whimsical_walk(starting_room, visited = None):

    wizard_trail = []

    magic_mirror = {
            'n':'s',
            'e':'w',
            's':'n',
            'w':'e'
        }

    if visited is None:
        visited = [starting_room]

    for door in wizard.current_room.get_exits():

        if wizard.current_room.get_room_in_direction(door).id not in visited:

            wizard.travel(door)
            wizard_trail.append(door)
            visited.append(wizard.current_room.id)

            wizard_trail = wizard_trail + a_wandering_wizards_whimsical_walk(wizard.current_room.id, visited)

            wizard.travel(magic_mirror[door])
            wizard_trail.append((magic_mirror[door]))

    return wizard_trail


traversal_path = a_wandering_wizards_whimsical_walk(0)
print(traversal_path, "WIZARD WALK")


# TRAVERSAL TEST
visited_rooms = set()
wizard.current_room = world.starting_room
visited_rooms.add(wizard.current_room)

for move in traversal_path:
    wizard.travel(move)
    visited_rooms.add(wizard.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# wizard.current_room.print_room_description(wizard)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         wizard.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
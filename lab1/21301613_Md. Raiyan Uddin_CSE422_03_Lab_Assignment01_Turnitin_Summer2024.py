#422
import heapq

heuristic_val = {}
map = {}

with open("./21301613_Md. Raiyan Uddin_CSE422_03_Lab_Assignment01_InputFile_Summer2024.txt", 'r') as file:
    input_list = file.readlines()
    for line in input_list:
        source = line.split()
        heuristic_val[source[0]] = int(source[1])
        map[source[0]] = []
        calu = 2
        for i in range(len(source[2:])//2):
            map[source[0]].append((int(source[calu+1]),source[calu]))
            calu+=2


def astar_searchpath_algorithm(start, goal, graph, heuristic):
    pri_list = []
    f_start = heuristic[start] + 0
    heapq.heappush(pri_list, (f_start, start))
    path_val = {start:0}
    source = {start:None}
    location = False

    while len(pri_list) > 0:
        present_node = heapq.heappop(pri_list)      
        if present_node[1] == goal:
            location = True
            break

        for child in graph[present_node[1]]:
            path_new =path_val[present_node[1]] + child[0]
            if child[1] not in path_val or path_new < path_val[child[1]]:
                path_val[child[1]] = path_new
                new_file = path_new + heuristic[child[1]]
                heapq.heappush(pri_list, (new_file, child[1]))
                source[child[1]] = present_node[1]

    if location == False:
        
        return None, None
    else:
        route = [goal]
        node = goal

        while node != start:
            node = source[node]
            route.append(node)

        pos = len(route)-1
        file_path = ''
        while pos != -1:
            if pos == 0:
                file_path += route[pos]
            else:
                file_path += route[pos]+' --> '
            pos -= 1

        return path_val, file_path

start_node = input("Enter the starting city: ")
goal_node = input("Enter the destination city: ")
path_val, file_path = astar_searchpath_algorithm(start_node, goal_node, map, heuristic_val)

if path_val is not None:
    file_output = "Outputfile.txt"
    with open(file_output, 'w') as output_file: 
        output_file.write(f"Path: {file_path}\n")
        output_file.write(f"Total distance: {path_val[goal_node]} km")
    print("The Output is shown at", file_output)
else:
    file_output = "Outputfile.txt"
    with open(file_output, 'w') as output_file:
        output_file.write("No path found from {} to {}".format(start_node, goal_node))
    print("Output written to", file_output)
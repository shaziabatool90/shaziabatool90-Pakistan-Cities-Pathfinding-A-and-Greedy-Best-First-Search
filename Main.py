
city_order = [
    'Karachi',
    'Hyderabad',
    'Sukkur',
    'Larkana',
    'Bahawalpur',
    'Multan',
    'Faisalabad',
    'Islamabad',
    'Rawalpindi',
    'Lahore',
    'Gujranwala',
    'Sialkot',
    'Peshawar',
    'Quetta',
    'Rahim Yar Khan',
    'Jhang',
    'Sargodha',
    'Abbottabad'
]

edges = {
    'Abbottabad': ['Peshawar'],
    'Bahawalpur': ['Multan', 'Rahim Yar Khan'],
    'Faisalabad': ['Multan', 'Islamabad', 'Sargodha', 'Jhang', 'Gujranwala', 'Lahore'],
    'Gujranwala': ['Lahore', 'Sialkot', 'Faisalabad'],
    'Hyderabad': ['Karachi', 'Sukkur', 'Larkana'],
    'Islamabad': ['Rawalpindi', 'Lahore', 'Faisalabad'],
    'Jhang': ['Faisalabad', 'Sargodha'],
    'Karachi': ['Hyderabad', 'Sukkur'],
    'Lahore': ['Islamabad', 'Rawalpindi', 'Faisalabad', 'Sialkot', 'Gujranwala'],
    'Larkana': ['Sukkur', 'Hyderabad'],
    'Multan': ['Bahawalpur', 'Faisalabad'],
    'Peshawar': ['Rawalpindi', 'Abbottabad'],
    'Quetta': ['Sukkur', 'Rahim Yar Khan'],
    'Rahim Yar Khan': ['Quetta', 'Bahawalpur'],
    'Rawalpindi': ['Islamabad', 'Lahore', 'Peshawar'],
    'Sargodha': ['Faisalabad', 'Jhang'],
    'Sialkot': ['Gujranwala', 'Lahore'],
    'Sukkur': ['Hyderabad', 'Karachi', 'Larkana']
}

# Define path costs based on approximate distances in kilometers
path_costs = {
    ('Abbottabad', 'Peshawar'): 198,
    ('Bahawalpur', 'Multan'): 99,
    ('Bahawalpur', 'Rahim Yar Khan'): 211,
    ('Faisalabad', 'Multan'): 249,
    ('Faisalabad', 'Islamabad'): 320,
    ('Faisalabad', 'Sargodha'): 91,
    ('Faisalabad', 'Jhang'): 93,
    ('Faisalabad', 'Gujranwala'): 186,
    ('Faisalabad', 'Lahore'): 90,
    ('Gujranwala', 'Lahore'): 80,
    ('Gujranwala', 'Sialkot'): 52,
    ('Gujranwala', 'Faisalabad'): 186,
    ('Hyderabad', 'Karachi'): 80,
    ('Hyderabad', 'Sukkur'): 334,
    ('Hyderabad', 'Larkana'): 315,
    ('Islamabad', 'Rawalpindi'): 23,
    ('Islamabad', 'Lahore'): 377,
    ('Islamabad', 'Faisalabad'): 320,
    ('Jhang', 'Faisalabad'): 93,
    ('Jhang', 'Sargodha'): 122,
    ('Karachi', 'Hyderabad'): 80,
    ('Karachi', 'Sukkur'): 474,
    ('Lahore', 'Islamabad'): 377,
    ('Lahore', 'Rawalpindi'): 361,
    ('Lahore', 'Faisalabad'): 90,
    ('Lahore', 'Sialkot'): 132,
    ('Lahore', 'Gujranwala'): 80,
    ('Larkana', 'Sukkur'): 83,
    ('Larkana', 'Hyderabad'): 315,
    ('Multan', 'Bahawalpur'): 99,
    ('Multan', 'Faisalabad'): 249,
    ('Peshawar', 'Rawalpindi'): 188,
    ('Peshawar', 'Abbottabad'): 198,
    ('Quetta', 'Sukkur'): 386,
    ('Quetta', 'Rahim Yar Khan'): 552,
    ('Rahim Yar Khan', 'Quetta'): 552,
    ('Rahim Yar Khan', 'Bahawalpur'): 211,
    ('Rawalpindi', 'Islamabad'): 23,
    ('Rawalpindi', 'Lahore'): 361,
    ('Rawalpindi', 'Peshawar'): 188,
    ('Sargodha', 'Faisalabad'): 91,
    ('Sargodha', 'Jhang'): 122,
    ('Sialkot', 'Gujranwala'): 52,
    ('Sialkot', 'Lahore'): 132,
    ('Sukkur', 'Hyderabad'): 334,
    ('Sukkur', 'Karachi'): 474,
    ('Sukkur', 'Larkana'): 83,
    ('Sukkur', 'Quetta'): 386
}

cities = {
    'Karachi': (24.8607, 67.0011),
    'Hyderabad': (25.3969, 68.3772),
    'Sukkur': (27.7138, 68.8304),
    'Larkana': (27.5609, 68.2268),
    'Bahawalpur': (28.9, 71.7112),
    'Multan': (30.1575, 71.5249),
    'Faisalabad': (29.9, 72.9),  
    'Islamabad': (32.8, 72.8),   
    'Rawalpindi': (33.5651, 74),  
    'Lahore': (31.5497, 73.8),    
    'Gujranwala': (31.8, 73),  
    'Sialkot': (32.4945, 74.3),     
    'Peshawar': (34.0151, 71.5249),
    'Quetta': (30.1798, 66.975),
    'Rahim Yar Khan': (28.4202, 70.2957),
    'Jhang': (31.2749, 72.3187),
    'Sargodha': (32.0836, 72.4),    
    'Abbottabad': (34.1546, 73.0)   
}

graph = {
    'Abbottabad': {'Peshawar': 198},
    'Bahawalpur': {'Multan': 99, 'Rahim Yar Khan': 211},
    'Faisalabad': {'Multan': 249, 'Islamabad': 320, 'Sargodha': 91, 'Jhang': 93, 'Gujranwala': 186, 'Lahore': 90},
    'Gujranwala': {'Lahore': 80, 'Sialkot': 52, 'Faisalabad': 186},
    'Hyderabad': {'Karachi': 80, 'Sukkur': 334, 'Larkana': 315},
    'Islamabad': {'Rawalpindi': 23, 'Lahore': 377, 'Faisalabad': 320},
    'Jhang': {'Faisalabad': 93, 'Sargodha': 122},
    'Karachi': {'Hyderabad': 80, 'Sukkur': 474},
    'Lahore': {'Islamabad': 377, 'Rawalpindi': 361, 'Faisalabad': 90, 'Sialkot': 132, 'Gujranwala': 80},
    'Larkana': {'Sukkur': 83, 'Hyderabad': 315},
    'Multan': {'Bahawalpur': 99, 'Faisalabad': 249},
    'Peshawar': {'Rawalpindi': 188, 'Abbottabad': 198},
    'Quetta': {'Sukkur': 386, 'Rahim Yar Khan': 552},
    'Rahim Yar Khan': {'Quetta': 552, 'Bahawalpur': 211},
    'Rawalpindi': {'Islamabad': 23, 'Lahore': 361, 'Peshawar': 188},
    'Sargodha': {'Faisalabad': 91, 'Jhang': 122},
    'Sialkot': {'Gujranwala': 52, 'Lahore': 132},
    'Sukkur': {'Hyderabad': 334, 'Karachi': 474, 'Larkana': 83, 'Quetta': 386}
}

# Heuristics Data
heuristic_values = {
    'Karachi': {
        'Hyderabad': 76,
        'Sukkur': 399,
        'Larkana': 347,
        'Bahawalpur': 1501,
        'Multan': 1623,
        'Faisalabad': 1900,
        'Islamabad': 2230,
        'Rawalpindi': 2232,
        'Lahore': 2000,
        'Gujranwala': 2071,
        'Sialkot': 2113,
        'Peshawar': 2410,
        'Quetta': 784,
        'Rahim Yar Khan': 1341,
        'Jhang': 2002,
        'Sargodha': 2001,
        'Abbottabad': 2510,
        'Karachi': 0
    },
    'Hyderabad': {
        'Karachi': 76,
        'Sukkur': 331,
        'Larkana': 310,
        'Bahawalpur': 1478,
        'Multan': 1573,
        'Faisalabad': 1829,
        'Islamabad': 2145,
        'Rawalpindi': 2172,
        'Lahore': 1919,
        'Gujranwala': 1998,
        'Sialkot': 2035,
        'Peshawar': 2330,
        'Quetta': 716,
        'Rahim Yar Khan': 1264,
        'Jhang': 1917,
        'Sargodha': 1913,
        'Abbottabad': 2430,
        'Hyderabad': 0
    },
    'Sukkur': {
        'Karachi': 399,
        'Hyderabad': 331,
        'Larkana': 80,
        'Bahawalpur': 1140,
        'Multan': 1228,
        'Faisalabad': 1437,
        'Islamabad': 1800,
        'Rawalpindi': 1810,
        'Lahore': 1507,
        'Gujranwala': 1627,
        'Sialkot': 1710,
        'Peshawar': 2008,
        'Quetta': 336,
        'Rahim Yar Khan': 908,
        'Jhang': 1500,
        'Sargodha': 1548,
        'Abbottabad': 2206,
        'Sukkur': 0
    },
    'Larkana': {
        'Karachi': 347,
        'Hyderabad': 310,
        'Sukkur': 80,
        'Bahawalpur': 1202,
        'Multan': 1321,
        'Faisalabad': 1530,
        'Islamabad': 1820,
        'Rawalpindi': 1753,
        'Lahore': 1640,
        'Gujranwala': 1730,
        'Sialkot': 1782,
        'Peshawar': 2001,
        'Quetta': 454,
        'Rahim Yar Khan': 1001,
        'Jhang': 1643,
        'Sargodha': 1571,
        'Abbottabad': 2280,
        'Larkana': 0
    },
    'Bahawalpur': {
        'Karachi': 1501,
        'Hyderabad': 1478,
        'Sukkur': 1140,
        'Larkana': 1202,
        'Multan': 97,
        'Faisalabad': 338,
        'Islamabad': 662,
        'Rawalpindi': 660,
        'Lahore': 433,
        'Gujranwala': 511,
        'Sialkot': 560,
        'Peshawar': 839,
        'Quetta': 758,
        'Rahim Yar Khan': 203,
        'Jhang': 432,
        'Sargodha': 435,
        'Abbottabad': 1076,
        'Bahawalpur': 0
    },
    'Multan': {
        'Karachi': 1623,
        'Hyderabad': 1573,
        'Sukkur': 1228,
        'Larkana': 1321,
        'Bahawalpur': 97,
        'Faisalabad': 239,
        'Islamabad': 529,
        'Rawalpindi': 502,
        'Lahore': 319,
        'Gujranwala': 409,
        'Sialkot': 470,
        'Peshawar': 750,
        'Quetta': 822,
        'Rahim Yar Khan': 302,
        'Jhang': 340,
        'Sargodha': 320,
        'Abbottabad': 938,
        'Multan': 0
    },
    'Faisalabad': {
        'Karachi': 1900,
        'Hyderabad': 1829,
        'Sukkur': 1437,
        'Larkana': 1530,
        'Bahawalpur': 338,
        'Multan': 238,
        'Islamabad': 317,
        'Rawalpindi': 333,
        'Lahore': 86,
        'Gujranwala': 165,
        'Sialkot': 222,
        'Peshawar': 524,
        'Quetta': 1111,
        'Rahim Yar Khan': 555,
        'Jhang': 90,
        'Sargodha': 84,
        'Abbottabad': 717,
        'Faisalabad': 0
    },
    'Islamabad': {
        'Karachi': 2230,
        'Hyderabad': 2145,
        'Sukkur': 1800,
        'Larkana': 1820,
        'Bahawalpur': 662,
        'Multan': 529,
        'Faisalabad': 314,
        'Rawalpindi': 20,
        'Lahore': 371,
        'Gujranwala': 455,
        'Sialkot': 503,
        'Peshawar': 210,
        'Quetta': 1430,
        'Rahim Yar Khan': 879,
        'Jhang': 411,
        'Sargodha': 401,
        'Abbottabad': 403,
        'Islamabad': 0
    },
    'Rawalpindi': {
        'Karachi': 2230,
        'Hyderabad': 2172,
        'Sukkur': 1810,
        'Larkana': 1753,
        'Bahawalpur': 660,
        'Multan': 502,
        'Faisalabad': 333,
        'Islamabad': 20,
        'Lahore': 331,
        'Gujranwala': 401,
        'Sialkot': 433,
        'Peshawar': 178,
        'Quetta': 1404,
        'Rahim Yar Khan': 900,
        'Jhang': 430,
        'Sargodha': 432,
        'Abbottabad': 380,
        'Rawalpindi': 0
    },
    'Lahore': {
        'Karachi': 2000,
        'Hyderabad': 1919,
        'Sukkur': 1507,
        'Larkana': 1640,
        'Bahawalpur': 433,
        'Multan': 319,
        'Faisalabad': 86,
        'Islamabad': 371,
        'Rawalpindi': 331,
        'Gujranwala': 71,
        'Sialkot': 130,
        'Peshawar': 542,
        'Quetta': 1200,
        'Rahim Yar Khan': 645,
        'Jhang': 180,
        'Sargodha': 173,
        'Abbottabad': 746,
        'Lahore': 0
    },
    'Gujranwala': {
        'Karachi': 2071,
        'Hyderabad': 1998,
        'Sukkur': 1627,
        'Larkana': 1730,
        'Bahawalpur': 511,
        'Multan': 409,
        'Faisalabad': 165,
        'Islamabad': 455,
        'Rawalpindi': 401,
        'Lahore': 71,
        'Sialkot': 47,
        'Peshawar': 621,
        'Quetta': 1277,
        'Rahim Yar Khan': 720,
        'Jhang': 258,
        'Sargodha': 259,
        'Abbottabad': 821,
        'Gujranwala': 0
    },
    'Sialkot': {
        'Karachi': 2113,
        'Hyderabad': 2035,
        'Sukkur': 1710,
        'Larkana': 1782,
        'Bahawalpur': 560,
        'Multan': 470,
        'Faisalabad': 222,
        'Islamabad': 503,
        'Rawalpindi': 433,
        'Lahore': 130,
        'Gujranwala': 47,
        'Peshawar': 645,
        'Quetta': 1223,
        'Rahim Yar Khan': 725,
        'Jhang': 302,
        'Sargodha': 304,
        'Abbottabad': 829,
        'Sialkot': 0
    },
    'Peshawar': {
        'Karachi': 2410,
        'Hyderabad': 2330,
        'Sukkur': 2008,
        'Larkana': 2001,
        'Bahawalpur': 839,
        'Multan': 750,
        'Faisalabad': 524,
        'Islamabad': 210,
        'Rawalpindi': 178,
        'Lahore': 542,
        'Gujranwala': 621,
        'Sialkot': 645,
        'Quetta': 1552,
        'Rahim Yar Khan': 1037,
        'Jhang': 613,
        'Sargodha': 612,
        'Abbottabad': 178,
        'Peshawar': 0
    },
    'Quetta': {
        'Karachi': 784,
        'Hyderabad': 716,
        'Sukkur': 336,
        'Larkana': 454,
        'Bahawalpur': 758,
        'Multan': 822,
        'Faisalabad': 1111,
        'Islamabad': 1430,
        'Rawalpindi': 1404,
        'Lahore': 1200,
        'Gujranwala': 1277,
        'Sialkot': 1223,
        'Peshawar': 1552,
        'Rahim Yar Khan': 432,
        'Jhang': 1094,
        'Sargodha': 1132,
        'Abbottabad': 1234,
        'Quetta': 0
    },
    'Rahim Yar Khan': {
        'Karachi': 1341,
        'Hyderabad': 1264,
        'Sukkur': 980,
        'Larkana': 1001,
        'Bahawalpur': 203,
        'Multan': 302,
        'Faisalabad': 555,
        'Islamabad': 879,
        'Rawalpindi': 900,
        'Lahore': 645,
        'Gujranwala': 720,
        'Sialkot': 725,
        'Peshawar': 1037,
        'Quetta': 432,
        'Jhang': 638,
        'Sargodha': 610,
        'Abbottabad': 1148,
        'Rahim Yar Khan': 0
    },
    'Jhang': {
        'Karachi': 2002,
        'Hyderabad': 1917,
        'Sukkur': 1500,
        'Larkana': 1643,
        'Bahawalpur': 432,
        'Multan': 340,
        'Faisalabad': 90,
        'Islamabad': 411,
        'Rawalpindi': 403,
        'Lahore': 180,
        'Gujranwala': 258,
        'Sialkot': 302,
        'Peshawar': 613,
        'Quetta': 1094,
        'Rahim Yar Khan': 638,
        'Sargodha': 115,
        'Abbottabad': 816,
        'Jhang': 0
    },
    'Sargodha': {
        'Karachi': 2001,
        'Hyderabad': 1913,
        'Sukkur': 1548,
        'Larkana': 1571,
        'Bahawalpur': 435,
        'Multan': 320,
        'Faisalabad': 84,
        'Islamabad': 401,
        'Rawalpindi': 432,
        'Lahore': 173,
        'Gujranwala': 259,
        'Sialkot': 304,
        'Peshawar': 612,
        'Quetta': 1132,
        'Rahim Yar Khan': 610,
        'Jhang': 115,
        'Abbottabad': 810,
        'Sargodha': 0
    },
    'Abbottabad': {
        'Karachi': 2510,
        'Hyderabad': 2430,
        'Sukkur': 2206,
        'Larkana': 2280,
        'Bahawalpur': 1076,
        'Multan': 938,
        'Faisalabad': 717,
        'Islamabad': 403,
        'Rawalpindi': 380,
        'Lahore': 746,
        'Gujranwala': 821,
        'Sialkot': 829,
        'Peshawar': 178,
        'Quetta': 1132,
        'Rahim Yar Khan': 1148,
        'Jhang': 816,
        'Sargodha': 810,
        'Abbottabad': 0
    }
}

import heapq

def astar(graph, heuristic_values, start, goal):
    print(f'\nA* Search Working ...\n')
    frontier = []
    heapq.heappush(frontier, (0, start))
    path_cost = {start: (0, None)}

    while frontier:
        estimated_cost, current_node = heapq.heappop(frontier)
        print(f'Current Node: {current_node}')
        
        if current_node == goal:
            print(f'-------------Reached GOAL City: {current_node}-------------')
            path = []
            total_cost = path_cost[current_node][0]
            while current_node is not None:
                path.append(current_node)
                current_node = path_cost[current_node][1]
            path.reverse()
            return path, total_cost

        print('Neighbors:')
        for neighbor, distance in graph[current_node].items():
            total_cost = path_cost[current_node][0] + distance
            estimated_total_cost = total_cost + heuristic_values[neighbor][goal]
            if current_node != goal:
                print(f'    {neighbor}: Path Cost: {total_cost} + Heuristic: {heuristic_values[neighbor][goal]} = {estimated_total_cost}')

        for neighbor, distance in graph[current_node].items():
            total_cost = path_cost[current_node][0] + distance
            if neighbor not in path_cost or total_cost < path_cost[neighbor][0]:
                path_cost[neighbor] = (total_cost, current_node)
                estimated_total_cost = total_cost + heuristic_values[neighbor][goal]
                heapq.heappush(frontier, (estimated_total_cost, neighbor))

    return None, float('inf')

def greedy_best_first(graph, heuristic_values, start, goal):
    print(f'\nGreedy Best-First Search Working ...\n')
    frontier = []
    heapq.heappush(frontier, (heuristic_values[start][goal], start))  # (heuristic, node)
    came_from = {start: None}  # To reconstruct path
    cost_so_far = {start: 0}   # To keep track of actual path costs

    while frontier:
        _, current_node = heapq.heappop(frontier)
        print(f'Current Node: {current_node}')
        
        if current_node == goal:
            print(f'-------------Reached GOAL City: {current_node}-------------')
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path, cost_so_far[goal]

        print('Neighbors:')
        for neighbor, distance in graph[current_node].items():
            new_cost = cost_so_far[current_node] + distance
            heuristic = heuristic_values[neighbor][goal]
            print(f'    {neighbor}: Heuristic: {heuristic}')
            
            if neighbor not in came_from or new_cost < cost_so_far.get(neighbor, float('inf')):
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(frontier, (heuristic, neighbor))

    return None, float('inf')

def main():
    print("Pakistan Cities Pathfinding")
    print("==========================")
    print("Available cities:", ", ".join(city_order))
    print("\nChoose search algorithm:")
    print("1. A* Search")
    print("2. Greedy Best-First Search")
    
    choice = input("Enter your choice: ").strip()
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice (1 or 2): ").strip()
    
    start_city = input("Enter the start city: ").strip()
    while start_city not in city_order:
        print("Invalid city. Please choose from the available cities.")
        start_city = input("Enter the start city: ").strip()
    
    goal_city = input("Enter the goal city: ").strip()
    while goal_city not in city_order:
        print("Invalid city. Please choose from the available cities.")
        goal_city = input("Enter the goal city: ").strip()

    print('\033[1m' + f'\nHeuristics to {goal_city}:' + '\033[0m')
    for city, h in heuristic_values[goal_city].items():
        print(f'{city} = {h}')

    if choice == '1':
        path, total_cost = astar(graph, heuristic_values, start_city, goal_city)
    else:
        path, total_cost = greedy_best_first(graph, heuristic_values, start_city, goal_city)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(15, 10))

    for city in city_order:
        coords = cities[city]
        plt.plot(coords[1], coords[0], 'bo', markersize=8)
        plt.text(coords[1], coords[0] + 0.02, city, ha='center', va='center', fontsize=8)

    for city, neighbors in edges.items():
        start_coords = cities[city]
        for neighbor in neighbors:
            end_coords = cities[neighbor]
            edge_color = 'b-'
            ALPHA = 0.2 

            if path and ((city in path and neighbor in path and abs(path.index(city) - path.index(neighbor)) == 1)):
                edge_color = '#C11C84'  
                ALPHA = 0.8  
            plt.plot([start_coords[1], end_coords[1]], [start_coords[0], end_coords[0]], edge_color, alpha=ALPHA)

            mid_x = (start_coords[1] + end_coords[1]) / 2
            mid_y = (start_coords[0] + end_coords[0]) / 2

            cost = path_costs.get((city, neighbor)) or path_costs.get((neighbor, city))
            if cost is not None:
                plt.text(mid_x, mid_y, str(cost), fontsize=8, color='purple', ha='center', va='center')

    plt.axis('off')
    plt.show()

    if path:
        print("\nOptimal Path from", start_city, "to", goal_city, ":\n", path)
        print("\nTotal cost:", total_cost)
    else:
        print("No path found from", start_city, "to", goal_city)

if __name__ == "__main__":
    main()
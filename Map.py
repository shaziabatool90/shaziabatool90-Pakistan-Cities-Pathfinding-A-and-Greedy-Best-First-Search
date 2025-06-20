import matplotlib.pyplot as plt
import math

city_order = [
    'Karachi', 'Hyderabad', 'Sukkur', 'Larkana', 'Bahawalpur', 'Multan', 'Faisalabad', 'Islamabad',
    'Rawalpindi', 'Lahore', 'Gujranwala', 'Sialkot', 'Peshawar', 'Quetta', 'Rahim Yar Khan', 'Jhang',
    'Sargodha', 'Abbottabad'
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
    ('Hyderabad', 'Larkana'): 315,
    ('Hyderabad', 'Sukkur'): 334,
    ('Islamabad', 'Lahore'): 377,
    ('Islamabad', 'Rawalpindi'): 23,
    ('Jhang', 'Sargodha'): 122,
    ('Karachi', 'Hyderabad'): 80,
    ('Karachi', 'Sukkur'): 474,
    ('Karachi', 'Quetta'): 700,
    ('Lahore', 'Rawalpindi'): 361,
    ('Lahore', 'Sialkot'): 132,
    ('Larkana', 'Sukkur'): 83,
    ('Peshawar', 'Rawalpindi'): 188,
    ('Quetta', 'Sukkur'): 386,
    ('Quetta', 'Rahim Yar Khan'): 552,
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


plt.figure(figsize=(20, 12), dpi=100)


for city, neighbors in edges.items():
    start_coords = cities[city]
    for neighbor in neighbors:
        end_coords = cities[neighbor]
        plt.plot([start_coords[1], end_coords[1]], 
                 [start_coords[0], end_coords[0]], 
                 'b-', linewidth=1, alpha=0.3)

        mid_x = (start_coords[1] + end_coords[1]) / 2
        mid_y = (start_coords[0] + end_coords[0]) / 2
        
        dx = end_coords[1] - start_coords[1]
        dy = end_coords[0] - start_coords[0]
        angle = (180/3.14159) * math.atan2(dy, dx)

        cost = path_costs.get((city, neighbor), path_costs.get((neighbor, city), None))
        if cost is not None:
            plt.text(mid_x, mid_y, str(cost), 
                     fontsize=7, color='purple', 
                     ha='center', va='center',
                     rotation=angle,
                     bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

for city in city_order:
    coords = cities[city]
    plt.plot(coords[1], coords[0], 'o', 
             markersize=12 if city in ['Lahore', 'Islamabad', 'Karachi'] else 10,
             markerfacecolor='red',
             markeredgecolor='black',
             markeredgewidth=0.5)
    
    offset_x = 0.15
    offset_y = 0.15

    if city == 'Lahore':
        offset_y = -0.2
    elif city == 'Islamabad':
        offset_x = -0.2
    elif city == 'Rawalpindi':
        offset_x = 0.2
    elif city == 'Faisalabad':
        offset_y = 0.2
    elif city == 'Multan':
        offset_y = -0.2
    elif city == 'Gujranwala':
        offset_x = -0.2
    elif city == 'Sialkot':
        offset_x = 0.2
        offset_y = -0.2
    elif city == 'Karachi':
        offset_y = -0.25
    
    plt.text(coords[1] + offset_x, coords[0] + offset_y, city, 
             ha='center', va='center', 
             fontsize=10 if city in ['Lahore', 'Islamabad', 'Karachi'] else 9, 
             fontweight='bold',
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

# Add title and adjust layout
plt.title('Pakistan Cities Road Network', fontsize=16, pad=1)
plt.axis('off')

# Add scale indicator
plt.plot([66, 67], [24, 24], 'k-', linewidth=2)
plt.text(66.5, 23.9, '≈100 km', ha='center', va='top', fontsize=9)

plt.tight_layout()
plt.show()
import random

# Define the dimensions of the village
GRID_SIZE = 10

# Define possible elements in the village
elements = ["H", "S", "T", "R"]  # H: House, S: Shop, T: Tree, R: Road

# Function to generate a random village
def generate_village(size):
    village = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.choice(elements))
        village.append(row)
    return village

# Function to display the village grid
def display_village(village):
    for row in village:
        print(" ".join(row))

# Generate and display the village
village = generate_village(GRID_SIZE)
display_village(village)
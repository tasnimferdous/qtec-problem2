import itertools
import math

def calculate_distance(coord1, coord2):
    # Calculate distance between two coordinates using Haversine formula
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # Radius of the Earth in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

def tsp(locations, start):
    n = len(locations)
    all_permutations = list(itertools.permutations(range(n)))  # Generate all possible permutations

    best_route = None
    min_distance = float('inf')

    for perm in all_permutations:
        route = [start] + list(perm) + [start]
        total_distance = 0

        for i in range(n):
            curr_location = locations[route[i]]
            next_location = locations[route[i + 1]]
            distance = calculate_distance(curr_location, next_location)
            total_distance += distance

        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route

    return best_route, min_distance

locations = [
    (23.8728568, 90.3984184), (23.8513998, 90.3944536),
    (23.8330429, 90.4092871), (23.8679743, 90.3840879),
    (23.8248293, 90.3551134), (23.827149, 90.4106238),
    (23.8629078, 90.3816318), (23.8673789, 90.429412),
    (23.8248938, 90.3549467), (23.813316, 90.4147498)
]  # Coordinates of bank branches

start_location = (23.8728568, 90.3984184)  # Starting coordinate (City Bank Uttara Branch)

best_route, min_distance = tsp(locations, start_location)

print("Optimized Route:")
for i in range(len(best_route) - 1):
    print("From:", locations[best_route[i]])
    print("To:", locations[best_route[i + 1]])
    print("Distance:", calculate_distance(locations[best_route[i]], locations[best_route[i + 1]]))
    print()

print("Total Distance:", min_distance)

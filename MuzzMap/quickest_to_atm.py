import math


def calculate_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)


def nearest_neighbor(engineer_location, locations):
    unvisited = set(locations.keys())
    path = [engineer_location]

    while unvisited:
        nearest = min(unvisited, key=lambda x: calculate_distance(
            locations[path[-1]], locations[x]))
        path.append(nearest)
        unvisited.remove(nearest)

    return path


# Example Usage:
engineer_location = 'Dundee'
atm_locations = {
    'Dundee': (56.4620, -2.9707),
    'London': (51.5099, -0.1180),
    'Cardiff': (51.4816, -3.1791),
    'Newcastle': (54.9783, -1.6174),
    'Edinburgh': (55.9533, -3.1883),
    'Aberdeen': (57.1497, -2.0943),
    'Brighton': (50.8225, -0.1372),
    'Belfast': (54.5970, -5.9300),
    'Glasgow': (55.8642, -4.2518),
    'Swansea': (51.6214, -3.9436),
    'Hull': (53.7466, -0.3384),
    'Southampton': (50.9097, -1.4044),
    'Liverpool': (53.4084, -2.9916),
    'Manchester': (53.4831, -2.2441),
    'Wooler': (55.5471, -2.0126),
    'Atlanta': (33.7490, -84.3880),
    'Toronto': (43.6532, -79.3832),
    'Accra': (5.6037, -0.1870),
    'Boston': (42.3601, -71.0589),
}

# Find the nearest neighbor path
path = nearest_neighbor(engineer_location, atm_locations)
path.pop(1)

print("Path:", path)

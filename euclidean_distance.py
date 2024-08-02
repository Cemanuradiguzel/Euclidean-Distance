import math

points = [(5, 6), (7,5), (9,3), (6,2), (8, 4)]

def euclideanDistance(points1, points2) :
  distance = 0
  for i in range(len(points1)) :
    distance += (points1[i] - points2[i])**2
  return distance**0.5

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

minDistance = min(distances)

print(f"Points: {points}")
print(f"Distances: {distances}")
print(f"Minimum distance: {minDistance}")
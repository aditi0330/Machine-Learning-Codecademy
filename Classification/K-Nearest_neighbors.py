def euclidean_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    distance += (pt1[i] - pt2[i]) ** 2
  return distance ** 0.5

def manhattan_distance(pt1, pt2):
  distance = 0
  
  for i in range(len(pt1)):
    distance += abs(pt1[i] - pt2[i])
  return distance

def hamming_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    if pt1[i] != pt2[i]:
      distance += 1
  return distance

print(hamming_distance([1, 2], [1, 100]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))

print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))

print(manhattan_distance([1, 2], [4, 0]))
print(manhattan_distance([5, 4, 3], [1, 7, 9]))

#First, the scipy implementation of Manhattan distance is called cityblock(). 
#Remember, computing Manhattan distance is like asking how many blocks away you are from a point.

#Second, the scipy implementation of Hamming distance will always return a number between 0 an 1.
# Rather than summing the number of differences in dimensions, this implementation sums those differences and then divides by the total number of dimensions.
# For example, in your implementation, the Hamming distance between [1, 2, 3] and [7, 2, -10] would be 2. In scipy‘s version, it would be 2/3.

print(distance.euclidean([1, 2], [4, 0]))
print(distance.cityblock([1, 2], [4, 0]))
print(distance.hamming([5, 4, 9], [1, 7, 9]))

# N-Fold Cross-Validation.
# K-Nearest Neighbors (KNN) is a classification algorithm. 
# The central idea is that data points with similar attributes tend to fall into similar categories.
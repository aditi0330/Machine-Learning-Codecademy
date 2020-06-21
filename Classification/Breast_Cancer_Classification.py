import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt

breast_cancer_data = load_breast_cancer()
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)

print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

#Call the train_test_split function. It takes several parameters:

#The data you want to split (for us breast_cancer_data.data)
#The labels associated with that data (for us, breast_cancer_data.target).
#The test_size. This is what percentage of your data you want to be in your testing set. Let’s use test_size = 0.2
#random_state. This will ensure that every time you run your code, the data is split in the same way. This can be any number. We used random_state = 100.

training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

print(len(training_data))
print(len(training_labels))

classifier = KNeighborsClassifier (n_neighbors = 3)
classifier.fit(training_data, training_labels)

print(classifier.score(validation_data, validation_labels))

#Put the previous 3 lines of code inside a for loop. The loop should have a variable named k that starts at 1 and increases to 100

#You should now see 100 different validation accuracies print out.

for k in range(1, 101):
  classifier = KNeighborsClassifier (n_neighbors = k)
  classifier.fit(training_data, training_labels)
  accuracies = []
  accuracies.append(classifier.score(validation_data, validation_labels)
  print(classifier.score(validation_data, validation_labels)

k_list = list(range(1, 101))

plt.plot(k_list, accuracies)
plt.xlabel("K")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")

plt.show()


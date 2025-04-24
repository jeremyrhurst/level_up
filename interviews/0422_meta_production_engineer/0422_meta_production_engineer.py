'''
You have been given two data files in CSV format, each of which contains specific statistics about various dinosaurs.
Using this formula to calculate the speeds of the dinosaurs found in the two-files:
speed ((STRIDE LENGTH / LEG LENGTH) - 1) * SQRT(LEG LENGTH 9.6)
write a program that will:
1. Take the paths of the two files as inputs
2. Parse the files
3. Calculate the speeds of the dinosaurs
4. Print only the names of the bipedal dinosaurs, ordered from fastest to slowest
The data files that you are given appear as follows:

 $ cat dataseti.csv
NAME, LEG LENGTH, DIET
Hadrosaurus, 1.2.herbivore
Struthiominus,0.92.omnivore
Velociraptor, 1.0, carnivore
Triceratops, 0.87, herbivore
Euoplocephalus, 1.6, herbivore
Stegosaurus, 1.40, herbivore
Tyrannosaurus Rex, 2.5, carnivore

$ cat dataset2.csv
NAME, STRIDE LENGTH, STANCE
Euoplocephalus, 1.87, quadrupedal
Stegosaurus, 1.90, quadrupedal
Tyrannosaurus Rex, 5.76, bipedal
Hadrosaurus, 1.4, bipedal
Deinonychus, 1.21, hipedal
Struthiomieus, 1.34,bipedal
Velociraptor, 2.72, bipedal
'''

dinos = {}

with open ('dataset2.csv', "r") as file:
    dataset2 = file.readlines()
    for line in dataset2[1:]:
        name, stride_length, stance = line.strip().split(",")
        if stance == "bipedal":
            name = name.strip()
            stride_length = float(stride_length.strip())
            stance = stance.strip()
            dinos[name] = {"stride_length": stride_length, "stance": stance}

with open ('dataset1.csv', "r") as file:
    dataset1 = file.readlines()
    for line in dataset1[1:]:
        name, leg_length, diet = line.strip().split(",")
        name = name.strip()
        if name in dinos:
            leg_length = float(leg_length.strip())
            diet = diet.strip()
            dinos[name]["leg_length"] = leg_length
            dinos[name]["diet"] = diet

for name, data in dinos.items():
    if "leg_length" not in data or "stride_length" not in data:
        continue
    stride_length = data["stride_length"]
    leg_length = data["leg_length"]
    speed = ((stride_length / leg_length) - 1) * ((leg_length * 9.6) ** 0.5)
    data["speed"] = speed

# Remove from dinos if speed is not calculated
for name in list(dinos.keys()):
    if "speed" not in dinos[name]:
        del dinos[name]
sorted_dinos = sorted(dinos.items(), key=lambda x: x[1]["speed"], reverse=True)
for name, data in sorted_dinos:
    print(name, data["speed"])

# Max heap solution:
import heapq
class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, (-item[1], item[0]))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def peek(self):
        return self.heap[0][1] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

# Create max heap and add dinos to it based on speed
max_heap = MaxHeap()
for name, data in dinos.items():
    if "speed" not in data:
        continue
    speed = data["speed"]
    max_heap.push((name, speed))

# Pop from max heap and print names in order of speed
while not max_heap.is_empty():
    name = max_heap.pop()
    print(name)
# encoding=utf8

jobs = {
    "John": "Guitar",
    "Paul": "Guitar",
    "George": "Bass",
    "Ringo": "Drums",
}
for name, job in jobs.items():
    print("{}: {}".format(name, job))

names = ["John", "Paul", "George", "Ringo"]
for index, name in enumerate(names):
    print("{}: {}".format(index, names[index]))


for i in range(1,10):
    print(i)

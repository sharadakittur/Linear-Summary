list1 = [3, "h","g", "k", "g", "k", "h", "k", 3]

def summary(lst):
  count = {}
  nlst = lst.copy() #making copy of the list
  print("In your list, there is the following:")
  for y in nlst:
    if y in count:
      count[y] += 1
    else:
      count[y] = 1
  print(count)
summary(list1)

list2 = [7, 3, 2, 3, 2, "h", "g", "h"]
summary(list2)

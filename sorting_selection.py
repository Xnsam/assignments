def selection_sort(l):
  """Function to sort the list using selection sort."""
  for i in range(len(l) - 1, 0, -1):
    max_j = i
    for j in range(max_j):
      if l[j] > l[max_j]:
        max_j = j
    l[i], l[max_j] = l[max_j], l[i]
  return l

print(selection_sort([1, 9, 10, 2, 55, 7, 1, 3]))

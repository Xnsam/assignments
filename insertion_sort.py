def insertion_sort(l):
  """Function to sort the list using insertion sort."""
  for i in range(len(l)):
    j = i
    while j > 0  and l[j - 1] > l[j]:
      l[j - 1], l[j] = l[j], l[j - 1]
      j -= 1
  return l

print(insertion_sort([1, 9, 10, 2, 55, 7, 1, 3]))

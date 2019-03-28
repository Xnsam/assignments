def gnome_sort(l):
  """Function to sort the list using gnome sort."""
  i = 0
  while i < len(l):
    if i ==0 or l[i - 1] <= l[i]:
      i += 1
    else:
      l[i], l[i - 1] = l[i - 1], l[i]
      i -= 1
  return l

print(gnome_sort([1, 9, 10, 2, 55, 7, 1, 3]))

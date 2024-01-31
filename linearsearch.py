list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linearsearch(arr, num):
  for x in arr:
    if x == num:
      print(f'Yes, {arr.index(num)}')
      break
    else:
      continue

linearsearch(list, 4)
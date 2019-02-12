products = {
  'A': [1, 3, 5],
  'B': [3, 4, 6],
  'C': [3, 4],
  'D': [2],
  'E': [3, 4, 1, 5]
}

def jaccard(a, b):
  set_a = set(a)
  set_b = set(b)

  return float(len(set_a & set_b)) / float(len(set_a | set_b))

result = {}

for p1 in products:
  result[p1] = {}

  for p2 in products:
    if p1 == p2:
      continue
    result[p1][p2] = jaccard(products[p1], products[p2])

for p in products:
  print(p, ":", dict(sorted(result[p].items(), key=lambda x: x[1], reverse=True)))

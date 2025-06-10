def count_words(text):
  return len(text.split())

def count_characters(text):
  map = {}

  for char in text:
    charLower = char.lower()
    if charLower not in map:
      map[charLower] = 1
    else:
      map[charLower] += 1

  return map

def sorting_func(e):
  return e['num']

def create_list(dictionary):
  res = []
  for key, value in dictionary.items():
    res.append({'char': key, 'num': value})

  res.sort(key=sorting_func, reverse=True)

  return res


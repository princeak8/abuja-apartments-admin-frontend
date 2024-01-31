def decode(message_file):
  f = open(message_file, "r")
  listOfFileItems = []
  listOfNumbers = []
  for x in f:
    item_list = x.split()
    listOfFileItems.append(item_list)
    listOfNumbers.append(int(item_list[0]))
  listOfNumbers.sort()
  step = 1
  subsets = []
  while listOfNumbers:
    subsets.append(listOfNumbers[:step])
    listOfNumbers = listOfNumbers[step:]
    step = step + 1
    
  lastItems = []
  for i in subsets:
    item = i[len(i) - 1]
    lastItems.append(item)
  print(lastItems)
  
  textList = []
  for fileLine in listOfFileItems:
    if int(fileLine[0]) in lastItems:
      textList.append(fileLine[1])

  return " ".join(textList)

str = decode("coding_qual_input.txt")
print(str)
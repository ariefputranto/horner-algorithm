def horner(data):
  splitedData = data.split(' ')
  removedOperandData = removedOperand(splitedData)
  convertedDegree = convertToDegree(removedOperandData)
  print(convertedDegree)
  
  getLowestDegree = min(convertedDegree[1])
  getLowestIndex = convertedDegree[1].index(getLowestDegree)
  getLowestX = convertedDegree[0][getLowestIndex]
  print(getLowestX)
  
  constanta = findConstanta(getLowestX)
  print(constanta)
  print('-----------')
  
  calculatedHorner = calculateHorner(convertedDegree[0], convertedDegree[1], constanta) 
  print('-----------')
  
  return calculatedHorner
  
  
def calculateHorner(listValue, listDegree, listConstanta, listX = []):
  for cons in listConstanta:
    calc = calculateNumber(cons, listValue)
    if calc[len(calc) - 1] == 0:
      listValue = cleanupValue(calc)
      listDegree = downgradeDegree(listDegree)
      
      getLowestDegree = min(listDegree)
      getLowestIndex = listDegree.index(getLowestDegree)
      getLowestX = listValue[getLowestIndex]
      
      listConstanta = findConstanta(getLowestX)
      
      listX.append(cons)
      calculateHorner(listValue, listDegree, listConstanta, listX)
      break

  return listX
  

def cleanupValue(listValue):
  newListValue = []
  for value in listValue:
    if value != 0:
      newListValue.append(value)
  return newListValue


def downgradeDegree(listDegree):
  newListDegree = []
  for degree in listDegree:
    if degree - 1 >= 0:
      newListDegree.append(degree - 1)
  return newListDegree
    
def calculateNumber(constanta, listValue):
  listCalculatedValue = []
  i = 0
  for value in listValue:
    if i == 0:
      listCalculatedValue.append(value)
    else:
      calculate = (listCalculatedValue[len(listCalculatedValue) - 1] * constanta) + value
      listCalculatedValue.append(calculate)
    
    i = i + 1
    
  print(listCalculatedValue)
  return listCalculatedValue


def findConstanta(number):
  number = abs(int(number))
  listConstanta = []
  for i in range(1, number + 1):
    if number % i == 0:
      listConstanta.append(i)
      listConstanta.append(-i)
  return listConstanta
  
  
def convertToDegree(data):
  listValue = []
  listDegree = []
  for item in data:
    try:
      index = item.index('x')
    except ValueError:
      index = -1
      
    if index >= 0:
      splitDegree = item.split('x')
      splitDegree[1] = 1 if splitDegree[1] == '' else splitDegree[1]
      splitDegree[0] = 1 if splitDegree[0] == '' else splitDegree[0]
      splitDegree[0] = -1 if splitDegree[0] == '-' else splitDegree[0]
      listDegree.append(int(splitDegree[1]))
      listValue.append(int(splitDegree[0]))
    else:
      listDegree.append(0)
      listValue.append(int(item))
  return [listValue, listDegree]
  
  
def removedOperand(data):
  listOperand = ['+', '-']
  cleanData = []
  lastOperand = ''
  for item in data:
    try:
      index = listOperand.index(item)
    except ValueError:
      index = -1
      
    if index == -1:
      if lastOperand == '-':
        cleanData.append('-' + item)
      else:
        cleanData.append(item)
    else:
      lastOperand = item
      
  return cleanData
  
  
data = 'x5 - 8x4 - 72x3 + 382x2 + 727x - 2310'
print(data)
print(horner(data))
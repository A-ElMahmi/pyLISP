import functools, string
import globals

def convertToNum(string):
  try:
    return int(string)
  except ValueError:
    return float(string)


def operation(operator, *operands):
  operands = [convertToNum(i) for i in operands]
  if len(operands) < 1: 
    raise Exception(f"Too little operands: + {operands}")
  
  if operator == "+":
    return sum(operands)
  
  elif operator == "-":
    if len(operands) > 2: 
      raise Exception(f"Too many operands: - {operands}")

    val1 = operands[0]
    val2 = operands[1] if len(operands) == 2 else 0
    return -val1 + val2
  
  elif operator == "*":
    if len(operands) < 2:
      raise Exception(f"Too little operands: * {operands}")

    return functools.reduce(lambda a, b: a * b, operands)

  elif operator == "/":
    if len(operands) != 2:
      raise Exception(f"Too many or too little operands: / {operands}")

    return operands[0] / operands[1]


def _checkName(name):
  if name in globals.builtIn:
    raise Exception(f"Invalid variable name: {name}") 
  if any([s not in string.ascii_letters for s in name]):
    raise Exception(f"Invalid variable name: {name}")

def makeVariable(variableName, value):
  _checkName(variableName)
  globals.variables[variableName] = convertToNum(value)

def makeFunction(functionName, parameters, body):
  _checkName(functionName)
  if parameters:
    for i in parameters:
      _checkName(i)
  globals.functions[functionName] = [parameters, body]
  

def compare(comparasion, value1, value2):
  value1, value2 = convertToNum(value1), convertToNum(value2)
  if comparasion == "=":
    return value1 == value2
  elif comparasion == "<":
    return value1 < value2
  elif comparasion == ">":
    return value1 > value2


def logicCompare(comparasion, boolean1, boolean2=None):
  if comparasion == "not":
    return not boolean1
  elif comparasion == "and":
    return boolean1 and boolean2
  elif comparasion == "or":
    return boolean1 or boolean2


def condition(predicates):
  for i, j in enumerate(predicates):
    if j:
      return i
  return None


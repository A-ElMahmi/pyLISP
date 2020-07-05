class Evaluate:

  def __init__(self):
    pass

  def add(self, *operands):
    if len(operands) < 1:
      raise Exception("Too small")

    return sum([int(i) for i in operands])

  def subtract(self, operand1, operand2=0):
    return -int(operand1) + int(operand2)
    
  def multiply(self, *operands):
    if len(operands) < 2:
      raise Exception("Too small")
    
    total = int(operands[0])
    for i in operands[1:]:
      total *= int(i)
    return total


  def divide(self, operand1, operand2):
    return int(operand1) / int(operand2)

  def makeVariable(variableName, value):
    pass

  def makeFunction(functionName, parameters, body):
    pass
import globals

class Tokenize:
  
  def __init__(self, codeBlock):
    self.topLevel = self.split(codeBlock)
    print(self.assignToken(self.topLevel))


  def assignToken(self, expression):
    keyword = expression[0]
    if keyword in globals.builtIn["operators"]:
      operands = expression[1:]
      for i, j in enumerate(operands):
        if j[0] == "(" and j[-1] == ")":
          operands[i] = self.assignToken(self.split(j))       

      return globals.builtIn["operators"][keyword](*operands)

    elif keyword == "define":
      if expression[1] == "(" and expression[-1] == ")":
        print("Making Funcion")

      else:
        value = expression[2]
        if value[1] == "(" and value[-1] == ")":
          value = self.assignToken(self.split(j))
        return globals.builtIn["define"]["variable"](expression[1], value)

    # elif variable named by user
    

  def split(self, expression):
    messySplit = expression[1:-1].split()
    cleanSplit = []
    pointer, parenthesesCount = 0, 0
    checkingEmbedded = False
    
    for i, j in enumerate(messySplit):
      if "(" in j or ")" in j:
        for c in [k for k in j if k == "("]:
          parenthesesCount += 1
        for d in [k for k in j if k == ")"]:
          parenthesesCount -= 1
      
      elif checkingEmbedded:
          continue

      else:
        cleanSplit.append(j)
        continue

      if parenthesesCount < 0:
        raise SyntaxError("Missing parentheses")
      
      if "(" in j and parenthesesCount == j.count("("):
        pointer = i
        checkingEmbedded = True
      if ")" in j and parenthesesCount == 0:
        embeddedExp = " ".join(messySplit[pointer : i+1])
        cleanSplit.append(embeddedExp)
        checkingEmbedded = False   

    if parenthesesCount != 0:
      raise SyntaxError("Missing parentheses")
    
    return cleanSplit
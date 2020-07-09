import re
import globals

def isNumber(s):
  return s.replace("-", "", 1).replace(".", "", 1).isdigit()

class Tokenize:
  
  def __init__(self, codeBlock):
    self.topLevel = self.split(codeBlock)
    assigned = self.assignToken(self.topLevel)
    if assigned is not None:
      print(assigned)


  def assignToken(self, expression):
    keyword = expression[0]
    if keyword in globals.builtIn["operators"]:
      operands = expression[1:]
      for i, j in enumerate(operands):
        if j[0] == "(" and j[-1] == ")":
          operands[i] = self.assignToken(self.split(j))
        elif j in globals.variables:
          operands[i] = globals.variables[j]      

      return globals.builtIn["operators"][keyword](keyword, *operands)

    elif keyword == "define":
      if expression[1][0] == "(" and expression[1][-1] == ")":
        options = self.split(expression[1])
        functionName = options[0]
        parameters = options[1:] if len(options) > 1 else []
        body = " ".join(expression[2:])
        
        return globals.builtIn["define"]["function"](functionName, parameters, body)

      else:
        value = expression[2]
        if value[0] == "(" and value[-1] == ")":
          value = self.assignToken(self.split(value))
        elif value in globals.variables:
          value = globals.variables[value]
        
        return globals.builtIn["define"]["variable"](expression[1], value)

    elif keyword in globals.builtIn["comparasions"]:
      for i, j in enumerate(expression[1:]):
        if j[0] == "(" and j[-1] == ")":
          expression[i+1] = self.assignToken(self.split(j))
        elif j in globals.variables:
          expression[i+1] = globals.variables[j]

      return globals.builtIn["comparasions"][keyword](keyword, *expression[1:])

    elif keyword in globals.builtIn["logic comparasions"]:
      for i, j in enumerate(expression[1:]):
        if j[0] == "(" and j[-1] == ")":
          expression[i+1] = self.assignToken(self.split(j))
        elif j in globals.variables:
          expression[i+1] = globals.variables[j]

      return globals.builtIn["logic comparasions"][keyword](keyword, *expression[1:])

    elif keyword in globals.functions:
      parameters, body = globals.functions[keyword]
      arguments = expression[1:]

      for i, j in enumerate(arguments):
        if j[0] == "(" and j[-1] == ")":
          arguments[i] = self.assignToken(self.split(j))
      
      for i, j in zip(parameters, arguments):
        body = self.splitFuncArgs(body, i, j)

      return self.assignToken(self.split(body))
      
    elif keyword == "cond":
      predicates, expressions, elseClause = [], [], None
      for e in expression[1:]:
        clause = self.split(e)

        if clause[0] == "else":
          elseClause = " ".join(clause[1:])
        else:
          predicates.append(self.assignToken(self.split(clause[0])))
          expressions.append(" ".join(clause[1:]))

      executeExp = globals.builtIn["cond"](predicates)

      if executeExp is None:
        if elseClause:
          return self.assignToken(self.split(elseClause))
        return

      return self.assignToken(self.split(expressions[executeExp]))
      
    elif keyword == "if":
      predicate = [self.assignToken(self.split(expression[1]))]
      expressions = expression[2:]
      executeExp = globals.builtIn["cond"](predicate)

      if executeExp is None:
        return self.assignToken(self.split(expressions[-1]))
        
      return self.assignToken(self.split(expressions[executeExp]))
      
    elif keyword in globals.variables:
      return globals.variables[keyword]

    elif isNumber(keyword):
      return keyword

    else:
      raise Exception(f"Invalid keyword: {keyword}")
    

  def split(self, expression):
    if expression in globals.variables or isNumber(expression):
      return [expression]
    
    messySplit = expression[1:-1].split()
    cleanSplit = []
    pointer, parenthesesCount = 0, 0
    checkingEmbedded = False

    for i, j in enumerate(messySplit):
      if "(" in j or ")" in j:
        possibleCompleteParentheses = False
        if parenthesesCount == 0:
          possibleCompleteParentheses = True

        for c in [k for k in j if k == "("]:
          parenthesesCount += 1
        for d in [k for k in j if k == ")"]:
          parenthesesCount -= 1

        if possibleCompleteParentheses and parenthesesCount == 0:
          cleanSplit.append(j)
          continue
      
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


  def splitFuncArgs(self, body, old, new):
    start, end = [], []
    for e in re.finditer(rf"\b{old}\b", body):
      start.append(e.start())
      end.append(e.end())

    if len(start) == 0:
      return body

    newBody = ""
    for i in range(len(start)):
      if i == 0 and i == len(start)-1:
        newBody += body[:start[i]] + str(new) + body[end[i]:]
        continue
      elif i == 0:
        newBody += body[:start[i]] + str(new) + body[end[i] : start[i+1]]
        continue
      elif i == len(start)-1:
        newBody += str(new) + body[end[i]:]
        continue

      newBody += str(new) + body[end[i] : start[i+1]]

    return newBody

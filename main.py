FILENAME = "test.txt"
codeLines = []

def findBrackets(string, index):
  bracketCount = 0
  for i, j in enumerate(string[index:]):
    if j == ")" and bracketCount == 0:
      return i + index
    
    if j == "(":
      bracketCount += 1
    elif j == ")":
      bracketCount -= 1
  raise SyntaxError("Missing right parentheses")

with open(FILENAME) as f:
  data = f.read()
  skipToIndex = 0
  for i, j in enumerate(data):
    if i < skipToIndex:
      continue

    if j == "(":
      nextBracket = findBrackets(data, i+1)
      codeLines.append(data[i : nextBracket+1])
      skipToIndex = nextBracket + 1


def add(*args):
  return sum(args)

commands = {
  "+": add
}

for line in codeLines:
  while "(" in line:
    index = line.find("(")
    EVALUATE: line[index : findBrackets(line, index+1)
    
  expressions = line.split()


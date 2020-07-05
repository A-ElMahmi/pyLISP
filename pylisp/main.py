from tokenizer import Tokenize

FILENAME = "../test.txt"

def splitCodeBlocks(fileData):
  codeBlocks = []
  pointer, parenthesesCount = 0, 0
  for i, j in enumerate(fileData):
    if j == "(":
      parenthesesCount += 1
    elif j == ")":
      parenthesesCount -= 1

    if parenthesesCount < 0:
      raise SyntaxError("Missing parentheses")
    
    if j == "(" and parenthesesCount == 1:
      pointer = i
    if j == ")" and parenthesesCount == 0:
      codeBlocks.append(fileData[pointer : i+1])

  if parenthesesCount != 0:
      raise SyntaxError("Missing parentheses")

  return codeBlocks


with open(FILENAME) as f:
  codeBlocks = splitCodeBlocks(f.read().strip())

for block in codeBlocks:
  Tokenize(block)
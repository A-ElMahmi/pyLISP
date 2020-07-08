import evaluate

builtIn = {
  "operators": {
    "+": evaluate.operation, 
    "-": evaluate.operation, 
    "*": evaluate.operation, 
    "/": evaluate.operation, 
  },

  "comparasions": {
    "=": evaluate.compare,
    "<": evaluate.compare,
    ">": evaluate.compare,
  },
  
  "logic comparasions": {
    "not": evaluate.logicCompare,
    "and": evaluate.logicCompare,
    "or": evaluate.logicCompare,
  },
  
  "define": {
    "variable": evaluate.makeVariable,
    "function": evaluate.makeFunction
  },

  "cond": evaluate.condition
}

variables = {}

functions = {}
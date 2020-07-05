from evaluate import Evaluate

builtIn = {
  "operators": {
    "+": Evaluate().add,
    "-": Evaluate().subtract,
    "*": Evaluate().multiply,
    "/": Evaluate().divide
  },
  "define": {
    "variable": Evaluate().makeVariable,
    "function": Evaluate().makeFunction
  }
}
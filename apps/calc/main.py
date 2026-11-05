import ast
import operator
import sys

sys.path.append("../..")
from api import Terminal as t

variables = {}
history = []

operators = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow, ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


def usage():
    t.write("""aysCalc - Calculator

Argument mode:
  calc.app expression
  Example: calc.app 5 + 3

Interactive mode:
  calc.app interactive

Commands: help, history, exit""")


def help_command():
    t.write("""aysCalc - Help

Arithmetic:
  +  Addition
  -  Subtraction
  *  Multiplication
  /  Division
  ** Exponents

Parentheses:
  (5 + 3) * 2

Variables:
  x = 25
  x * 2

Commands:
  help     Show this help
  history  Show calculations
  exit     Quit interactive mode""")


def evaluate_node(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return node.value
        raise ValueError("unsupported value")

    elif isinstance(node, ast.Name):
        if node.id not in variables:
            raise ValueError(f"unknown variable: {node.id}")
        return variables[node.id]

    elif isinstance(node, (ast.BinOp, ast.UnaryOp)):
        operation = operators.get(type(node.op))
        if operation is None:
            raise ValueError("unsupported operator")

        if isinstance(node, ast.BinOp):
            return operation(evaluate_node(node.left), evaluate_node(node.right))

        return operation(evaluate_node(node.operand))

    raise ValueError("unsupported expression")


def calculate(expression):
    try:
        return evaluate_node(ast.parse(expression, mode="eval").body)
    except ZeroDivisionError:
        t.error("error: division by zero")
    except (ValueError, OverflowError):
        t.error("error: invalid expression or value")
    except SyntaxError:
        t.error("error: invalid expression")


def process_expression(expression):
    expression = expression.strip()

    if "=" in expression:
        if expression.count("=") != 1:
            t.error("error: invalid assignment")
            return

        name, value = map(str.strip, expression.split("=", 1))

        if not name.isidentifier():
            t.error("error: invalid variable name")
            return
        if not value:
            t.error("error: missing value")
            return

        result = calculate(value)
        if result is not None:
            variables[name] = result
            history.append(f"{expression} = {result}")
            t.write(f"{name} = {result}")
        return

    result = calculate(expression)
    if result is not None:
        history.append(f"{expression} = {result}")
        t.write(f"result: {result}")


def show_history():
    t.write(
        "Calculation history:\n" + "\n".join(
            f"  {i}. {entry}" for i, entry in enumerate(history, 1)
        ) if history else "No calculations yet."
    )


def interactive():
    t.write("aysCalc\nType 'help' for commands.\n")

    while True:
        expression = t.ask("calc>")

        if expression.lower() == "exit":
            break
        elif expression.lower() == "help":
            help_command()
        elif expression.lower() == "history":
            show_history()
        elif expression:
            process_expression(expression)


def main(dictionary):
    values = dictionary["args"]

    if not values:
        usage()
    elif values[0].lower() == "interactive":
        if len(values) == 1:
            interactive()
        else:
            usage()
    else:
        process_expression(" ".join(values))


if __name__ == "__main__":
    import json

    t.write("DEVELOPER MODE ACTIVE\ncalculator")
    usage()
    main(json.loads(t.ask("enter a dictionary: ")))
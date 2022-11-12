import re


exp = ["2+2", "1+2*3", "1-2*3", "1+2*3", "(1+2)*3"]
actions = {
    "*": lambda x, y: str(int(x) * int(y)),
    "/": lambda x, y: str(int(x) / int(y)),
    "+": lambda x, y: str(int(x) + int(y)),
    "-": lambda x, y: str(int(x) - int(y))
}
priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

def my_eval(expresion: str) -> str:
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
    return expresion


def main(a):
    for i in a:
        result = my_eval(i)
        print(f"{i} => {result}")

if __name__ == '__main__':
    main(exp)


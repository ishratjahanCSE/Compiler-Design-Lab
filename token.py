import re

text = "this is a int sum = 10; and a + b = 20"

# Define keywords
keywords = {"is", "int", "and"}

# Tokenize
tokens = re.findall(r'[a-zA-Z_]\w*|\d+|[=+;]', text)

# Classify and print
for token in tokens:
    if token in keywords:
        print(f"{token} -> Keyword")
    elif re.match(r'^\d+$', token):
        print(f"{token} -> Literal")
    elif token in {"=", "+"}:
        print(f"{token} -> Operator")
    elif token == ";":
        print(f"{token} -> Separator")
    else:
        print(f"{token} -> Identifier")



s = "dot net perls"

# Use the in-operator.
if "dot" in s:
    print("dot")

if "perls" in s:
    print("perls")

if " " in s:
    print("space")

if "D" in s:
    # Not reached, case matters.
    print("D")

if "lycurgus" in s:
    # Not reached.
    print("lycurgus")

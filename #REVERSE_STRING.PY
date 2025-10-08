#REVERSE_STRING.PY
def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == "__main__":
    inp = "Microsoft"
    print("input :", inp)
    print("Reversed :", reverse_string(inp))

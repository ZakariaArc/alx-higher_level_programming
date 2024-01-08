#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    aliases = dir(hidden_4)
    for alias in aliases:
        if not alias.startswith("__"):
            print(alias)

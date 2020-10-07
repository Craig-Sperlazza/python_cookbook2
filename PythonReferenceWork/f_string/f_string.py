name = "Craig"

age = 38

print(f"Hello, {name}. You are {age}")


# can call functions in f strings
def to_lower(str):
    return str.lower()


print(f"{to_lower(name)} is cool.")


def to_upper(str):
    return str.upper()


print(f"Hello {to_upper(name)}, this is your name in caps.")


# can also call the method directly
print(f"Hello caps name: {name.lower()}")

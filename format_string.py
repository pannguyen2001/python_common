"""
Format string to make beautiful print output
"""

# Apply :^ to center, :< to left, :> to right, add */-/= for replace spaces
string_01: str = "Hello"
print("{:=^20}".format(f" {string_01} "))  # ====== Hello =======

# use Template for many line string
from string import Template

template = Template("""Hello.
My name is ${name}.
I am ${age} years old.
""")
print(template.safe_substitute(name="John", age=25))
"""Hello.
My name is John.
I am 25 years old."""

# use f"{variable = }" to print variable name and value
name: str = __name__
print(f"{name = }")  #   name = "__main__"

# Use json.dumps for beautify object
import json

dict_data: dict = {"id": 1, "name": "John", "age": 25, "job": "unknown"}
print(json.dumps(dict_data, indent=4))
"""
{
    "id": 1,
    "name": "John",
    "age": 25,
    "job": "unknown"
}
"""

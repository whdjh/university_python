input_str = "a:b:c:d"

pass

output_str = input_str.replace(":", "#")

assert output_str == "a#b#c#d"
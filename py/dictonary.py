di = {"name":"AHad","age":23,"class":43}

print(di)
print(di["name"])

print(di.keys())

print(di.values())

print(di.items())

for key in (di):
    print(f"The value for {key} is {di[key]}")

di["wow"]="Added one more"
print(di)

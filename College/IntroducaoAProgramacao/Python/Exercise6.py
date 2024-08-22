def check_type(datum):
    match datum:
        case str(datum):
            print("String:", datum)    
        case int(datum):
            print("Integer:", datum)
        case float(datum):
            print("Float:", datum)
        case _:
            print("Unrecognized data.")

data = ["Python", 53, 2.14, 23, "C"]

for datum in data:
    check_type(datum)


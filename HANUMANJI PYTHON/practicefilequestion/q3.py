def multiply(n):
    table=" "
    for i in range(1,11):
        table+=f"{n}*{i}={n*i}\n"


    with open(f"practicefilequestion/table/table_{n}","w") as f:
        f.write(table)
for n in range(2,32):
    multiply(n)

    
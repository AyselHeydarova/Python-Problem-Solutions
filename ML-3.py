inputText = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# inputText = open('test3.txt').read()

result = 0
do = True

for start in range(0, len(inputText)):
    for shift in range(13):
        extract = inputText[start: start + shift]

        if extract == 'do()':
            do = True
        if extract == "don't()":
            do = False

        if do and extract.startswith('mul(') and  extract.endswith(")"):
            args = extract[4:-1]

            try:
                a, b = args.split(",")
                a = int(a)
                b = int(b)

                result += a * b
            except:
                pass

print("result", result)



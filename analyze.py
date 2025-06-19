import os

files = os.listdir('./src')

for file in files:
    if not file.endswith('.py'):
        continue  

    path = './src/' + file
    violations = 0
    keywords = 0

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            if len(line) > 80:
                violations += 1

            if '#' in line:
                line = line.split('#')[0]

            if 'print' in line or 'eval' in line or 'exec' in line:
                keywords += 1

            if line.count('"') % 2 == 1 or line.count("'") % 2 == 1:
                violations += 1

    if violations == 0 and keywords == 0:
        result = "CLEAN"
    elif violations <= 5 and keywords == 0:
        result = "LOW RISK"
    else:
        result = "HIGH RISK"

    print('/src/' + file + ' : ' + result)
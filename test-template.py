with open('scratch/short.json', mode='r', encoding='utf-8', errors='ignore') as f:
    json = ' '.join(f.readlines())

from libzk2setevi.setevi_template import template
lines = template.split('\n')

output_lines = []
for line in lines:
    if '/*GENERATED JSON*/' in line:
        line = line.replace('/*GENERATED JSON*/', json)
    output_lines.append(line)

with open('output/out.html', mode='w', encoding='utf-8') as f:
    for line in output_lines:
        f.write(line + '\n')

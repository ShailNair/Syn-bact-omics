import sys

columns = []
data = {}
ids = set()
for filename in sys.argv[1:]:
    with open(filename, 'rU') as f:
        key = next(f).strip().split()[1]
        columns.append(key)
        data[key] = {}
        for line in f:
            if line.strip():
                KO, Metag = line.strip().split()
                try:
                    data[key][int(id)] = Metag
                except ValueError as exc:
                    raise ValueError(
                        "Problem in line: '{}' '{}' '{}'".format(
                            KO, Metag, line.rstrip()))

                ids.add(int(id))

print('\t'.join(['ID'] + columns))

for id in sorted(ids):
    line = []
    for column in columns:
        line.append(data[column].get(id, '0'))
    print('\t'.join([str(id)] + line))
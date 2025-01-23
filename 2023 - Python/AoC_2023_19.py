from timeit import default_timer as timer
from functools import reduce
from operator import mul

def part_result(x, m, a, s, workflow_dict):
    """
    Determine if part is accepted or rejected
    """

    workflow = 'in'

    while True:
        rules = workflow_dict[workflow]

        for rule in rules:
            if rule in ('A', 'R'):
                return rule
            if isinstance(rule, str):
                workflow = rule
                break

            if rule[0]=='x':
                var = x
            elif rule[0]=='m':
                var = m
            elif rule[0]=='a':
                var = a
            else:
                var = s

            if rule[1]=='>':
                workflow = rule[3] if var>int(rule[2]) else -1
            else:
                workflow = rule[3] if var<int(rule[2]) else -1

            if workflow in ('A', 'R'):
                return workflow
            if isinstance(workflow, str):
                break

def ranges_acceptance(ranges, workflow):
    """
    Determine which ranges of inputs will be accepted and rejected
    """

    num_combs = 0

    rules = workflow_dict[workflow]

    for rule in rules:
        if rule in ('A', 'R'):
            num_combs += reduce(mul, (b-a+1 for a, b in ranges)) if rule=='A' else 0
            break
        if isinstance(rule, str):
            num_combs += ranges_acceptance(ranges, rule)
            break

        r_idx = order_dict[rule[0]]
        comp, val, workflow  = rule[1], int(rule[2]), rule[3]

        if comp=='>':
            ranges_low = tuple((a, b) if i!=r_idx else (a, val) for i, (a, b) in enumerate(ranges))
            ranges_high = tuple((a, b) if i!=r_idx else (val+1, b) for i, (a, b) in enumerate(ranges))
            if workflow in ('A', 'R'):
                num_combs += reduce(mul, (b-a+1 for a, b in ranges_high)) if workflow=='A' else 0
            else:
                num_combs += ranges_acceptance(ranges_high, workflow)
            ranges = ranges_low
        else:
            ranges_low = tuple((a, b) if i!=r_idx else (a, val-1) for i, (a, b) in enumerate(ranges))
            ranges_high = tuple((a, b) if i!=r_idx else (val, b) for i, (a, b) in enumerate(ranges))
            if workflow in ('A', 'R'):
                num_combs += reduce(mul, (b-a+1 for a, b in ranges_low)) if workflow=='A' else 0
            else:
                num_combs += ranges_acceptance(ranges_low, workflow)
            ranges = ranges_high

    return num_combs

start_time_1 = timer()

TEST_NAME = 'Tests/Test_2023_19.txt'
INPUT_NAME = 'Inputs/Input_2023_19.txt'

with open(INPUT_NAME, encoding='utf-8') as file:
    file_lines = file.read().splitlines()

workflow_dict = {}

for line_num, line in enumerate(file_lines):
    if line=='':
        empty_line_num = line_num
        break

    line = line.split('{')
    workflow = line[0]

    line = line[1].split(',')

    rules = []
    for rule in line:
        if '}' in rule:
            rules.append((rule[:-1]))
            break
        rule = rule.split(':')
        rules.append((rule[0][0], rule[0][1], rule[0][2:], rule[1]))

    rules = tuple(rules)
    workflow_dict[workflow] = rules

ans1 = 0

for i in range(empty_line_num + 1, len(file_lines)):
    vals = file_lines[i].split(',')

    x, m, a, s = [int(vals[idx].split('=')[1]) if idx<3 else int(
                                vals[idx].split('=')[1][:-1]) for idx in range(4)]

    if part_result(x, m, a, s, workflow_dict)=='A':
        ans1 += x + m + a + s

end_time_1 = timer()

print(ans1)
print(f'Time elapsed: {end_time_1 - start_time_1:.6f} s')

# Part II

start_time_2 = timer()

order_dict = {'x': 0, 'm': 1, 'a': 2, 's': 3}

initial_ranges = tuple((1, 4000) for _ in range(4))

ans2 = ranges_acceptance(initial_ranges, 'in')

end_time_2 = timer()

print(ans2)
print(f'Time elapsed: {end_time_2 - start_time_2:.6f} s')

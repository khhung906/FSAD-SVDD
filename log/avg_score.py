import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--file', default='result.txt')
args = parser.parse_args()

f = open(args.file, "r")

acc = 0
cnt = 0

for x in f:
    if 'Det' in x:
        cnt += 1
        acc += float(x.split()[25])



print(f'avg auc score: {acc / cnt}')
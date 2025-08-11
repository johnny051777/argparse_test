import argparse

parser = argparse.ArgumentParser()

parser.add_argument("base",type=int,help="第一個數字")
parser.add_argument("-add",type=int,nargs="+",help="負責加法",dest="A")  ->nargs為+時，自動回傳一個list
parser.add_argument("-sub",type=int,help="負責減法")
parser.add_argument("-mul",type=int,help="負責乘法")
parser.add_argument("-div",type=int,help="負責除法")

args = parser.parse_args()

result = args.base

if args.A:
    result += sum(args.A)
if args.sub:
    result -= args.sub
if args.mul:
    result *= args.mul
if args.div:
    result /= args.div


print(result)

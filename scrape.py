import argparse
from PostFetcher import PostFetcher
from itertools import takewhile
from durationutil.parser import parse
import time
from sys import stderr


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("subreddit", type=str)
arg_parser.add_argument("--age", "-a", default="1h")

args = arg_parser.parse_args()

try:
    age = parse(args.age)
except:
    print("invalid value for --age", file=stderr)
    exit(1)

age_limit = int(time.time()) - age

pf = PostFetcher(args.subreddit)

for post in takewhile(lambda p: int(float(p.time)) > age_limit, pf):
    print(post)


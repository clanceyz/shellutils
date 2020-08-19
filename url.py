import argparse
import requests.utils

def cmd_encode(args):
    print(requests.utils.requote_uri(args.url))

def cmd_decode(args):
    print(requests.utils.unquote(args.url))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers()

    subcmd = subparsers.add_parser('encode', help='encode', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subcmd.add_argument('url')
    subcmd.set_defaults(func=cmd_encode)

    subcmd = subparsers.add_parser('decode', help='decode', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subcmd.add_argument('url')
    subcmd.set_defaults(func=cmd_decode)

    args = parser.parse_args()
    if not args.__dict__:
        parser.print_help()
        exit(1)
    exit(args.func(args))

import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--V0', type=float, default=1.0,
                        help='Berapa Kecepatan Awal?')
    parser.add_argument('--a', type=float, default=1.0,
                        help='Berapa Akselerasi Awal?')
    parser.add_argument('--t', type=float, default=1.0,
                        help='Berapa Waktu yang dibutuhkan?')
    parser.add_argument('--rumus', type=str, default='Vt',
                        help='Rumus apa yang akan digunakan?')
    args = parser.parse_args()
    sys.stdout.write(str(rumus(args)))

def rumus(args):
    if args.rumus == 'Vt':
        Vt = args.V0 + (args.a*args.t)
        return Vt
    elif args.rumus == 's':
        s = (args.V0*args.t) + ((args.a*(args.t**2))/2)
        return s

if __name__ == '__main__':
    main()
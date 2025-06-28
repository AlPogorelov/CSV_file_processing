import argparse

from src.csv_aggregate import csv_aggregate
from src.open_csv import open_csv
from src.tabuleta import print_tabl
from src.where_csv import where_csv

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        required=True,
                        help='Путь до файла')

    parser.add_argument('-w', '--where',
                        help='Условие фильтрации')

    parser.add_argument('-agg', '--aggregate',
                        help='Условие фильтрации')

    args = parser.parse_args()

    if args.file:
        dict_ = open_csv(args.file)

        if args.where:
            dict_ = where_csv(dict_, args.where)

        if args.aggregate:
            dict_ = csv_aggregate(dict_, args.aggregate)

    print_tabl(dict_)

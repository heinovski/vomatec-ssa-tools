#!/usr/bin/env python3

# Copyright (c) 2016 Julian Heinovski <mail@julian-heinovski.de>
# This script takes an element database in xml formatand and creates a corresponding txt file for SSA.

import argparse
import xml.etree.ElementTree as ET


parser = argparse.ArgumentParser()
parser.add_argument("source", help="the source xml file name")
parser.add_argument("--destination", help="the destination file name")
parser.add_argument("--version", action="version", version="%(prog)s version 0.1")

args = parser.parse_args()

tree = ET.parse(args.source)
root = tree.getroot()

destination_filename = args.destination if args.destination else args.source[0:len(args.source)-4] + ".txt"

with open(destination_filename, "w") as f:

    f.write("Stoff\t|UN\t|CAS\t|Molmasse\t|Grenzwert\t|Geruchsschwelle\t|Hinweis")

    for element in root:
        name = str(element[0].text)
        try:
            un = int(element[1].text)
        except ValueError:
            un = r"-"
        try:
            cas = str(element[2].text)
        except ValueError:
            cas = r"-"
        try:
            mol = float(element[3].text)
        except ValueError:
            mol = r"-"
        try:
            limit = float(element[4].text.replace(" ppm", ""))
        except ValueError:
            limit = r"-"
        try:
            threshold = float(element[5].text)
        except ValueError:
            threshold = r"-"
        comment = r"-" #TODO

        f.write("\n{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}".format(name, un, cas, mol, limit, threshold, comment))
        print("Wrote " + name)

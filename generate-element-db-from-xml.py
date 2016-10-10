#!/usr/bin/env python3

# Copyright (c) 2016 Julian Heinovski <mail@julian-heinovski.de>
# This script takes an element database in xml formatand and creates a corresponding txt file for SSA.

import argparse
import xml.etree.ElementTree as ET

def read(filename):
    return ET.parse(filename)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")

    args = parser.parse_args()

    root = read(args.filename)

if __name__ == "__main__":
    main()

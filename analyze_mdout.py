import os
import argparse
import glob
import matplotlib.pyplot as plt

# Get filename from argparse

parser = argparse.ArgumentParser("This script parses amber mdout file to extract the total energy.")

parser.add_argument("path", help="The filepath of the file to be analyzed.", nargs='*')

# store_true makes this True by default
parser.add_argument("make_plots", help="Flag to create plots", action='store_true')

args = parser.parse_args()

filenames = glob.glob(args.path)

for filename in filenames:

    # Figure out the file name for writing output
    fname = os.path.basename(filename).split('.')[0]

   # Open the file.

    f = open(filename, 'r')

   # Read the data.
    data = f.readlines()

   # Close the file.
    f.close()

    etot = []
   # Loop through lines in the file.
    for line in data:
        # Get information from lines.
        split_line = line.split()

        if 'Etot' in line:
            #print(split_line[2])
            etot.append(f'{split_line[2]}')
    values = etot[:-2]

    # Open a file for writing
    outfile_location = F'{fname}_Etot.txt'
    outfile = open(outfile_location, 'w+')

    for value in values:
        outfile.write(f'{value}\n')

    outfile.close()
   
    if args.make_plots == True:
        plt.figure()
        plt.plot(values)
        plt.savefig(F'{fname}.png')
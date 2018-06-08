import spikepost.parsers
from collections import Counter
import sqlite3

conn = sqlite3.connect('set.db')
print "Opened database successfully";

'''Histogram post-processing module'''

help_message = '{:<20s} {:<10s}'.format('hist_instr', 'Histogram of instructions')

def compute(input_file, args):
    '''Compute the histogram'''
    cnt = Counter()
    total_insts = 0
    j=0
    output_size = None if args.output_size is None else args.output_size
    addr_min = None if args.addr_min is None else args.addr_min
    addr_max = None if args.addr_max is None else args.addr_max
  
    with open(input_file) as fp:
        for line in fp:
            addr = spikepost.parsers.extractAddress(line)

            if addr_min is not None and addr < addr_min:
                continue
            if addr_max is not None and addr > addr_max:
                break

            inst = spikepost.parsers.parseInstruction(line)

            if inst.instr_name is not None:
                cnt[inst.instr_name] += 1
                total_insts += 1

    print("Histogram of Instructions\n")
    print("  Total number of instructions: {0:d}\n".format(total_insts))
    print("  {0:<10s} {1:<10s} {2:<10s}".format("Name", "Frequency", "Percentage"))
    print("  -------------------------------------")

    for inst in cnt.most_common(output_size):
       print("  {0:<10s} {1:<10} {2:<10.2f}".format(inst[0], inst[1], 100*inst[1]/total_insts))
       conn.execute("INSERT INTO INSTR (NAME,FREQ) \
             VALUES (?, ?)",(inst[0], inst[1]));
       conn.commit()
       
    print "the table inst(sb.s)";
    cursor = conn.execute("SELECT name, freq from INSTR")
    for row in cursor:
        print "NAME = ", row[0]
        print "FREQ = ", row[1], "\n"

    print "Operation done successfully";

    conn.close() 

import pandas as pd
import utils
import intrepyd
import intrepyd.tools as it
import intrepyd.atg.mcdc as mcdc

def doMain():
    ctx = intrepyd.Context()
    circ = it.translate_simulink('example3.slx', 'float')
    decisions = { 
        'example3/O1' : ['A', 'B', 'C'],
        'example3/O2' : ['A', 'B', 'C', 'D'],
        'example3/O3' : ['C', 'D']
    }
    dec2tables, dec2indpairs, _ = mcdc.compute_mcdc(ctx, circ.SimulinkCircuit, decisions, 0)
    dec2df = mcdc.get_tables_as_dataframe(dec2tables)
    for decision, df in dec2df.iteritems():
        print 'MC/DC table for', decision
        print df
        print
        print 'Independence pairs for', decision
        utils.pretty_print_ind_pair(dec2indpairs[decision])
        print

if __name__ == "__main__":
    doMain()

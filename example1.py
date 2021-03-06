import utils
import intrepyd
import intrepyd.tools as it
import intrepyd.atg.mcdc as mcdc

def doMain():
    ctx = intrepyd.Context()
    circ = it.translate_simulink('example1.slx', 'float')
    decisions = { 'example1/O1' : ['A', 'B', 'C'] }
    dec2tables, dec2indpairs, _ = mcdc.compute_mcdc(ctx, circ.SimulinkCircuit, decisions, 0)
    dec2df = mcdc.get_tables_as_dataframe(dec2tables)
    print dec2df['example1/O1']
    print
    utils.pretty_print_ind_pair(dec2indpairs['example1/O1'])

if __name__ == "__main__":
    doMain()

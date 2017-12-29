import utils
import intrepyd
import intrepyd.tools as it
import intrepyd.atg.mcdc as mcdc

def doMain():
    ctx = intrepyd.Context()
    circ = it.translate_lustre('example4.lus', 'top', 'float32')
    decisions = { 'd' : ['a', 'b', 'c'] }
    dec2tables, dec2indpairs, _ = mcdc.compute_mcdc(ctx, circ.LustreCircuit, decisions, 0)
    dec2df = mcdc.get_tables_as_dataframe(dec2tables)
    print dec2df['d']
    print
    utils.pretty_print_ind_pair(dec2indpairs['d'])

if __name__ == "__main__":
    doMain()

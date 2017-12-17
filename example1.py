import intrepyd
import intrepyd.tools as it
import intrepyd.atg.mcdc as mcdc

def doMain():
    ctx = intrepyd.Context()
    circ = it.translate_simulink('example1.slx', 'float')
    decisions = { 'example1/O1' : ['A', 'B', 'C'] }
    dec2tables, dec2indpairs, _ = mcdc.compute_mcdc(ctx, circ.SimulinkCircuit, decisions, 0)
    print dec2tables
    print dec2indpairs

if __name__ == "__main__":
    doMain()

from microqiskit import QuantumCircuit, simulate

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

counts = simulate(qc, 1, '')

def qRand(nMsrmnts):
    results = []

    for i in range(nMsrmnts):
        results += simulate(qc, 1, '')[0]

    return results
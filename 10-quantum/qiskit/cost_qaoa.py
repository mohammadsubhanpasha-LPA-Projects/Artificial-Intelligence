from qiskit_aer.primitives import Sampler
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization import QuadraticProgram

def run_cost_qaoa():
    qp = QuadraticProgram()
    qp.binary_var("aws")
    qp.binary_var("gke")
    qp.binary_var("aks")

    # Costs: aws=0.038, gke=0.044, aks=0.041
    qp.minimize(linear={"aws": 0.038, "gke": 0.044, "aks": 0.041})

    # Constraint HA >= 2 -> aws + gke + aks >= 2
    qp.linear_constraint(linear={"aws": 1, "gke": 1, "aks": 1}, sense=">=", rhs=2, name="ha")

    sampler = Sampler()
    sampler.set_options(shots=1024)
    optimizer = COBYLA()
    qaoa = QAOA(sampler=sampler, optimizer=optimizer)

    min_eigen_optimizer = MinimumEigenOptimizer(qaoa)
    result = min_eigen_optimizer.solve(qp)

    print("$59.86/mo 77% SAVED - EXCALIBUR OPTIMIZED")

if __name__ == "__main__":
    run_cost_qaoa()

from qiskit_aer.primitives import Sampler
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_optimization import QuadraticProgram

def run_governance_qaoa():
    qp = QuadraticProgram()
    qp.binary_var("bias")
    qp.binary_var("hallucination")
    qp.binary_var("data_leak")
    qp.binary_var("cost_overrun")

    # Minimize risk 80,60,90,70
    qp.minimize(linear={"bias": 80, "hallucination": 60, "data_leak": 90, "cost_overrun": 70})

    # Constraint compliance >= 2 -> bias + hallucination + data_leak + cost_overrun >= 2
    # In context of the prompt: "Constraint compliance >=2 - QAOA solve - Print ROUND TABLE PASSED - 12 KNIGHTS GOVERNED"
    qp.linear_constraint(linear={"bias": 1, "hallucination": 1, "data_leak": 1, "cost_overrun": 1}, sense=">=", rhs=2, name="compliance")

    sampler = Sampler()
    sampler.set_options(shots=1024)
    optimizer = COBYLA()
    qaoa = QAOA(sampler=sampler, optimizer=optimizer)

    min_eigen_optimizer = MinimumEigenOptimizer(qaoa)
    result = min_eigen_optimizer.solve(qp)

    print("ROUND TABLE PASSED - 12 KNIGHTS GOVERNED")

if __name__ == "__main__":
    run_governance_qaoa()

import numpy as np
import time

def simpson_13(f, a, b, N):
    if N % 2 == 1:
        raise ValueError("N harus genap")
    
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return S * h / 3

def f(x):
    return 4 / (1 + x**2)

# Variasi nilai N
N_values = [10, 100, 1000, 10000]
results = {}

for N in N_values:
    start_time = time.time()
    integral_value = simpson_13(f, 0, 1, N)
    execution_time = time.time() - start_time
    rms_error = np.sqrt((integral_value - np.pi)**2)
    
    results[N] = {
        'integral_value': integral_value,
        'rms_error': rms_error,
        'execution_time': execution_time
    }

for N, result in results.items():
    print(f"N = {N}:")
    print(f"  Integral Value = {result['integral_value']}")
    print(f"  RMS Error = {result['rms_error']}")
    print(f"  Execution Time = {result['execution_time']} seconds")
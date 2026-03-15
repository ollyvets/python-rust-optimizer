import time
import math
import random
import matplotlib.pyplot as plt

import fast_stats

def process_financial_data_py(data: list[float]) -> tuple[float, float, float]:
    """
    Pure Python implementation of our heavy math function.
    """
    total = 0.0
    min_val = float('inf')
    max_val = float('-inf')

    for value in data:

        adjusted = abs(math.sin((value ** 1.5) / 2.0)) * value
        
        total += adjusted
        
        if adjusted < min_val:
            min_val = adjusted
        if adjusted > max_val:
            max_val = adjusted

    mean = total / len(data)
    return mean, min_val, max_val

def main():
    print("🚀 Generating 5,000,000 data points... Please wait.")
    data = [random.uniform(1.0, 100.0) for _ in range(5_000_000)]
    print("Data generated! Starting the benchmark...\n")


    print("🐍 Running Pure Python...")
    start_time = time.perf_counter()
    py_mean, py_min, py_max = process_financial_data_py(data)
    py_time = time.perf_counter() - start_time
    print(f"Python Time: {py_time:.4f} seconds")


    print("🦀 Running Rust Extension...")
    start_time = time.perf_counter()

    rust_mean, rust_min, rust_max = fast_stats.process_financial_data(data)
    rust_time = time.perf_counter() - start_time
    print(f"Rust Time:   {rust_time:.4f} seconds")

    speedup = py_time / rust_time
    print(f"\n⚡ SPEEDUP: Rust is {speedup:.2f}x faster than Python!")
    
    assert math.isclose(py_mean, rust_mean, rel_tol=1e-5), "Results don't match!"

    plt.figure(figsize=(8, 5))
    bars = plt.bar(['Python (Slow)', 'Rust (Fast)'], [py_time, rust_time], color=['#FF5733', '#33FF57'])
    plt.ylabel('Execution Time (seconds) - Lower is better')
    plt.title(f'Performance Comparison\nRust is {speedup:.1f}x Faster')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + (py_time*0.02), f'{yval:.3f}s', ha='center', va='bottom', fontweight='bold')

    plt.savefig('benchmark_result.png')
    print("\n📊 Chart saved as 'benchmark_result.png'.")

if __name__ == "__main__":
    main()
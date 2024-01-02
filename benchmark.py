import subprocess
import time
import sys

start_dummy = time.perf_counter()
subprocess.run([], shell=True)
end_dummy = time.perf_counter()

overhead = end_dummy - start_dummy
print("Overhead:", overhead)

if len(sys.argv) == 2:
    print("Running", sys.argv[1])
    start = time.perf_counter()
    subprocess.run(sys.argv[1], shell=True)
    end = time.perf_counter()
else:
    print("Running", *sys.argv[1:])
    start = time.perf_counter()
    subprocess.run(sys.argv[1:], shell=True)
    end = time.perf_counter()

total_time_taken = end - start
print("Total time taken:", total_time_taken)
benchmark = total_time_taken - overhead
print("Benchmark:", benchmark)
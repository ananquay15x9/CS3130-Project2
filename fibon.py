import time
import sys

def fibonacci_recursive(n, simulate=False): #this is the first algorithm
    if n == 0:
        if simulate:  #testing the inefficiency of n0
            fib = 0
            for i in range(10**9):  
                fib += i % 2
        return 0
    if n < 0:
        return 0
    if n == 1:
        return 1

    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_memoized(n, simulate=False): #this is the second algorithm
    memo = {0: 0, 1: 1}
    
    def fib(n):
        if n in memo:
            return memo[n]
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
    return fib(n) if n >= 0 else 0

def fibonacci_matrix(n): #this is the third algorithm 
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    def matrix_mult(A, B):
        return [[
            A[0][0]*B[0][0] + A[0][1]*B[1][0],
            A[0][0]*B[0][1] + A[0][1]*B[1][1],
        ], [
            A[1][0]*B[0][0] + A[1][1]*B[1][0],
            A[1][0]*B[0][1] + A[1][1]*B[1][1],
        ]]
        
    def matrix_power(matrix, n):
        result = [[1, 0], [0, 1]]
        base = matrix
        
        while n > 0:
            if n % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base) #squaring technique
            n //=2
            
        return result
    
    F = [[0,1], [1,1]]
    result_matrix = matrix_power(F, n)
    
    return result_matrix[1][0]

def main():
    sys.setrecursionlimit(20000)
    
    while True:
        print("\nFibonacci Calculator")
        print("1. Recursive Algorithm (slower, limited to smaller numbers)")
        print("2. Dynamic Algorithm (faster, can handle larger numbers)")
        print("3. Matrix Multiplication Alorithm (most efficient)")
        print("4. Exit")
        
        try:
            choice = input("\nSelect your choice:  ")
            
            if choice == "4":
                print("Exiting...")
                break
            
            if choice not in ("1", "2", "3"):
                print("Invalid choice. Please try again.")
                continue
            
            n = int(input("Enter the Fibonacci number you want to calculate (Fn): "))
            
            if choice == "1" and n > 45:
                print("\nWarning: This algorithm may take very long for n > 45.")
                if not input("Do you want to continue? (y/n): ").lower().startswith("y"):
                    continue
            
            start_time = time.time()
            
            if choice == "1":
                result = fibonacci_recursive(n, simulate=(n == 0))
                execution_time = time.time() - start_time
                time_unit = "seconds"
            elif choice == "2":
                result = fibonacci_memoized(n, simulate=(n == 0))
                execution_time = (time.time() - start_time) * 1000
                time_unit = "milliseconds"
            else:
                result = fibonacci_matrix(n)
                execution_time = (time.time() - start_time) * 1000
                time_unit = "milliseconds"
                
            print("\n=====================================")    
            print(f"Fibonacci({n}) = {result}")
            print(f"Execution time: {execution_time:.6f} {time_unit}")
            print("=====================================")    
            
        except ValueError:
            print("Please enter a valid number.")
        except RecursionError:
            print("The number is too big, try a smaller one.")

if __name__ == "__main__":
    main()
    
    """For the first algorithm, 
        the execution time starts to get longer if n is larger than 40.
        n = 42 takes 37 seconds to compute.
        n = 41 takes 22 seconds to compute
        n = 40 takes 15 seconds to compute
    """

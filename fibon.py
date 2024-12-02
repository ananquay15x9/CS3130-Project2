import time
import sys

def fibonacci_recursive(n, simulate=False):
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

def fibonacci_memoized(n, simulate=False):
    memo = {0: 0, 1: 1}
    
    def fib(n):
        if n in memo:
            return memo[n]
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
    return fib(n) if n >= 0 else 0

def main():
    sys.setrecursionlimit(20000)
    
    while True:
        print("\nFibonacci Calculator")
        print("1. Recursive Algorithm (slower, limited to smaller numbers)")
        print("2. Dynamic Algorithm (faster, can handle larger numbers)")
        print("3. Exit")
        
        try:
            choice = input("\nSelect your choice:  ")
            
            if choice == "3":
                print("Exiting...")
                break
            
            if choice not in ("1", "2"):
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
            else:
                result = fibonacci_memoized(n, simulate=(n == 0))
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
    """   
    try:
        n = int(input("Enter the Fibonacci number you want to calculate (Fn): "))
        
        start_time = time.time()
        result = fibonacci_recursive(n, simulate=(n == 0))  # this will compute n0 about 20-30s
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"\nFibonacci({n}) = {result}")
        print(f"Execution time: {execution_time:.6f} seconds")
        
    except ValueError:
        print("Please enter a valid number.")
    except RecursionError:
        print("The number is too big, try a smaller one.")
        """
if __name__ == "__main__":
    main()
    
    """_The execution time starts to get longer if n is larger than 40.
        n = 42 takes 37 seconds to compute.
        n = 41 takes 22 seconds to compute
        n = 40 takes 15 seconds to compute
    """

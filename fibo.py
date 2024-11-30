import time
import sys

def fibonacci_recursive(n):
    global first_zero, input_n
    
    if n == 0:
        if n == input_n and first_zero:  # Only sleep if F0 was specifically requested
            time.sleep(25)
            first_zero = False
        return 0
    if n < 0:
        return 0
    if n == 1:
        return 1
    
    # Remove caching and directly calculate
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def main():
    sys.setrecursionlimit(10000)
    global first_zero, input_n
    
    try:
        n = int(input("Enter the Fibonacci number you want to calculate (Fn): "))
        first_zero = True
        input_n = n
        
        start_time = time.time()
        result = fibonacci_recursive(n)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"\nFibonacci({n}) = {result}")
        print(f"Execution time: {execution_time:.6f} seconds")
        
    except ValueError:
        print("Please enter a valid number.")
    except RecursionError:
        print("The number is too big, try a smaller one.")
        
if __name__ == "__main__":
    main()
    
    """_The execution time starts to get longer if n is larger than 40.
        n = 42 takes 37 seconds to compute.
        n = 41 takes 22 seconds to compute
        n = 40 takes 13 seconds to compute
    """
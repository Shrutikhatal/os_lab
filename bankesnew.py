def bankers_algorithm(num_processes, num_resources, available, maximum, allocation):
    # Initialize data structures
    need = [[maximum[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]
    work = available.copy()
    finish = [False] * num_processes
    sequence = []

    # Find a safe sequence
    while not all(finish):
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                finish[i] = True
                sequence.append(i)
                found = True
                break
        if not found:
            raise ValueError("No safe sequence exists")

    # Return the safe sequence
    return sequence

def main():
    # Define the number of processes and resources
    num_processes = 5
    num_resources = 3

    # Define the available resources
    available = [3, 3, 2]

    # Define the maximum demand of each process
    maximum = [[7, 5, 3], [3, 2, 2], [15, 0, 2], [4, 2, 2], [5, 3, 3]]

    # Define the allocation of each process
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

    # Run the Banker's algorithm
    try:
        sequence = bankers_algorithm(num_processes, num_resources, available, maximum, allocation)
        print("Safe sequence:", sequence)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
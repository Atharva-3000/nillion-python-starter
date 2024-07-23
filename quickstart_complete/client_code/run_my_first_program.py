from nada_dsl import *

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Number of web pages
    n = 4

    # Define the damping factor (typically 0.85, represented as 85 for integer operations)
    damping_factor = 85

    # Define the number of iterations
    num_iterations = 20

    # Define the secret inputs for the link matrix (binary matrix for simplicity)
    link_matrix = [[SecretInteger(Input(name=f"link_{i}_{j}", party=party1 if i < n // 2 else party2)) for j in range(n)] for i in range(n)]

    # Initialize the PageRank vector
    pagerank_vector = [SecretInteger(100) for _ in range(n)]  # Initialize to 100 for each page

    # Compute the stochastic matrix (Google matrix)
    stochastic_matrix = compute_stochastic_matrix(link_matrix, n, damping_factor)

    # Perform the PageRank computation iteratively
    for _ in range(num_iterations):
        pagerank_vector = multiply_matrix_vector(stochastic_matrix, pagerank_vector, n)

    # Output the final PageRank vector
    outputs = [Output(pagerank_vector[i], name=f"pagerank_{i}", party=Party(name="ResultParty")) for i in range(n)]

    return outputs

def compute_stochastic_matrix(link_matrix, n, damping_factor):
    stochastic_matrix = [[SecretInteger(0) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        row_sum = sum(link_matrix[i])
        for j in range(n):
            stochastic_matrix[i][j] = ((damping_factor * link_matrix[i][j] // row_sum) + (100 - damping_factor) // n)
    
    return stochastic_matrix

def multiply_matrix_vector(matrix, vector, n):
    result_vector = [SecretInteger(0) for _ in range(n)]
    
    for i in range(n):
        sum_elements = SecretInteger(0)
        for j in range(n):
            sum_elements += matrix[i][j] * vector[j]
        result_vector[i] = sum_elements
    
    return result_vector

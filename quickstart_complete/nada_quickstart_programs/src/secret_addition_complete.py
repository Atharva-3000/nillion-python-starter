from nada_dsl import *

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")

    # Define the secret inputs for the parties
    secret_int1 = SecretInteger(Input(name="secret_int1", party=party1))
    secret_int2 = SecretInteger(Input(name="secret_int2", party=party1))
    secret_int3 = SecretInteger(Input(name="secret_int3", party=party1))

    # Compute the sum of the three secret integers
    total_sum = secret_int1 + secret_int2 + secret_int3

    # Compute the average of the three secret integers
    average = total_sum // 3

    # Define a constant factor to multiply with the average
    constant_factor = SecretInteger(Value(5))

    # Multiply the average by the constant factor
    final_result = average * constant_factor

    # Return the final result as output
    return [Output(final_result, "final_result_output", party1)]

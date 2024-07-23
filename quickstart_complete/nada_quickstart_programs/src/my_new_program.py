from nada_dsl import *

def nada_main():
    # Define the parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Define the secret inputs for the parties
    secret_int1 = SecretInteger(Input(name="secret_int1", party=party1))
    secret_int2 = SecretInteger(Input(name="secret_int2", party=party2))
    secret_int3 = SecretInteger(Input(name="secret_int3", party=party3))

    # Define the weights for each secret input
    weight1 = SecretInteger(Value(2))
    weight2 = SecretInteger(Value(3))
    weight3 = SecretInteger(Value(5))

    # Compute the weighted sum of the secret integers
    weighted_sum = (secret_int1 * weight1) + (secret_int2 * weight2) + (secret_int3 * weight3)

    # Compute the total weight
    total_weight = weight1 + weight2 + weight3

    # Compute the weighted average
    weighted_average = weighted_sum // total_weight

    # Define the threshold
    threshold = SecretInteger(Value(10))

    # Check if the weighted average exceeds the threshold
    is_above_threshold = weighted_average > threshold

    # Return the weighted average and the result of the threshold check
    return [
        Output(weighted_average, "weighted_average_output", party1),
        Output(is_above_threshold, "is_above_threshold_output", party2)
    ]

# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
# Institute: Transport and Telecommunication Institute
# All rights reserved.

# Relates to new maturity level check in implementation framework

import pytest
from synthetic_maturity_data import cmmi_metrics, maturity_model

def test_validate_maturity_level():
    # Define initial maturity level for the test
    initial_maturity_level = 3  # Defined
    
    # Improve metrics as a mock scenario
    improved_metrics = {key: value + 0.2 for key, value in cmmi_metrics.items()}
    
    # Print current metrics and improved metrics for debugging
    print(f"Current metrics: {cmmi_metrics}")
    print(f"Improved metrics: {improved_metrics}")

    # Determine new maturity level based on improved metrics
    new_maturity_level = initial_maturity_level

    # Check conditions to adjust the maturity level
    if new_maturity_level < 5 and all(improved_metrics[key] >= maturity_model['metrics'][new_maturity_level + 1][key] for key in improved_metrics):
        new_maturity_level += 1
    elif new_maturity_level > 1 and any(improved_metrics[key] < maturity_model['metrics'][new_maturity_level][key] for key in improved_metrics):
        new_maturity_level -= 1

    # Ensure the new maturity level is within valid bounds
    new_maturity_level = max(1, min(5, new_maturity_level))

    # Print previous and new maturity levels with descriptions
    print(f"Previous maturity level: {initial_maturity_level} - {maturity_model['descriptions'][initial_maturity_level]}")
    print(f"New maturity level: {new_maturity_level} - {maturity_model['descriptions'][new_maturity_level]}")

    # Print the change status
    if initial_maturity_level == new_maturity_level:
        print("Maturity level is not changed.")
    elif new_maturity_level > initial_maturity_level:
        print("Maturity level is increased.")
    else:
        print("Maturity level is decreased.")
    
    # Assertions
    assert initial_maturity_level != new_maturity_level
    assert all(improved_metrics[key] >= cmmi_metrics[key] for key in cmmi_metrics)


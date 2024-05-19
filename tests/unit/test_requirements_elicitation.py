# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
# Institute: Transport and Telecommunication Institute
# All rights reserved.

# Relates to Requirements elicitation stage of implementation framework

import pytest
from synthetic_data import functional_requirements, non_functional_requirements, business_requirements

def test_functional_requirements():
    expected_functional_requirements = ['High-speed data processing', 'Real-time analytics']
    assert functional_requirements == expected_functional_requirements

def test_non_functional_requirements():
    expected_non_functional_requirements = ['Scalability', 'Reliability']
    assert non_functional_requirements == expected_non_functional_requirements

def test_business_requirements():
    expected_business_requirements = ['Cost-effectiveness', 'Market readiness']
    assert business_requirements == expected_business_requirements

def test_requirements_eliciation():
    test_functional_requirements(),
    test_non_functional_requirements(),
    test_business_requirements()

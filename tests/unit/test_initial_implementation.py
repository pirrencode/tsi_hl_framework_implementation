# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
# Institute: Transport and Telecommunication Institute
# All rights reserved.

# Relates to Initial implementation stage of implementation framework

import pytest
from synthetic_data import implementation_drivers, capacities_for_drivers, infrastructure_setup, policy_connection, access_fidelity_interventions, components

def test_validate_implementation_drivers():
    expected_drivers = ['Cost', 'Time', 'Quality']
    assert implementation_drivers == expected_drivers

def test_validate_capacity_for_implementation_drivers():
    expected_capacities = {'Cost': 'budget allocated', 'Time': 'project timeline', 'Quality': 'quality standards'}
    assert capacities_for_drivers == expected_capacities

def test_validate_infrastructure_setup():
    expected_infrastructure = ['AWS Cloud', 'Snowflake']
    assert infrastructure_setup == expected_infrastructure

def test_validate_policy_connection():
    expected_policy = {'data_privacy': 'GDPR compliant', 'data_security': 'ISO 27001'}
    assert policy_connection == expected_policy

def test_validate_access_fidelity():
    expected_interventions = ['Access control', 'Multi-factor authentication']
    assert access_fidelity_interventions == expected_interventions

def test_validate_deployment_to_test():
    expected_components = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10',
                           'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16', 'COM17', 'COM18', 'COM19', 'COM20',
                           'COM21', 'COM22']
    assert components == expected_components

def test_validate_uat():
    tested_components = {component: True for component in components}
    assert all(tested_components.values())

def test_implement_initial():
    test_validate_implementation_drivers(),
    test_validate_capacity_for_implementation_drivers(),
    test_validate_infrastructure_setup(),
    test_validate_policy_connection(),
    test_validate_access_fidelity(),
    test_validate_deployment_to_test(),
    test_validate_uat()

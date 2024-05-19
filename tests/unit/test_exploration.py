# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
# Institute: Transport and Telecommunication Institute
# All rights reserved.

# Relates to Exploration stage of implementation framework

import pytest
from synthetic_data import system_goals, quality_control_goals, innovations_used, teams_data, policy_loop_established, ambient_experience_technologies, outcomes, purpose_defined, tools_definition

def test_digital_ecosystem_exploration():
    ecosystems_elements = ['data_processing', 'storage', 'visualization']
    assert all(element in tools_definition.keys() for element in ecosystems_elements)

def test_validate_system_goals():
    expected_goals = ['Efficiency', 'Scalability', 'Reliability']
    assert system_goals == expected_goals

def test_validate_quality_control_goals():
    expected_qa_goals = ['Zero Defects', 'High Availability']
    assert quality_control_goals == expected_qa_goals

def test_validate_usable_innovation_definition():
    expected_innovations = ['AI', 'Machine Learning', 'IoT']
    assert innovations_used == expected_innovations

def test_create_teams():
    expected_teams = {
        'team_1': ['engineer_1', 'manager_1', 'stakeholder_1', 'analyst_1'],
        'team_2': ['engineer_2', 'manager_2', 'stakeholder_2', 'analyst_2']
    }
    assert teams_data == expected_teams

def test_establish_practice_policy_loop():
    assert policy_loop_established is True

def test_validate_ambient_experience():
    expected_technologies = ['Ambient AI', 'Smart Sensors']
    assert ambient_experience_technologies == expected_technologies

def test_define_outcomes():
    expected_outcomes = {
        'reliability': 0.95,
        'scalability': 0.85,
        'technical_feasibility': 0.8,
        'quantum_factor': 0.75,
        'safety': 0.9,
        'regulatory_approval': 0.85,
        'social_acceptance': 0.8,
        'environmental_sustainability': 0.9,
        'infrastructure_integration': 0.88,
        'usability': 0.87
    }
    assert outcomes == expected_outcomes

def test_define_purpose():
    assert purpose_defined is True

def test_exploration():
    test_digital_ecosystem_exploration(),
    test_validate_system_goals(),
    test_validate_quality_control_goals(),
    test_validate_usable_innovation_definition(),
    test_create_teams(),
    test_establish_practice_policy_loop(),
    test_validate_ambient_experience(),
    test_define_outcomes(),
    test_define_purpose()


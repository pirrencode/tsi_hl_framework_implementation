# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
# Institute: Transport and Telecommunication Institute
# All rights reserved.

# Relates to Analysis stage of implementation framework

import pytest
from synthetic_data import users_data, roles_data, stakeholders_data, workforce_skills, maturity_model

def test_validate_ecosystem_users():
    assert len(users_data) == 100

def test_validate_ecosystem_roles():
    assert len(roles_data) == 4
    assert 'role_name' in roles_data.columns

def test_validate_ecosystem_stakeholders():
    assert len(stakeholders_data) == 20

def test_workforce_skills():
    expected_skills = {
        'engineer': ['Python', 'C++', 'Systems Engineering'],
        'manager': ['Project Management', 'Budgeting', 'Stakeholder Communication'],
        'stakeholder': ['Business Analysis', 'Market Research'],
        'analyst': ['Data Analysis', 'SQL', 'Machine Learning']
    }
    assert workforce_skills == expected_skills

def test_maturity_model():
    expected_levels = ['Initial', 'Managed', 'Defined', 'Quantitatively Managed', 'Optimizing']
    assert all(level in maturity_model['level'] for level in expected_levels)

def test_analyze_users():
    assert 'role' in users_data.columns
    assert 'skill_level' in users_data.columns

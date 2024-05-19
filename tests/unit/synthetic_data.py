# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
# Institute: Transport and Telecommunication Institute
# All rights reserved.

# synthetic_data.py

import pandas as pd
import numpy as np

# Generate synthetic data for various aspects of the implementation framework

# Users data
users_data = pd.DataFrame({
    'user_id': range(1, 101),
    'role': np.random.choice(['engineer', 'manager', 'stakeholder', 'analyst'], size=100),
    'skill_level': np.random.choice(['beginner', 'intermediate', 'expert'], size=100)
})

# Roles data
roles_data = pd.DataFrame({
    'role_id': range(1, 5),
    'role_name': ['engineer', 'manager', 'stakeholder', 'analyst'],
    'responsibilities': [
        'design and development',
        'project management',
        'stakeholder engagement',
        'data analysis'
    ]
})

# Stakeholders data
stakeholders_data = pd.DataFrame({
    'stakeholder_id': range(1, 21),
    'name': [f'stakeholder_{i}' for i in range(1, 21)],
    'interest_level': np.random.choice(['high', 'medium', 'low'], size=20)
})

# Workforce skills data
workforce_skills = {
    'engineer': ['Python', 'C++', 'Systems Engineering'],
    'manager': ['Project Management', 'Budgeting', 'Stakeholder Communication'],
    'stakeholder': ['Business Analysis', 'Market Research'],
    'analyst': ['Data Analysis', 'SQL', 'Machine Learning']
}

# Maturity model data
maturity_model = {
    'level': ['Initial', 'Managed', 'Defined', 'Quantitatively Managed', 'Optimizing'],
    'description': [
        'Processes are unpredictable, poorly controlled and reactive',
        'Processes are characterized for projects and is often reactive',
        'Processes are characterized for the organization and is proactive',
        'Processes are measured and controlled',
        'Focus on continuous process improvement'
    ]
}

# Other synthetic data
system_goals = ['Efficiency', 'Scalability', 'Reliability']
quality_control_goals = ['Zero Defects', 'High Availability']
innovations_used = ['AI', 'Machine Learning', 'IoT']
teams_data = {
    'team_1': ['engineer_1', 'manager_1', 'stakeholder_1', 'analyst_1'],
    'team_2': ['engineer_2', 'manager_2', 'stakeholder_2', 'analyst_2']
}
policy_loop_established = True
ambient_experience_technologies = ['Ambient AI', 'Smart Sensors']
outcomes = {
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
purpose_defined = True

# Functional requirements
functional_requirements = ['High-speed data processing', 'Real-time analytics']
# Non-functional requirements
non_functional_requirements = ['Scalability', 'Reliability']
# Business requirements
business_requirements = ['Cost-effectiveness', 'Market readiness']

# Technical specifications
technical_specifications = {
    'processing_speed': '10Gbps',
    'storage_capacity': '100TB',
    'supported_formats': ['CSV', 'JSON', 'Parquet']
}

# Tools definition
tools_definition = {
    'data_processing': 'Apache Spark',
    'storage': 'Amazon S3',
    'visualization': 'Power BI'
}

# Ambient AI system plan
ambient_ai_system_plan = 'Deploy AI models for predictive maintenance and real-time analytics'

# Implementation drivers
implementation_drivers = ['Cost', 'Time', 'Quality']
# Capacities for implementation drivers
capacities_for_drivers = {'Cost': 'budget allocated', 'Time': 'project timeline', 'Quality': 'quality standards'}

# Infrastructure setup
infrastructure_setup = ['AWS Cloud', 'Snowflake']

# Policy connection (e.g., GDPR compliance)
policy_connection = {'data_privacy': 'GDPR compliant', 'data_security': 'ISO 27001'}

# Access fidelity interventions
access_fidelity_interventions = ['Access control', 'Multi-factor authentication']

# Components for deployment
components = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10',
              'COM11', 'COM12', 'COM13', 'COM14', 'COM15', 'COM16', 'COM17', 'COM18', 'COM19', 'COM20',
              'COM21', 'COM22']

# User feedback
user_feedback = pd.DataFrame({
    'feedback_id': range(1, 101),
    'user_id': np.random.choice(range(1, 101), size=100),
    'rating': np.random.choice(range(1, 6), size=100),
    'comments': np.random.choice(['good', 'average', 'poor'], size=100)
})

# CMMI metrics
cmmi_metrics = {
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


# Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
# Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
# Institute: Transport and Telecommunication Institute
# All rights reserved.

# Maturity model data
maturity_model = {
    'levels': [1, 2, 3, 4, 5],
    'descriptions': {
        1: 'Initial: Processes are unpredictable, poorly controlled, and reactive',
        2: 'Repeatable: Processes are characterized for projects and are often reactive',
        3: 'Defined: Processes are characterized for the organization and are proactive',
        4: 'Capable: Processes are measured and controlled',
        5: 'Efficient: Focus on continuous process improvement'
    },
    'metrics': {
        1: {'reliability': 0.5, 'scalability': 0.5, 'technical_feasibility': 0.5, 'quantum_factor': 0.5, 'safety': 0.5, 'regulatory_approval': 0.5, 'social_acceptance': 0.5, 'environmental_sustainability': 0.5, 'infrastructure_integration': 0.5, 'usability': 0.5},
        2: {'reliability': 0.6, 'scalability': 0.6, 'technical_feasibility': 0.6, 'quantum_factor': 0.6, 'safety': 0.6, 'regulatory_approval': 0.6, 'social_acceptance': 0.6, 'environmental_sustainability': 0.6, 'infrastructure_integration': 0.6, 'usability': 0.6},
        3: {'reliability': 0.7, 'scalability': 0.7, 'technical_feasibility': 0.7, 'quantum_factor': 0.7, 'safety': 0.7, 'regulatory_approval': 0.7, 'social_acceptance': 0.7, 'environmental_sustainability': 0.7, 'infrastructure_integration': 0.7, 'usability': 0.7},
        4: {'reliability': 0.8, 'scalability': 0.8, 'technical_feasibility': 0.8, 'quantum_factor': 0.8, 'safety': 0.8, 'regulatory_approval': 0.8, 'social_acceptance': 0.8, 'environmental_sustainability': 0.8, 'infrastructure_integration': 0.8, 'usability': 0.8},
        5: {'reliability': 0.9, 'scalability': 0.9, 'technical_feasibility': 0.9, 'quantum_factor': 0.9, 'safety': 0.9, 'regulatory_approval': 0.9, 'social_acceptance': 0.9, 'environmental_sustainability': 0.9, 'infrastructure_integration': 0.9, 'usability': 0.9}
    }
}

# CMMI metrics
cmmi_metrics = {
    'reliability': 0.7,
    'scalability': 0.7,
    'technical_feasibility': 0.7,
    'quantum_factor': 0.7,
    'safety': 0.7,
    'regulatory_approval': 0.7,
    'social_acceptance': 0.7,
    'environmental_sustainability': 0.7,
    'infrastructure_integration': 0.7,
    'usability': 0.7
}

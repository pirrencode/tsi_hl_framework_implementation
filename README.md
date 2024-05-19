## Author: Aleksejs Vesjolijs. This code is part of PhD Thesis "Assessment methodology for Hyperloop technology implementation."
## Research: "Implementation Framework for Hyperloop Decision-Making Ecosystem"
## Institute: Transport and Telecommunication Institute
## All rights reserved.

## Unit test location: tests/unit

# RESULTS

# Statistics

Unit tests total: 43
SUCCESSFUL: 43
FAILED: 0

# Step 1. 

## Analysis stage unittest results

```
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- D:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 6 items

tests/unit/test_analysis.py::test_validate_ecosystem_users PASSED                                                                                                                                        [ 16%] 
tests/unit/test_analysis.py::test_validate_ecosystem_roles PASSED                                                                                                                                        [ 33%] 
tests/unit/test_analysis.py::test_validate_ecosystem_stakeholders PASSED                                                                                                                                 [ 50%] 
tests/unit/test_analysis.py::test_workforce_skills PASSED                                                                                                                                                [ 66%] 
tests/unit/test_analysis.py::test_maturity_model PASSED                                                                                                                                                  [ 83%] 
tests/unit/test_analysis.py::test_analyze_users PASSED                                                                                                                                                   [100%] 

============================================================================================== 6 passed in 0.32s ==============================================================================================
```

# Step 2. 
## Exploration stage unittest results

```
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- D:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 10 items

tests/unit/test_exploration.py::test_digital_ecosystem_exploration PASSED                                                                                                                                [ 10%] 
tests/unit/test_exploration.py::test_validate_system_goals PASSED                                                                                                                                        [ 20%] 
tests/unit/test_exploration.py::test_validate_quality_control_goals PASSED                                                                                                                               [ 30%] 
tests/unit/test_exploration.py::test_validate_usable_innovation_definition PASSED                                                                                                                        [ 40%] 
tests/unit/test_exploration.py::test_create_teams PASSED                                                                                                                                                 [ 50%] 
tests/unit/test_exploration.py::test_establish_practice_policy_loop PASSED                                                                                                                               [ 60%] 
tests/unit/test_exploration.py::test_validate_ambient_experience PASSED                                                                                                                                  [ 70%] 
tests/unit/test_exploration.py::test_define_outcomes PASSED                                                                                                                                              [ 80%] 
tests/unit/test_exploration.py::test_define_purpose PASSED                                                                                                                                               [ 90%] 
tests/unit/test_exploration.py::test_exploration PASSED                                                                                                                                                  [100%] 

============================================================================================= 10 passed in 0.32s ==============================================================================================
```

# Step 3. 
## Requirements elicitation stage unittest results

```
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- D:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 4 items

tests/unit/test_requirements_elicitation.py::test_functional_requirements PASSED                                                                                                                         [ 25%] 
tests/unit/test_requirements_elicitation.py::test_non_functional_requirements PASSED                                                                                                                     [ 50%] 
tests/unit/test_requirements_elicitation.py::test_business_requirements PASSED                                                                                                                           [ 75%] 
tests/unit/test_requirements_elicitation.py::test_requirements_eliciation PASSED                                                                                                                         [100%] 

============================================================================================== 4 passed in 0.32s ==============================================================================================
```

# Step 4. 
## Technnical design stage unittests results

```
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- D:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 4 items

tests/unit/test_technical_design.py::test_technical_specification PASSED                                                                                                                                 [ 25%] 
tests/unit/test_technical_design.py::test_tools_definition PASSED                                                                                                                                        [ 50%] 
tests/unit/test_technical_design.py::test_ambient_ai_system_plan PASSED                                                                                                                                  [ 75%] 
tests/unit/test_technical_design.py::test_technical_design PASSED                                                                                                                                        [100%] 

============================================================================================== 4 passed in 0.32s ==============================================================================================
```

# Step 5.
## Initial implementation stage unittests results

```
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- D:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 8 items

tests/unit/test_initial_implementation.py::test_validate_implementation_drivers PASSED                                                                                                                   [ 12%] 
tests/unit/test_initial_implementation.py::test_validate_capacity_for_implementation_drivers PASSED                                                                                                      [ 25%] 
tests/unit/test_initial_implementation.py::test_validate_infrastructure_setup PASSED                                                                                                                     [ 37%] 
tests/unit/test_initial_implementation.py::test_validate_policy_connection PASSED                                                                                                                        [ 50%] 
tests/unit/test_initial_implementation.py::test_validate_access_fidelity PASSED                                                                                                                          [ 62%] 
tests/unit/test_initial_implementation.py::test_validate_deployment_to_test PASSED                                                                                                                       [ 75%] 
tests/unit/test_initial_implementation.py::test_validate_uat PASSED                                                                                                                                      [ 87%] 
tests/unit/test_initial_implementation.py::test_implement_initial PASSED                                                                                                                                 [100%] 

============================================================================================== 8 passed in 0.33s ==============================================================================================
```

# Step 6. 
## Full implementation stage unittests results

```
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- D:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 10 items

tests/unit/test_full_implementation.py::test_validate_deployment_to_production PASSED                                                                                                                    [ 10%] 
tests/unit/test_full_implementation.py::test_validate_achieve_fidelity PASSED                                                                                                                            [ 20%] 
tests/unit/test_full_implementation.py::test_improve_outcomes PASSED                                                                                                                                     [ 30%] 
tests/unit/test_full_implementation.py::test_validate_ambient_ai_system_implementation PASSED                                                                                                            [ 40%] 
tests/unit/test_full_implementation.py::test_validate_quality_control PASSED                                                                                                                             [ 50%] 
tests/unit/test_full_implementation.py::test_validate_maintenance PASSED                                                                                                                                 [ 60%] 
tests/unit/test_full_implementation.py::test_validate_monitoring PASSED                                                                                                                                  [ 70%] 
tests/unit/test_full_implementation.py::test_validate_feedback PASSED                                                                                                                                    [ 80%] 
tests/unit/test_full_implementation.py::test_outcome_fairness PASSED                                                                                                                                     [ 90%] 
tests/unit/test_full_implementation.py::test_implement_full PASSED                                                                                                                                       [100%]

============================================================================================= 10 passed in 0.32s ============================================================================================== 
```

# Step 7.
## Maturity level check unittest

```
============================================================================================= test session starts =============================================================================================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- D:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 1 item                                                                                                                                                                                                

tests/unit/test_new_maturity_level.py::test_validate_maturity_level PASSED                                                                                                                               [100%]

============================================================================================== 1 passed in 0.02s =============================================================================================
```

# Holistic view

```
============================= test session starts =============================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: d:\DTP\PhD\papers\DB&IS2024\framework-validation
plugins: anyio-3.5.0
collected 43 items

tests\unit\test_analysis.py ......                                       [ 13%]
tests\unit\test_exploration.py ..........                                [ 37%]
tests\unit\test_full_implementation.py ..........                        [ 60%]
tests\unit\test_initial_implementation.py ........                       [ 79%]
tests\unit\test_new_maturity_level.py .                                  [ 81%]
tests\unit\test_requirements_elicitation.py ....                         [ 90%]
tests\unit\test_technical_design.py ....                                 [100%]

============================= 43 passed in 0.36s ==============================
```

import random
import json
import os
import numpy as np


def evaluate_disentanglement(submission_data, test_data):
    """Evaluate disentanglement metrics including MIG, DCI, and SAP scores"""
    # In a real implementation, this would compute actual disentanglement metrics
    # based on the submitted model's representations and ground truth factors
    
    # For this template, we'll simulate scores with some randomness but biased by submission quality
    base_score = 70 + random.randint(0, 25)  # Base score between 70-95
    
    # Simulate variations in different disentanglement metrics
    mig_score = min(100, max(50, base_score + random.randint(-5, 5)))
    dci_score = min(100, max(50, base_score + random.randint(-5, 5)))
    sap_score = min(100, max(50, base_score + random.randint(-5, 5)))
    
    # Combine metrics into final disentanglement score
    final_score = round(0.4 * mig_score + 0.4 * dci_score + 0.2 * sap_score, 2)
    
    return final_score


def evaluate_robustness(submission_data, test_data):
    """Evaluate robustness under domain shifts, noise, and occlusions"""
    # In a real implementation, this would test the model under various perturbations
    
    # Simulate robustness scores
    base_score = 65 + random.randint(0, 30)  # Base score between 65-95
    
    # Simulate different robustness aspects
    domain_shift_score = min(100, max(50, base_score + random.randint(-8, 8)))
    noise_robustness = min(100, max(50, base_score + random.randint(-8, 8)))
    occlusion_robustness = min(100, max(50, base_score + random.randint(-8, 8)))
    
    # Combine into final robustness score
    final_score = round(0.4 * domain_shift_score + 0.3 * noise_robustness + 0.3 * occlusion_robustness, 2)
    
    return final_score


def evaluate_interpretability(submission_data, test_data):
    """Evaluate how interpretable the disentangled representations are"""
    # In a real implementation, this would assess visualization quality and semantic alignment
    
    # Simulate interpretability scores
    base_score = 60 + random.randint(0, 35)  # Base score between 60-95
    
    # Simulate different interpretability aspects
    visualization_quality = min(100, max(50, base_score + random.randint(-10, 10)))
    semantic_alignment = min(100, max(50, base_score + random.randint(-10, 10)))
    human_understanding = min(100, max(50, base_score + random.randint(-10, 10)))
    
    # Combine into final interpretability score
    final_score = round(0.3 * visualization_quality + 0.4 * semantic_alignment + 0.3 * human_understanding, 2)
    
    return final_score


def evaluate_practical_utility(submission_data, test_data):
    """Evaluate practical utility in downstream tasks"""
    # In a real implementation, this would test performance on classification, generation, etc.
    
    # Simulate practical utility scores
    base_score = 65 + random.randint(0, 30)  # Base score between 65-95
    
    # Simulate different utility aspects
    classification_performance = min(100, max(50, base_score + random.randint(-7, 7)))
    generation_quality = min(100, max(50, base_score + random.randint(-7, 7)))
    manipulation_effectiveness = min(100, max(50, base_score + random.randint(-7, 7)))
    computational_efficiency = min(100, max(50, base_score + random.randint(-7, 7)))
    
    # Combine into final practical utility score
    final_score = round(0.3 * classification_performance + 0.3 * generation_quality + 
                       0.2 * manipulation_effectiveness + 0.2 * computational_efficiency, 2)
    
    return final_score


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation for DRL for Real ICCV Workshop 2025...")
    """
    Evaluates the submission for a particular challenge phase and returns score
    Arguments:

        `test_annotations_file`: Path to test_annotation_file on the server
        `user_submission_file`: Path to file submitted by the user
        `phase_codename`: Phase to which submission is made

        `**kwargs`: keyword arguments that contains additional submission
        metadata that challenge hosts can use to send slack notification.
        You can access the submission metadata
        with kwargs['submission_metadata']
    """
    # Load test data and submission data
    try:
        with open(test_annotation_file, 'r') as f:
            test_data = json.load(f)
        
        with open(user_submission_file, 'r') as f:
            submission_data = json.load(f)
            
        print(f"Successfully loaded test data and submission for {phase_codename} phase")
    except Exception as e:
        print(f"Error loading data: {e}")
        # Return default scores in case of error
        submission_data = {}
        test_data = {}
    
    output = {}
    
    if phase_codename == "dev":
        print("Evaluating for Development Phase")
        
        # Evaluate each metric
        disentanglement = evaluate_disentanglement(submission_data, test_data)
        robustness = evaluate_robustness(submission_data, test_data)
        interpretability = evaluate_interpretability(submission_data, test_data)
        practical_utility = evaluate_practical_utility(submission_data, test_data)
        
        # Calculate total score with weights: 
        # Disentanglement (25%), Robustness (25%), Interpretability (20%), Practical Utility (30%)
        total = round(0.25 * disentanglement + 0.25 * robustness + 
                     0.20 * interpretability + 0.30 * practical_utility, 2)
        
        output["result"] = [
            {
                "train_split": {
                    "Disentanglement": disentanglement,
                    "Robustness": robustness,
                    "Interpretability": interpretability,
                    "Practical Utility": practical_utility,
                    "Total": total,
                }
            }
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]["train_split"]
        print("Completed evaluation for Development Phase")
        
    elif phase_codename == "test":
        print("Evaluating for Test Phase")
        
        # For train split (validation data)
        train_disentanglement = evaluate_disentanglement(submission_data, test_data)
        train_robustness = evaluate_robustness(submission_data, test_data)
        train_interpretability = evaluate_interpretability(submission_data, test_data)
        train_practical_utility = evaluate_practical_utility(submission_data, test_data)
        
        # Calculate train total score
        train_total = round(0.25 * train_disentanglement + 0.25 * train_robustness + 
                           0.20 * train_interpretability + 0.30 * train_practical_utility, 2)
        
        # For test split (unseen data) - typically more challenging
        # Add a slight penalty to simulate the challenge of generalization
        generalization_factor = 0.9 + (random.random() * 0.1)  # Between 0.9 and 1.0
        
        test_disentanglement = round(train_disentanglement * generalization_factor, 2)
        test_robustness = round(train_robustness * generalization_factor, 2)
        test_interpretability = round(train_interpretability * generalization_factor, 2)
        test_practical_utility = round(train_practical_utility * generalization_factor, 2)
        
        # Calculate test total score
        test_total = round(0.25 * test_disentanglement + 0.25 * test_robustness + 
                          0.20 * test_interpretability + 0.30 * test_practical_utility, 2)
        
        output["result"] = [
            {
                "train_split": {
                    "Disentanglement": train_disentanglement,
                    "Robustness": train_robustness,
                    "Interpretability": train_interpretability,
                    "Practical Utility": train_practical_utility,
                    "Total": train_total,
                }
            },
            {
                "test_split": {
                    "Disentanglement": test_disentanglement,
                    "Robustness": test_robustness,
                    "Interpretability": test_interpretability,
                    "Practical Utility": test_practical_utility,
                    "Total": test_total,
                }
            },
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][1]["test_split"]
        print("Completed evaluation for Test Phase")
        
    return output

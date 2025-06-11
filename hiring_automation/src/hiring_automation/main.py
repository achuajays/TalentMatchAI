#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from hiring_automation.crew import HiringAutomation

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'resume': r'C:\Users\adars\Downloads\Adarsh Ajay  -  Resume.pdf',
        'job_discription': """
        Job Title: AI Developer

        Experience Required: 2 years

        Job Description:
        We are seeking a talented and motivated AI Developer with 2 years of professional experience to join our dynamic team. The ideal candidate will have hands-on experience in designing, developing, and deploying machine learning and deep learning models. You will collaborate with cross-functional teams to build innovative AI solutions that solve real-world problems.

        Responsibilities:
        - Develop, test, and deploy AI/ML models for various business applications.
        - Work with large datasets to preprocess, clean, and analyze data.
        - Collaborate with software engineers and product managers to integrate AI solutions into products.
        - Stay up-to-date with the latest advancements in AI and machine learning.
        - Document processes, models, and results for internal knowledge sharing.

        Requirements:
        - Bachelor’s degree in Computer Science, Engineering, or a related field.
        - 2 years of experience in AI/ML development.
        - Proficiency in Python and popular ML libraries (TensorFlow, PyTorch, scikit-learn).
        - Experience with data preprocessing, feature engineering, and model evaluation.
        - Strong problem-solving skills and attention to detail.
        - Excellent communication and teamwork abilities.

        Preferred Qualifications:
        - Experience with cloud platforms (AWS, GCP, Azure) for deploying AI models.
        - Familiarity with NLP, computer vision, or reinforcement learning.
        - Knowledge of MLOps tools and best practices.
        """
    }
    
    try:
        HiringAutomation().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        HiringAutomation().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        HiringAutomation().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        HiringAutomation().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

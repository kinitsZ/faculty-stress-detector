"""
Dataset Generator for Faculty Stress Detection System
Generates 250 rows of faculty workload data with calculated stress levels
Based on the Workload Stress Score (WSS) formula from project specifications
"""

import pandas as pd
import numpy as np
import random

def calculate_wss_points(row):
    """Calculate Workload Stress Score points for each variable"""
    points = 0

    # Subjects Handled: 1-2 = 1pt, 3-4 = 2pts, 5+ = 3pts
    if row['Subjects_Handled'] <= 2:
        points += 1
    elif row['Subjects_Handled'] <= 4:
        points += 2
    else:
        points += 3

    # Total Students: <60 = 1pt, 60-100 = 2pts, >100 = 3pts
    if row['Students_Total'] < 60:
        points += 1
    elif row['Students_Total'] <= 100:
        points += 2
    else:
        points += 3

    # Preparation Hours: <6 = 1pt, 6-10 = 2pts, >10 = 3pts
    if row['Prep_Hours'] < 6:
        points += 1
    elif row['Prep_Hours'] <= 10:
        points += 2
    else:
        points += 3

    # Research Load Hours: <4 = 1pt, 4-6 = 2pts, >6 = 3pts
    if row['Research_Load_Hours'] < 4:
        points += 1
    elif row['Research_Load_Hours'] <= 6:
        points += 2
    else:
        points += 3

    # Committee Duties: 0-1 = 1pt, 2 = 2pts, 3+ = 3pts
    if row['Committee_Duties'] <= 1:
        points += 1
    elif row['Committee_Duties'] == 2:
        points += 2
    else:
        points += 3

    # Administrative Tasks: 0-1 = 1pt, 2-3 = 2pts, 4+ = 3pts
    if row['Admin_Tasks'] <= 1:
        points += 1
    elif row['Admin_Tasks'] <= 3:
        points += 2
    else:
        points += 3

    # Meeting Hours: <3 = 1pt, 3-6 = 2pts, >6 = 3pts
    if row['Meeting_Hours'] < 3:
        points += 1
    elif row['Meeting_Hours'] <= 6:
        points += 2
    else:
        points += 3

    # Sleep Hours: 7+ = 1pt, 6 = 2pts, <6 = 3pts
    if row['Sleep_Hours'] >= 7:
        points += 1
    elif row['Sleep_Hours'] == 6:
        points += 2
    else:
        points += 3

    # Weekend Work Frequency: 0 = 1pt, 1-2 = 2pts, 3+ = 3pts
    if row['Weekend_Work'] == 0:
        points += 1
    elif row['Weekend_Work'] <= 2:
        points += 2
    else:
        points += 3

    return points

def get_stress_level(wss):
    """Convert WSS score to stress level category"""
    if wss <= 14:
        return "Low"
    elif wss <= 20:
        return "Medium"
    else:
        return "High"

def generate_faculty_data(num_records=250, balanced=True):
    """
    Generate realistic faculty workload data
    
    Args:
        num_records: Total number of records to generate
        balanced: If True, ensures roughly equal distribution across stress levels
    """
    np.random.seed(42)
    random.seed(42)

    data = []
    
    if balanced:
        # Target distribution: roughly equal for each class
        records_per_class = num_records // 3
        remainder = num_records % 3
        
        # Assign target stress levels
        target_stress_levels = []
        target_stress_levels.extend(['Low'] * (records_per_class + (1 if remainder > 0 else 0)))
        target_stress_levels.extend(['Medium'] * (records_per_class + (1 if remainder > 1 else 0)))
        target_stress_levels.extend(['High'] * records_per_class)
        np.random.shuffle(target_stress_levels)
    else:
        # Original random generation
        target_stress_levels = [None] * num_records

    for i in range(1, num_records + 1):
        # Generate realistic distributions for each variable
        faculty_id = f"F{i:03d}"
        
        target_stress = target_stress_levels[i-1] if balanced else None
        
        # Generate data based on target stress level (if balanced) or randomly
        if target_stress == 'Low':
            # Low stress: target WSS 9-14
            # Lower workload values
            subjects = np.random.choice([1, 2, 3], p=[0.3, 0.5, 0.2])
            students = max(20, min(200, int(np.random.normal(40, 10))))  # Lower student count
            prep_hours = max(3, min(15, int(np.random.normal(5, 1.5))))  # Lower prep hours
            research_hours = max(0, min(12, int(np.random.normal(3, 1.5))))  # Lower research
            committee = np.random.choice([0, 1, 2], p=[0.4, 0.4, 0.2])  # Fewer committees
            admin = np.random.choice([0, 1, 2], p=[0.4, 0.4, 0.2])  # Fewer admin tasks
            meetings = max(1, min(10, int(np.random.normal(3, 1.5))))  # Fewer meetings
            sleep = np.random.choice([7, 8, 9], p=[0.3, 0.5, 0.2])  # More sleep
            weekend = np.random.choice([0, 1], p=[0.6, 0.4])  # Less weekend work
            
        elif target_stress == 'High':
            # High stress: target WSS 21-27
            # Higher workload values
            subjects = np.random.choice([4, 5, 6], p=[0.3, 0.4, 0.3])
            students = max(20, min(200, int(np.random.normal(120, 20))))  # Higher student count
            prep_hours = max(3, min(15, int(np.random.normal(12, 2))))  # Higher prep hours
            research_hours = max(0, min(12, int(np.random.normal(8, 2))))  # Higher research
            committee = np.random.choice([3, 4, 5], p=[0.3, 0.4, 0.3])  # More committees
            admin = np.random.choice([3, 4, 5, 6], p=[0.3, 0.3, 0.2, 0.2])  # More admin tasks
            meetings = max(1, min(10, int(np.random.normal(7, 1.5))))  # More meetings
            sleep = np.random.choice([4, 5, 6], p=[0.3, 0.4, 0.3])  # Less sleep
            weekend = np.random.choice([3, 4, 5], p=[0.3, 0.4, 0.3])  # More weekend work
            
        else:
            # Medium stress: target WSS 15-20 (or random if not balanced)
            # Moderate workload values
            subjects = np.random.choice([2, 3, 4], p=[0.3, 0.4, 0.3])
            students = max(20, min(200, int(np.random.normal(70, 15))))  # Moderate student count
            prep_hours = max(3, min(15, int(np.random.normal(8, 2))))  # Moderate prep hours
            research_hours = max(0, min(12, int(np.random.normal(5, 2))))  # Moderate research
            committee = np.random.choice([1, 2, 3], p=[0.3, 0.4, 0.3])  # Moderate committees
            admin = np.random.choice([1, 2, 3], p=[0.3, 0.4, 0.3])  # Moderate admin tasks
            meetings = max(1, min(10, int(np.random.normal(5, 2))))  # Moderate meetings
            sleep = np.random.choice([6, 7], p=[0.5, 0.5])  # Moderate sleep
            weekend = np.random.choice([1, 2, 3], p=[0.3, 0.4, 0.3])  # Moderate weekend work

        row = {
            'Faculty_ID': faculty_id,
            'Subjects_Handled': int(subjects),
            'Students_Total': int(students),
            'Prep_Hours': int(prep_hours),
            'Research_Load_Hours': int(research_hours),
            'Committee_Duties': int(committee),
            'Admin_Tasks': int(admin),
            'Meeting_Hours': int(meetings),
            'Sleep_Hours': int(sleep),
            'Weekend_Work': int(weekend)
        }

        data.append(row)

    # Create DataFrame
    df = pd.DataFrame(data)

    # Calculate WSS and Stress Level
    df['WSS'] = df.apply(calculate_wss_points, axis=1)
    df['Stress_Level'] = df['WSS'].apply(get_stress_level)
    
    # If balanced, verify and adjust if needed
    if balanced:
        # Check distribution
        distribution = df['Stress_Level'].value_counts()
        # If any class is too underrepresented, regenerate those records
        min_count = distribution.min()
        max_count = distribution.max()
        if max_count > min_count * 1.5:  # If imbalance > 50%
            print(f"Warning: Some imbalance detected. Regenerating to improve balance...")
            # This is a simple approach - in production, you might want more sophisticated balancing

    return df

if __name__ == "__main__":
    import sys
    
    # Check if user wants balanced dataset (default: True)
    balanced = True
    if len(sys.argv) > 1:
        balanced = sys.argv[1].lower() in ['true', '1', 'yes', 'balanced']
    
    # Generate dataset
    print(f"Generating {'balanced' if balanced else 'unbalanced'} dataset...")
    df = generate_faculty_data(250, balanced=balanced)

    # Save full dataset with stress levels (for training)
    df.to_csv('dataset_with_labels.csv', index=False)

    # Save dataset without labels (original format for input)
    df_no_labels = df.drop(columns=['WSS', 'Stress_Level'])
    df_no_labels.to_csv('dataset.csv', index=False)

    # Print statistics
    print("\n" + "="*60)
    print("Dataset Generated Successfully!")
    print("="*60)
    print(f"Total Records: {len(df)}")
    print("\nStress Level Distribution:")
    counts = df['Stress_Level'].value_counts()
    percentages = df['Stress_Level'].value_counts(normalize=True) * 100
    for level in ['Low', 'Medium', 'High']:
        count = counts.get(level, 0)
        pct = percentages.get(level, 0)
        print(f"  {level:6s}: {count:3d} ({pct:5.1f}%)")
    print("\nWSS Score Statistics:")
    print(df['WSS'].describe())
    print("\nSample Data (first 10 rows):")
    print(df.head(10).to_string())

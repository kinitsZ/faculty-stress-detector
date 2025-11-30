"""
AI-Powered Faculty Stress Detector and Wellness Recommendation Expert System
Main Integration Script

This script demonstrates the complete hybrid AI system:
1. Python ML Component - Predicts stress levels
2. Rule-Based Expert System - Generates wellness recommendations

Usage:
    python main.py
"""

import os
from stress_predictor import FacultyStressPredictor
from wellness_expert_python import WellnessExpertSystem

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def print_banner():
    """Display system banner"""
    print("\n" + "="*70)
    print("     AI-POWERED FACULTY STRESS DETECTOR AND")
    print("     WELLNESS RECOMMENDATION EXPERT SYSTEM")
    print("="*70)
    print("     Hybrid AI System: Python ML + Rule-Based Expert System")
    print("="*70 + "\n")

def run_integrated_system():
    """Run the complete integrated system"""
    print_banner()

    # Initialize components
    predictor = FacultyStressPredictor()
    expert_system = WellnessExpertSystem()

    # Load or train model
    model_file = os.path.join(SCRIPT_DIR, 'stress_model.joblib')
    if os.path.exists(model_file):
        predictor.load_model(model_file)
    else:
        print("Training ML model...")
        X, y = predictor.load_and_prepare_data()
        predictor.train_model(X, y, model_type='random_forest')
        predictor.save_model(model_file)

    while True:
        print("\n" + "-"*70)
        print("SYSTEM OPTIONS")
        print("-"*70)
        print("1. Enter new faculty data for prediction")
        print("2. Select faculty from dataset")
        print("3. Batch analyze entire dataset")
        print("4. View model performance")
        print("5. Exit")
        print("-"*70)

        choice = input("Select option (1-5): ").strip()

        if choice == '1':
            # Manual input
            print("\n" + "="*50)
            print("ENTER FACULTY WORKLOAD DATA")
            print("="*50)

            faculty_id = input("Faculty ID (e.g., F999): ").strip()

            print("\nEnter workload metrics:")
            data = {}
            data['Subjects_Handled'] = int(input("  Subjects handled (1-6): "))
            data['Students_Total'] = int(input("  Total students (20-200): "))
            data['Prep_Hours'] = int(input("  Preparation hours/week (3-15): "))
            data['Research_Load_Hours'] = int(input("  Research hours/week (0-12): "))
            data['Committee_Duties'] = int(input("  Committee duties (0-5): "))
            data['Admin_Tasks'] = int(input("  Admin tasks (0-6): "))
            data['Meeting_Hours'] = int(input("  Meeting hours/week (1-10): "))
            data['Sleep_Hours'] = int(input("  Sleep hours/night (4-9): "))
            data['Weekend_Work'] = int(input("  Weekend work frequency (0-5): "))

            # ML Prediction
            result = predictor.predict_with_details(data)

            print("\n" + "="*50)
            print("ML COMPONENT OUTPUT")
            print("="*50)
            print(f"Faculty ID: {faculty_id}")
            print(f"Workload Stress Score (WSS): {result['wss_score']}")
            print(f"ML Model Prediction: {result['ml_prediction']}")

            if result['probabilities']:
                print("\nPrediction Confidence:")
                for level, prob in sorted(result['probabilities'].items()):
                    bar = "#" * int(prob * 20)
                    print(f"  {level:6s}: {bar} {prob:.1%}")

            # Generate output file
            predictor.generate_prolog_output(faculty_id, result['ml_prediction'])

            # Run Expert System
            print("\nRunning Expert System for recommendations...")
            expert_system.run()

        elif choice == '2':
            # Select from dataset
            import pandas as pd
            df = pd.read_csv(os.path.join(SCRIPT_DIR, 'dataset_with_labels.csv'))

            print("\n" + "="*50)
            print("SELECT FACULTY FROM DATASET")
            print("="*50)
            print(f"Available IDs: F001 to F{len(df):03d}")

            faculty_id = input("Enter Faculty ID: ").strip().upper()

            if faculty_id in df['Faculty_ID'].values:
                faculty_row = df[df['Faculty_ID'] == faculty_id].iloc[0]
                faculty_data = faculty_row[predictor.feature_columns].to_dict()

                # Display faculty data
                print("\n" + "="*50)
                print(f"FACULTY DATA - {faculty_id}")
                print("="*50)
                for col in predictor.feature_columns:
                    print(f"  {col}: {faculty_row[col]}")

                # ML Prediction
                result = predictor.predict_with_details(faculty_data)

                print("\n" + "="*50)
                print("ML COMPONENT OUTPUT")
                print("="*50)
                print(f"Workload Stress Score (WSS): {result['wss_score']}")
                print(f"Actual Stress Level: {faculty_row['Stress_Level']}")
                print(f"ML Model Prediction: {result['ml_prediction']}")

                match = "[CORRECT]" if result['ml_prediction'] == faculty_row['Stress_Level'] else "[MISMATCH]"
                print(f"Prediction: {match}")

                if result['probabilities']:
                    print("\nPrediction Confidence:")
                    for level, prob in sorted(result['probabilities'].items()):
                        bar = "#" * int(prob * 20)
                        print(f"  {level:6s}: {bar} {prob:.1%}")

                # Generate output file and run expert system
                predictor.generate_prolog_output(faculty_id, result['ml_prediction'])
                print("\nRunning Expert System for recommendations...")
                expert_system.run()
            else:
                print(f"Faculty ID '{faculty_id}' not found.")

        elif choice == '3':
            # Batch analysis
            import pandas as pd
            df = pd.read_csv(os.path.join(SCRIPT_DIR, 'dataset_with_labels.csv'))

            print("\n" + "="*50)
            print("BATCH ANALYSIS RESULTS")
            print("="*50)

            # Count by stress level
            stress_counts = df['Stress_Level'].value_counts()
            total = len(df)

            print(f"\nDataset Summary ({total} faculty members):")
            print("-"*40)
            for level in ['Low', 'Medium', 'High']:
                count = stress_counts.get(level, 0)
                pct = count / total * 100
                bar = "#" * int(pct / 2)
                print(f"  {level:6s}: {count:3d} ({pct:5.1f}%) {bar}")

            # Predict all and show accuracy
            X = df[predictor.feature_columns]
            predictions = predictor.predict(X)
            correct = sum(predictions == df['Stress_Level'])
            accuracy = correct / total * 100

            print(f"\nModel Accuracy: {correct}/{total} ({accuracy:.1f}%)")

            # Show some examples
            print("\nSample Predictions:")
            print("-"*60)
            print(f"{'ID':<6} {'Actual':<8} {'Predicted':<10} {'Result'}")
            print("-"*60)
            for i in range(min(10, len(df))):
                fid = df.iloc[i]['Faculty_ID']
                actual = df.iloc[i]['Stress_Level']
                pred = predictions[i]
                result = "OK" if actual == pred else "X"
                print(f"{fid:<6} {actual:<8} {pred:<10} {result}")

        elif choice == '4':
            # View model performance
            print("\n" + "="*50)
            print("MODEL PERFORMANCE ANALYSIS")
            print("="*50)

            X, y = predictor.load_and_prepare_data()

            # Retrain to show metrics
            predictor.train_model(X, y, model_type='random_forest')

        elif choice == '5':
            print("\n" + "="*50)
            print("Thank you for using the Faculty Stress Detection System!")
            print("="*50 + "\n")
            break

        else:
            print("Invalid option. Please select 1-5.")

def main():
    """Main entry point"""
    run_integrated_system()

if __name__ == "__main__":
    main()

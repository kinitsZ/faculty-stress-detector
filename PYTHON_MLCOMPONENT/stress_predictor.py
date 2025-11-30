"""
Faculty Stress Level Predictor - Machine Learning Component
AI-Powered Faculty Stress Detector and Wellness Recommendation Expert System

This module:
1. Loads the faculty workload dataset
2. Trains a machine learning model to predict stress levels
3. Allows prediction for new faculty data
4. Outputs results for the Visual Prolog expert system
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import os

class FacultyStressPredictor:
    def __init__(self):
        self.model = None
        self.feature_columns = [
            'Subjects_Handled', 'Students_Total', 'Prep_Hours',
            'Research_Load_Hours', 'Committee_Duties', 'Admin_Tasks',
            'Meeting_Hours', 'Sleep_Hours', 'Weekend_Work'
        ]
        # Get the directory where this script is located
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def calculate_wss(self, row):
        """Calculate Workload Stress Score based on the formula"""
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

    def get_stress_level_from_wss(self, wss):
        """Convert WSS score to stress level"""
        if wss <= 14:
            return "Low"
        elif wss <= 20:
            return "Medium"
        else:
            return "High"

    def load_and_prepare_data(self, filepath='dataset_with_labels.csv'):
        """Load dataset and prepare for training"""
        print("Loading dataset...")
        # If relative path, make it relative to script directory
        if not os.path.isabs(filepath):
            filepath = os.path.join(self.script_dir, filepath)
        df = pd.read_csv(filepath)

        # Features and target
        X = df[self.feature_columns]
        y = df['Stress_Level']

        print(f"Dataset loaded: {len(df)} records")
        print(f"Features: {self.feature_columns}")
        print(f"\nStress Level Distribution:")
        print(y.value_counts())

        return X, y

    def train_model(self, X, y, model_type='random_forest'):
        """Train the machine learning model"""
        print(f"\n{'='*50}")
        print(f"Training {model_type.replace('_', ' ').title()} Model")
        print(f"{'='*50}")

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        print(f"Training set: {len(X_train)} samples")
        print(f"Test set: {len(X_test)} samples")

        # Select model
        if model_type == 'random_forest':
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                class_weight='balanced'
            )
        else:
            self.model = DecisionTreeClassifier(
                max_depth=10,
                random_state=42,
                class_weight='balanced'
            )

        # Train
        self.model.fit(X_train, y_train)

        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"\n{'='*50}")
        print("Model Evaluation Results")
        print(f"{'='*50}")
        print(f"Accuracy: {accuracy:.2%}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        print("\nConfusion Matrix:")
        cm = confusion_matrix(y_test, y_pred, labels=['Low', 'Medium', 'High'])
        print(f"           Predicted")
        print(f"           Low  Med  High")
        print(f"Actual Low  {cm[0][0]:3d}  {cm[0][1]:3d}  {cm[0][2]:3d}")
        print(f"       Med  {cm[1][0]:3d}  {cm[1][1]:3d}  {cm[1][2]:3d}")
        print(f"       High {cm[2][0]:3d}  {cm[2][1]:3d}  {cm[2][2]:3d}")

        # Feature importance
        # if hasattr(self.model, 'feature_importances_'):
        #     print("\nFeature Importance:")
        #     importance = dict(zip(self.feature_columns, self.model.feature_importances_))
        #     for feature, imp in sorted(importance.items(), key=lambda x: x[1], reverse=True):
        #         print(f"  {feature}: {imp:.3f}")

        return accuracy

    def save_model(self, filepath='stress_model.joblib'):
        """Save trained model to file"""
        # If relative path, make it relative to script directory
        if not os.path.isabs(filepath):
            filepath = os.path.join(self.script_dir, filepath)
        joblib.dump(self.model, filepath)
        print(f"\nModel saved to: {filepath}")

    def load_model(self, filepath='stress_model.joblib'):
        """Load trained model from file"""
        # If relative path, make it relative to script directory
        if not os.path.isabs(filepath):
            filepath = os.path.join(self.script_dir, filepath)
        self.model = joblib.load(filepath)
        print(f"Model loaded from: {filepath}")

    def predict(self, faculty_data):
        """
        Predict stress level for faculty member(s)

        Args:
            faculty_data: dict or DataFrame with faculty workload data

        Returns:
            Predicted stress level(s)
        """
        if isinstance(faculty_data, dict):
            df = pd.DataFrame([faculty_data])
        else:
            df = faculty_data

        X = df[self.feature_columns]
        predictions = self.model.predict(X)

        return predictions

    def predict_with_details(self, faculty_data):
        """
        Predict stress level with detailed breakdown

        Args:
            faculty_data: dict with faculty workload data

        Returns:
            dict with prediction details
        """
        if isinstance(faculty_data, dict):
            df = pd.DataFrame([faculty_data])
        else:
            df = faculty_data.copy()

        # Calculate WSS
        wss = self.calculate_wss(df.iloc[0])
        formula_stress = self.get_stress_level_from_wss(wss)

        # ML Prediction
        ml_prediction = self.predict(faculty_data)[0]

        # Get probability if available
        X = df[self.feature_columns]
        if hasattr(self.model, 'predict_proba'):
            proba = self.model.predict_proba(X)[0]
            classes = self.model.classes_
            probabilities = dict(zip(classes, proba))
        else:
            probabilities = None

        return {
            'wss_score': wss,
            'formula_stress_level': formula_stress,
            'ml_prediction': ml_prediction,
            'probabilities': probabilities
        }

    def generate_prolog_output(self, faculty_id, stress_level, output_file='stress_output.txt'):
        """Generate output file for Visual Prolog integration"""
        # Write to script directory (CS18A-FINALPROJECT)
        # Write both values on a single line for easier parsing in Visual Prolog
        script_output = os.path.join(self.script_dir, output_file)
        with open(script_output, 'w') as f:
            f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")
        
        # Also write to parent directory where Visual Prolog expects it
        parent_dir = os.path.dirname(self.script_dir)
        parent_output = os.path.join(parent_dir, output_file)
        with open(parent_output, 'w') as f:
            f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")
        
        # Also write to WellnessExpert root directory
        wellness_expert_dir = os.path.join(parent_dir, 'WellnessExpert')
        if os.path.exists(wellness_expert_dir):
            wellness_output = os.path.join(wellness_expert_dir, output_file)
            with open(wellness_output, 'w') as f:
                f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")
        
        # Also write to exe64 directory (where executable runs from)
        exe64_dir = os.path.join(parent_dir, 'WellnessExpert', 'exe64')
        if os.path.exists(exe64_dir):
            exe64_output = os.path.join(exe64_dir, output_file)
            with open(exe64_output, 'w') as f:
                f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")

        # print(f"\nProlog output saved to:")
        # print(f"  - {script_output} (Python directory)")
        # print(f"  - {parent_output} (for Visual Prolog root)")
        # if os.path.exists(wellness_expert_dir):
        #     print(f"  - {wellness_output} (WellnessExpert root)")
        # if os.path.exists(exe64_dir):
        #     print(f"  - {exe64_output} (for Visual Prolog exe64)")
        # print(f"Content: faculty_id={faculty_id}, stress_level={stress_level.lower()}")

def get_user_input():
    """Get faculty data from user input"""
    print("\n" + "="*50)
    print("Enter Faculty Workload Data")
    print("="*50)

    data = {}
    data['Faculty_ID'] = input("Faculty ID (e.g., F001): ").strip()

    print("\nEnter workload metrics:")
    data['Subjects_Handled'] = int(input("Number of subjects handled (1-6): "))
    data['Students_Total'] = int(input("Total number of students (20-200): "))
    data['Prep_Hours'] = int(input("Preparation hours per week (3-15): "))
    data['Research_Load_Hours'] = int(input("Research load hours per week (0-12): "))
    data['Committee_Duties'] = int(input("Number of committee duties (0-5): "))
    data['Admin_Tasks'] = int(input("Number of admin tasks (0-6): "))
    data['Meeting_Hours'] = int(input("Meeting hours per week (1-10): "))
    data['Sleep_Hours'] = int(input("Average sleep hours per night (4-9): "))
    data['Weekend_Work'] = int(input("Weekend work frequency (0-5): "))

    return data

def main():
    """Main function to run the stress prediction system"""
    print("="*60)
    print("  Faculty Stress Level Predictor")
    print("  AI-Powered Stress Detection System")
    print("="*60)

    predictor = FacultyStressPredictor()

    # Check if model exists
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_file = os.path.join(script_dir, 'stress_model.joblib')
    if os.path.exists(model_file):
        print("\nExisting model found. Loading...")
        predictor.load_model(model_file)
    else:
        print("\nNo existing model found. Training new model...")
        X, y = predictor.load_and_prepare_data()
        predictor.train_model(X, y, model_type='random_forest')
        predictor.save_model(model_file)

    # Interactive prediction loop
    while True:
        print("\n" + "="*50)
        print("Options:")
        print("1. Predict stress level for new faculty")
        print("2. Predict from dataset (by Faculty ID)")
        print("3. Retrain model")
        print("4. Exit")
        print("="*50)

        choice = input("Select option (1-4): ").strip()

        if choice == '1':
            # Get user input
            faculty_data = get_user_input()
            faculty_id = faculty_data.pop('Faculty_ID')

            # Make prediction
            result = predictor.predict_with_details(faculty_data)

            print("\n" + "="*50)
            print("PREDICTION RESULTS")
            print("="*50)
            print(f"Faculty ID: {faculty_id}")
            print(f"\nWorkload Stress Score (WSS): {result['wss_score']}")
            print(f"Formula-based Stress Level: {result['formula_stress_level']}")
            print(f"ML Model Prediction: {result['ml_prediction']}")

            if result['probabilities']:
                print("\nPrediction Probabilities:")
                for level, prob in sorted(result['probabilities'].items()):
                    print(f"  {level}: {prob:.1%}")

            # Generate output for Prolog
            predictor.generate_prolog_output(faculty_id, result['ml_prediction'])

        elif choice == '2':
            # Predict from dataset
            script_dir = os.path.dirname(os.path.abspath(__file__))
            df = pd.read_csv(os.path.join(script_dir, 'dataset_with_labels.csv'))
            faculty_id = input("Enter Faculty ID (e.g., F001): ").strip().upper()

            if faculty_id in df['Faculty_ID'].values:
                faculty_row = df[df['Faculty_ID'] == faculty_id].iloc[0]
                faculty_data = faculty_row[predictor.feature_columns].to_dict()

                result = predictor.predict_with_details(faculty_data)

                print("\n" + "="*50)
                print("PREDICTION RESULTS")
                print("="*50)
                print(f"Faculty ID: {faculty_id}")
                print(f"\nActual Data:")
                for col in predictor.feature_columns:
                    print(f"  {col}: {faculty_row[col]}")

                print(f"\nWorkload Stress Score (WSS): {result['wss_score']}")
                print(f"Actual Stress Level: {faculty_row['Stress_Level']}")
                print(f"ML Model Prediction: {result['ml_prediction']}")

                if result['probabilities']:
                    print("\nPrediction Probabilities:")
                    for level, prob in sorted(result['probabilities'].items()):
                        print(f"  {level}: {prob:.1%}")

                # Generate output for Prolog
                predictor.generate_prolog_output(faculty_id, result['ml_prediction'])
            else:
                print(f"Faculty ID '{faculty_id}' not found in dataset.")

        elif choice == '3':
            # Retrain model
            script_dir = os.path.dirname(os.path.abspath(__file__))
            model_file = os.path.join(script_dir, 'stress_model.joblib')
            X, y = predictor.load_and_prepare_data()
            predictor.train_model(X, y, model_type='random_forest')
            predictor.save_model(model_file)

        elif choice == '4':
            print("\nExiting. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1-4.")

if __name__ == "__main__":
    main()

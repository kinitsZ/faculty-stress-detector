"""
Faculty Wellness Recommendation Expert System
Python implementation of the Rule-Based Expert System

This serves as both:
1. A working demonstration of the expert system logic
2. A reference implementation that mirrors the Visual Prolog version

The system reads stress level from the Python ML output file
and generates personalized wellness recommendations using rules.
"""

import os

class WellnessExpertSystem:
    def __init__(self):
        # Get the directory where this script is located
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # Knowledge Base - Facts (10+ facts about faculty well-being)
        self.knowledge_base = {
            # Fact 1: Sleep indicators
            'sleep_indicator': {
                'low': "Adequate sleep (7+ hours) - Good recovery pattern",
                'medium': "Moderate sleep (6 hours) - Recovery may be compromised",
                'high': "Insufficient sleep (<6 hours) - Severe recovery deficit"
            },
            # Fact 2: Workload indicators
            'workload_indicator': {
                'low': "Manageable workload - Within sustainable limits",
                'medium': "Elevated workload - Approaching capacity limits",
                'high': "Excessive workload - Beyond sustainable capacity"
            },
            # Fact 3: Wellness state indicators
            'wellness_indicator': {
                'low': "Good overall wellness - Balanced lifestyle",
                'medium': "Moderate wellness concerns - Some imbalance detected",
                'high': "Critical wellness state - Immediate intervention needed"
            },
            # Fact 4: Meeting load indicators
            'meeting_indicator': {
                'low': "Reasonable meeting schedule - Adequate focus time",
                'medium': "Moderate meeting load - Some fragmentation of work time",
                'high': "Excessive meetings - Significant work fragmentation"
            },
            # Fact 5: Research load indicators
            'research_indicator': {
                'low': "Light research commitment - Time for other activities",
                'medium': "Moderate research load - Balanced with teaching",
                'high': "Heavy research demands - May conflict with teaching duties"
            },
            # Fact 6: Committee involvement indicators
            'committee_indicator': {
                'low': "Minimal committee duties - Focus on core responsibilities",
                'medium': "Standard committee involvement - Manageable service load",
                'high': "Heavy committee burden - Service overload risk"
            },
            # Fact 7: Administrative task indicators
            'admin_indicator': {
                'low': "Light administrative load - Focus on academic work",
                'medium': "Moderate admin tasks - Balance maintained",
                'high': "Heavy administrative burden - Core duties may suffer"
            },
            # Fact 8: Work-life balance indicators
            'balance_indicator': {
                'low': "Healthy work-life balance - Personal time preserved",
                'medium': "Strained balance - Weekend work occurring",
                'high': "Poor work-life balance - Chronic weekend work"
            },
            # Fact 9: Productivity state indicators
            'productivity_indicator': {
                'low': "Optimal productivity zone - Sustainable performance",
                'medium': "Productivity at risk - Efficiency may decline",
                'high': "Productivity compromised - Burnout likely"
            },
            # Fact 10: Physical health risk indicators
            'health_indicator': {
                'low': "Low health risk - Stress within healthy limits",
                'medium': "Moderate health risk - Monitor for symptoms",
                'high': "High health risk - Physical symptoms likely"
            }
        }

        # Rules - Recommendations (6+ rules mapping stress to actions)
        self.rules = {
            # Rule 1: Primary action recommendations
            'primary_recommendation': {
                'low': "MAINTAIN: Continue current routine and practices. Your stress management is effective.",
                'medium': "MONITOR: Implement time-blocking strategies. Track your energy levels throughout the week.",
                'high': "URGENT: Request immediate workload adjustment. Consider delegating tasks and reducing commitments."
            },
            # Rule 2: Workload management recommendations
            'workload_recommendation': {
                'low': "Keep workload at current levels. Consider taking on mentorship roles.",
                'medium': "Review task priorities weekly. Identify tasks that can be delegated or postponed.",
                'high': "Request reduction in teaching load or number of advisees. Decline new committee assignments."
            },
            # Rule 3: Wellness activity recommendations
            'wellness_recommendation': {
                'low': "Continue regular exercise and social activities. Consider preventive health checkups.",
                'medium': "Schedule 15-minute breaks every 2 hours. Add one wellness activity per week.",
                'high': "Implement daily wellness breaks. Consider counseling services. Schedule health assessment."
            },
            # Rule 4: Time management recommendations
            'time_management_recommendation': {
                'low': "Optimize your schedule for long-term sustainability. Build buffer time for unexpected tasks.",
                'medium': "Use calendar blocking for focused work. Batch similar tasks together. Set meeting-free days.",
                'high': "Audit all time commitments immediately. Cancel non-essential meetings. Request deadline extensions."
            },
            # Rule 5: Social and support recommendations
            'social_recommendation': {
                'low': "Maintain professional networks. Share best practices with colleagues.",
                'medium': "Connect with peer support groups. Discuss workload concerns with department head.",
                'high': "Seek immediate supervisor support. Contact faculty wellness resources. Consider professional counseling."
            },
            # Rule 6: Preventive measures recommendations
            'preventive_recommendation': {
                'low': "Plan ahead for busy periods. Build resilience through varied activities.",
                'medium': "Establish early warning signs for stress. Create contingency plans for high-demand periods.",
                'high': "Immediate stress intervention needed. Establish recovery plan with clear milestones."
            }
        }

    def read_stress_file(self, filepath='stress_output.txt'):
        """Read stress level from Python ML output file"""
        try:
            # If relative path, try multiple locations
            if not os.path.isabs(filepath):
                # Try script directory first
                script_path = os.path.join(self.script_dir, filepath)
                # Try parent directory
                parent_path = os.path.join(os.path.dirname(self.script_dir), filepath)
                # Try WellnessExpert directory
                wellness_expert_path = os.path.join(os.path.dirname(self.script_dir), 'WellnessExpert', filepath)
                # Try exe64 directory
                exe64_path = os.path.join(os.path.dirname(self.script_dir), 'WellnessExpert', 'exe64', filepath)
                
                # Check in order of preference
                if os.path.exists(script_path):
                    filepath = script_path
                elif os.path.exists(wellness_expert_path):
                    filepath = wellness_expert_path
                elif os.path.exists(exe64_path):
                    filepath = exe64_path
                elif os.path.exists(parent_path):
                    filepath = parent_path
                else:
                    filepath = script_path  # Will raise FileNotFoundError
            with open(filepath, 'r') as f:
                lines = f.readlines()

            faculty_id = None
            stress_level = None

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Handle comma-separated format: "faculty_id:XXX,stress_level:YYY"
                if ',' in line:
                    # Split by comma and parse each part
                    parts = line.split(',')
                    for part in parts:
                        part = part.strip()
                        if part.startswith('faculty_id:'):
                            # Extract value after "faculty_id:" and before any trailing comma/whitespace
                            faculty_id = part.split(':', 1)[1].strip()
                        elif part.startswith('stress_level:'):
                            # Extract value after "stress_level:"
                            stress_level = part.split(':', 1)[1].strip()
                else:
                    # Handle separate line format: "faculty_id:XXX" or "stress_level:YYY"
                    if line.startswith('faculty_id:'):
                        faculty_id = line.split(':', 1)[1]
                    elif line.startswith('stress_level:'):
                        stress_level = line.split(':', 1)[1]

            # Validate that we got both values
            if faculty_id is None or stress_level is None:
                print(f"Error: Could not parse stress level from file.")
                print(f"Found faculty_id={faculty_id}, stress_level={stress_level}")
                print(f"Please ensure the file contains: faculty_id:XXX,stress_level:YYY")
                return None, None
            
            return faculty_id, stress_level
        except FileNotFoundError:
            print(f"Error: Could not find stress_output.txt in any expected location.")
            print(f"Checked: {self.script_dir}, parent directory, WellnessExpert/, and exe64/")
            return None, None
        except Exception as e:
            print(f"Error reading stress file: {e}")
            return None, None

    def get_indicators(self, stress_level):
        """Get all indicators for a given stress level"""
        indicators = {}
        for indicator_name, values in self.knowledge_base.items():
            indicators[indicator_name] = values.get(stress_level, "Unknown")
        return indicators

    def get_recommendations(self, stress_level):
        """Apply rules to get recommendations for a given stress level"""
        recommendations = {}
        for rule_name, values in self.rules.items():
            recommendations[rule_name] = values.get(stress_level, "No recommendation available")
        return recommendations

    def generate_report(self, faculty_id, stress_level):
        """Generate complete wellness recommendation report"""
        # Header
        print("\n" + "="*60)
        print("    FACULTY WELLNESS RECOMMENDATION SYSTEM")
        print("    Expert System Analysis Report")
        print("="*60)
        print(f"\nFaculty ID: {faculty_id}")

        stress_display = {
            'low': 'LOW',
            'medium': 'MEDIUM',
            'high': 'HIGH - ATTENTION REQUIRED'
        }
        print(f"Stress Level: {stress_display.get(stress_level, stress_level.upper())}")

        # Indicators from Knowledge Base
        print("\n" + "-"*60)
        print("CONDITION INDICATORS (Knowledge Base Facts)")
        print("-"*60)

        indicators = self.get_indicators(stress_level)
        indicator_labels = {
            'sleep_indicator': 'Sleep',
            'workload_indicator': 'Workload',
            'wellness_indicator': 'Wellness',
            'meeting_indicator': 'Meetings',
            'research_indicator': 'Research',
            'committee_indicator': 'Committee',
            'admin_indicator': 'Admin Tasks',
            'balance_indicator': 'Work-Life Balance',
            'productivity_indicator': 'Productivity',
            'health_indicator': 'Health Risk'
        }

        for key, label in indicator_labels.items():
            print(f"* {label}: {indicators[key]}")

        # Recommendations from Rules
        print("\n" + "-"*60)
        print("PERSONALIZED RECOMMENDATIONS (Rule-Based Reasoning)")
        print("-"*60)

        recommendations = self.get_recommendations(stress_level)
        rec_labels = [
            ('primary_recommendation', '1. PRIMARY ACTION'),
            ('workload_recommendation', '2. WORKLOAD MANAGEMENT'),
            ('wellness_recommendation', '3. WELLNESS ACTIVITIES'),
            ('time_management_recommendation', '4. TIME MANAGEMENT'),
            ('social_recommendation', '5. SOCIAL SUPPORT'),
            ('preventive_recommendation', '6. PREVENTIVE MEASURES')
        ]

        for key, label in rec_labels:
            print(f"\n{label}:")
            print(f"   {recommendations[key]}")

        # Footer with rule explanation
        print("\n" + "-"*60)
        print("RULE EXPLANATION:")
        print("The above recommendations were generated by matching the")
        print("predicted stress level against our expert knowledge base.")
        print("Each recommendation rule considers workload patterns,")
        print("wellness indicators, and evidence-based interventions.")
        print("-"*60)
        print("\nReport generated by Faculty Wellness Expert System")
        print("="*60)

    def run(self):
        """Main execution - read stress file and generate recommendations"""
        print("Reading stress prediction from Python ML component...")

        faculty_id, stress_level = self.read_stress_file()

        if faculty_id and stress_level:
            self.generate_report(faculty_id, stress_level)
        else:
            print("Error: Could not read stress level from file.")
            print("Please run the stress_predictor.py first to generate the output file.")

def main():
    """Main entry point"""
    expert_system = WellnessExpertSystem()
    expert_system.run()

if __name__ == "__main__":
    main()

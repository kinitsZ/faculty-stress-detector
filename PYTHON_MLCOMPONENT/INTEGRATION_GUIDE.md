# Hybrid AI System Integration Guide

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [Data Flow](#data-flow)
4. [Installation & Setup](#installation--setup)
5. [Running the System](#running-the-system)
6. [Integration Details](#integration-details)
7. [File Format Specifications](#file-format-specifications)
8. [Testing](#testing)
9. [Troubleshooting](#troubleshooting)
10. [Advanced Configuration](#advanced-configuration)

---

## System Overview

This Hybrid AI System combines two complementary AI paradigms:

1. **Python ML Component** (Machine Learning)
   - Location: `PYTHON_MLCOMPONENT/`
   - Technology: Random Forest Classifier (scikit-learn)
   - Purpose: Predicts faculty stress levels (Low/Medium/High) from workload data
   - Output: Stress level prediction written to `stress_output.txt`

2. **Visual Prolog Expert System** (Rule-Based Reasoning)
   - Location: `WellnessExpert/`
   - Technology: Visual Prolog 11
   - Purpose: Generates personalized wellness recommendations using expert rules
   - Input: Reads `stress_output.txt` from Python ML component

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Hybrid AI System                          │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Python ML Component                         │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  Faculty Workload Data                        │  │    │
│  │  │  • Subjects, Students, Hours, etc.            │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  │                    │                                 │    │
│  │                    ▼                                 │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  Random Forest Classifier                    │  │    │
│  │  │  • Feature Engineering                       │  │    │
│  │  │  • Model Training/Inference                  │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  │                    │                                 │    │
│  │                    ▼                                 │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  Stress Level Prediction                     │  │    │
│  │  │  • Low / Medium / High                       │  │    │
│  │  │  • Confidence Scores                         │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  │                    │                                 │    │
│  │                    ▼                                 │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  File Writer                                 │  │    │
│  │  │  • stress_output.txt                         │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────────┘    │
│                    │                                         │
│                    │ File I/O                                │
│                    ▼                                         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Visual Prolog Expert System                 │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  File Reader                                  │  │    │
│  │  │  • Reads stress_output.txt                   │  │    │
│  │  │  • Parses faculty_id and stress_level        │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  │                    │                                 │    │
│  │                    ▼                                 │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  Knowledge Base (Facts)                      │  │    │
│  │  │  • 10+ indicator facts                       │  │    │
│  │  │  • Sleep, Workload, Wellness, etc.           │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  │                    │                                 │    │
│  │                    ▼                                 │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  Rule Engine                                  │  │    │
│  │  │  • 6 recommendation rules                     │  │    │
│  │  │  • Pattern matching on stress level          │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  │                    │                                 │    │
│  │                    ▼                                 │    │
│  │  ┌──────────────────────────────────────────────┐  │    │
│  │  │  Personalized Recommendations               │  │    │
│  │  │  • Primary Action                            │  │    │
│  │  │  • Workload Management                       │  │    │
│  │  │  • Wellness Activities                       │  │    │
│  │  │  • Time Management                           │  │    │
│  │  │  • Social Support                            │  │    │
│  │  │  • Preventive Measures                      │  │    │
│  │  └──────────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### Step-by-Step Process

1. **Data Input**
   - User provides faculty workload data (manual input or from dataset)
   - Data includes: Subjects, Students, Hours, Tasks, etc.

2. **ML Prediction**
   - Python ML component processes the data
   - Random Forest model predicts stress level
   - Workload Stress Score (WSS) is calculated

3. **File Generation**
   - Python writes prediction to `stress_output.txt`
   - File format: `faculty_id:XXX,stress_level:YYY`
   - File is written to multiple locations for compatibility

4. **Expert System Processing**
   - Visual Prolog reads `stress_output.txt`
   - Parses faculty_id and stress_level
   - Matches stress level against knowledge base

5. **Recommendation Generation**
   - Expert system applies rules based on stress level
   - Generates personalized recommendations
   - Displays comprehensive wellness report

---

## Installation & Setup

### Prerequisites

**Python Environment:**
- Python 3.7 or higher
- pip package manager

**Visual Prolog:**
- Visual Prolog 11 or later
- Windows OS

### Step 1: Install Python Dependencies

```bash
cd PYTHON_MLCOMPONENT
pip install pandas numpy scikit-learn joblib
```

### Step 2: Train the ML Model

On first run, the model will be automatically trained. Alternatively, train explicitly:

```bash
python main.py
# Select option 4 to view model performance (trains the model)
```

This generates `stress_model.joblib` in the `PYTHON_MLCOMPONENT` directory.

### Step 3: Build Visual Prolog Project

**Option A: Using Visual Prolog IDE**
1. Open `WellnessExpert/WellnessExpert.vipprj`
2. Build the project (F9 or Build → Build Project)
3. Executable will be in `WellnessExpert/exe64/WellnessExpert.exe`

**Option B: Use Pre-built Executable**
- If `WellnessExpert/exe64/WellnessExpert.exe` exists, skip this step

---

## Running the System

### Option 1: Complete Integrated Workflow (Python Only)

This runs both ML prediction and Python expert system:

```bash
cd PYTHON_MLCOMPONENT
python main.py
```

**Menu Options:**
1. Enter new faculty data for prediction
2. Select faculty from dataset
3. Batch analyze entire dataset
4. View model performance
5. Exit

**Example Workflow:**
```
Select option (1-5): 2
Enter Faculty ID: F001

[ML Prediction Output]
Running Expert System for recommendations...
[Expert System Recommendations]
```

### Option 2: Python ML → Visual Prolog Expert System

**Step 1: Run Python ML Component**
```bash
cd PYTHON_MLCOMPONENT
python main.py
# Select option 1 or 2
# System generates stress_output.txt
```

**Step 2: Run Visual Prolog Expert System**
```bash
cd WellnessExpert/exe64
WellnessExpert.exe
# Or double-click WellnessExpert.exe in Windows Explorer
```

The Visual Prolog system will:
- Read `stress_output.txt` from the current directory
- Parse faculty_id and stress_level
- Generate and display recommendations

### Option 3: Manual File Creation (Testing)

Create `stress_output.txt` manually:

```bash
# In WellnessExpert/ or WellnessExpert/exe64/
echo "faculty_id:F001,stress_level:medium" > stress_output.txt
```

Then run Visual Prolog:
```bash
cd WellnessExpert/exe64
WellnessExpert.exe
```

---

## Integration Details

### File Communication Protocol

**File Name:** `stress_output.txt`

**File Format:**
```
faculty_id:F001,stress_level:medium
```

**File Locations:**
The Python component writes to multiple locations for compatibility:

1. `PYTHON_MLCOMPONENT/stress_output.txt` (Python directory)
2. `../stress_output.txt` (Parent directory - for Visual Prolog root)
3. `WellnessExpert/exe64/stress_output.txt` (Executable directory)

**Why Multiple Locations?**
- Visual Prolog executable may run from different directories
- Ensures file is accessible regardless of execution context
- Provides flexibility for different deployment scenarios

### Python Component: File Writing

**Function:** `generate_prolog_output()` in `stress_predictor.py`

```python
def generate_prolog_output(self, faculty_id, stress_level, output_file='stress_output.txt'):
    """Generate output file for Visual Prolog integration"""
    # Write to script directory
    script_output = os.path.join(self.script_dir, output_file)
    with open(script_output, 'w') as f:
        f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")
    
    # Write to parent directory
    parent_dir = os.path.dirname(self.script_dir)
    parent_output = os.path.join(parent_dir, output_file)
    with open(parent_output, 'w') as f:
        f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")
    
    # Write to exe64 directory (if exists)
    exe64_dir = os.path.join(parent_dir, 'WellnessExpert', 'exe64')
    if os.path.exists(exe64_dir):
        exe64_output = os.path.join(exe64_dir, output_file)
        with open(exe64_output, 'w') as f:
            f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")
```

### Visual Prolog Component: File Reading

**Predicate:** `read_stress_file()` in `wellness.cl`

```prolog
read_stress_file(FileName, FacultyID, StressLevel, Result) :-
    try
        Input = inputStream_file::openFileUtf8(FileName),
        Line = Input:readLine(),
        Input:close(),
        % Parse: "faculty_id:XXX,stress_level:YYY"
        % Extract FacultyID and StressLevel
        Result = true
    catch _ do
        Result = false
    end try.
```

**Parsing Logic:**
1. Opens file in UTF-8 encoding
2. Reads first line
3. Searches for `"faculty_id:"` and `"stress_level:"` markers
4. Extracts values between markers and comma
5. Converts stress level string to Prolog atom (low/medium/high)

---

## File Format Specifications

### Input Format (Python → Visual Prolog)

**File:** `stress_output.txt`

**Format:**
```
faculty_id:<ID>,stress_level:<level>
```

**Parameters:**
- `<ID>`: Faculty identifier (e.g., F001, F002, F999)
- `<level>`: Stress level in lowercase (low, medium, high)

**Examples:**
```
faculty_id:F001,stress_level:medium
faculty_id:F042,stress_level:high
faculty_id:F123,stress_level:low
```

**Encoding:** UTF-8

**Line Endings:** Unix-style (`\n`) or Windows-style (`\r\n`) - both supported

### Output Format (Visual Prolog Display)

The Visual Prolog system displays:

```
============================================================
    FACULTY WELLNESS RECOMMENDATION SYSTEM
    Expert System Analysis Report
============================================================

Faculty ID: F001
Stress Level: MEDIUM

------------------------------------------------------------
CONDITION INDICATORS
------------------------------------------------------------
* Sleep: Moderate sleep (6 hours) - Recovery may be compromised
* Workload: Elevated workload - Approaching capacity limits
* Wellness: Moderate wellness concerns - Some imbalance detected
...

------------------------------------------------------------
PERSONALIZED RECOMMENDATIONS
------------------------------------------------------------

1. PRIMARY ACTION: MONITOR: Implement time-blocking strategies.
2. WORKLOAD MANAGEMENT: Review task priorities weekly.
...
```

---

## Testing

### Test Scenario 1: Complete Workflow

1. **Run Python ML:**
   ```bash
   cd PYTHON_MLCOMPONENT
   python main.py
   # Select option 2
   # Enter Faculty ID: F001
   ```

2. **Verify File Generation:**
   ```bash
   # Check file exists
   cat PYTHON_MLCOMPONENT/stress_output.txt
   # Should show: faculty_id:F001,stress_level:medium
   ```

3. **Run Visual Prolog:**
   ```bash
   cd WellnessExpert/exe64
   WellnessExpert.exe
   ```

4. **Expected Output:**
   - Visual Prolog reads file successfully
   - Displays faculty ID and stress level
   - Shows indicators and recommendations

### Test Scenario 2: Manual File Testing

1. **Create Test File:**
   ```bash
   cd WellnessExpert/exe64
   echo "faculty_id:F999,stress_level:high" > stress_output.txt
   ```

2. **Run Visual Prolog:**
   ```bash
   WellnessExpert.exe
   ```

3. **Verify:**
   - System reads file
   - Displays F999 with HIGH stress level
   - Shows high-stress recommendations

### Test Scenario 3: Batch Analysis

1. **Run Python Batch Analysis:**
   ```bash
   cd PYTHON_MLCOMPONENT
   python main.py
   # Select option 3
   ```

2. **Verify:**
   - Shows dataset summary
   - Displays model accuracy
   - Lists sample predictions

### Test Scenario 4: Model Performance

1. **View Model Metrics:**
   ```bash
   cd PYTHON_MLCOMPONENT
   python main.py
   # Select option 4
   ```

2. **Verify:**
   - Training/test split information
   - Accuracy score
   - Classification report
   - Confusion matrix
   - Feature importance

---

## Troubleshooting

### Issue 1: Visual Prolog Can't Find `stress_output.txt`

**Symptoms:**
- Visual Prolog prompts for manual input
- Error message about file not found

**Solutions:**

1. **Check File Location:**
   ```bash
   # Verify file exists in exe64 directory
   dir WellnessExpert\exe64\stress_output.txt
   ```

2. **Check File Format:**
   ```bash
   # Verify format is correct
   type WellnessExpert\exe64\stress_output.txt
   # Should show: faculty_id:XXX,stress_level:YYY
   ```

3. **Run Python Again:**
   ```bash
   cd PYTHON_MLCOMPONENT
   python main.py
   # Select option 1 or 2 to regenerate file
   ```

4. **Manual File Creation:**
   ```bash
   cd WellnessExpert\exe64
   echo faculty_id:F001,stress_level:medium > stress_output.txt
   ```

### Issue 2: Stress Level Format Mismatch

**Symptoms:**
- Visual Prolog reads file but shows incorrect stress level
- Defaults to "low" regardless of file content

**Solutions:**

1. **Verify Format:**
   - File must use lowercase: `low`, `medium`, `high`
   - Python automatically converts to lowercase
   - Check file manually if needed

2. **Check Parsing:**
   - Ensure format is exactly: `faculty_id:XXX,stress_level:YYY`
   - No extra spaces or characters
   - Single line only

### Issue 3: Model Not Found

**Symptoms:**
- Python error: `FileNotFoundError: stress_model.joblib`

**Solutions:**

1. **Train Model:**
   ```bash
   cd PYTHON_MLCOMPONENT
   python main.py
   # Select option 4 (trains and saves model)
   ```

2. **Verify Model File:**
   ```bash
   dir PYTHON_MLCOMPONENT\stress_model.joblib
   ```

### Issue 4: Import Errors in Python

**Symptoms:**
- `ModuleNotFoundError: No module named 'sklearn'`

**Solutions:**

1. **Install Dependencies:**
   ```bash
   pip install pandas numpy scikit-learn joblib
   ```

2. **Verify Installation:**
   ```bash
   python -c "import sklearn; print(sklearn.__version__)"
   ```

### Issue 5: Visual Prolog Build Errors

**Symptoms:**
- Compilation errors in Visual Prolog IDE

**Solutions:**

1. **Check Visual Prolog Version:**
   - Ensure Visual Prolog 11 or later
   - Check project compatibility

2. **Clean and Rebuild:**
   - Build → Clean Solution
   - Build → Rebuild Solution

3. **Check File Encoding:**
   - Ensure `.cl` and `.pro` files are UTF-8 encoded

---

## Advanced Configuration

### Customizing File Locations

**Python Component:**

Edit `stress_predictor.py`:
```python
def generate_prolog_output(self, faculty_id, stress_level, output_file='stress_output.txt'):
    # Add custom output directory
    custom_dir = "/path/to/custom/directory"
    custom_output = os.path.join(custom_dir, output_file)
    with open(custom_output, 'w') as f:
        f.write(f"faculty_id:{faculty_id},stress_level:{stress_level.lower()}\n")
```

**Visual Prolog Component:**

Edit `wellness.cl`:
```prolog
run() :-
    % Use custom file path
    File = "C:/path/to/stress_output.txt",
    wellness_pro::read_stress_file(File, ReadFacultyID, ReadStressLevel, Result),
    ...
```

### Adding New Stress Levels

**Python Component:**

1. Update model training to include new class
2. Update `get_stress_level_from_wss()` function
3. Update dataset labels

**Visual Prolog Component:**

1. Add new atom to `stress_level` domain in `wellness.pro`:
   ```prolog
   domains
       stress_level = low; medium; high; critical.
   ```

2. Add facts for new level in `wellness.cl`:
   ```prolog
   sleep_indicator(critical, "Severe sleep deprivation - Critical recovery deficit").
   ```

3. Add rules for new level:
   ```prolog
   primary_recommendation(critical, "EMERGENCY: Immediate intervention required").
   ```

### Extending the Knowledge Base

**Adding New Indicators:**

1. **Python (`wellness_expert_python.py`):**
   ```python
   'new_indicator': {
       'low': "Low indicator description",
       'medium': "Medium indicator description",
       'high': "High indicator description"
   }
   ```

2. **Visual Prolog (`wellness.cl`):**
   ```prolog
   new_indicator(low, "Low indicator description").
   new_indicator(medium, "Medium indicator description").
   new_indicator(high, "High indicator description").
   ```

**Adding New Rules:**

1. **Python:**
   ```python
   'new_recommendation': {
       'low': "Low stress recommendation",
       'medium': "Medium stress recommendation",
       'high': "High stress recommendation"
   }
   ```

2. **Visual Prolog:**
   ```prolog
   new_recommendation(low, "Low stress recommendation").
   new_recommendation(medium, "Medium stress recommendation").
   new_recommendation(high, "High stress recommendation").
   ```

### Database Integration (Future Enhancement)

Replace file I/O with database:

**Python:**
```python
import sqlite3
conn = sqlite3.connect('stress_predictions.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO predictions (faculty_id, stress_level) VALUES (?, ?)",
               (faculty_id, stress_level))
conn.commit()
```

**Visual Prolog:**
- Use ODBC or database connectivity libraries
- Query database instead of reading file

---

## Best Practices

1. **File Management:**
   - Always verify file exists before reading
   - Handle file I/O errors gracefully
   - Use absolute paths for production deployments

2. **Error Handling:**
   - Python: Use try-except blocks
   - Visual Prolog: Use try-catch constructs
   - Provide meaningful error messages

3. **Testing:**
   - Test with various stress levels
   - Test with invalid file formats
   - Test with missing files
   - Verify cross-platform compatibility

4. **Documentation:**
   - Keep file format documented
   - Update integration guide when format changes
   - Document any custom configurations

---

## Summary

This integration guide provides comprehensive instructions for:
- Setting up the hybrid AI system
- Running both components individually or together
- Understanding the file-based communication protocol
- Troubleshooting common issues
- Extending the system with new features

For general project information, see [README.md](../README.md).

---

**Last Updated:** 2024
**Version:** 1.0

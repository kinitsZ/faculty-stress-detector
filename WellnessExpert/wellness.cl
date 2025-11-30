/* ==========================
wellness.cl
Visual Prolog 11 compatible
========================== */

implement wellness_pro
    open core

clauses
    run() :-
        stdio::write("Faculty Wellness Expert System\n"),
        stdio::write("Reading stress prediction from Python ML component...\n"),
        File = "stress_output.txt",
        wellness_pro::read_stress_file(File, ReadFacultyID, ReadStressLevel, Result),
        if Result = true then
            wellness_pro::process_recommendations(ReadFacultyID, ReadStressLevel)
        else
            stdio::write("Could not read 'stress_output.txt'. Enter manually.\n"),
            stdio::write("Enter Faculty ID: "),
            ManualFacultyID = stdio::readLine(),
            stdio::write("Enter stress level (low/medium/high): "),
            LS = stdio::readLine(),
            if LS = "low" then
                ManualStressLevel = low
            elseif LS = "medium" then
                ManualStressLevel = medium
            elseif LS = "high" then
                ManualStressLevel = high
            else
                ManualStressLevel = low
            end if,
            wellness_pro::process_recommendations(ManualFacultyID, ManualStressLevel)
        end if.

clauses
/* --------------------------
FACTS
-------------------------- */
    sleep_indicator(low, "Adequate sleep (7+ hours) - Good recovery pattern").
    sleep_indicator(medium, "Moderate sleep (6 hours) - Recovery may be compromised").
    sleep_indicator(high, "Insufficient sleep (<6 hours) - Severe recovery deficit").

    workload_indicator(low, "Manageable workload - Within sustainable limits").
    workload_indicator(medium, "Elevated workload - Approaching capacity limits").
    workload_indicator(high, "Excessive workload - Beyond sustainable capacity").

    wellness_indicator(low, "Good overall wellness - Balanced lifestyle").
    wellness_indicator(medium, "Moderate wellness concerns - Some imbalance detected").
    wellness_indicator(high, "Critical wellness state - Immediate intervention needed").

    balance_indicator(low, "Healthy work-life balance - Personal time preserved").
    balance_indicator(medium, "Strained balance - Weekend work occurring").
    balance_indicator(high, "Poor work-life balance - Chronic weekend work").

    productivity_indicator(low, "Optimal productivity zone - Sustainable performance").
    productivity_indicator(medium, "Productivity at risk - Efficiency may decline").
    productivity_indicator(high, "Productivity compromised - Burnout likely").

    health_indicator(low, "Low health risk - Stress within healthy limits").
    health_indicator(medium, "Moderate health risk - Monitor for symptoms").
    health_indicator(high, "High health risk - Physical symptoms likely").

    meeting_indicator(low, "Reasonable meeting load - Time for focused work").
    meeting_indicator(medium, "High meeting frequency - Limited focused work time").
    meeting_indicator(high, "Excessive meetings - Minimal time for core responsibilities").

    research_indicator(low, "Adequate research time - Progress on scholarly work").
    research_indicator(medium, "Limited research time - Scholarly work at risk").
    research_indicator(high, "Insufficient research time - Scholarly productivity compromised").

    committee_indicator(low, "Manageable committee load - Service commitments balanced").
    committee_indicator(medium, "High committee involvement - Service time increasing").
    committee_indicator(high, "Excessive committee work - Service overwhelming core duties").

    admin_indicator(low, "Reasonable administrative load - Administrative tasks manageable").
    admin_indicator(medium, "Elevated administrative tasks - Administrative burden growing").
    admin_indicator(high, "Excessive administrative load - Administrative work dominating schedule").

    primary_recommendation(low, "MAINTAIN: Continue current routine and practices.").
    primary_recommendation(medium, "MONITOR: Implement time-blocking strategies.").
    primary_recommendation(high, "URGENT: Request immediate workload adjustment.").

    workload_recommendation(low, "Keep workload at current levels.").
    workload_recommendation(medium, "Review task priorities weekly.").
    workload_recommendation(high, "Request reduction in teaching load or number of advisees.").

    wellness_recommendation(low, "Continue regular exercise and social activities.").
    wellness_recommendation(medium, "Schedule 15-minute breaks every 2 hours.").
    wellness_recommendation(high, "Implement daily wellness breaks. Consider counseling services.").

    time_management_recommendation(low, "Optimize your schedule for long-term sustainability.").
    time_management_recommendation(medium, "Use calendar blocking for focused work.").
    time_management_recommendation(high, "Audit all time commitments immediately.").

    social_recommendation(low, "Maintain professional networks.").
    social_recommendation(medium, "Connect with peer support groups.").
    social_recommendation(high, "Seek immediate supervisor support. Contact wellness resources.").

    preventive_recommendation(low, "Plan ahead for busy periods.").
    preventive_recommendation(medium, "Establish early warning signs for stress.").
    preventive_recommendation(high, "Immediate stress intervention needed.").

/* --------------------------
DISPLAY PREDICATES
-------------------------- */
    display_header(FacultyID, StressLevel) :-
        stdio::write("\n============================================================\n"),
        stdio::write("    FACULTY WELLNESS RECOMMENDATION SYSTEM\n"),
        stdio::write("    Expert System Analysis Report\n"),
        stdio::write("============================================================\n\n"),
        stdio::write("Faculty ID: "),
        stdio::write(FacultyID),
        stdio::write("\n"),
        if StressLevel = low then
            stdio::write("Stress Level: LOW\n")
        elseif StressLevel = medium then
            stdio::write("Stress Level: MEDIUM\n")
        elseif StressLevel = high then
            stdio::write("Stress Level: HIGH - ATTENTION REQUIRED\n")
        else
            stdio::write("Stress Level: UNKNOWN\n")
        end if.

    display_indicators(StressLevel) :-
        stdio::write("\n------------------------------------------------------------\n"),
        stdio::write("CONDITION INDICATORS\n"),
        stdio::write("------------------------------------------------------------\n"),
        sleep_indicator(StressLevel, S),
        stdio::write("* Sleep: "),
        stdio::write(S),
        stdio::write("\n"),
        workload_indicator(StressLevel, W),
        stdio::write("* Workload: "),
        stdio::write(W),
        stdio::write("\n"),
        wellness_indicator(StressLevel, WL),
        stdio::write("* Wellness: "),
        stdio::write(WL),
        stdio::write("\n"),
        balance_indicator(StressLevel, B),
        stdio::write("* Work-Life Balance: "),
        stdio::write(B),
        stdio::write("\n"),
        productivity_indicator(StressLevel, P),
        stdio::write("* Productivity: "),
        stdio::write(P),
        stdio::write("\n"),
        health_indicator(StressLevel, H),
        stdio::write("* Health Risk: "),
        stdio::write(H),
        stdio::write("\n").

    display_recommendations(StressLevel) :-
        stdio::write("\n------------------------------------------------------------\n"),
        stdio::write("PERSONALIZED RECOMMENDATIONS\n"),
        stdio::write("------------------------------------------------------------\n\n"),
        primary_recommendation(StressLevel, PR),
        stdio::write("1. PRIMARY ACTION: "),
        stdio::write(PR),
        stdio::write("\n"),
        workload_recommendation(StressLevel, WR),
        stdio::write("2. WORKLOAD MANAGEMENT: "),
        stdio::write(WR),
        stdio::write("\n"),
        wellness_recommendation(StressLevel, WLR),
        stdio::write("3. WELLNESS ACTIVITIES: "),
        stdio::write(WLR),
        stdio::write("\n"),
        time_management_recommendation(StressLevel, TM),
        stdio::write("4. TIME MANAGEMENT: "),
        stdio::write(TM),
        stdio::write("\n"),
        social_recommendation(StressLevel, SR),
        stdio::write("5. SOCIAL SUPPORT: "),
        stdio::write(SR),
        stdio::write("\n"),
        preventive_recommendation(StressLevel, PRV),
        stdio::write("6. PREVENTIVE MEASURES: "),
        stdio::write(PRV),
        stdio::write("\n").

    display_footer() :-
        stdio::write("\n------------------------------------------------------------\n"),
        stdio::write("Report generated by Faculty Wellness Expert System\n"),
        stdio::write("============================================================\n").

/* --------------------------
FILE READING PREDICATE (class predicates)
-------------------------- */
clauses
    read_stress_file(FileName, FacultyID, StressLevel, Result) :-
        try
            Input = inputStream_file::openFileUtf8(FileName),
            % Read the entire first line (should contain both values separated by a delimiter)
            Line = Input:readLine(),
            Input:close(),
            % Parse the line: format is "faculty_id:XXX,stress_level:YYY"
            if string::length(Line) > 0 then
                % Find positions of key strings
                FacultyIDStart = string::search(Line, "faculty_id:"),
                CommaPos = string::search(Line, ","),
                StressLevelStart = string::search(Line, "stress_level:"),
                % Check if all required strings were found
                if FacultyIDStart >= 0 and CommaPos >= 0 and StressLevelStart >= 0 then
                    % Extract faculty_id (between "faculty_id:" and comma)
                    FacultyIDStartPos = FacultyIDStart + 11,
                    FacultyIDLength = CommaPos - FacultyIDStartPos,
                    FacultyID = string::subString(Line, FacultyIDStartPos, FacultyIDLength),
                    % Extract stress_level (after "stress_level:" to end of line)
                    StressLevelStartPos = StressLevelStart + 13,
                    StressLevelLength = string::length(Line) - StressLevelStartPos,
                    LS = string::subString(Line, StressLevelStartPos, StressLevelLength),
                    % Parse stress level
                    if LS = "low" then
                        StressLevel = low
                    elseif LS = "medium" then
                        StressLevel = medium
                    elseif LS = "high" then
                        StressLevel = high
                    else
                        StressLevel = low
                    end if,
                    Result = true
                else
                    FacultyID = "",
                    StressLevel = low,
                    Result = false
                end if
            else
                FacultyID = "",
                StressLevel = low,
                Result = false
            end if
        catch _ do
            FacultyID = "",
            StressLevel = low,
            Result = false
        end try.

    process_recommendations(FacultyID, StressLevel) :-
        display_header(FacultyID, StressLevel),
        display_indicators(StressLevel),
        display_recommendations(StressLevel),
        display_footer().

end implement wellness_pro

implement main
    open core

clauses
    run() :-
        stdio::write("Reading stress prediction from Python ML component...\n"),
        % Try multiple file locations (executable runs from exe64/, so check parent directory)
        % Use backslashes for Windows paths
        File1 = "..\\stress_output.txt",
        File2 = "stress_output.txt",
        File3 = "..\\PYTHON_MLCOMPONENT\\stress_output.txt",
        % Try reading from parent directory first (most likely location)
        wellness_pro::read_stress_file(File1, ReadFacultyID1, ReadStressLevel1, Result1),
        if Result1 = true then
            ReadFacultyID = ReadFacultyID1,
            ReadStressLevel = ReadStressLevel1,
            Result = true
        else
            % Try current directory
            wellness_pro::read_stress_file(File2, ReadFacultyID2, ReadStressLevel2, Result2),
            if Result2 = true then
                ReadFacultyID = ReadFacultyID2,
                ReadStressLevel = ReadStressLevel2,
                Result = true
            else
                % Try CS18A-FINALPROJECT directory
                wellness_pro::read_stress_file(File3, ReadFacultyID3, ReadStressLevel3, Result3),
                if Result3 = true then
                    ReadFacultyID = ReadFacultyID3,
                    ReadStressLevel = ReadStressLevel3,
                    Result = true
                else
                    ReadFacultyID = "",
                    ReadStressLevel = wellness_pro::low,
                    Result = false
                end if
            end if
        end if,
        if Result = true then
            wellness_pro::process_recommendations(ReadFacultyID, ReadStressLevel)
        else
            stdio::write("Could not read 'stress_output.txt'. Enter manually.\n"),
            stdio::write("Enter Faculty ID: "),
            ManualFacultyID = stdio::readLine(),
            stdio::write("Enter stress level (low/medium/high): "),
            LS = stdio::readLine(),
            if LS = "low" then
                ManualStressLevel = wellness_pro::low
            elseif LS = "medium" then
                ManualStressLevel = wellness_pro::medium
            elseif LS = "high" then
                ManualStressLevel = wellness_pro::high
            else
                ManualStressLevel = wellness_pro::low
            end if,
            wellness_pro::process_recommendations(ManualFacultyID, ManualStressLevel)
        end if.

    runMain() :-
        try
            if run() then
                succeed
            else
                succeed
            end if
        catch _ do
            stdio::write("An error occurred.\n")
        end try,
        stdio::write("\nPress Enter to exit...\n"),
        _ = stdio::readLine().

end implement main

goal
    console::runUtf8(main::runMain).

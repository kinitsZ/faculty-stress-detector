class wellness_pro
    open core

domains
    stress_level = low; medium; high.

predicates
    run : () determ.
    read_stress_file : (string, string [out], stress_level [out], boolean [out]) determ.
    process_recommendations : (string, stress_level).
    sleep_indicator : (stress_level, string [out]).
    workload_indicator : (stress_level, string [out]).
    wellness_indicator : (stress_level, string [out]).
    meeting_indicator : (stress_level, string [out]).
    research_indicator : (stress_level, string [out]).
    committee_indicator : (stress_level, string [out]).
    admin_indicator : (stress_level, string [out]).
    balance_indicator : (stress_level, string [out]).
    productivity_indicator : (stress_level, string [out]).
    health_indicator : (stress_level, string [out]).
    primary_recommendation : (stress_level, string [out]).
    workload_recommendation : (stress_level, string [out]).
    wellness_recommendation : (stress_level, string [out]).
    time_management_recommendation : (stress_level, string [out]).
    social_recommendation : (stress_level, string [out]).
    preventive_recommendation : (stress_level, string [out]).
    display_header : (string, stress_level).
    display_indicators : (stress_level).
    display_recommendations : (stress_level).
    display_footer : ().

end class wellness_pro

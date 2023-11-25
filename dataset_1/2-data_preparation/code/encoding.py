from pandas import read_csv, DataFrame
from dslabs_functions import get_variable_types, encode_cyclic_variables, dummify

data: DataFrame = read_csv("../../../class_pos_covid.csv", na_values="")
vars: dict[str, list] = get_variable_types(data)

yes_no: dict[str, int] = {"no": 0, "No": 0, "yes": 1, "Yes": 1}
sex_values: dict[str, int] = {"Male": 0, "Female": 1}

state_values: dict[str, int] = {
    #dummify???
    '''
    'Alabama' 'Alaska' 'Arizona' 'Arkansas' 'California' 'Colorado'
    'Connecticut' 'Delaware' 'District of Columbia' 'Florida' 'Georgia'
    'Hawaii' 'Idaho' 'Illinois' 'Indiana' 'Iowa' 'Kansas' 'Kentucky'
    'Louisiana' 'Maine' 'Maryland' 'Massachusetts' 'Michigan' 'Minnesota'
    'Mississippi' 'Missouri' 'Montana' 'Nebraska' 'Nevada' 'New Hampshire'
    'New Jersey' 'New Mexico' 'New York' 'North Carolina' 'North Dakota'
    'Ohio' 'Oklahoma' 'Oregon' 'Pennsylvania' 'Rhode Island' 'South Carolina'
    'South Dakota' 'Tennessee' 'Texas' 'Utah' 'Vermont' 'Virginia'
    'Washington' 'West Virginia' 'Wisconsin' 'Wyoming' 'Guam' 'Puerto Rico'
    'Virgin Islands'
    '''
}

health_values: dict[str, int] = {
    "Poor": 0,
    "Fair": 1,
    "Good": 2,
    "Very Good": 3,
    "Excelent": 4,
}
last_checkup_time_values: dict[str, int] = {
    '''
    "Within past year (anytime less than 12 months ago)"
    "Within past 2 years (1 year but less than 2 years ago)"
    "Within past 5 years (2 years but less than 5 years ago)"
    "5 or more years ago"
    '''
}
removed_teeth_values: dict[str, int] = {
    '''
    "None of them"
    "1 to 5"
    "6 or more, but not all"
    "All"
    '''
}
had_diabetes_values: dict[str, int] = {
    # divir em yes e no???
    '''
    "Yes"
    "No"
    "No, pre-diabetes or borderline diabetes"
    "Yes, but only during pregnancy (female)"
    '''
}
smoker_status_values: dict[str, int] = {
    "Current smoker - now smokes every day": 0,
    "Current smoker - now smokes some days": 1,
    "Former smoker": 2,
    "Never smoked": 3,
    }
e_cigarrete_values: dict[str, int] = {
    "Use them every day": 0,
    "Use them some days": 1,
    "Not at all (right now)": 2,
    "Never used e-cigarettes in my entire life": 3,
}
race_ethnicity_values: dict[str, int] = {
    # taxonomia em que dividi em hispanic e non-hispanic e depois em raças por ordem de parecença
    "Hispanic": 0,
    "White only, Non-Hispanic": 1,
    "Multiracial, Non-Hispanic": 2,
    "Black only, Non-Hispanic": 3,
    "Other race only, Non-Hispanic": 4,
}
age_category_values: dict[str, int] = {
    '''
    'Age 80 or older' nan 'Age 40 to 44' 'Age 75 to 79' 'Age 70 to 74'
 'Age 55 to 59' 'Age 65 to 69' 'Age 60 to 64' 'Age 50 to 54'
 'Age 45 to 49' 'Age 35 to 39' 'Age 30 to 34' 'Age 25 to 29'
 'Age 18 to 24'
 '''
}
tetanus_last_10_tdap_values: dict[str, int] = {
    # diviir em yes e no???
    '''
    "Yes, received tetanus shot but not sure what type"
    "No, did not receive any tetanus shot in the past 10 years"
    "Yes, received Tdap"
    "Yes, received tetanus shot, but not Tdap"
    '''
}

encoding: dict[str, dict[str, int]] = {
    "State": state_values,
    "Sex": sex_values,
    "GeneralHealth": health_values,
    "LastCheckupTime": last_checkup_time_values,
    "PhysicalActivities": yes_no,
    "RemovedTeeth": removed_teeth_values,
    "HadHeartAttack": yes_no,
    "HadAngina": yes_no,
    "HadStroke": yes_no,
    "HadAsthma": yes_no,
    "HadSkinCancer": yes_no,
    "HadCOPD": yes_no,
    "HadDepressiveDisorder": yes_no,
    "HadKidneyDisease": yes_no,
    "HadArthritis": yes_no,
    "HadDiabetes": had_diabetes_values,
    "DeafOrHardOfHearing": yes_no,
    "BlindOrVisionDifficulty": yes_no,
    "DificultyConcentrating": yes_no,
    "DifficultyWalking": yes_no,
    "DifficultyDressingBathing": yes_no,
    "DifficultyErrands": yes_no,
    "SmokerStatus": smoker_status_values,
    "ECigarreteUsage": e_cigarrete_values,
    "ChestScan": yes_no,
    "RaceEthnicityCategory": race_ethnicity_values,
    "AgeCategory": age_category_values,
    "AlcoholDrinkers": yes_no,
    "HIVTesting": yes_no,
    "FluVaxLast12": yes_no,
    "PneumoVaxEver": yes_no,
    "TetanusLast10Tdap": tetanus_last_10_tdap_values,
    "HighRiskLastYear": yes_no,
    "CovidPos": yes_no,
}
df: DataFrame = data.replace(encoding, inplace=False)
df.head()

for v in vars["symbolic"]:
    print(v, data[v].unique())
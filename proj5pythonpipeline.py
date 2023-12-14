# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:24:37 2023

@author: John Torres
"""

import pandas as pd

data = pd.read_csv('./IP5_CountyData_GISFriendly_2020.csv')

## Data Check
print("Data Before: ")
print(data)
print("")

print("Columns Before: ")
print(data.columns)
print("")

print("Values Before: ")
print(data.values)
print("")

#Drop 95% Confidence Interval columns
data.drop(list(data.filter(regex='95CI')), axis=1, inplace=True)

#Drop Geolocation column
data.drop(list(data.filter(regex='Geolocation')), axis=1, inplace=True)


## Create Mean cols out of Crude/Adj cols and drop Crude/Adj
# Create ACCESS2_Mean Column
data['ACCESS2_Mean'] = (data['ACCESS2_CrudePrev'] + data['ACCESS2_AdjPrev']) / 2
#Drop ACCESS2 columns
data.drop(list(data.filter(regex='ACCESS2_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='ACCESS2_AdjPrev')), axis=1, inplace=True)

#Create ARTHRITIS_Mean Column
data['ARTHRITIS_Mean'] = (data['ARTHRITIS_CrudePrev'] + data['ARTHRITIS_AdjPrev']) / 2
#Drop ARTHRITIS columns
data.drop(list(data.filter(regex='ARTHRITIS_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='ARTHRITIS_AdjPrev')), axis=1, inplace=True)

#Create BINGE_Mean Column
data['BINGE_Mean'] = (data['BINGE_CrudePrev'] + data['BINGE_AdjPrev']) / 2
#Drop BINGE columns
data.drop(list(data.filter(regex='BINGE_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='BINGE_AdjPrev')), axis=1, inplace=True)

#Create BPHIGH_Mean Column
data['BPHIGH_Mean'] = (data['BPHIGH_CrudePrev'] + data['BPHIGH_AdjPrev']) / 2
#Drop BPHIGH columns
data.drop(list(data.filter(regex='BPHIGH_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='BPHIGH_AdjPrev')), axis=1, inplace=True)

#Create BPMED_Mean Column
data['BPMED_Mean'] = (data['BPMED_CrudePrev'] + data['BPMED_AdjPrev']) / 2
#Drop BPMED columns
data.drop(list(data.filter(regex='BPMED_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='BPMED_AdjPrev')), axis=1, inplace=True)

#Create CANCER_Mean Column
data['CANCER_Mean'] = (data['CANCER_CrudePrev'] + data['CANCER_AdjPrev']) / 2
#Drop CANCER columns
data.drop(list(data.filter(regex='CANCER_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='CANCER_AdjPrev')), axis=1, inplace=True)

#Create CASTHMA_Mean Column
data['CASTHMA_Mean'] = (data['CASTHMA_CrudePrev'] + data['CASTHMA_AdjPrev']) / 2
#Drop CASTHMA columns
data.drop(list(data.filter(regex='CASTHMA_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='CASTHMA_AdjPrev')), axis=1, inplace=True)

#Create CERVICAL_Mean Column
data['CERVICAL_Mean'] = (data['CERVICAL_CrudePrev'] + data['CERVICAL_AdjPrev']) / 2
#Drop CASTHMA columns
data.drop(list(data.filter(regex='CERVICAL_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='CERVICAL_AdjPrev')), axis=1, inplace=True)

#Create CHD_Mean Column
data['CHD_Mean'] = (data['CHD_CrudePrev'] + data['CHD_AdjPrev']) / 2
#Drop CHD columns
data.drop(list(data.filter(regex='CHD_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='CHD_AdjPrev')), axis=1, inplace=True)

#Create CHECKUP_Mean Column
data['CHECKUP_Mean'] = (data['CHECKUP_CrudePrev'] + data['CHECKUP_AdjPrev']) / 2
#Drop CHECKUP columns
data.drop(list(data.filter(regex='CHECKUP_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='CHECKUP_AdjPrev')), axis=1, inplace=True)

#Create CHOLSCREEN_Mean Column
data['CHOLSCREEN_Mean'] = (data['CHOLSCREEN_CrudePrev'] + data['CHOLSCREEN_AdjPrev']) / 2
#Drop CHOLSCREEN columns
data.drop(list(data.filter(regex='CHOLSCREEN_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='CHOLSCREEN_AdjPrev')), axis=1, inplace=True)

#Create COLON_SCREEN_Mean Column
data['COLON_SCREEN_Mean'] = (data['COLON_SCREEN_CrudePrev'] + data['COLON_SCREEN_AdjPrev']) / 2
#Drop COLON_SCREEN columns
data.drop(list(data.filter(regex='COLON_SCREEN_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='COLON_SCREEN_AdjPrev')), axis=1, inplace=True)

#Create COPD_Mean Column
data['COPD_Mean'] = (data['COPD_CrudePrev'] + data['COPD_AdjPrev']) / 2
#Drop COPD columns
data.drop(list(data.filter(regex='COPD_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='COPD_AdjPrev')), axis=1, inplace=True)

#Create COREM_Mean Column
data['COREM_Mean'] = (data['COREM_CrudePrev'] + data['COREM_AdjPrev']) / 2
#Drop COREM columns
data.drop(list(data.filter(regex='COREM_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='COREM_AdjPrev')), axis=1, inplace=True)

#Create COREW_Mean Column
data['COREW_Mean'] = (data['COREW_CrudePrev'] + data['COREW_AdjPrev']) / 2
#Drop COREW columns
data.drop(list(data.filter(regex='COREW_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='COREW_AdjPrev')), axis=1, inplace=True)

#Create CSMOKING_Mean Column
data['CSMOKING_Mean'] = (data['CSMOKING_CrudePrev'] + data['CSMOKING_AdjPrev']) / 2
#Drop CSMOKING columns
data.drop(list(data.filter(regex='CSMOKING_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='CSMOKING_AdjPrev')), axis=1, inplace=True)

#Create DENTAL_Mean Column
data['DENTAL_Mean'] = (data['DENTAL_CrudePrev'] + data['DENTAL_AdjPrev']) / 2
#Drop DENTAL columns
data.drop(list(data.filter(regex='DENTAL_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='DENTAL_AdjPrev')), axis=1, inplace=True)

#Create DIABETES_Mean Column
data['DIABETES_Mean'] = (data['DIABETES_CrudePrev'] + data['DIABETES_AdjPrev']) / 2
#Drop DIABETES columns
data.drop(list(data.filter(regex='DIABETES_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='DIABETES_AdjPrev')), axis=1, inplace=True)

#Create HIGHCHOL_Mean Column
data['HIGHCHOL_Mean'] = (data['HIGHCHOL_CrudePrev'] + data['HIGHCHOL_AdjPrev']) / 2
#Drop HIGHCHOL columns
data.drop(list(data.filter(regex='HIGHCHOL_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='HIGHCHOL_AdjPrev')), axis=1, inplace=True)

#Create KIDNEY_Mean Column
data['KIDNEY_Mean'] = (data['KIDNEY_CrudePrev'] + data['KIDNEY_AdjPrev']) / 2
#Drop KIDNEY columns
data.drop(list(data.filter(regex='KIDNEY_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='KIDNEY_AdjPrev')), axis=1, inplace=True)

#Create LPA_Mean Column
data['LPA_Mean'] = (data['LPA_CrudePrev'] + data['LPA_AdjPrev']) / 2
#Drop LPA columns
data.drop(list(data.filter(regex='LPA_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='LPA_AdjPrev')), axis=1, inplace=True)

#Create MAMMOUSE_Mean Column
data['MAMMOUSE_Mean'] = (data['MAMMOUSE_CrudePrev'] + data['MAMMOUSE_AdjPrev']) / 2
#Drop MAMMOUSE columns
data.drop(list(data.filter(regex='MAMMOUSE_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='MAMMOUSE_AdjPrev')), axis=1, inplace=True)

#Create MHLTH_Mean Column
data['MHLTH_Mean'] = (data['MHLTH_CrudePrev'] + data['MHLTH_AdjPrev']) / 2
#Drop MHLTH columns
data.drop(list(data.filter(regex='MHLTH_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='MHLTH_AdjPrev')), axis=1, inplace=True)

#Create OBESITY_Mean Column
data['OBESITY_Mean'] = (data['OBESITY_CrudePrev'] + data['OBESITY_AdjPrev']) / 2
#Drop OBESITY columns
data.drop(list(data.filter(regex='OBESITY_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='OBESITY_AdjPrev')), axis=1, inplace=True)

#Create PHLTH_Mean Column
data['PHLTH_Mean'] = (data['PHLTH_CrudePrev'] + data['PHLTH_AdjPrev']) / 2
#Drop PHLTH columns
data.drop(list(data.filter(regex='PHLTH_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='PHLTH_AdjPrev')), axis=1, inplace=True)

#Create SLEEP_Mean Column
data['SLEEP_Mean'] = (data['SLEEP_CrudePrev'] + data['SLEEP_AdjPrev']) / 2
#Drop SLEEP columns
data.drop(list(data.filter(regex='SLEEP_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='SLEEP_AdjPrev')), axis=1, inplace=True)

#Create STROKE_Mean Column
data['STROKE_Mean'] = (data['STROKE_CrudePrev'] + data['STROKE_AdjPrev']) / 2
#Drop STROKE columns
data.drop(list(data.filter(regex='STROKE_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='STROKE_AdjPrev')), axis=1, inplace=True)

#Create TEETHLOST_Mean Column
data['TEETHLOST_Mean'] = (data['TEETHLOST_CrudePrev'] + data['TEETHLOST_AdjPrev']) / 2
#Drop TEETHLOST columns
data.drop(list(data.filter(regex='TEETHLOST_CrudePrev')), axis=1, inplace=True)
data.drop(list(data.filter(regex='TEETHLOST_AdjPrev')), axis=1, inplace=True)

print("Data After: ")
print(data)
print("")

print("Columns After: ")
print(data.columns)
print("")

print("Values After: ")
print(data.values)
print("")

data.drop(list(data.filter(regex='CountyFIPS')), axis=1, inplace=True)
data.drop(list(data.filter(regex='TotalPopulation')), axis=1, inplace=True)


## Health Outcomes Data
locCols = {'State': data['StateAbbr'], 'County': data['CountyName']}
dataHlthScrn = pd.DataFrame(data=locCols)

dataHlthScrn['No Healthcare'] = (data['ACCESS2_Mean'])
dataHlthScrn['Routine Checkups'] = data['CHECKUP_Mean']
dataHlthScrn['Dental Visits'] = data['DENTAL_Mean']
dataHlthScrn['Medicated for BP'] = data['BPMED_Mean']
dataHlthScrn['Cervical Cancer Screening'] = data['CERVICAL_Mean']
dataHlthScrn['Mammography'] = data['MAMMOUSE_Mean']
dataHlthScrn['Cholesterol Screening'] = data['CHOLSCREEN_Mean']
dataHlthScrn['Colon Screening'] = data['COLON_SCREEN_Mean']
dataHlthScrn['Core Clinical Services'] = data['COREM_Mean']
dataHlthScrn['Core Clinical Services'] = data['COREW_Mean']

print('Health Outcomes Data: ')
print(dataHlthScrn)

alHlthScrnData = dataHlthScrn.loc[dataHlthScrn['State'] == 'AL']
baldwinHlthScrnData = alHlthScrnData.loc[dataHlthScrn['County'] == 'Baldwin']

print('Baldwin, AL Health Outcomes Data: ')
print(baldwinHlthScrnData)

plot = baldwinHlthScrnData.plot(title="Baldwin County, Alabama Health Screening Data", kind="bar", xlabel='Health Screenings', ylabel='Mean / 100', figsize=(16,16))
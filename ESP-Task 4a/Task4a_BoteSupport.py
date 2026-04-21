import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time taken to resolve different types of issues")
        print("### 3. Show issues and resolutions based on region")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
    
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("ESP-Task 4a/Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg


#######################################################################################BREAKPOINT#######################################################################################



main_menu_choice = main_menu()
if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))

elif main_menu_choice == "2":

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    
    timeTaken = pd.read_csv("ESP-Task 4a/Task4a_data.csv")

    print("\n########## Average time to resolve by issue type ##########")
    
    #loop through all issue types and show average days for each
    for issue_type in issueTypeList:
        filtered_data = timeTaken[timeTaken['Issue Type'] == issue_type]
        average_days = filtered_data['Days To Resolve'].mean()
        print(f"{issue_type}: {average_days:.2f} days average")

#####################################################BREAKPOINT##################################################################################################


elif main_menu_choice == "3":
    
    regionData = pd.read_csv("ESP-Task 4a/Task4a_data.csv")
    
    regions = regionData['Region'].unique()
    
    print("\n########## Issues and Resolutions by Region ##########\n")
    
    for region in sorted(regions):
        region_filtered = regionData[regionData['Region'] == region]
        print(f"{region}")
        print(f"Total Issues: {len(region_filtered)}")
        
        for i in range(len(region_filtered)):
            issue_row = region_filtered.iloc[i]
            issue_type = issue_row['Issue Type']
            how_resolved = issue_row['How Resolved']
            parcels = issue_row['No Of Parcels']
            print(f"  - {issue_type}: {how_resolved} ({parcels} parcels)")

        print()

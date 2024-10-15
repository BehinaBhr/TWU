# **********************************************************************
# Homework Assignment 2: <input validation, branching/conditionals>
#
# Description: <A Hospital reporting system to provide a quick overview of the patient’s condition by collecting
# patient's name, weight, height, and specific lab test results related to genetic mutations. From these results,
# Determine the ProMisE subtype grouping which is a system classify patients into four group which leads to certain
# treatment type as follows:
#   If POLE mutation = yes (regardless of results of the other two lab tests), then ProMisE = POLEmut
#   If POLE mutation = no and MMR deficiency = yes (regardless of the p53 mutation's result), then ProMisE = MMRd
#   If POLE mutation = no and MMR deficiency = no and p53 mutation = yes, then ProMisE = p53abn
#   If POLE mutation = no and MMR deficiency = no and p53 mutation = no, then ProMisE = NSMP/p53wt
# Verify that the user provides input in the correct format:
#   height and weight should be integers
#   lab test result questions should be “yes” or “no”
#   if an invalid input is encountered the program will end with an error message.
# The report displays the patient's name, calculated BMI based on weight and height,
# results for genetic mutations and the ProMisE subtype.>
#
# Author: <Behina.Bahramsari@mytwu.ca> <student_id: 6600360>
# Date: <September 19, 2024>
#
# Input: <patient name: Bh
#         weight (kg): 64
#         height (cm): 165
#         have POLE mutation? (yes/no): yes
#         have MMR deficiency? (yes/no): no
#         have p53 mutation? (yes/no): no>
#
# Output: <*** Patient (Bh) Test Results ***
#         BMI: 23.51
#         POLE mutation: yes
#         MMR deficiency: no
#         p53 mutation: no
#         ProMisE: POLEmut >
#
#   I pledge that I have completed the programming assignment independently.
#   I have not copied the code from a student or any source.
#   I have not given my code to any student.
#
# Sign here: <Behina Bahramsari>
# *********************************************************************/


# prompt for collecting patient's details :
name = input("Please Enter the patient name: ")

# Verify height and weight inputs should be integers.
# Note: isdigit() method will check if a string consists of decimal digits (0-9), while isnumeric() method will check
# if a string consists of only numeric characters including decimal digits (0-9), fractions (½), Roman numerals(IV).
# If input is invalid, the program will end with an error message.
weight = input("Please Enter the patient weight (kg - only integer): ")
if weight.isdigit():
    weight = int(weight)
else:
    print("Error: Weight should be integers (a whole number without decimal point).")
    exit()

height = input("Please Enter the patient height (cm - only integer): ")
if height.isdigit():
    height = int(height)
else:
    print("Error: Height should be integers (a whole number without decimal point).")
    exit()

# Verify lab test result questions should be “yes” or “no”
# If input is invalid, the program will end with an error message.
pole_mutation = input("Does the patient have POLE mutation? (yes/no): ")
if pole_mutation != "yes" and pole_mutation != "no":
    print("Error: POLE mutation should be 'yes' or 'no'.")
    exit()

mmr_deficiency = input("Does the patient have MMR deficiency? (yes/no): ")
if mmr_deficiency != "yes" and mmr_deficiency != "no":
    print("Error: MMR deficiency should be 'yes' or 'no'.")
    exit()

p53_mutation = input("Does the patient have p53 mutation? (yes/no): ")
if p53_mutation != "yes" and p53_mutation != "no":
    print("Error: p53 mutation should be 'yes' or 'no'.")
    exit()

# calculate patient's BMI from weight and height
bmi = weight / (height / 100 * height / 100)

# Determine the ProMisE subtype grouping
if pole_mutation == "yes":
    promisE = "POLEmut"
elif pole_mutation == "no" and mmr_deficiency == "yes":
    promisE = "MMRd"
elif pole_mutation == "no" and mmr_deficiency == "no" and p53_mutation == "yes":
    promisE = "p53abn"
else:
    promisE = "NSMP/p53wt"

# display formatted report
print(f"*** Patient ({name}) Test Results ***")
# format BMI to two decimal places
print(f"BMI: {bmi:.2f}")
print(f"POLE mutation: {pole_mutation}")
print(f"MMR deficiency: {mmr_deficiency}")
print(f"p53 mutation: {p53_mutation}")
print(f"ProMisE: {promisE}")

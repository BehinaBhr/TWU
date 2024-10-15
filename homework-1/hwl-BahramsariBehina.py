# **********************************************************************
# Homework Assignment 1: <Variables, Input/Output>
#
# Description:
# <A Hospital reporting system to provide a quick overview of the patient’s condition
# by collecting patient's name, weight, height, and specific lab test results related to genetic mutations.
# Assumes that the user provides input in the correct format.
# the report displays the patient's name, calculated BMI based on weight and height, and results for genetic mutations.>
#
# Author: <Behina.Bahramsari@mytwu.ca> <student_id: 6600360>
# Date: <September 13, 2024>
#
# Input: <patient name: Bh
#         weight (kg): 64
#         height (cm): 165
#         have POLE mutation? (yes/no): no
#         have MMR deficiency? (yes/no): yes
#         have p53 mutation? (yes/no): no>
#
# Output: <*** Patient (Bh) Test Results ***
#         BMI: 23.51
#         POLE mutation: no
#         MMR deficiency: yes
#         p53 mutation: no>
#
#   I pledge that I have completed the programming assignment independently.
#   I have not copied the code from a student or any source.
#   I have not given my code to any student.
#
# Sign here: <Behina Bahramsari>
# *********************************************************************/


# prompt for collecting patient's details :
name = input("Please Enter the patient name: ")
# Convert weight and height from input strings to floats for BMI calculation
weight = float(input("Please Enter the patient weight (kg): "))
height = float(input("Please Enter the patient height (cm): "))
pole_mutation = input("Does the patient have POLE mutation? (yes/no): ")
mmr_deficiency = input("Does the patient have MMR deficiency? (yes/no): ")
p53_mutation = input("Does the patient have p53 mutation? (yes/no): ")

# calculate patient's BMI from weight and height
bmi = weight / (height / 100 * height / 100)

# display formatted report
print(f"*** Patient ({name}) Test Results ***")
# format BMI to two decimal places
print(f"BMI: {bmi:.2f}")
print(f"POLE mutation: {pole_mutation}")
print(f"MMR deficiency: {mmr_deficiency}")
print(f"p53 mutation: {p53_mutation}")

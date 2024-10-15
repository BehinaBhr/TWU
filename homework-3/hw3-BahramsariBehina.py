# ***********************************************************************/
# Homework Assignment 3: <Data cleaning with for loop, string processing>
#
# Description:
# Iterates through a list of specimen id's and convert the labelling format
# e.g. "VOA1392a" -> "VOA1392@A"
#      "VOA1392A" -> "VOA1392#A" 
# We can assume the last character is always an alphabet.
# if last character is lower case, replace it with @[upper case of last character]
# if last character is upper case, replace it with #[upper case of last character]
# Make sure “VOA” is always all upper case.
# Store the newly formatted ID’s in a list then iterate through it and print out the content.
#
# Author: <Behina.Bahramsari@mytwu.ca> <student_id: 6600360>
# Date: <October 1, 2024>
#
# Input: <Assume that the Specimen ID column in the Excel file contains the following sample IDs:
#         VOA2025A
#         VOA2024a
#         VOA2024b
#         VOA2024c>
# Output: <formatted sample IDs:
#          VOA2025#A
#          VOA2024@A
#          VOA2024@B
#          VOA2024@C>
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: <Behina Bahramsari>
# *********************************************************************/

# Install Python library Pandas with pip install pandas openpyxl in terminal
# to read in an Excel file.
import pandas as pd


# import os


def main():
    # call the corresponding read_excel function to open an Excel file and read the data into a pandas DataFrame
    # which is similar to a spreadsheet with rows/columns
    d = pd.read_excel("specimen_ids.xlsx")

    # initialize an empty list to store the reformatted ID's.
    new_ids = []

    # iterate through all rows in a DataFrame
    for index, row_content in d.iterrows():

        # print the index (row number) and its content inside the for loop to observe the content of the Excel file.
        print("row " + str(index) + " " + str(row_content))
        # more detail:
        # index refers to row number row holds actual content of the row (row data)
        print("row number:", str(index))
        # row_content holds the data for the current row, with each column value accessible via its label (column name).
        print("row content:", str(row_content))
        # data type of row content is a pandas "Series", which is an array-like data structure and somewhat like a list.
        print(type(row_content))
        # To access a specific column's value in the current row (access an element in a pandas Series),
        # used the following syntax: row_content["<column_name>"].
        # To access the value in the "Specimen ID" column in the current row:
        print("specimen id:", str(row_content["Specimen ID"]))

        # Assume all specimen IDs are located in the "Specimen ID" column of the DataFrame so NO NEED TO iterate
        # through all "columns" or "cell" of a row.
        # Store the value in the "Specimen ID" column in the current row in a variable for us to manipulate it
        id = row_content["Specimen ID"]

        # Convert "VOA" part to uppercase if not already
        if id[:3] != "VOA":
            id = "VOA" + id[3:]

        # Check the last character of the ID
        last_char = id[-1]
        # please generate the id in new format based on the last character's case
        if last_char.islower():
            new_id = id[:-1] + "@" + last_char.upper()
        else:  # isupper
            new_id = id[:-1] + "#" + last_char.upper()
        # Add the formatted ID to the list "new_ids"
        new_ids.append(new_id)
    # Iterate through all items in the list "new_ids" and print the reformatted IDs
    for new_id in new_ids:
        print(new_id)

    # EXTRA ###############################################################################################
    # # To write the contents of the newly formatted IDs list to a text file in Python
    # output_file = "formatted_specimen_ids.txt"
    # # Open the file in write mode (will create the file if it doesn't exist)
    # with open(output_file, "w") as file:
    #     # Iterate through all items in the list "new_ids" and write each ID on a new line to the file
    #     for new_id in new_ids:
    #         file.write(new_id + "\n")
    # print(f"Formatted specimen IDs have been written to a text file called {output_file}.")

    # # To write the contents of the newly formatted IDs list to an Excel file in Python
    # output_file = "formatted_specimen_ids.xlsx"
    # # Create a new DataFrame with the new_ids list
    # df = pd.DataFrame(new_ids, columns=["Formatted Specimen ID"])
    # # Write the DataFrame to an Excel file
    # df.to_excel(output_file, index=False)
    # print(f"Formatted specimen IDs have been written to an Excel file called {output_file} .")
    # EXTRA ###############################################################################################


# Change working directory to the folder where data file is stored, If your file is in the same folder as your
# script, you don't need it
# os.chdir("hw3")

# call the main function
main()

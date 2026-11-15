
import pandas as pd # Import pandas to organize, filter, and perform calculations on the forfeiture dataset
import matplotlib.pyplot as plt # Import matplotlib to create a line graph showing how forfeiture amounts change over time

# Read the Iowa forfeiture CSV file located inside the Data folder of our shared GitHub repository
# Using a relative file path allows teammates to run the program without changing the file location for their computers
data=pd.read_csv("Data/state_of_iowa_forfeiture_cases_957_rows.csv")

# Convert the fiscal year closed column into numerical values so the years can be grouped and sorted correctly
# Any missing or invalid values are converted to NaN rather than causing the program to stop
data["fiscal_year_closed"]=pd.to_numeric(data["fiscal_year_closed"],errors="coerce")

# Convert the total money forfeited column into numerical values so the amounts can be added together
# Invalid or missing monetary values are converted to NaN to prevent errors during calculations
data["total_money_forfeited"]=pd.to_numeric(data["total_money_forfeited"],errors="coerce")

# Remove cases that do not have a valid fiscal year closed because they cannot be assigned to a specific year
# This ensures that only cases with a recorded closing year are included in the yearly comparison
data=data.dropna(subset=["fiscal_year_closed"])

# Group all forfeiture cases by the fiscal year in which they were closed
# Add together the total money forfeited for every case within each year to calculate annual forfeiture totals
# Sort the results by fiscal year so the values appear in chronological order on the graph
yearly_totals=data.groupby("fiscal_year_closed")["total_money_forfeited"].sum().sort_index()

# Print a heading to identify the results displayed in the terminal
# Display the total amount of money forfeited for each fiscal year so the numerical results can be compared
print("Total Money Forfeited by Year:")
print(yearly_totals.to_string())

# Create a line graph using the fiscal years on the x-axis and the total money forfeited on the y-axis
# The marker adds a visible point for each year, making it easier to identify increases and decreases
plt.plot(yearly_totals.index,yearly_totals.values,marker="o")

# Add a descriptive title explaining that the graph represents annual money forfeiture totals in Iowa
plt.title("Total Money Forfeited in Iowa by Year")

# Label the horizontal axis to identify the fiscal year in which each forfeiture case was closed
plt.xlabel("Fiscal Year Closed")

# Label the vertical axis to identify the total amount of money forfeited, measured in US dollars
plt.ylabel("Total Money Forfeited ($)")

# Add gridlines to make it easier to compare the monetary values between different years
plt.grid(True)

# Automatically adjust the spacing of the graph to prevent labels and titles from overlapping
plt.tight_layout()

# Display the completed line graph so the yearly forfeiture trends can be visually analyzed
plt.show()

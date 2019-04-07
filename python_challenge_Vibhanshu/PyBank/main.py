import os, csv
from pathlib import Path 

# Declare file location through pathlib
file_to_load = Path("budget_data.csv")
file_to_output = Path("Financial_Analysis.text")


total_months = []
total_profit = []
monthly_revenue_variation = []
 

with open(file_to_load,newline="", encoding="utf-8") as revenueData:

    csvreader = csv.reader(revenueData,delimiter=",") 
    header = next(csvreader)  

    # Iterate through the rows in the Budget_Data
    for row in csvreader: 

        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterating through the monthly profits to get monthly revenue variation
    for i in range(len(total_profit)-1):
        monthly_revenue_variation.append(total_profit[i+1]-total_profit[i])
        
    # Greatest Increase and Decrease in the montly revenue
    greatest_profit_increase_value = max(monthly_revenue_variation)
    greatest_profit_decrease_value = min(monthly_revenue_variation)

    # Months with the greatest profit increase and decrease
    greatest_profit_increase_month = monthly_revenue_variation.index(max(monthly_revenue_variation)) + 1
    greatest_profit_decrease_month = monthly_revenue_variation.index(min(monthly_revenue_variation)) + 1 


output = (
    f"    Financial Analysis    \n"
    f"--------------------------\n"
    f"Total Months: {len(total_months)}\n"
    f"Net Total Amount of Profit/Losses: ${sum(total_profit)}\n"
    f"Average Change: {round(sum(monthly_revenue_variation)/len(monthly_revenue_variation),2)}\n"
    f"Greatest Increase in Profits: {total_months[greatest_profit_increase_month]} (${(str(greatest_profit_increase_value))})\n"
    f"Greatest Decrease in Profits: {total_months[greatest_profit_decrease_month]} (${(str(greatest_profit_decrease_value))})\n"
    f"--------------------------\n"
    )
print(output)

# Convert Code to Text
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
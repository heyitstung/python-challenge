import csv
budget_file = "budget_data.csv"
budget_output = "budget_analysis.txt"

total_months = 0
net_total = []
average_changes = []
greatest_profits = [" ", 0]
greatest_losses = [" ", 0]

with open(budget_file) as pybank_revenue:
    reader = csv.reader(pybank_revenue)
    
    
    total_months = total_months + 1
    net_total = net_total + int(row[1])

    if net_total > greatest_prfots[1]:
        greatest_profits[0] = row[0]

    if net_total < greatest_losses[1]:
         greatest_losses[0] = row[0]

#test
output = (
    f"Financial Analysis"
    f"Total Months {total_months}"
    f"Greatest Increase in Profits: {greatest_profits[0]}"
    f"Greatest Decrease in Profits: {greatest_losses[0]}"
)

print(output)

with open(budget_output, "w") as txt_file:
    txt_file.write(output)
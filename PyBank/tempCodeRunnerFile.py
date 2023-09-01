first_row = next(csvreader)
    
    total_months = total_months + 1
    total_profits = total_profits + int(first_row[1])
    value = int(first_row[1])
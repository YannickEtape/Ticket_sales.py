# Yannick Etape

# price allocated to silver, gold and platinum tickets respectively
# price in $
silver_price = 35
gold_price = 55
platinum_price = 85

# Enter the number of silver, gold and platinum tickets sold
silver = int(input('Enter number of silver tickets:'))
gold = int(input('Enter number of gold tickets:'))
platinum = int(input('Enter number of platinum tickets:'))

total_tickets = (silver + gold + platinum)  # Displays the sum of all tickets sold

# Display individual revenue from silver, gold and platinum tickets sale
silver_revenue = silver * silver_price
gold_revenue = gold * gold_price
platinum_revenue = platinum * platinum_price

# Displays total revenue from sale of silver, gold and platinum tickets
total_revenue = (silver_revenue + gold_revenue + platinum_revenue)

print()
print('Section', 'Tickets', 'Revenue')
print('-----   ------   ------')
print('  silver', silver, '$', format(silver_revenue, ','))
print('    gold',   gold, '$', format(gold_revenue, ','))
print('platinum',   platinum, '$', format(platinum_revenue, ','))
print('====== ===== ===========')
print('   Total', total_tickets,  '$', format(total_revenue, ','))


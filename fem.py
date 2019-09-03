class FoodExpenseManager:
    def fem(self, amount, days):

        avg_amount = amount/days
        days_list = []
        
        for i in range(0, days):
            days_list.append(round(avg_amount, 2))
        
        print(days_list)

        # for i in range(0,days):
        #     day_trev = ex_days-days+1
        #     temp_amount = int(input("Day " + str(count) + " Expense >"))
        #     amount = amount - temp_amount
        #     count = count+1
        #     self.fem(amount, days-day_trev)
        


if __name__ == '__main__':
    main = FoodExpenseManager()
    food_amount = float(input("Enter the Food Amount Limit > "))
    days = int(input("Enter the no. of Days > "))

    for i in range(0, days):
        main.fem(food_amount, days-i)
        temp_amount = int(input("Day " + str(i+1) + " Expense >"))
        food_amount = food_amount - temp_amount




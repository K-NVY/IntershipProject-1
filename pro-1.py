def mortgage_calculator():
    loan_amount = float(input("Enter loan amount ($): "))
    annual_interest_rate = float(input("Enter annual interest rate (%): "))
    loan_term_years = int(input("Enter loan term (in years): "))
    
    # Monthly interest rate
    monthly_interest_rate = annual_interest_rate / 100 / 12
    # Number of payments (months)
    number_of_payments = loan_term_years * 12
    
    # Monthly payment formula
    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / ((1 + monthly_interest_rate)**number_of_payments - 1)
    else:
        monthly_payment = loan_amount / number_of_payments
    
    print(f"Your monthly mortgage payment is: ${monthly_payment:.2f}")

def investment_calculator():
    principal = float(input("Enter initial investment amount ($): "))
    annual_interest_rate = float(input("Enter expected annual rate of return (%): "))
    years = int(input("Enter number of years: "))
    compounding_per_year = int(input("Enter number of times interest is compounded per year: "))
    
    # Convert annual rate to a decimal
    annual_interest_rate /= 100
    
    # Future value formula
    future_value = principal * (1 + annual_interest_rate / compounding_per_year) ** (compounding_per_year * years)
    
    print(f"The future value of your investment is: ${future_value:.2f}")

def savings_goal_calculator():
    goal_amount = float(input("Enter your savings goal amount ($): "))
    annual_interest_rate = float(input("Enter expected annual rate of return (%): "))
    years = int(input("Enter time horizon (in years): "))
    compounding_per_year = int(input("Enter number of times interest is compounded per year: "))
    
    # Convert annual rate to a decimal
    annual_interest_rate /= 100
    
    # Monthly investment formula
    monthly_investment = goal_amount * (annual_interest_rate / compounding_per_year) / ((1 + annual_interest_rate / compounding_per_year) ** (compounding_per_year * years) - 1)
    
    print(f"You need to invest ${monthly_investment:.2f} every month to reach your savings goal.")

def income_tax_calculator():
    income = float(input("Enter your annual income ($): "))
    deductions = float(input("Enter your total deductions ($): "))
    
    # Taxable income
    taxable_income = income - deductions
    
    # Sample tax brackets for simplicity
    if taxable_income <= 9875:
        tax = taxable_income * 0.10
    elif taxable_income <= 40125:
        tax = 9875 * 0.10 + (taxable_income - 9875) * 0.12
    elif taxable_income <= 85525:
        tax = 9875 * 0.10 + (40125 - 9875) * 0.12 + (taxable_income - 40125) * 0.22
    elif taxable_income <= 163300:
        tax = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + (taxable_income - 85525) * 0.24
    else:
        tax = 9875 * 0.10 + (40125 - 9875) * 0.12 + (85525 - 40125) * 0.22 + (163300 - 85525) * 0.24 + (taxable_income - 163300) * 0.32

    print(f"Your estimated tax liability is: ${tax:.2f}")



def main():
    while True:
        print("\nFinancial Planning Toolkit")
        print("1. Mortgage Calculator")
        print("2. Investment Return Calculator")
        print("3. Savings Goal Calculator")
        print("4. Income Tax Calculator")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            mortgage_calculator()
        elif choice == '2':
            investment_calculator()
        elif choice == '3':
            savings_goal_calculator()
        elif choice == '4':
            income_tax_calculator()
        elif choice == '5':
            print("Exiting the toolkit.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()





























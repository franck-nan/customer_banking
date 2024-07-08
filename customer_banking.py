# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input(f"Please enter the initial savings account balance: "))
    savings_interest = float(input(f"Please enter the APR interest rate of your savings account: "))
    savings_maturity = int(input(f"Please enter the number of months of your savings account: "))
                             
    # Call the create_savings_account function and pass the variables from the user.
    savings_balance_updated, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your updated savings account balance is: ${savings_balance_updated:,.2f}")
    print(f"Your earned interest amount is ${savings_interest_earned:,.2f} ")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input(f"Please enter the initial CD account balance: "))
    cd_interest = float(input(f"Please enter the APR interest rate of your CD account: "))
    cd_maturity = int(input(f"Please enter the number of months of your CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    cd_balance_updated, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your updated CD account balance is: ${cd_balance_updated:,.2f}")
    print(f"Your earned interest amount is ${cd_interest_earned:,.2f} ")

if __name__ == "__main__":
    # Call the main function.
    main()
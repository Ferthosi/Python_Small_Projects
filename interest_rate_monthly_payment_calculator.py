#collect the necessaryinputs principle, apr, years
# calculate the monthly payment
# show to the user

def main():
    print("This is a monthly paument loann calculator")
    print("")

    principle= float(input("Enter the loan ammount: "))
    annual_interest = float(input("Enter the annual interest rate: "))
    years = int(input("Enter amount of years: "))

    monthly_interest = annual_interest/1200
    amount_of_months= years*12
    monthly_payment = principle*monthly_interest/(1-(1+monthly_interest)**(-amount_of_months))

    print("The monthly payment for this loan: %.2f " % monthly_payment)

main()


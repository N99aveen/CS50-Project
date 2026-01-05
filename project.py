"""
Financial Literacy Assistant (CLI)

This program helps users understand financial concepts,
calculate savings, SIP, investments, loans, retirement planning,
and overall financial health.

CS50P Final Project
"""

import sys
import math
from datetime import datetime


# =========================================================
# MAIN FUNCTION
# =========================================================
def main():
    show_welcome()

    while True:
        show_main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            explain_finance_terms()
        elif choice == "2":
            savings_calculator()
        elif choice == "3":
            investment_calculator()
        elif choice == "4":
            loan_calculator()
        elif choice == "5":
            sip_calculator()
        elif choice == "6":
            finance_calculators()
        elif choice == "7":
            risk_profile_assessment()
        elif choice == "8":
            budgeting_tips()
        elif choice == "9":
            financial_health_check()
        elif choice == "10":
            net_worth_calculator()
        elif choice == "11":
            emergency_fund_calculator()
        elif choice == "12":
            retirement_planner()
        elif choice == "13":
            exit_program()
        else:
            print("❌ Invalid choice. Try again.")


# =========================================================
# UI FUNCTIONS
# =========================================================
def show_welcome():
    print("=" * 70)
    print("📘 FINANCIAL LITERACY ASSISTANT (CLI)")
    print("Learn • Save • Invest • Grow")
    print(f"Date: {datetime.now().strftime('%d-%m-%Y')}")
    print("=" * 70)


def show_main_menu():
    print("\nMAIN MENU")
    print("1. Learn Financial Terms")
    print("2. Savings Calculator")
    print("3. Investment Calculator")
    print("4. Loan & EMI Calculator")
    print("5. SIP Calculator")
    print("6. Finance Calculators")
    print("7. Risk Profile Assessment")
    print("8. Budgeting Tips")
    print("9. Financial Health Check")
    print("10. Net Worth Calculator")
    print("11. Emergency Fund Calculator")
    print("12. Retirement Planner")
    print("13. Exit")


def exit_program():
    print("\nThank you for using Financial Literacy Assistant 🙏")
    sys.exit(0)


# =========================================================
# FINANCIAL TERMS (50+)
# =========================================================
def explain_finance_terms():
    terms = {
        "Savings": "Money kept aside for future use.",
        "Investment": "Using money to generate returns.",
        "Inflation": "Increase in prices reducing money value.",
        "EMI": "Equated Monthly Installment.",
        "SIP": "Systematic Investment Plan.",
        "Mutual Fund": "Pooled investment vehicle.",
        "Stock": "Ownership in a company.",
        "Bond": "Debt instrument with fixed return.",
        "FD": "Fixed Deposit.",
        "Credit Score": "Score representing creditworthiness.",
        "CAGR": "Compound Annual Growth Rate.",
        "Liquidity": "Ease of converting asset into cash.",
        "Diversification": "Spreading investment risk.",
        "Equity": "Ownership capital.",
        "Debt": "Borrowed capital.",
        "Assets": "What you own.",
        "Liabilities": "What you owe.",
        "Net Worth": "Assets minus liabilities.",
        "Index Fund": "Tracks market index.",
        "ETF": "Exchange Traded Fund.",
        "NAV": "Net Asset Value.",
        "Yield": "Income from investment.",
        "Capital Gain": "Profit from asset sale.",
        "Tax": "Government levy.",
        "Repo Rate": "RBI lending rate.",
        "Bull Market": "Rising market.",
        "Bear Market": "Falling market.",
        "Volatility": "Market fluctuation.",
        "Risk": "Uncertainty of returns.",
        "Return": "Profit from investment.",
        "Leverage": "Using borrowed money.",
        "Amortization": "Loan repayment structure.",
        "Principal": "Original loan amount.",
        "Tenure": "Loan duration.",
        "KYC": "Know Your Customer.",
        "PAN": "Permanent Account Number.",
        "Demat": "Electronic shares account.",
        "IPO": "Initial Public Offering",
        "Emergency Fund": "Money for emergencies",
        "Retirement Corpus": "Money saved for retirement",
        "Annuity": "Regular income product",
        "Real Return": "Return after inflation",
        "Asset Allocation": "Distribution of assets",
        "Expense Ratio": "Fund management cost"
    }

    print("\n📖 FINANCIAL TERMS")
    for term, meaning in terms.items():
        print(f"{term}: {meaning}")

    input("\nPress Enter to continue...")


# =========================================================
# SAVINGS
# =========================================================
def savings_calculator():
    print("\n💰 SAVINGS CALCULATOR")
    try:
        income = float(input("Monthly Income (₹): "))
        expenses = float(input("Monthly Expenses (₹): "))

        savings = income - expenses
        print(f"Monthly Savings: ₹{savings:.2f}")
        print(f"Yearly Savings: ₹{savings * 12:.2f}")

        analyze_savings_ratio(savings, income)

    except ValueError:
        print("❌ Invalid input.")


def analyze_savings_ratio(savings, income):
    ratio = savings / income
    if ratio >= 0.3:
        print("✅ Excellent savings habit")
    elif ratio >= 0.2:
        print("👍 Good savings habit")
    else:
        print("⚠️ Try to save more")


# =========================================================
# INVESTMENT
# =========================================================
def investment_calculator():
    print("\n📈 INVESTMENT CALCULATOR")
    try:
        p = float(input("Initial Investment (₹): "))
        r = float(input("Annual Return (%): "))
        t = int(input("Years: "))

        fv = calculate_compound_interest(p, r, t)
        print(f"Future Value: ₹{fv:.2f}")

    except ValueError:
        print("❌ Invalid input.")


def calculate_compound_interest(p, r, t):
    return p * ((1 + r / 100) ** t)


# =========================================================
# LOAN & EMI
# =========================================================
def loan_calculator():
    print("\n🏦 LOAN & EMI CALCULATOR")
    try:
        p = float(input("Loan Amount (₹): "))
        r = float(input("Annual Interest Rate (%): "))
        y = int(input("Tenure (years): "))

        emi = calculate_emi(p, r, y)
        total_payment = emi * y * 12

        print(f"Monthly EMI: ₹{emi:.2f}")
        print(f"Total Payment: ₹{total_payment:.2f}")
        print(f"Total Interest: ₹{total_payment - p:.2f}")

    except ValueError:
        print("❌ Invalid input.")


def calculate_emi(p, r, y):
    m = r / (12 * 100)
    n = y * 12
    return (p * m * (1 + m) ** n) / ((1 + m) ** n - 1)


# =========================================================
# SIP CALCULATOR
# =========================================================
def sip_calculator():
    print("\n📊 SIP CALCULATOR")
    try:
        monthly = float(input("Monthly SIP Amount (₹): "))
        rate = float(input("Expected Annual Return (%): "))
        years = int(input("Investment Duration (Years): "))

        fv = calculate_sip_future_value(monthly, rate, years)
        invested = monthly * years * 12

        print(f"Total Investment: ₹{invested:.2f}")
        print(f"Future Value: ₹{fv:.2f}")
        print(f"Total Gains: ₹{fv - invested:.2f}")

    except ValueError:
        print("❌ Invalid input.")


def calculate_sip_future_value(monthly, rate, years):
    months = years * 12
    r = rate / (12 * 100)
    return monthly * (((1 + r) ** months - 1) / r) * (1 + r)


# =========================================================
# FINANCE CALCULATORS
# =========================================================
def finance_calculators():
    print("\n📐 FINANCE CALCULATORS")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. CAGR")
    print("4. Inflation Adjusted Return")

    choice = input("Choose: ")

    try:
        if choice == "1":
            simple_interest()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            cagr_calculator()
        elif choice == "4":
            inflation_adjusted_return()
        else:
            print("Invalid choice")
    except ValueError:
        print("❌ Invalid input.")


def simple_interest():
    p = float(input("Principal: "))
    r = float(input("Rate (%): "))
    t = float(input("Time: "))
    print(f"SI: ₹{(p * r * t) / 100:.2f}")


def compound_interest():
    p = float(input("Principal: "))
    r = float(input("Rate (%): "))
    t = float(input("Time: "))
    print(f"CI: ₹{p * ((1 + r / 100) ** t):.2f}")


def cagr_calculator():
    start = float(input("Beginning Value: "))
    end = float(input("Ending Value: "))
    years = float(input("Years: "))
    cagr = ((end / start) ** (1 / years) - 1) * 100
    print(f"CAGR: {cagr:.2f}%")


def inflation_adjusted_return():
    nominal = float(input("Nominal Return (%): "))
    inflation = float(input("Inflation (%): "))
    real = ((1 + nominal / 100) / (1 + inflation / 100) - 1) * 100
    print(f"Real Return: {real:.2f}%")


# =========================================================
# ADDITIONAL MODULES
# =========================================================
def net_worth_calculator():
    print("\n📊 NET WORTH CALCULATOR")
    assets = float(input("Total Assets (₹): "))
    liabilities = float(input("Total Liabilities (₹): "))
    print(f"Net Worth: ₹{assets - liabilities:.2f}")


def emergency_fund_calculator():
    print("\n🚑 EMERGENCY FUND CALCULATOR")
    expenses = float(input("Monthly Expenses (₹): "))
    months = 6
    print(f"Recommended Emergency Fund: ₹{expenses * months:.2f}")


def retirement_planner():
    print("\n👴 RETIREMENT PLANNER")
    age = int(input("Current Age: "))
    retire_age = int(input("Retirement Age: "))
    monthly_expense = float(input("Expected Monthly Expense (₹): "))

    years = retire_age - age
    corpus = monthly_expense * 12 * 25
    print(f"Years to Retirement: {years}")
    print(f"Estimated Retirement Corpus Needed: ₹{corpus:.2f}")


# =========================================================
# RISK PROFILING
# =========================================================
def risk_profile_assessment():
    print("\n📊 RISK PROFILE")
    score = 0

    score += ask_question("Age?", ["<25", "25-40", "40-55", "55+"], [4, 3, 2, 1])
    score += ask_question("Investment Horizon?", ["10+ years", "5-10", "3-5", "<3"], [4, 3, 2, 1])
    score += ask_question("Market Reaction?", ["Buy", "Hold", "Wait", "Sell"], [4, 3, 2, 1])

    show_risk_result(score)


def ask_question(q, options, scores):
    print(q)
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    return scores[int(input("Choose: ")) - 1]


def show_risk_result(score):
    if score >= 10:
        print("🔥 High Risk Investor")
    elif score >= 7:
        print("⚖️ Moderate Risk Investor")
    else:
        print("🛡️ Low Risk Investor")


# =========================================================
# TIPS & HEALTH
# =========================================================
def budgeting_tips():
    tips = [
        "Save at least 20% of income",
        "Track expenses",
        "Avoid unnecessary debt",
        "Build emergency fund",
        "Invest early",
        "Diversify investments"
    ]
    print("\n💡 BUDGETING TIPS")
    for t in tips:
        print("-", t)


def financial_health_check():
    income = float(input("Monthly Income: "))
    savings = float(input("Monthly Savings: "))
    emi = float(input("Monthly EMI: "))

    if savings / income >= 0.2:
        print("✅ Healthy savings")
    else:
        print("⚠️ Improve savings")

    if emi / income <= 0.35:
        print("✅ EMI under control")
    else:
        print("❌ High debt burden")


# =========================================================
# ENTRY POINT
# =========================================================
if __name__ == "__main__":
    main()

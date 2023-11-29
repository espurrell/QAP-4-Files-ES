#QAP 4 - One Stop Insurance Company#
#Program designed to enter and calculate new insurance policy information for customers
#Prepared for: Maurice Baubin
#Prepared by: Ed Spurrell
#Date Completed:


#imports 

import FormatValues as FV

import datetime

from datetime import date, timedelta


#set up program constants

NEXT_POL_NUM = 1944
BASE_PREM = 869.00
MULTI_VEH_DISC = .25
ADD_VEH = 651.75
EXTRA_LIAB_RATE = 130.00
GLASS_COV_RATE = 86.00
SEF_27_RATE = 58.00
HST_RATE = 0.15
PROCESS_FEE = 39.99
PMT_MONTHS = 8
CLAIM_NUM = 1944

#Define  program functions


#User Inputs

while True:

    CustFirstName = input("Please enter your first name: ").title()
    CustLastName = input("Please enter your last name: ").title()
    StreetAdd = input("Please enter your street address: ")
    City = input("Please enter your home city: ").title()

    ValidProvLst = ["AB","BC","MN","NB","NL","NS","ON","PE","QC","SK","NT","YT","NU"]
    while True: 
        Prov = input("Please enter your home province (abbreviated): ").upper()
        if Prov == "":
            print("Please make a selection, province cannot be blank.")
        elif len(Prov) != 2:
            print("Please re-enter your selection, must be 2 digits")
        elif Prov not in ValidProvLst:
            print("Please re-enter, selection was not a valid province.")
        else:
            break

    PostCode = input("Please enter your postal code: ").upper()

    PhoneNum = input("Please enter your phone number (##########): ")
    
    while True:    
        NumCars = input("Please enter the number of vehicles you will be insuring: ")

        if NumCars.isdigit():
            break
        else: 
            print("Please re-enter your selection, invalid input.")
        

    while True:
        IncrLiabCov = input("Would you like to increase liability coverage to $1 million? Y/N:").upper

        if IncrLiabCov == "":
            print("Please make a selection, do you wish to increase liability coverages?")
        else:
            break

    while True:
        OptGlassCov = input("Would you like to include glass coverage? (Y/N):").upper

        if OptGlassCov == "":
            print("Please make a selection, do you wish to include optional glass coverages? (Y/N) ")
        else:
            break

    while True:
        Sef27 = input("Would you like us to include loss of use coverages? (Y/N):").upper

        if Sef27 == "":
            print("Please make a selection, do you wish to include loss of use coverage?")
        else:
            break

    ValidPmtLst = ["F","M","D"]
    while True:
        Payment = input("Please enter your payment method, in Full(F) or Monthly(M). To have a downpayment on monthly, enter 'D' instead.").title()
        if Payment == "":
            print ("Please make a selection, payment cannot be blank.")
        elif len(Payment) != 1:
            print("Please re-enter your selection, can only include 1 digit.")
        elif Payment not in ValidPmtLst:
            print("Please re-enter, selection was not a valid option (F,M,D).")
        else:
            break

        while True:
            if Payment == "D":
                try:
                    DownPmtAmt = float(input("Please enter the amount of downpayment: "))
                except:
                    print("Error: Downpayment must be a numerical amount, please re-enter:")
                if DownPmtAmt == "":
                    print ("Please make a selection, downpayment amount cannot be left blank.")
                else:
                    break
    
    
    
    ClaimLst = []
    while True:
        ClaimDate = input ("Please enter when your claim occurred (YYYY-MM-DD):(press enter to finish) ")
        if ClaimDate == "":
            break

        ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
        ClaimAmt = float(input("Please enter total claim amount: "))
        ClaimNum = CLAIM_NUM + 1

        ClaimLst.append((ClaimNum, FV.FDateS(ClaimDate), FV.FDollar2(ClaimAmt)))
        



    #calculations

    #multi car
    NumCars = int(NumCars)
    if NumCars == 1:
        CarPrem = BASE_PREM
    else:
        CarPrem = (BASE_PREM) + (NumCars - 1) * ADD_VEH
    
    AddCar = (NumCars - 1) * ADD_VEH

    #optional coverages

    if IncrLiabCov == "Y":
        IncrLiabChrg = EXTRA_LIAB_RATE
        IncrLiabDsp = "Y"
    else:
        IncrLiabChrg = 0
        IncrLiabDsp = "N"
    
    if OptGlassCov == "Y":
        OptGlassCov = GLASS_COV_RATE
        OptGlassDsp = "Y"
    else:
        OptGlassCov = 0
        OptGlassDsp = "N"

    if Sef27 == "Y":
        Sef27 = SEF_27_RATE
        Sef27Dsp = "Y"
    else:
        Sef27 = 0
        Sef27Dsp = "N"
    
    #paymenttype
    if Payment == "F":
        PaymentDsp = "Full"
    elif Payment == "M":
        PaymentDsp = "Monthly"
    else:
        PaymentDsp = "Down Payment (Monthly)"


 #PaymentCalcs

    OptCovCost= IncrLiabChrg + OptGlassCov + Sef27
    TotalCost = CarPrem + OptCovCost
    Tax = TotalCost * HST_RATE
    TotInclTax = TotalCost + Tax

    if Payment == "D":
        MonthlyCost = (TotInclTax - DownPmtAmt + PROCESS_FEE) / PMT_MONTHS
        PaymentDsp = "Down Payment (Monthly) - Fees apply"
    elif Payment == "M":
        MonthlyCost = (TotInclTax + PROCESS_FEE) / PMT_MONTHS
        PaymentDsp = "Monthly - Fees apply"
    else:
        PaymentDsp = "In Full"


    #dateformating

    today = date.today()

    FirstPmtDate = date(today.year, today.month, 1) + timedelta(days=32 -today.day)

    FirstPmtDate = FirstPmtDate.replace(day=1,month=FirstPmtDate.month + 1)


    #Outputs - well-designed receipt
    
    print()
    print(f"        One Stop Insurance Company      ")
    print(f"       Insurance Policy Information          ")
    print()
    print(f"         Invoice Date: {today} ")
    print(f"___________________________________________")
    print()
    print(f"Applicant Details: ")
    print()
    custname = CustFirstName + " " + CustLastName
    print(f"Applicant Name:  {custname:<24s}")
    print()
    print(f"Address:         {StreetAdd:<24s}")
    mailadd = Prov + " " + PostCode
    print(f"                 {City:<12s}{mailadd:<12s}")
    print()
    print(f"Phone #:         {PhoneNum:<10s}")
    print()
    print()
    print(f"         ------------------------          ")
    print()
    print(f"Quote Details: ")
    print()
    print(f"Number of Vehicles:  {NumCars:<10d} ")
    print(f"Optional Liability:  {IncrLiabDsp:<10s}")
    print(f"Optional Glass:      {OptGlassDsp:<10s}")
    print(f"Optional Loaner:     {Sef27Dsp:<10s}")
    print(f"Payment Type:        {PaymentDsp:<22s}")
    print()
    print()
    print(f"Premium Amounts: ") 
    print()
    BasePremDsp = "${:,.2f}".format(BASE_PREM)
    print(f"Base Premium:           {BasePremDsp:>10s}") 
    print()
    AddCarDsp = "${:,.2f}".format(AddCar)
    print(f"Additional Vehicle(s):  {AddCar:>10d} ")
    IncrLiabCovDsp = "${:,.2f}".format(IncrLiabChrg)
    print(f"Increased Liability:    {IncrLiabChrg:>10s}")
    OptGlassCovDsp = "${:,.2f}".format(OptGlassCov)
    print(f"Additional Glass:       {OptGlassCovDsp:>10s}")
    Sef27Dsp = "${:,.2f}".format(Sef27)
    print(f"Loaner Vehicle(SEF27):  {Sef27Dsp:>10s}")
    print(f"                         ---------")
    print(f"Total Optional:         {OptCovCost:>10s}")
    print(f"                         ---------")
    print(f"Base + Optional:        {TotalCost:>10s}")
    print(f"Tax:                    {Tax:>10s}")
    print(f"                         ---------")
    print(f"Subtotal:               {TotInclTax:>10s}")
    print()
    print(f"Monthly Payments:       {MonthlyCost:>10s}")
    print(f"Payment Start Date:     {FirstPmtDate}")
    print()
    print(f"Previous Claims:")
    print(f"Claim Number:    Date:     Amount:         ")
    print(f"-------------------------------------------")
    #for i in range(0,len(ClaimLst)):
        #claim_date = datetime.datetime.strptime(ClaimsLst[i][1], "%Y-%m-%d")
        #print(f"{ClaimNum} {FV.FDateM(ClaimDate)}      {FV.FDollar2(ClaimAmt)}")
    print(f"-------------------------------------------")
    print(f" One Stop Insurance Company, come stop by! ")
    print(f"-------------------------------------------")
    print()
    print()
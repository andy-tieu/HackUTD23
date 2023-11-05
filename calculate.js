function getValues() {
    var creditScore = parseInt(document.getElementById("creditScore").value);
    var downPay = parseFloat(document.getElementById("downPay").value);
    var grossMonthlyIncome = parseFloat(document.getElementById("grossIncome").value);
    var houseValue = parseFloat(document.getElementById("houseValue").value);
    var mortgage = parseFloat(document.getElementById("mortgage").value);
    var creditCardPay = parseFloat(document.getElementById("creditCardPay").value);
    var carPay = parseFloat(document.getElementById("carPay").value);
    var studentLoan = parseFloat(document.getElementById("studentLoans").value);

    var LTVValue = LTV(downPay, houseValue);
    if(LTVValue > 0.80) {
        var PMIValue = PMI(houseValue);
    }
    else {
        var PMIValue = 0;
    }
    var monthlyDebtValue = monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMIValue);
    var DTIValue = DTI(monthlyDebtValue, grossMonthlyIncome);
    var FEDTIValue = FEDTI(mortgage, grossMonthlyIncome);

    if(creditScore < 640) {
        document.getElementById("creditScoreOut").innerHTML = "Your credit score is " + creditScore + ", which is less than 640."
        + " To have a better chance of being eligible to buy a house, increasing your credit score is a fundamental step to doing so."
        + " Please chat with the AI bot to see what methods can be used to increase your own credit score.";
    }
    else {
        document.getElementById("creditScoreOut").innerHTML = "Your credit score is " + creditScore + ", which is greater than or equal to 640."
        + " There is nothing else to do with credit score since you meet the required condition."
    }

    if(LTVValue > 0.80) {
        document.getElementById("LTVOut").innerHTML = "Your current loan-to-value is " + LTVValue*100 + "%, which exceeds the 80% needed to be eligible."
        + " The recommended course of action here is to find a cheaper appraised house or increase down payment to reach the 80% and avoid the private mortgage insurance."
        + " If you decide to continue, keep in mind that an approximate private mortgage insurance monthly payment of $" 
        + PMIValue.toFixed(2) + " would be necessary."
        + " Please consult the AI bot for further questions and recommended action to take.";
    }
    else {
        document.getElementById("LTVOut").innerHTML = "Your current loan-to-value of " + LTVValue*100 + "% meets the condition of less than or equal 80%.";
    }

    if(DTIValue > 0.43) {
        document.getElementById("DTIOut").innerHTML = "Your current debt-to-income ratio is " + (DTIValue*100).toFixed(2) + "%, which exceeds the 43% needed to be eligible."
        + " The recommended course of action here is to pay off current debts or move high interest loans to a low interest credit card."
        + " Keep in mind that having many credit cards could also be risky as it could become more payments to be liable for." 
        + " Please consult the AI bot for further questions and recommended action to take.";
    }
    else {
        document.getElementById("DTIOut").innerHTML = "Your current debt-to-income ratio is " + (DTIValue*100).toFixed(2) +
        "%, which meets the recommended value of less than 43%.";
    }

    if(FEDTIValue > 0.28) {
        document.getElementById("FEDTIOut").innerHTML = "Your current frontend debt-to-income ratio is " + FEDTIValue*100 + "%, which exceeds the 28% needed to be eligible."
        + " To lower this, your monthly income must become higher or to lower your mortgage payments to reduce the ratio low enough to be eligible."
        + " Please consult the AI bot for further questions and recommended action to take.";
    }   
    else {
        document.getElementById("FEDTIOut").innerHTML = "Your current frontend debt-to-income ratio is " + FEDTIValue*100 + "%, which meets the less than or equal to 28% condition needed to be eligible.";
    }
}

function LTV(downPayment, houseValue) {
    return 1-(downPayment/houseValue);
}

function PMI(houseValue) {
    return (0.01 * houseValue) / 12;
}

function monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMIValue) {
    var sum = 0;
    sum += carPay;
    sum += creditCardPay;
    sum += mortgage;
    sum += studentLoan;
    sum += PMIValue;
    return sum;
}

function DTI(monthlyDebt, grossMonthlyIncome) {
    return monthlyDebt / grossMonthlyIncome;
}

function FEDTI(mortgage, grossMonthlyIncome) {
    return mortgage / grossMonthlyIncome;
}


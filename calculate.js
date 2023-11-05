function getValues() {
    var downPay = parseFloat(document.getElementById("downPay").value);
    var grossMonthlyIncome = parseFloat(document.getElementById("grossIncome").value);
    var houseValue = parseFloat(document.getElementById("houseValue").value);
    var mortgage = parseFloat(document.getElementById("mortgage").value);
    var creditCardPay = parseFloat(document.getElementById("creditCardPay").value);
    var carPay = parseFloat(document.getElementById("carPay").value);
    var studentLoan = parseFloat(document.getElementById("studentLoans").value);

    var LTVResult = LTV(downPay, houseValue);
    alert(LTVResult);

    var PMIValue = PMI(houseValue);

    var monthlyDebtResult = monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMIValue);

    var DTIResult = DTI(monthlyDebtResult, grossMonthlyIncome);

    var FEDTIResult = FEDTI(mortgage, grossMonthlyIncome);
}

function LTV(downPayment, houseValue) {
    return downPayment / houseValue;
}

function PMI(houseValue) {
    return (0.01 * houseValue) / 12;
}

function monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMIValue) {
    return carPay + creditCardPay + mortgage + studentLoan + PMIValue;
}

function DTI(monthlyDebt, grossMonthlyIncome) {
    return monthlyDebt / grossMonthlyIncome;
}

function FEDTI(mortgage, grossMonthlyIncome) {
    return mortgage / grossMonthlyIncome;
}

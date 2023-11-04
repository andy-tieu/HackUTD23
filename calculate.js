function LTV(downPayment, houseValue) {
    return downPayment/houseValue;
}

function PMI(houseValue) {
    return (0.01 * houseValue)/12;
}

function monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMI) {
    return carPay + creditCardPay + mortgage + studentLoan + PMI;
}

function DTI(monthlyDebt, grossMonthlyIncome) {
    return monthlyDebt/grossMonthlyIncome;
}

function FEDTI(mortgage, grossMonthlyIncome) {
    return mortgage/grossMonthlyIncome;
}
document.getElementById("submitButton").addEventListener("click", function () {
    // Get the input value
    var grossMonthlyIncome = document.getElementById("grossIncome").value;
    var houseValue = document.getElementById("houseValue").value;
    var mortgage = document.getElementById("mortgage").value;
    var creditCardPay = document.getElementById("creditCardPay").value;
    var carPay = document.getElementById("carPay").value;
    var studentLoan = document.getElementById("studentLoans").value;
    alert("Your mortgage is $" + mortgage);
});

function LTV(downPayment, houseValue) {
    return downPayment/houseValue;
}

function PMI(houseValue) {
    return (0.01 * houseValue)/12;
}

var PMIValue = PMI(houseValue);

function monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMIValue) {
    return carPay + creditCardPay + mortgage + studentLoan + PMI;
}

var monthlyDebt = monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMIValue);

function DTI(monthlyDebt, grossMonthlyIncome) {
    return monthlyDebt/grossMonthlyIncome;
}

function FEDTI(mortgage, grossMonthlyIncome) {
    return mortgage/grossMonthlyIncome;
}
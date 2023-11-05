function getValues() {
    var downPay = parseFloat(document.getElementById("downPay").value);
    var grossMonthlyIncome = parseFloat(document.getElementById("grossIncome").value);
    var houseValue = parseFloat(document.getElementById("houseValue").value);
    var mortgage = parseFloat(document.getElementById("mortgage").value);
    var creditCardPay = parseFloat(document.getElementById("creditCardPay").value);
    var carPay = parseFloat(document.getElementById("carPay").value);
    var studentLoan = parseFloat(document.getElementById("studentLoans").value);

    var LTVValue = LTV(downPay, houseValue);
    var PMIValue = PMI(houseValue);
    var monthlyDebtValue = monthlyDebt(carPay, creditCardPay, mortgage, studentLoan, PMIValue);
    var DTIValue = DTI(monthlyDebtValue, grossMonthlyIncome);
    var FEDTIValue = FEDTI(mortgage, grossMonthlyIncome);
    alert(LTVValue);
    alert(PMIValue);
    alert(DTIValue);
    alert(FEDTIValue);

    fetch('/api/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(inputData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the API response data
    })
    .catch(error => {
        // Handle any errors
    });
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

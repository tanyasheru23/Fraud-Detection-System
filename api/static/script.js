const predictBtn = document.getElementById("predictBtn");
const spinner = document.getElementById("loading-spinner");
const featureNames = {

    balanceDiffOrig: "Origin Balance Difference",

    balanceDiffDest: "Destination Balance Difference",

    origError: "Origin Balance Error",

    destError: "Destination Balance Error",

    fraction_used: "Fraction of Balance Used",

    remaining_fraction: "Remaining Balance Fraction",

    transaction_fraction: "Transaction Fraction",

    origin_zero_balance: "Origin Balance is Zero",

    destination_zero_balance: "Destination Balance is Zero",

    origin_balance_changed: "Origin Balance Changed",

    destination_balance_changed: "Destination Balance Changed",

    full_balance_transfer: "Entire Balance Transferred",

    is_cash_transfer: "Cash Transfer Transaction",
    
    type_TRANSFER: "Transaction type: TRANSFER",

    type_CASH_OUT: "Transaction type: CASH_OUT",

    type_CASH_IN: "Transaction type: CASH_IN"

};

predictBtn.addEventListener("click", predictTransaction);

async function predictTransaction() {

    const form = document.getElementById("fraudForm");

    if (!form.checkValidity()) {
        console.log("Validation failed");
        form.reportValidity();
        return;
    }

    predictBtn.disabled = true;

    const transaction = {

        step: Number(document.getElementById("step").value),
        type: document.getElementById("type").value,
        amount: Number(document.getElementById("amount").value),

        nameOrig: document.getElementById("nameOrig").value,
        oldbalanceOrg: Number(document.getElementById("oldbalanceOrg").value),
        newbalanceOrig: Number(document.getElementById("newbalanceOrig").value),

        nameDest: document.getElementById("nameDest").value,
        oldbalanceDest: Number(document.getElementById("oldbalanceDest").value),
        newbalanceDest: Number(document.getElementById("newbalanceDest").value)

    };

    
    try {
        spinner.style.display = "block";
        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(transaction)

        });

        const result = await response.json();

        document.getElementById("percentage").textContent =
            result.fraud_percentage + "%";
        
        const predictionElement = document.getElementById("prediction");

        predictionElement.textContent = result.prediction;

        // Remove any previous class
        predictionElement.classList.remove("fraud", "legitimate");

        // Add the correct one
        if (result.is_fraud) {
            predictionElement.classList.add("fraud");
        } else {
            predictionElement.classList.add("legitimate");
        }

        const featureList = document.getElementById("top-features");

        featureList.innerHTML = "";

        result.top_features.forEach(item => {

            const listItem = document.createElement("li");

            const name =
                featureNames[item.feature] ?? item.feature;

            listItem.textContent =
                `${name}: ${item.contribution.toFixed(1)}%`;

            featureList.appendChild(listItem);

        });
    }

    catch(error){

        console.error(error);

        document.getElementById("prediction").textContent =
            "Prediction Failed";

        document.getElementById("percentage").textContent =
            "--";

        document.getElementById("top-features").innerHTML = "";
    }
    finally{
        predictBtn.disabled = false;
        spinner.style.display = "none";
    }
}
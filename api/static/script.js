const predictBtn = document.getElementById("predictBtn");
const spinner = document.getElementById("loading-spinner");

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

        document.getElementById("prediction").textContent =
            result.prediction;

        document.getElementById("percentage").textContent =
            result.fraud_percentage + "%";
    }

    catch(error){

        console.error(error);

        document.getElementById("prediction").textContent =
            "Prediction Failed";

        document.getElementById("percentage").textContent =
            "--";
    }
    finally{
        predictBtn.disabled = false;
        spinner.style.display = "none";
    }
}
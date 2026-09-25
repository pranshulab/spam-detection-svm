async function checkMessage() {

    const message = document.getElementById("message").value;

    const result = document.getElementById("result");


    // Check if message is empty

    if (message.trim() === "") {

        result.innerHTML = "⚠️ Please enter a message.";

        return;
    }


    // Show loading message

    result.innerHTML = "🔄 Checking...";


    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (data.prediction === "Spam") {

            result.innerHTML = `
        <div>
            🚨 SPAM MESSAGE
            <br>
            <small>SVM Score: ${data.svm_score}</small>
        </div>
    `;

        } else {

            result.innerHTML = `
        <div>
            ✅ HAM — SAFE MESSAGE
            <br>
            <small>SVM Score: ${data.svm_score}</small>
        </div>
    `;

        }


    } catch (error) {

        result.innerHTML =
            "❌ Error connecting to the server.";

        console.error(error);

    }

}
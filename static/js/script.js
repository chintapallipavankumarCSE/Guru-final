function askQuestion() {
    const url = document.getElementById('url').value;
    const question = document.getElementById('question').value;
    const responseContainer = document.getElementById('response');

    if (!url || !question) {
        responseContainer.innerHTML = "Please provide both URL and question.";
        return;
    }

    responseContainer.innerHTML = "Loading...";

    // Send the URL and question to the Flask backend
    fetch('http://localhost:5000/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url, question }),
    })
    .then(response => response.json())
    .then(data => {
        responseContainer.innerHTML = data.answer || "No answer found.";
    })
    .catch(err => {
        responseContainer.innerHTML = "Error fetching data.";
        console.log(err);
    });
}

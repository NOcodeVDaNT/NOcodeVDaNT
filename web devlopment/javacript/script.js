async function askWolframAlpha() {
    const query = document.getElementById('query').value;
    const appId = 'E5W64X-9G4YTU9AVR'; // Replace with your Wolfram|Alpha API key

    try {
        console.log("vedant");
        const response = await fetch(`https://api.wolframalpha.com/v1/result?i=${encodeURIComponent(query)}&appid=${appId}`);
        
       console.log(response);

        const data = await response.text();
        document.getElementById('result').textContent = data;
    }
     catch (error) {
        document.getElementById('result').innerText= 'Error: ' + error.message;
        console.log(error);
    }
}

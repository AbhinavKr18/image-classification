const form = document.querySelector('#image-form');
const predictionContainer = document.querySelector('#prediction-container');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const formData = new FormData(event.target);
  document.getElementById('loading').style.display = 'inline-block';

  try {
    // Send a POST request to the server with the image data
    const response = await fetch('/predict', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error(`Failed with status ${response.status}`);
    }

    // Parse the response and display the prediction
    const prediction = await response.json();

    // Hide the loading animation and displaying the prediction
    setTimeout(() => {
      document.getElementById('loading').style.display = 'none';
      predictionContainer.innerHTML = `<p>Prediction: ${prediction.class}</p>`;
    }, 600);

  } catch (error) {
    // Display an error message if something went wrong
    console.error(error);
    predictionContainer.innerHTML = `<p class="error">Something went wrong.</p>`;
  }
});
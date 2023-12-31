function predictCharacter() {
  const fileInput = document.getElementById('imageUpload');
  const predictionOutput = document.getElementById('predictionOutput');
  const predictionImagePreview = document.getElementById('predictionImagePreview');

  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append('file', file);

  const url = '/predict'; // Replace this with your endpoint URL

  fetch(url, {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      updatePredictionUI(predictionOutput, data);
      displayImagePreview(predictionImagePreview, file, data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function updatePredictionUI(element, prediction) {
  element.textContent = `Prediction: ${prediction.prediction}`;
}
// Function to handle file change (show image preview)
function handleFileChange(event) {
  const file = event.target.files[0];
  displayImagePreview(file);
}

function displayImagePreview(file) {
  const reader = new FileReader();

  reader.onload = function (event) {
    const img = new Image();
    img.src = event.target.result;

    img.onload = function () {
      const imagePreview = document.getElementById('imagePreview');
      imagePreview.src = img.src;
      imagePreview.style.display = 'block';
    };
  };

  if (file) {
    reader.readAsDataURL(file);
  }
}

document.getElementById('imageUpload').addEventListener('change', handleFileChange);
// Event listener for scrolling to sections
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();

    const targetId = this.getAttribute('href').substring(1);
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
      targetElement.scrollIntoView({
        behavior: 'smooth'
      });
    }
  });
});



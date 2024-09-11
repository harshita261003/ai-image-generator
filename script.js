// script.js
document.getElementById('imageForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const prompt = document.getElementById('prompt').value;
    
    try {
        const response = await fetch('/generate-image', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        });
        const data = await response.json();
        document.getElementById('generatedImage').src = data.image_url;
    } catch (error) {
        console.error('Error:', error);
    }
});

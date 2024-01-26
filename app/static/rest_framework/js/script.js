    document.getElementById('submitBtn').addEventListener('click', function() {
        var fileInput = document.getElementById('fileInput');
        var file = fileInput.files[0];
        var formData = new FormData();
        formData.append('audioFile', file);

         fetch('/api/v1/upload-file/', {
            method: 'POST',
            body: formData
            })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = data.transcription;
        })
        .catch(error => console.error('Error:', error));
    });
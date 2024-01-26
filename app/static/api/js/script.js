document.getElementById('submitBtn').addEventListener('click', function() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('audioFile', file, file.name); // Указываем имя файла

    for (var pair of formData.entries()) {
        console.log(pair[0] + ', ' + pair[1]);
    }

    fetch('/api/v1/upload-file/', {
        method: 'POST',
        body: formData,
        headers: {
            'Accept': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.transcription;
    })
    .catch(error => console.error('Error:', error));
});

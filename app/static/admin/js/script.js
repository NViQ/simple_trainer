document.getElementById('submitBtn').addEventListener('click', function() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('audioFile', file, file.name);

    // Для отладки, вывод содержимого FormData
    for (var pair of formData.entries()) {
        console.log(pair[0] + ', ' + pair[1]);
    }

    fetch('/api/v1/upload-file/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) // Преобразование ответа в JSON
    .then(data => {
        // Обращаемся к конкретному свойству ответа
        if (data.transcription) {
            document.getElementById('result').innerText = data.transcription;
        } else if (data.error) {
            document.getElementById('result').innerText = data.error;
        } else {
            document.getElementById('result').innerText = 'Неизвестная ошибка';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Ошибка при запросе';
    });
});

document.querySelector('.custom-file-button').addEventListener('click', function() {
    document.getElementById('file-upload').click();
});
document.getElementById('form-id').addEventListener('submit', function(event) {
    event.preventDefault(); 
});

document.getElementById("btn-upload").addEventListener('click',function(){
    var fileInput = document.getElementById('file-upload');
    if (fileInput.files.length > 0) {
        var file = fileInput.files[0];
        console.log('File selected:', file.name);

        // Optionally, use FormData to submit the form via AJAX
        var formData = new FormData();
        formData.append('file', file);
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(result => console.log('Success:', result))
        .catch(error => console.error('Error:', error));
    } else {
        console.log('No file selected');
    }
});
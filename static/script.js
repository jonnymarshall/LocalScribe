function dragOverHandler(event) {
  event.preventDefault();  // Prevent the browser from performing the default action for the event.
  console.log('Drag over the drop zone.');
}

function dropHandler(event) {
  event.preventDefault();  // This is crucial to prevent the browser from navigating to the file.
  console.log('File dropped.');

  if (event.dataTransfer.items) {
    // Use DataTransferItemList interface to access the file(s)
    console.log(`Dropped ${event.dataTransfer.items.length} items.`);
    for (var i = 0; i < event.dataTransfer.items.length; i++) {
      if (event.dataTransfer.items[i].kind === 'file') {
        var file = event.dataTransfer.items[i].getAsFile();
        console.log(`... file[${i}].name = ${file.name}`);
        uploadFile(file);
      }
    }
  } else {
    // Use DataTransfer interface to access the file(s)
    console.log(`Dropped ${event.dataTransfer.files.length} files.`);
    for (var i = 0; i < event.dataTransfer.files.length; i++) {
      console.log(`... file[${i}].name = ${event.dataTransfer.files[i].name}`);
      uploadFile(event.dataTransfer.files[i]);
    }
  }
}

function uploadFile(file) {
  var url = '/upload';
  var formData = new FormData();
  formData.append('file', file);

  fetch(url, {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(result => {
      console.log('Success:', result);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

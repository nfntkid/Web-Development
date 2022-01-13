/* will take the note id that we pass and send 
 a post request to the delete note endpoint
 after getting a response it will refresh the page */
function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteImage(imgId) {
  fetch("/delete-img", {
    method: "POST",
    body: JSON.stringify({ imgId: imgId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}


// Set the Width and Height of the resized image 

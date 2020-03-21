let inputs = document.getElementsByClassName("inputfile")

Array.prototype.forEach.call(inputs, function (input) {
  input.addEventListener("change", function (e) {

    if (this.files) {
      if (validateFileSize()) {
        document.getElementById("file-name").innerText = e.target.value.split("\\").pop()
        document.getElementById("upload-btn").disabled = false
      } else {
        alert("File size is too large, the limit is 2MB")
      }
    }
  })

  input.addEventListener("focus", function () { input.classList.add("has-focus") })
  input.addEventListener("blur", function () { input.classList.remove("has-focus") })
})

function validateFileSize() {
  let input, file

  if (!window.FileReader) {
    console.error("The file API isn't supported on this browser yet")
    return
  }

  input = document.getElementById("file")

  if (!input) {
    console.error("Can't find the File input element")
  }
  else if (!input.files) {
    console.error("This browser don't support the `files` property of file inputs")
  }
  else {
    file = input.files[0]

    if (file.size > 2 * 1024 * 1024) {
      return false
    }
    return true
  }
}
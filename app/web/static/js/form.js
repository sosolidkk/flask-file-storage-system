let inputs = document.getElementsByClassName("inputfile")

Array.prototype.forEach.call(inputs, function (input) {
  input.addEventListener("change", function (e) {
    let fileName = ""

    if (this.files) {
      document.getElementById("upload-btn").innerText = e.target.value.split("\\").pop()
      document.getElementById("upload-btn").disabled = false
    }
  })

  input.addEventListener("focus", function () { input.classList.add("has-focus"); });
  input.addEventListener("blur", function () { input.classList.remove("has-focus"); });
})
let inputs = document.getElementsByClassName("inputfile")

Array.prototype.forEach.call(inputs, function (input) {
  input.addEventListener("change", function (e) {
    let fileName = ""
    let label = input.nextElementSibling
    let labelVal = label.innerHTML

    console.log("Entrou aqui")
    if (this.files)
      fileName = e.target.value.split("\\").pop();

    if (fileName)
      label.querySelector("span").innerHTML = fileName;
    else
      label.innerHTML = labelVal;

    document.getElementById("upload-btn").disabled = false
  })

  input.addEventListener("focus", function () { input.classList.add("has-focus"); });
  input.addEventListener("blur", function () { input.classList.remove("has-focus"); });
})
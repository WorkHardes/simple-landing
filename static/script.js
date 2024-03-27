document.addEventListener("click", function (e) {
  if (e.target.classList.contains("gallery-item")) {
    const src = e.target.getAttribute("src");
    document.querySelector(".modal-img").src = src;

    content = document.querySelector(".opalubka-img-header").innerHTML;
    document.querySelector(".modal-title").innerHTML = content;

    content = document.querySelector(".opalubka-img-description").innerHTML;
    document.querySelector(".modal-description").innerHTML = content;

    const myModal = new bootstrap.Modal(
      document.getElementById("gallery-popup")
    );
    myModal.show();
  }
});

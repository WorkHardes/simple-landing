// Order
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("orderForm");
  const sendButton = document.getElementById("sendButton");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    try {
      const formworkInput = form.elements["formworkType"];
      const formworkTypeValue = formworkInput.value;
      const totalAreaInput = form.elements["totalArea"];
      const totalAreaValue = totalAreaInput.value;
      const addressInput = form.elements["address"];
      const addressValue = addressInput.value;
      const customerNameInput = form.elements["customerName"];
      const customerNameValue = customerNameInput.value;
      const customerPhoneInput = form.elements["customerPhoneNumber"];
      const customerPhoneValue = customerPhoneInput.value;
      const customerEmailInput = form.elements["customerEmail"];
      const customerEmailValue = customerEmailInput.value;

      const response = await fetch("http://localhost:5000/api/v1/mail", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          formwork_type: formworkTypeValue,
          total_area: totalAreaValue,
          address: addressValue,
          customer_name: customerNameValue,
          customer_phone_number: customerPhoneValue,
          customer_email: customerEmailValue,
        }),
      });

      if (response.ok) {
        alert("Message sent successfully!");
        form.reset();
      } else {
        throw new Error("Failed to send message.");
      }
    } catch (error) {
      console.error(error);
      alert("An error occurred while sending the message.");
    } finally {
      sendButton.disabled = false;
    }
  });
});

// Gallery
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

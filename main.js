document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
  }

  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = document.getElementById("form-status");
      status.style.display = "block";
      status.style.color = "#4f8cff";
      status.textContent = "문의가 접수되었습니다. 입력하신 이메일로 빠른 시일 내에 답변드리겠습니다.";
      form.reset();
    });
  }
});

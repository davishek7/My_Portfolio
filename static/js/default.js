let theme = localStorage.getItem("theme");

if (theme == null) {
  setTheme("light");
} else {
  setTheme(theme);
}

let themeDots = document.getElementsByClassName("theme-dot");

for (var i = 0; themeDots.length > i; i++) {
  themeDots[i].addEventListener("click", function () {
    let mode = this.dataset.mode;
    setTheme(mode);
  });
}

const setTheme = (mode) => {
  if (mode == "light") {
    document.getElementById("theme-style").href = "static/css/default.css";
  }
  if (mode == "blue") {
    document.getElementById("theme-style").href = "static/css/blue.css";
  }
  if (mode == "green") {
    document.getElementById("theme-style").href = "static/css/green.css";
  }
  if (mode == "purple") {
    document.getElementById("theme-style").href = "static/css/purple.css";
  }
  localStorage.setItem("theme", mode);
}

var mybutton = document.getElementById("topBtn");

window.onscroll = function () {
  scrollFunction();
};


const scrollFunction = () => {
  if (
    document.body.scrollTop > 200 ||
    document.documentElement.scrollTop > 200
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

const ValidateEmail = (inputText) => {
  var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if (inputText.value.match(mailformat)) {
    alert("Valid email address!");
    return true;
  } else {
    alert("Invalid email address!");
    return false;
  }
}

/*
const contactForm = document.querySelector(".contact-us");

let name = document.getElementById("name");
let subject = document.getElementById("subject");
let email = document.getElementById("email");
let message = document.getElementById("message");

contactForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let formData = {
    name: name.value,
    subject: subject.value,
    email: email.value,
    message: message.value,
  };

  let xhr = new XMLHttpRequest();
  xhr.open("POST", "/");
  xhr.setRequestHeader("content-type", "application/json");
  xhr.onload = function () {
    if (xhr.responseText == "Success!") {
      alert("Email sent successfully!");
      names.value = "";
      subject.value = "";
      email.value = "";
      message.value = "";
    } else {
      alert("Something went wrong!");
    }
  };
  xhr.send(JSON.stringify(formData));
});
*/

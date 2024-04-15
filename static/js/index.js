//btn
const shortLinkBtn = document.getElementById('shrt-lnk-btn');
const copyItBtn = document.getElementById('shrt-cpy-btn');


//text
const shortUrlDiv = document.getElementById('cpy-url-div');
const shortUrlText = document.getElementById('shrt-url-text');

shortLinkBtn.addEventListener('click', function() {
    const longUrlInput = document.getElementById('lng-url-text');
    const originalUrl = longUrlInput.value; 
  
    fetch('/api/home/app', {
      method: 'POST',
      body: JSON.stringify({ original_url: originalUrl }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then((response) => {
      console.log(response)
      if (response.status === 200){
        shortUrlDiv.style.display="block";
        shortUrlText.value = response.url_short;
        
        longUrlInput.value = '';
    }else{
      var errorMessage = document.getElementById('error-message');
        errorMessage.classList.add("show-message");
        errorMessage.style.display = "block";
        errorMessage.innerHTML = response.detail;
    }
    })
    .catch((error) => {
        var errorMessage = document.getElementById('error-message');
        errorMessage.classList.add("show-message");
        errorMessage.style.display = "block";
        errorMessage.innerHTML = error.message;
      })
    setTimeout(() => {
      var errorMessage = document.getElementById('error-message');
      errorMessage.style.display = "none";
    }, 1500);  
});


copyItBtn.addEventListener('click', function() {
  const shortUrlText = document.getElementById('shrt-url-text');
  shortUrlText.select();
  document.execCommand("copy");
  copyItBtn.innerText = "copied";
  copyItBtn.classList.add("green-copied");
  setTimeout(() => {
    copyItBtn.innerHTML = '<i class="bx bxs-copy-alt"></i>';
    copyItBtn.classList.remove("green-copied");
  }, 1500); 
});


// faq
const faqHeaders = document.querySelectorAll(".content-container .faq-header");

faqHeaders.forEach((header, i) => {
  header.addEventListener("click", () => {
    header.nextElementSibling.classList.toggle("active");

    const open = header.querySelector(".open");
    const close = header.querySelector(".close");
    if (header.nextElementSibling.classList.contains("active")) {
      open.classList.remove("active");
      close.classList.add("active");
      
    } else {
      open.classList.add("active");
      close.classList.remove("active");

    }
  });
});


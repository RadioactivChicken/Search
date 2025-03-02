function isValidURL(url) {
    return url.startsWith("http://") || url.startsWith("https://");
}

async function searchAPI(event) {
    event.preventDefault();
    const key = document.getElementById("key").value;
    const url = document.getElementById("url").value;

   // Validate the URL
    if (!isValidURL(url)) {
        alert("Invalid URL! Please enter a URL that starts with http:// or https://");
        return;
    }
    
    const encoded = window.btoa(url);

    const response = await fetch(`http://search.twhite.uk/add/${key}/${encoded}`);
    const result = await response.json();

    event.target.reset();
    showNotification("Search Submitted Sucessfully");
}

async function forwardSession(event) {
    event.preventDefault();
    const s_url = document.getElementById("s_url").value;

    const response = await fetch(`http://search.twhite.uk/search/${s_url}`);
    const result = await response.json();

    if (result[1]) {
        window.location.href = window.atob(result[1]);
    } else {
        document.getElementById("forward_result").innerText = "Failed to forward session.";
    }
}

function showNotification(message) {
    const notification = document.getElementById("notification");
    notification.innerText = message;
    notification.classList.add("show");

    // Hide the notification after 3 seconds
    setTimeout(() => {
        notification.classList.remove("show");
    }, 3000);
}

function showForm(formId) {
     const forms = document.querySelectorAll('.form-container');
     forms.forEach(form => {
         form.classList.remove('active');
     });

     document.getElementById(formId).classList.add('active');
 }

 function handleSubmit(event) {
     event.preventDefault();
     alert("Form submitted successfully!");
     event.target.reset();
 }


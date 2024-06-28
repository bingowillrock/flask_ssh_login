// document.addEventListener("DOMContentLoaded", function() {
//     var storedUsername = localStorage.getItem("username");
//     var usernameInput = document.getElementById("username");
//     var usernameButton = document.getElementById("usernameButton");
    
//     if (storedUsername) {
//         usernameInput.value = storedUsername;
//         usernameButton.textContent = "Edit Username";
//     } else {
//         usernameInput.disabled = false;
//         usernameButton.textContent = "Save Username";
//     }
// });

// function editOrSaveUsername() {
//     var usernameInput = document.getElementById("username");
//     var usernameButton = document.getElementById("usernameButton");
    
//     if (usernameInput.disabled) {
//         // Currently in "Edit" mode
//         usernameInput.disabled = false;
//         usernameButton.textContent = "Save Username";
//     } else {
//         // Currently in "Save" mode
//         var username = usernameInput.value;
//         if (username) {
//             localStorage.setItem("username", username);
//             sendUsernameToServer(username);
//             usernameInput.disabled = true;
//             usernameButton.textContent = "Edit Username";
//         } else {
//             alert("Username cannot be empty.");
//         }
//     }
// }

// function sendUsernameToServer(username) {
//     fetch('/set_username', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ username: username })
//     }).then(response => {
//         if (response.ok) {
//             console.log('Username set on server successfully.');
//         } else {
//             console.error('Failed to set username on server.');
//         }
//     }).catch(error => {
//         console.error('Error:', error);
//     });
// }

// -------------------------------------
// try2


document.addEventListener("DOMContentLoaded", function() {
    var storedUsername = localStorage.getItem("username");
    var usernameInput = document.getElementById("username");
    var usernameButton = document.getElementById("usernameButton");
    var usernameDisplay = document.getElementById("usernameDisplay");
    
    if (storedUsername) {
        usernameInput.value = storedUsername;
        usernameButton.textContent = "Edit Username";
        usernameDisplay.textContent = storedUsername;
    } else {
        var username = prompt("Please enter your username:");
        if (username) {
            localStorage.setItem("username", username);
            usernameInput.value = username;
            usernameButton.textContent = "Edit Username";
            usernameDisplay.textContent = username;
        } else {
            alert("Username is required. Please reload the page and enter a username.");
        }
    }
});

function editOrSaveUsername() {
    var usernameInput = document.getElementById("username");
    var usernameButton = document.getElementById("usernameButton");
    var usernameDisplay = document.getElementById("usernameDisplay");
    
    if (usernameInput.disabled) {
        // Currently in "Edit" mode
        usernameInput.disabled = false;
        usernameButton.textContent = "Save Username";
    } else {
        // Currently in "Save" mode
        var username = usernameInput.value;
        if (username) {
            localStorage.setItem("username", username);
            sendUsernameToServer(username);
            usernameInput.disabled = true;
            usernameButton.textContent = "Edit Username";
            usernameDisplay.textContent = username;
        } else {
            alert("Username cannot be empty.");
        }
    }
}

function sendUsernameToServer(username) {
    fetch('/set_username', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username })
    }).then(response => {
        if (response.ok) {
            console.log('Username set on server successfully.');
        } else {
            console.error('Failed to set username on server.');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}

// -------------- try3












// document.addEventListener("DOMContentLoaded", function() {
//     var storedUsername = localStorage.getItem("username");
//     console.log("Stored username on load:", storedUsername);
    
//     if (storedUsername) {
//         document.getElementById("username").value = storedUsername;
//         sendUsernameToServer(storedUsername);
//     } else {
//         var username = prompt("Please enter your username:");
//         console.log("Username entered in prompt:", username);
        
//         if (username) {
//             localStorage.setItem("username", username);
//             document.getElementById("username").value = username;
//             sendUsernameToServer(username);
//         } else {
//             alert("Username is required. Please reload the page and enter a username.");
//         }
//     }
// });

// function saveUsername() {
//     var username = document.getElementById("username").value;
//     console.log("Username to save:", username);
    
//     if (username) {
//         localStorage.setItem("username", username);
//         sendUsernameToServer(username);
//     }
// }

// function sendUsernameToServer(username) {
//     fetch('/set_username', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ username: username })
//     }).then(response => {
//         if (response.ok) {
//             console.log('Username set on server successfully.');
//         } else {
//             console.error('Failed to set username on server.');
//         }
//     }).catch(error => {
//         console.error('Error:', error);
//     });
// }

function openPuTTY(username, ip, port) {
    var username = localStorage.getItem("username");
    console.log("Username for PuTTY:", username);
    
    if (!username) {
        alert("Please enter and save a username first.");
        return;
    }
    
     // Construct the SSH URI with proper encoding
     var uri = "ssh://" + username + ":" + port + "@" + ip
     console.log("SSH URI:", uri);
 
     // Log the attempt
     logAttempt(username, ip, port, "success");
 
     // Attempt to open PuTTY using the SSH URI
     window.location.href = uri;
}


// function openPuTTY(username, ip, port) {
//     // Construct the SSH URI with proper encoding
//     var uri = "ssh://" + username + ":" + port + "@" + ip
//     console.log("SSH URI:", uri);

//     // Log the attempt
//     logAttempt(username, ip, port, "success");

//     // Attempt to open PuTTY using the SSH URI
//     window.location.href = uri;

    
// }

function logAttempt(username, ip, port, status) {
    var form = document.getElementById('logForm');
    form.username.value = username;
    form.putty_ip.value = ip;
    form.port.value = port;
    form.status.value = status;
    form.submit();
}
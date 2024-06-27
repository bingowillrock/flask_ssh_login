document.addEventListener('DOMContentLoaded', function() {
    var usernameDisplay = document.getElementById('username-display');
    var usernameField = document.getElementById('username-field');

    // Retrieve username from local storage
    var storedUsername = localStorage.getItem('username');

    // Function to prompt user for username if not stored or display stored username
    function displayUsername() {
        if (storedUsername) {
            usernameDisplay.textContent = 'Logged in as: ' + storedUsername;
            usernameField.value = storedUsername;  // Set value for hidden input fields
        } else {
            var username = prompt("Please enter your username:");
            if (username) {
                localStorage.setItem('username', username);
                usernameDisplay.textContent = 'Logged in as: ' + username;
                usernameField.value = username;  // Set value for hidden input fields
            } else {
                usernameDisplay.textContent = 'Not logged in';
            }
        }
    }

    // Call the function to display username on page load
    displayUsername();

    // Event listener to handle editing username
    usernameDisplay.addEventListener('click', function() {
        var newUsername = prompt("Enter new username:", storedUsername);
        if (newUsername && newUsername !== storedUsername) {
            localStorage.setItem('username', newUsername);
            usernameDisplay.textContent = 'Logged in as: ' + newUsername;
            usernameField.value = newUsername;  // Update value for hidden input fields
        }
    });
});













// document.addEventListener('DOMContentLoaded', function() {
//     var username = localStorage.getItem('username');
//     var usernameDisplay = document.getElementById('username-display');

//     if (!username) {
//         username = prompt("Please enter your username:");
//         if (username) {
//             localStorage.setItem('username', username);
//         }
//     }

//     if (username) {
//         usernameDisplay.textContent = 'Logged in as: ' + username;
//     } else {
//         usernameDisplay.textContent = 'Not logged in';
//     }
// });

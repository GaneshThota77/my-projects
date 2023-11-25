// // JavaScript code to handle user interactions and messages
// document.addEventListener("DOMContentLoaded", function () {
//     const chatMessages = document.getElementById("chat-messages");
//     const userInput = document.getElementById("user-input");
//     const sendButton = document.getElementById("send-button");

//     sendButton.addEventListener("click", function () {
//         const userMessage = userInput.value;

//         // Display user message in the chat
//         appendMessage("You", userMessage);

//         // Send user message to your HR assistant API and handle the response
//         // You can use the fetch API or another method to send the message to your server

//         // For this example, we'll simulate a response from the HR assistant
//         setTimeout(function () {
//             const assistantResponse = "This is a response from the HR assistant.";
//             appendMessage("HR Assistant", assistantResponse);
//         }, 1000);

//         // Clear the user input field
//         userInput.value = "";
//     });

//     function appendMessage(sender, message) {
//         const messageDiv = document.createElement("div");
//         messageDiv.classList.add("message");
//         messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
//         chatMessages.appendChild(messageDiv);

//         // Scroll to the bottom of the chat container
//         chatMessages.scrollTop = chatMessages.scrollHeight;
//     }
// });

document.addEventListener("DOMContentLoaded", function () {
    const chatMessages = document.getElementById("chat-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", function () {
        const userMessage = userInput.value;

        // Display user message in the chat
        appendMessage("You", userMessage);

        // Send user message to your HR assistant API and handle the response
        fetch('http://127.0.0.1:5000/handle_message', { // Replace with the actual API endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const assistantResponse = data.message;
            appendMessage("GPT-3", assistantResponse);
            console.log("responce Message",data.message)
        })
        .catch(error => {
            console.error('Error:', error);
        });

        // Clear the user input field
        userInput.value = "";

        
    });

    function appendMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message");
        messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatMessages.appendChild(messageDiv);

        // Scroll to the bottom of the chat container
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});



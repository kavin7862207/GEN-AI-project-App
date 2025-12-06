const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const mediaDisplay = document.getElementById('media-display');
const genImageBtn = document.getElementById('gen-image-btn');
const genVideoBtn = document.getElementById('gen-video-btn');

let messageHistory = [];

// Helper to add message to UI
function addMessage(role, text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role}`;
    msgDiv.innerHTML = `<p>${text}</p>`;
    chatHistory.appendChild(msgDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

// Send Chat Message
async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    addMessage('user', text);
    userInput.value = '';

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text, history: messageHistory })
        });
        const data = await response.json();

        addMessage('assistant', data.response);
        messageHistory.push({ role: 'user', content: text });
        messageHistory.push({ role: 'assistant', content: data.response });

    } catch (error) {
        addMessage('system', 'Error communicating with server.');
        console.error(error);
    }
}

// Generate Image
async function generateImage() {
    // Use the last user message or a generic prompt
    const lastMsg = messageHistory.length > 0 ? messageHistory[messageHistory.length - 1].content : "A futuristic scene";
    const prompt = `Visual representation of: ${lastMsg}`;

    mediaDisplay.innerHTML = '<div class="placeholder"><p>Generating Image...</p></div>';

    try {
        const response = await fetch('/api/image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });
        const data = await response.json();

        mediaDisplay.innerHTML = `<img src="${data.url}" alt="Generated Image">`;

    } catch (error) {
        mediaDisplay.innerHTML = '<div class="placeholder"><p>Error generating image.</p></div>';
    }
}

// Generate Video
async function generateVideo() {
    const lastMsg = messageHistory.length > 0 ? messageHistory[messageHistory.length - 1].content : "A futuristic scene";
    const prompt = `Video of action: ${lastMsg}`;

    mediaDisplay.innerHTML = '<div class="placeholder"><p>Generating Video...</p></div>';

    try {
        const response = await fetch('/api/video', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });
        const data = await response.json();

        // Check if it's a mock URL or real one
        if (data.url.includes("mp4") || data.url.includes("video")) {
            mediaDisplay.innerHTML = `<video controls autoplay loop src="${data.url}"></video>`;
        } else {
            // Fallback for mock text response
            mediaDisplay.innerHTML = `<div class="placeholder"><p>${data.url}</p></div>`;
        }

    } catch (error) {
        mediaDisplay.innerHTML = '<div class="placeholder"><p>Error generating video.</p></div>';
    }
}

// Event Listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

genImageBtn.addEventListener('click', generateImage);
genVideoBtn.addEventListener('click', generateVideo);

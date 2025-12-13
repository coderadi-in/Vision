// ? CREATING SOCKET INSTANCE
var socket = io();

// ? GETTING DOCUMENT ELEMENTS
handle = document.querySelector('#handle');
handleStatus = document.querySelector('#handle-status');
handleInput = document.querySelector("#handle-input");
handleMessage = document.querySelector("#handle-status-message");
submitBtn = document.querySelector('.btn');

// & EVENT LISTENER FOR HANDLE FIELD INPUT
handle.addEventListener('input', () => {
    if (handle.value.trim() != "") {        
        handleStatus.innerHTML = "progress_activity";
        handleStatus.classList.add('load');
        socket.emit('handle-validation', handle.value);
        
    } else {
        handleStatus.classList.remove('load');
        handleInput.style.borderColor = "var(--border)";
        handleMessage.innerHTML = "";
        handleStatus.innerHTML = "";
    }
})

// | SOCKET LISTENER FOR HANDLE VALIDATION
socket.on('handle-validation', (data) => {
    handleStatus.classList.remove('load');
    handleMessage.innerHTML = data.message;

    if (data.status == 200) {
        handleStatus.innerHTML = "check_circle";
        handleStatus.style.color = "#059669";
        handleInput.style.borderColor = "#059669";
        handleMessage.style.color = "#059669";
        submitBtn.disabled = false;
        
    } else {
        handleStatus.innerHTML = "error";
        handleStatus.style.color = "#FF3D3D";
        handleInput.style.borderColor = "#FF3D3D";
        handleMessage.style.color = "#FF3D3D";
        submitBtn.disabled = true;
    }
})
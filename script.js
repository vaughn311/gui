document.getElementById('addTaskBtn').addEventListener('click', function() {
    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();
    
    if (taskText !== "") {
        const taskList = document.getElementById('taskList');
        const li = document.createElement('li');
        li.innerHTML = `
            ${taskText} 
            <button onclick="removeTask(this)">X</button>
        `;
        taskList.appendChild(li);
        taskInput.value = ""; // Clear input field
    }
});

function removeTask(button) {
    const taskItem = button.parentElement;
    taskItem.remove();
}

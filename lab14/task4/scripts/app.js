const container = document.getElementById('list-container');

// Show loading skeleton
container.innerHTML = `<div class="skeleton">Loading users...</div>`;

fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    })
    .then(users => {
        // Remove loading
        container.innerHTML = '';
        const ul = document.createElement('ul');
        ul.className = 'user-list';
        users.forEach(user => {
            const li = document.createElement('li');
            li.className = 'user-list__item';
            // Safely set text content
            li.textContent = `${user.name} (${user.email})`;
            ul.appendChild(li);
        });
        container.appendChild(ul);
    })
    .catch(error => {
        container.innerHTML = `<div class="error">Failed to load users. Please try again later.</div>`;
    });
document.addEventListener('DOMContentLoaded', function() {
    const proteinInput = document.getElementById('protein-input');
    const preferenceSelect = document.getElementById('preference-select');
    const submitButton = document.getElementById('submit-button');
    const mealOptions = document.getElementById('meal-options');

    submitButton.addEventListener('click', function() {
        const proteinGoal = proteinInput.value;
        const preference = preferenceSelect.value;

        if (!proteinGoal || !preference) {
            alert('Please fill in all fields.');
            return;
        }

        fetch(`/get_meals?protein=${proteinGoal}&preference=${preference}`)
            .then(response => response.json())
            .then(data => {
                mealOptions.innerHTML = '';
                data.meals.forEach(meal => {
                    const mealItem = document.createElement('li');
                    mealItem.textContent = meal;
                    mealOptions.appendChild(mealItem);
                });
            })
            .catch(error => console.error('Error fetching meals:', error));
    });
});
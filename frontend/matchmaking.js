// app.js

const form = document.querySelector('form');
const tableBody = document.querySelector('tbody');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  
  // get the player's score from the form
  const scoreInput = document.querySelector('input[type="text"]');
  const score = parseInt(scoreInput.value);
  
  // generate some sample data for the matchmaking results
  const data = [
    { name: 'Player 1', score: 900, matches: 16 },
    { name: 'Player 2', score: 850, matches: 14 },
    { name: 'Player 3', score: 800, matches: 12 },
    { name: 'Player 4', score: 750, matches: 10 },
    { name: 'Player 5', score: 700, matches: 8 },
  ];
  
  // filter the data to only include players with similar scores
  const filteredData = data.filter((player) => {
    return Math.abs(player.score - score) <= 50;
  });
  
  // populate the table with the filtered data
  tableBody.innerHTML = '';
  filteredData.forEach((player) => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${player.name}</td>
      <td>${player.score}</td>
      <td>${player.matches}</td>
    `;
    tableBody.appendChild(row);
  });
  
  // clear the form input
  scoreInput.value = '';
});

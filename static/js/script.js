let currentEntry = null;

function generateEntry() {
    fetch('/generate')
        .then(response => response.json())
        .then(data => {
            currentEntry = data
            const letter = data.word.charAt(0); // Extract the first character of the word
            document.getElementById('letter').textContent = letter;
            document.getElementById('word').textContent = '';
            document.getElementById('desc').textContent = '';
        });
}
function showWordMeaning() {
    const letter = document.getElementById('letter').textContent;
    if (letter === '') {
        fetch('/generate')
            .then(response => response.json())
            .then(data => {
                const letter = data.word.charAt(0); // Extract the first character of the word
                document.getElementById('letter').textContent = letter;
                document.getElementById('word').textContent = data.word;
                document.getElementById('desc').textContent = data.desc;
            });
            return;
    } else {
        document.getElementById('word').textContent = currentEntry.word;
        document.getElementById('desc').textContent = currentEntry.desc;
    }
}
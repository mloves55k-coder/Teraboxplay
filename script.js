document.getElementById('playBtn').addEventListener('click', async function() {
    const inputUrl = document.getElementById('teralink').value.trim();
    const loading = document.getElementById('loading');
    const playerCard = document.getElementById('player-card');
    const video = document.getElementById('mainPlayer');
    const title = document.getElementById('videoTitle');
    const dlBtn = document.getElementById('downloadBtn');

    if (!inputUrl) return alert("Please paste a link!");

    loading.style.display = "block";
    playerCard.style.display = "none";

    try {
        // Replace with your Vercel URL after deployment
        const response = await fetch(`/api/extract?url=${encodeURIComponent(inputUrl)}`);
        const data = await response.json();

        if (data.list && data.list.length > 0) {
            const file = data.list[0];
            video.src = file.main_url;
            title.innerText = file.filename;
            dlBtn.href = file.main_url;
            
            loading.style.display = "none";
            playerCard.style.display = "block";
            video.play();
        } else {
            alert("API limit full or link invalid.");
            loading.style.display = "none";
        }
    } catch (e) {
        loading.style.display = "none";
        alert("Server Error! Try again.");
    }
});

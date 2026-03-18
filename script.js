document.getElementById('playBtn').addEventListener('click', async function() {
    const inputUrl = document.getElementById('teralink').value.trim();
    const loading = document.getElementById('loading');
    const playerCard = document.getElementById('player-card');
    const video = document.getElementById('mainPlayer');
    const title = document.getElementById('videoTitle');
    const dlBtn = document.getElementById('downloadBtn');

    // 1. Basic Validation
    if (!inputUrl) {
        alert("Please paste a TeraBox link first!");
        return;
    }

    // 2. UI Reset (Loading dikhana)
    loading.style.display = "block";
    playerCard.style.display = "none";
    video.src = ""; // Purani video clear karna

    try {
        /* 3. API Call: 
           Ye aapke Vercel backend (/api/extract) ko request bhejega 
           jo humne vercel.json mein set kiya hai.
        */
        const apiUrl = `/api/extract?url=${encodeURIComponent(inputUrl)}`;
        const response = await fetch(apiUrl);
        
        if (!response.ok) {
            throw new Error("Server response was not OK");
        }

        const data = await response.json();

        // 4. Data Check (Check if video link exists)
        if (data && data.list && data.list.length > 0) {
            const fileData = data.list[0];
            const directVideoUrl = fileData.main_url;

            // Video aur Download button set karna
            video.src = directVideoUrl;
            title.innerText = fileData.filename || "TeraBox Video";
            dlBtn.href = directVideoUrl;

            // UI Update (Player dikhana)
            loading.style.display = "none";
            playerCard.style.display = "block";
            
            // Auto-play attempt
            video.play().catch(e => console.log("Auto-play blocked by browser. Click play manually."));
        } 
        else {
            loading.style.display = "none";
            alert("Video nahi mil saki! Shayad link expire ho gaya hai ya private hai.");
        }

    } catch (error) {
        console.error("Error fetching data:", error);
        loading.style.display = "none";
        alert("Server Error: Backend se rabta nahi ho pa raha. Vercel dashboard check karein.");
    }
});

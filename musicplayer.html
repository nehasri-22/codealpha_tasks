<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Music Player</title>

<style>
body {
    font-family: Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: #121212;
    color: white;
}

.player {
    width: 300px;
    background: #1e1e1e;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

h2, p {
    margin: 5px;
}

.controls button {
    margin: 10px;
    padding: 10px;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    font-size: 16px;
}

.play { background: green; color: white; }
.next, .prev { background: #444; color: white; }

.progress-container {
    width: 100%;
    height: 5px;
    background: #555;
    margin: 10px 0;
    cursor: pointer;
}

.progress {
    height: 5px;
    background: #1db954;
    width: 0%;
}

.volume {
    width: 100%;
}

.playlist {
    margin-top: 10px;
    text-align: left;
    max-height: 100px;
    overflow-y: auto;
}

.playlist div {
    padding: 5px;
    cursor: pointer;
}

.playlist div:hover {
    background: #333;
}

.active {
    background: #1db954;
}
</style>
</head>

<body>

<div class="player">
    <h2 id="title">Song Title</h2>
    <p id="artist">Artist</p>

    <audio id="audio"></audio>

    <div class="progress-container" onclick="setProgress(event)">
        <div class="progress" id="progress"></div>
    </div>

    <div>
        <span id="currentTime">0:00</span> / 
        <span id="duration">0:00</span>
    </div>

    <div class="controls">
        <button class="prev" onclick="prevSong()">⏮</button>
        <button class="play" onclick="togglePlay()">▶</button>
        <button class="next" onclick="nextSong()">⏭</button>
    </div>

    <input type="range" class="volume" min="0" max="1" step="0.1" onchange="setVolume(this.value)">

    <div class="playlist" id="playlist"></div>
</div>

<script>
const songs = [
    {
        title: "SoundHelix Song 1",
        artist: "Artist 1",
        src: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    {
        title: "SoundHelix Song 2",
        artist: "Artist 2",
        src: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    },
    {
        title: "SoundHelix Song 3",
        artist: "Artist 3",
        src: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    }
];

let index = 0;
const audio = document.getElementById("audio");
const title = document.getElementById("title");
const artist = document.getElementById("artist");
const progress = document.getElementById("progress");
const currentTimeEl = document.getElementById("currentTime");
const durationEl = document.getElementById("duration");
const playlistEl = document.getElementById("playlist");

// Load song
function loadSong(i) {
    const song = songs[i];
    title.textContent = song.title;
    artist.textContent = song.artist;
    audio.src = song.src;
    highlightPlaylist();
}

// Play/Pause
function togglePlay() {
    if (audio.paused) {
        audio.play();
    } else {
        audio.pause();
    }
}

// Next song
function nextSong() {
    index = (index + 1) % songs.length;
    loadSong(index);
    audio.play();
}

// Previous song
function prevSong() {
    index = (index - 1 + songs.length) % songs.length;
    loadSong(index);
    audio.play();
}

// Update progress
audio.addEventListener("timeupdate", () => {
    const percent = (audio.currentTime / audio.duration) * 100;
    progress.style.width = percent + "%";

    currentTimeEl.textContent = formatTime(audio.currentTime);
    durationEl.textContent = formatTime(audio.duration);
});

// Set progress
function setProgress(e) {
    const width = e.currentTarget.clientWidth;
    const clickX = e.offsetX;
    audio.currentTime = (clickX / width) * audio.duration;
}

// Volume
function setVolume(value) {
    audio.volume = value;
}

// Format time
function formatTime(time) {
    if (isNaN(time)) return "0:00";
    const min = Math.floor(time / 60);
    const sec = Math.floor(time % 60).toString().padStart(2, '0');
    return `${min}:${sec}`;
}

// Playlist UI
function loadPlaylist() {
    songs.forEach((song, i) => {
        const div = document.createElement("div");
        div.textContent = song.title;
        div.onclick = () => {
            index = i;
            loadSong(index);
            audio.play();
        };
        playlistEl.appendChild(div);
    });
}

// Highlight active song
function highlightPlaylist() {
    const items = playlistEl.children;
    for (let i = 0; i < items.length; i++) {
        items[i].classList.toggle("active", i === index);
    }
}

// Autoplay next
audio.addEventListener("ended", nextSong);

// Initialize
loadSong(index);
loadPlaylist();
</script>

</body>
</html>

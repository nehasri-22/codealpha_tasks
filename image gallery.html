<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Image Gallery</title>

<style>
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0;
}

h1 {
    margin: 20px;
}

/* Filter buttons */
.filters button {
    padding: 10px;
    margin: 5px;
    border: none;
    background: #333;
    color: white;
    cursor: pointer;
    transition: 0.3s;
}

.filters button:hover {
    background: #555;
}

/* Gallery */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 10px;
    padding: 20px;
}

.image {
    width: 100%;
    cursor: pointer;
    transition: transform 0.3s, filter 0.3s;
}

.image:hover {
    transform: scale(1.05);
    filter: brightness(80%);
}

/* Lightbox */
.lightbox {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.9);
    align-items: center;
    justify-content: center;
}

.lightbox img {
    max-width: 80%;
    max-height: 80%;
}

/* Buttons */
.prev, .next {
    position: absolute;
    top: 50%;
    font-size: 30px;
    color: white;
    background: transparent;
    border: none;
    cursor: pointer;
}

.prev { left: 20px; }
.next { right: 20px; }

.close {
    position: absolute;
    top: 20px;
    right: 30px;
    font-size: 35px;
    color: white;
    cursor: pointer;
}

/* Responsive */
@media(max-width: 600px) {
    .lightbox img {
        max-width: 95%;
    }
}
</style>
</head>

<body>

<h1>Image Gallery</h1>

<!-- Filters -->
<div class="filters">
    <button onclick="filterImages('all')">All</button>
    <button onclick="filterImages('nature')">Nature</button>
    <button onclick="filterImages('city')">City</button>
</div>

<!-- Gallery -->
<div class="gallery">
    <img src="https://picsum.photos/id/1015/400/300" class="image nature">
    <img src="https://picsum.photos/id/1011/400/300" class="image nature">
    <img src="https://picsum.photos/id/1016/400/300" class="image city">
    <img src="https://picsum.photos/id/1020/400/300" class="image city">
</div>

<!-- Lightbox -->
<div class="lightbox" id="lightbox">
    <span class="close">&times;</span>
    <button class="prev">&#10094;</button>
    <img id="lightbox-img">
    <button class="next">&#10095;</button>
</div>

<script>
const images = document.querySelectorAll(".image");
const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const closeBtn = document.querySelector(".close");
const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");

let currentIndex = 0;

// Open lightbox
images.forEach((img, index) => {
    img.addEventListener("click", () => {
        lightbox.style.display = "flex";
        lightboxImg.src = img.src;
        currentIndex = index;
    });
});

// Close
closeBtn.onclick = () => lightbox.style.display = "none";

// Next
nextBtn.onclick = () => {
    currentIndex = (currentIndex + 1) % images.length;
    lightboxImg.src = images[currentIndex].src;
};

// Prev
prevBtn.onclick = () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    lightboxImg.src = images[currentIndex].src;
};

// Filter
function filterImages(category) {
    images.forEach(img => {
        if (category === "all" || img.classList.contains(category)) {
            img.style.display = "block";
        } else {
            img.style.display = "none";
        }
    });
}
</script>

</body>
</html>

const slides = document.querySelector('.slides');
const slideWidth = document.querySelector('.slide').offsetWidth;

let currentSlideIndex = 1;

function showSlides(index) {
    slides.style.transform = `translateX(${-slideWidth * (index - 1)}px)`;
}

function currentSlide(index) {
    currentSlideIndex = index;
    showSlides(currentSlideIndex);
}

function enlargeImage(imageURL) {
    document.getElementById('enlargedImg').src = imageURL;
    document.querySelector('.enlarged-modal').classList.add('active');
}

function closeEnlarged() {
    document.querySelector('.enlarged-modal').classList.remove('active');
}

// Automatic slideshow
setInterval(() => {
    if (currentSlideIndex === 5) {
        currentSlideIndex = 1;
    } else {
        currentSlideIndex++;
    }
    showSlides(currentSlideIndex);
}, 5000); // Change slide every 5 seconds
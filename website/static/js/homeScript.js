let currentPosition = 1; // Initial position
const totalItems = document.querySelectorAll('#carousel .item').length;
const interval = 5000; // Change slide every 5 seconds
const transitionDuration = 2; // Duration of transition between slides in seconds

function updateCarousel() {
    const currentItem = document.querySelector(`#carousel .item:nth-of-type(${currentPosition})`);
    currentItem.style.transition = `transform ${transitionDuration}s ease-in-out`;
    currentItem.style.transform = `rotateY(calc(-10deg * 0)) translateX(calc(-300px * 0))`; // Reset the current slide

    currentPosition = (currentPosition % totalItems) + 1; // Move to the next slide
    const nextItem = document.querySelector(`#carousel .item:nth-of-type(${currentPosition})`);
    nextItem.style.transition = `transform ${transitionDuration}s ease-in-out`;
    nextItem.style.transform = `rotateY(calc(-10deg * 1)) translateX(calc(-300px * 1))`; // Apply transformation to the next slide

    setTimeout(updateCarousel, transitionDuration * 1000); // Schedule the next update
}

updateCarousel(); // Start the slideshow



  // Top Image Slider
function preloadImages() {
    const images = [
        "static/Images/homeSlides/IMG26.jpg",
        "static/Images/homeSlides/IMG27.jpg",
        "static/Images/homeSlides/IMG28.jpg",
        "static/Images/homeSlides/IMG29.jpg",
        "static/Images/homeSlides/IMG30.jpg"
    ];

    images.forEach(src => {
        const img = new Image();
        img.src = src;
    });
}

// Call preload function when the page loads


const track = document.getElementById("image-track");

const handleOnDown = e => track.dataset.mouseDownAt = e.clientX;

const handleOnUp = () => {
track.dataset.mouseDownAt = "0";  
track.dataset.prevPercentage = track.dataset.percentage;
};

const handleOnMove = e => {
if (track.dataset.mouseDownAt === "0") return;

const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
      maxDelta = window.innerWidth / 2;

const percentage = (mouseDelta / maxDelta) * -100,
      nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
      nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);

track.dataset.percentage = nextPercentage;

track.animate({
  transform: `translate(${nextPercentage}%, -50%)`
}, { duration: 1200, fill: "forwards" });

for (const image of track.getElementsByClassName("images")) {
  image.animate({
    objectPosition: `${100 + nextPercentage}% center`
  }, { duration: 1200, fill: "forwards" });
}
};


/* --  extra lines for touch events -- */

window.onmousedown = e => handleOnDown(e);

window.ontouchstart = e => handleOnDown(e.touches[0]);

window.onmouseup = e => handleOnUp(e);

window.ontouchend = e => handleOnUp(e.touches[0]);

window.onmousemove = e => handleOnMove(e);

window.ontouchmove = e => handleOnMove(e.touches[0]);
















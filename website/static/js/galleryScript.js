var currentImageIndex = 0;
var images = document.querySelectorAll(".grid-item .image");
var totalImages = images.length;

function openModal(url, alt) {
    var modal = document.getElementById("myModal");
    var modalImg = document.getElementById("modalImg");
    modal.style.display = "block";
    modalImg.src = url;
    modalImg.alt = alt;
    currentImageIndex = Array.from(images).findIndex(function(image) {
        return image.src === url;
    });
}

function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + totalImages) % totalImages;
    openModal(images[currentImageIndex].src, images[currentImageIndex].alt);
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % totalImages;
    openModal(images[currentImageIndex].src, images[currentImageIndex].alt);
}

function rotateLeft() {
    var modalImg = document.getElementById("modalImg");
    var currentRotation = parseInt(modalImg.style.transform.replace("rotate(", "").replace("deg)", ""));
    currentRotation = isNaN(currentRotation) ? 0 : currentRotation;
    modalImg.style.transform = "rotate(" + (currentRotation - 90) + "deg)";
}

function rotateRight() {
    var modalImg = document.getElementById("modalImg");
    var currentRotation = parseInt(modalImg.style.transform.replace("rotate(", "").replace("deg)", ""));
    currentRotation = isNaN(currentRotation) ? 0 : currentRotation;
    modalImg.style.transform = "rotate(" + (currentRotation + 90) + "deg)";
}

// Close the modal when clicking outside the modal content
window.onclick = function(event) {
    var modal = document.getElementById("myModal");
    if (event.target == modal) {
        closeModal();
    }
};

//SLIDER//
var TrandingSlider = new Swiper('.tranding-slider', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 'auto',
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2.5,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });
let slideIndex = 0;
    showSlides();

    function prevSlide() {
        showSlides(slideIndex -= 1);
        document.querySelector('.prev').classList.add('clicked');
        setTimeout(() => document.querySelector('.prev').classList.remove('clicked'), 300); // Reset after 300ms
    }
    
    function nextSlide() {
        showSlides(slideIndex += 1);
        document.querySelector('.next').classList.add('clicked');
        setTimeout(() => document.querySelector('.next').classList.remove('clicked'), 300); // Reset after 300ms
    }
    


    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides() {
        const slides = document.querySelectorAll('.slide');
        const dots = document.querySelector('.dot-container');
        slides.forEach(slide => slide.style.display = 'none');
        dots.innerHTML = '';
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = 'none';
            const dot = document.createElement('span');
            dot.className = 'dot';
            dot.addEventListener('click', () => currentSlide(i));
            dots.appendChild(dot);
        }
        if (slideIndex >= slides.length) { slideIndex = 0; }
        if (slideIndex < 0) { slideIndex = slides.length - 1; }
        slides[slideIndex].style.display = 'block';
        dots.childNodes[slideIndex].classList.add('active');
        slideIndex++;
        setTimeout(showSlides, 5000); // Change slide every 3 seconds (3000 milliseconds)
    }




















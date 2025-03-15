const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

import PhotoSwipeLightbox from "../js/PhotoSwipe-5.4.4/photoswipe-lightbox.esm.js";

const lightbox = new PhotoSwipeLightbox({
    gallery: ".gallery--responsive-images",
    children: "a",
    pswpModule: () => import("../js/PhotoSwipe-5.4.4/photoswipe.esm.min.js"),
    bgOpacity: 0.2,
    spacing: 0.5,
    allowPanToNext: true
})

lightbox.init()
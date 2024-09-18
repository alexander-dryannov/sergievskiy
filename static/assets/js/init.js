const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

import PhotoSwipeLightbox from "../js/PhotoSwipe-5.4.4/photoswipe-lightbox.esm.js";

const options = {
    gallery: ".gallery--responsive-images",
    children: "a",
    pswpModule: () => import("../js/PhotoSwipe-5.4.4/photoswipe.esm.min.js")
}
const lightbox = new PhotoSwipeLightbox(options)
lightbox.init()
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

import PhotoSwipeLightbox from "../js/PhotoSwipe-5.4.4/photoswipe-lightbox.esm.js";

const options = {
    gallery: ".gallery--responsive-images",
    children: "a",
    pswpModule: () => import("../js/PhotoSwipe-5.4.4/photoswipe.esm.min.js")
}
const lightbox = new PhotoSwipeLightbox(options)
lightbox.on('uiRegister', function () {
    lightbox.pswp.ui.registerElement({
        name: 'detail',
        ariaLabel: 'detail',
        order: 9,
        isButton: true,
        html: '<i class="fa-solid fa-circle-info"></i>',
        onClick: (event, el, pswp) => {
            let slug = pswp.currSlide.data.element.dataset.imageSlug
            let album_slug = location.pathname.split('/')[3]
            location.replace(`${location.origin}/gallery/album/${album_slug}/${slug}/`)
        }
    })
})
lightbox.init()
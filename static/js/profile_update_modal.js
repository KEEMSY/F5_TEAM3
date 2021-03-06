var modal = document.getElementById("modal");

function modalOn() {
    modal.style.display = "flex";
}

function isModalOn() {
    return modal.style.display === "flex";
}

function modalOff() {
    modal.style.display = "none";
}

const btnModal = document.getElementById("btn-modal")
btnModal.addEventListener("click", e => {
    modalOn();
})

const imgModal = document.getElementById("img-modal")
imgModal.addEventListener("click", e => {
    modalOn();
})

const closeBtn = document.getElementById("close-area")
closeBtn.addEventListener("click", e => {
    modalOff();
})
modal.addEventListener("click", e => {
    const evTarget = e.target
    if (evTarget.classList.contains("modal-overlay")) {
        modalOff();
    }
})
window.addEventListener("keyup", e => {
    if (isModalOn() && e.key === "Escape") {
        modalOff();
    }
})


$.ajaxSetup({
    headers: {"X-CSRFToken": '{{csrf_token}}'}
});



btn = document.getElementById('copyUrl')

btn.addEventListener('click', (e) => {
    navigator.clipboard.writeText(e.target.value)
    window.location.href="/thankyou";
})
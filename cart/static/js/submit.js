const createCartSubmit = (submitUrl, token) => {
    const btn = document.createElement('button');
    btn.setAttribute('id', 'cart-submit-button');
    btn.innerHTML = 'Submit';

    btn.addEventListener(
        'click',
        evt => {
            fetch(
                submitUrl,
                {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': token,
                    },
                    body: localStorage.getItem('products')
                },
            )
                .then(request => request.json())
                .then(data => location.replace(data.success_url))
        }
    )

    return btn;
}

const createEmptyMock = (url, text) => {
    const emptyLink = document.createElement('a');
    emptyLink.classList.add('empty-cart__link');
    emptyLink.setAttribute('href', url);
    emptyLink.innerHTML = text;

    return emptyLink;
}

const Product = ({title}) => (
    '<li class="menu__item">
        <h2>
            ${title}
        </h2>
    </li>'
);

const renderProductData = res => {
    menuHtml = res.data.results.map(Product)
        .join('')
    menu = document.getElementById('products')
    meny.innerHTML += menuHtml
}
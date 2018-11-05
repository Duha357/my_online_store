const Category = ({title}) => (
    '<li class="menu__item">
        <h2>
            ${title}
        </h2>
    </li>'
);

const renderCategoryData = res => {
    menuHtml = res.data.results.map(Category)
        .join('')
    menu = document.getElementById('categories')
    meny.innerHTML += menuHtml
}
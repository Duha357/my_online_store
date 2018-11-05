const Category = ({title}) => (
    '<li class="menu__item">
        <h2>
            ${title}
        </h2>
    </li>'
)

const renderData = res => {
    menuHtml = res.data.results.map(Category)
        .join('')
    menu = document.getElementById('menu')
    meny.innerHTML += menuHtml
}
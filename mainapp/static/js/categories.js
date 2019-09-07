var Category = ({title}) => (
    '<li class="menu__item">\
        <h2>\
            ${title}\
        </h2>\
    </li>'
);

var renderCategoryData = res => {
    menuHtml = res.data.results.map(Category)
        .join('')
    menu = document.getElementById('categories')
    menu.innerHTML += menuHtml
}
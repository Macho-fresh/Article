const drop     = document.querySelector(".drop");
const cat = document.querySelector(".cat")
const dropdown = document.querySelector(".click");

// Toggle when arrow/button is clicked
dropdown.addEventListener("click", (e) => {
  e.stopPropagation(); // don’t bubble to document

  if (drop.classList.contains("show")) {
    // If it's open, play hide animation
    drop.classList.remove("show");
    drop.classList.add("hide");
  } else {
    // If it's closed, play show animation
    drop.classList.remove("hide");
    drop.classList.add("show");
  }
});

cat.addEventListener("click", (e) => {
  e.stopPropagation(); // don’t bubble to document

  if (drop.classList.contains("show")) {
    // If it's open, play hide animation
    drop.classList.remove("show");
    drop.classList.add("hide");
  } else {
    // If it's closed, play show animation
    drop.classList.remove("hide");
    drop.classList.add("show");
  }
});
// Close when clicking anywhere else
document.addEventListener("click", (e) => {
  if (!drop.contains(e.target) && !dropdown.contains(e.target)) {
    if (drop.classList.contains("show")) {
      drop.classList.remove("show");
      drop.classList.add("hide");
    }
  }
});

let increase = 0;
const bookmarks = document.querySelectorAll(".bookmark2");
const bookadd = document.querySelector(".bookadd");


bookmarks.forEach(button => {
  button.addEventListener("click", () => {
    // check current state
    const isBookmarked = button.classList.toggle("active");

    if (isBookmarked) {
      button.src = "/static/imgs/bookmark-svgrepo-com (1).svg";  // change to filled
      // increase++;
    } else {
      button.src = "/static/imgs/bookmark-svgrepo-com.svg";  // back to empty
      // increase--;
    }

    // update the counter
    // bookadd.textContent = increase;
  });
});

// dark mode & light mode
const sun = document.querySelector('.sun')
const nav = document.querySelector('.nav-section')
const vert = document.querySelector('.vertical-bar')
const light = document.querySelector('.light-mode')
const p = document.querySelectorAll('p')
const daily = document.querySelector('.trending')
const weekly = document.querySelector('.weekly-roundup')
const dailyRight = document.querySelector('.daily-insights')
const rating = document.querySelectorAll('.rating-middle')
const article = document.querySelectorAll('.article-highlight')
const ratings = document.querySelector('.ratings-holder')
const rate = document.querySelector('.ratings')
const views = document.querySelectorAll('.views')
sun.addEventListener('click', ()=> {
  const isClicked = sun.classList.toggle('active');
  if (isClicked) {
    nav.style.backgroundColor = '#1212';
    sun.src = '/static/imgs/moon-svgrepo-com.svg'
    vert.style.backgroundColor = 'white'
    light.style.backgroundColor = 'transparent'
    weekly.style.backgroundColor = 'rgb(48, 45, 45)'
    drop.style.backgroundColor = 'rgb(48, 45, 45)'
    p.forEach(para => {
      para.style.color = 'white'
    });
    daily.style.backgroundColor = 'rgb(48, 45, 45)'
    dailyRight.style.backgroundColor = 'rgb(48, 45, 45)'
    ratings.style.backgroundColor = 'rgb(48, 45, 45)'
    rate.style.backgroundColor = 'rgb(48, 45, 45)'

    rating.forEach(rate => {
      rate.style.backgroundColor = 'rgb(48, 45, 45)'
      rate.style.border = '1px solid white'
    })

    article.forEach(art => {
      art.style.borderRight = '1px solid white'
    })

    views.forEach( view => {
      view.style.borderBottom = '1px solid white'
    })
  } else{
    nav.style.backgroundColor = '';
    sun.src = '/static/imgs/sun-svgrepo-com (3).svg'
    vert.style.backgroundColor = 'rgb(48, 45, 45)'
    light.style.backgroundColor = 'orange'
    p.forEach(para => {
      para.style.color = ''
    });
    daily.style.backgroundColor = ''
    dailyRight.style.backgroundColor = ''
    ratings.style.backgroundColor = ''
    drop.style.backgroundColor = ''
    

    rate.style.backgroundColor = ''
    rating.forEach(rate => {
      rate.style.backgroundColor = ''
      rate.style.border = '1px solid white'
    })
  }
    
})
console.log(p);

const search = document.querySelector('.search-bar')
const searchBtn = document.querySelector('.searchBtn')

searchBtn.addEventListener('click', ()=> {
  search.classList.toggle('on')
 
})
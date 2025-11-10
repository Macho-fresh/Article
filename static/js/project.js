document.addEventListener('DOMContentLoaded',  ()=>{


// const drop     = document.querySelector(".drop");
// const cat = document.querySelector(".cat")
// const dropdown = document.querySelector(".click");

// Toggle when arrow/button is clicked
// dropdown.addEventListener("click", (e) => {
//   e.stopPropagation(); // don’t bubble to document

//   if (drop.classList.contains("show")) {
//     // If it's open, play hide animation
//     drop.classList.remove("show");
//     drop.classList.add("hide");
//   } else {
//     // If it's closed, play show animation
//     drop.classList.remove("hide");
//     drop.classList.add("show");
//   }
// });

// cat.addEventListener("click", (e) => {
//   e.stopPropagation(); // don’t bubble to document

//   if (drop.classList.contains("show")) {
//     // If it's open, play hide animation
//     drop.classList.remove("show");
//     drop.classList.add("hide");
//   } else {
//     // If it's closed, play show animation
//     drop.classList.remove("hide");
//     drop.classList.add("show");
//   }
// });
// Close when clicking anywhere else
// document.addEventListener("click", (e) => {
//   if (!drop.contains(e.target) && !dropdown.contains(e.target)) {
//     if (drop.classList.contains("show")) {
//       drop.classList.remove("show");
//       drop.classList.add("hide");
//     }
//   }
// });

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

// Saving the dark theme
// Save the theme
localStorage.setItem('theme', 'dark');

// Get the theme
// Get stored theme or default to light
let theme = localStorage.getItem('theme') || 'light';

// Select your elements
const sun = document.querySelector('.sun');
const nav = document.querySelector('.nav-section');
const vert = document.querySelector('.vertical-bar');
const light = document.querySelector('.light-mode');
const p = document.querySelectorAll('p');
const daily = document.querySelector('.trending');
const weekly = document.querySelector('.weekly-roundup');
const dailyRight = document.querySelector('.daily-insights');
const rating = document.querySelectorAll('.rating-middle');
const article = document.querySelectorAll('.article-highlight');
const ratings = document.querySelector('.ratings-holder');
const rate = document.querySelector('.ratings');
const views = document.querySelectorAll('.views');
const pop_up_content = document.querySelector('.popup-content')
const label = document.querySelectorAll('label')

sun.addEventListener('click', () => {
  theme = theme === 'light' ? 'dark' : 'light'; // toggle theme
  localStorage.setItem('theme', theme); // save new theme
  applyTheme(theme); // apply it
  console.log('Theme switched to:', theme);
});

// Function that applies styles for each theme
function applyTheme(theme) {
  if (theme === 'dark') {
    document.body.style.backgroundColor = 'black';
    sun.src = '/static/imgs/moon-svgrepo-com.svg';
    nav.style.backgroundColor = '#1212';
    vert.style.backgroundColor = 'white';
    light.style.backgroundColor = 'transparent';
    weekly.style.backgroundColor = 'rgb(48, 45, 45)';
    daily.style.backgroundColor = 'rgb(48, 45, 45)';
    dailyRight.style.backgroundColor = 'rgb(48, 45, 45)';
    pop_up_content.style.backgroundColor = 'rgb(48, 45, 45)';
   
    article.forEach(a => {
      a.style.borderRight = '1px solid white';
    });
    views.forEach(v => {
      v.style.borderBottom = '1px solid white';
    });
    p.forEach(para => para.style.color = 'white');
    label.forEach(l => l.style.color = 'white');
  } else {
    document.body.style.backgroundColor = '';
    sun.src = '/static/imgs/sun-svgrepo-com (3).svg';
    nav.style.backgroundColor = '';
    vert.style.backgroundColor = 'rgb(48, 45, 45)';
    light.style.backgroundColor = 'orange';
    weekly.style.backgroundColor = '';
    daily.style.backgroundColor = '';
    dailyRight.style.backgroundColor = '';
    pop_up_content.style.backgroundColor = '';
    rating.forEach(r => {
      r.style.backgroundColor = '';
      r.style.border = '1px solid white';
    });
    article.forEach(a => {
      a.style.borderRight = '';
    });
    views.forEach(v => {
      v.style.borderBottom = '';
    });
    p.forEach(para => para.style.color = '');
  }
}

// Apply theme immediately on load
applyTheme(theme);

// When user clicks the sun/moon icon

console.log(p);

const search = document.querySelector('.search-bar')
const searchBtn = document.querySelector('.searchBtn')

searchBtn.addEventListener('click', ()=> {
  search.classList.toggle('on')
 
})

});
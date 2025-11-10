let theme = localStorage.getItem('theme') || 'light';


let blog_title = document.querySelector('.title')
let blog_title2 = document.querySelector('.title04')
let bog_author = document.querySelector('.blog_author')
let blog_content = document.querySelector('.text')
let second_sec_right = document.querySelector('.second-sec-right')
let second_sec_left = document.querySelector('.second-sec-left')
let second_sec_middle = document.querySelector('.second-sec-middle')
let second_sec = document.querySelector('.second-sec')


if (theme === 'dark') {
second_sec_left.style.backgroundColor='rgb(48, 45, 45)';
second_sec_middle.style.backgroundColor='rgb(48, 45, 45)';
second_sec_right.style.backgroundColor='rgb(48, 45, 45)';
second_sec.style.backgroundColor='rgb(48, 45, 45)';

blog_title.style.color =  'white';
blog_content.style.color='white';
     

}


console.log(second_sec_left);

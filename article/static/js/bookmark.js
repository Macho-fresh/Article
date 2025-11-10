let theme = localStorage.getItem('theme') || 'light';
let p = document.querySelectorAll('p');


let body = document.querySelector('body')
if (theme === 'dark') {
    body.style.backgroundColor='rgb(48, 45, 45)'
    p.forEach(para => para.style.color = 'white');
    
}
const menu=document.querySelector('.menu');
const nav=document.querySelector('.nav');
const header=document.querySelector('.site-header');
const progress=document.querySelector('.progress span');
const topButton=document.querySelector('.top');

if(menu&&nav){
  menu.addEventListener('click',()=>{
    const open=nav.classList.toggle('open');
    menu.setAttribute('aria-expanded',String(open));
  });
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
    nav.classList.remove('open');
    menu.setAttribute('aria-expanded','false');
  }));
}

function updateScroll(){
  const y=window.scrollY;
  const max=document.documentElement.scrollHeight-window.innerHeight;
  if(progress)progress.style.width=`${max>0?y/max*100:0}%`;
  if(header)header.classList.toggle('scrolled',y>20);
  if(topButton)topButton.classList.toggle('visible',y>700);
}
updateScroll();
window.addEventListener('scroll',updateScroll,{passive:true});
if(topButton)topButton.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));

document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());

const revealObserver=new IntersectionObserver((entries,observer)=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
},{threshold:.12,rootMargin:'0px 0px -45px'});
document.querySelectorAll('.reveal').forEach(el=>revealObserver.observe(el));

const sections=document.querySelectorAll('[data-section]');
const links=document.querySelectorAll('[data-nav]');
if(sections.length){
  const sectionObserver=new IntersectionObserver(entries=>{
    const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>b.intersectionRatio-a.intersectionRatio)[0];
    if(!visible)return;
    const current=visible.target.dataset.section;
    links.forEach(link=>link.classList.toggle('active',link.dataset.nav===current));
  },{threshold:[.25,.5,.75],rootMargin:'-25% 0px -55%'});
  sections.forEach(section=>sectionObserver.observe(section));
}

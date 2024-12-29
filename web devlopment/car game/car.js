let text = document.getElementById("bx");
let l=399;
let t=0;
let move=55;


document.addEventListener("keydown",(event)=>{
 if(event.key==='d'){
    l+=move;
    text.style.left=move+l+"px";

 }
    
})

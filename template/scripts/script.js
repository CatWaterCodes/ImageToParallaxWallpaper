var mouseX = 0,
    mouseY = 0;

var w = window.innerWidth,
    h = window.innerHeight;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX - w/2;
    mouseY = e.clientY - h/2; //has to be reversed
    updateImagePositions();
    console.log(`Mouse X: ${mouseX}, Mouse Y: ${mouseY}`);
});

function updateImagePositions() {
    let images = document.getElementsByClassName("layers");
    let imageArray = Array.from(images);
    imageArray.reverse()
    let moveSpeed = 0.032;

    imageArray.forEach((element) => {
        if(element.classList.contains("fill")) {
            if(element.classList.contains("top")) {
                element.style.top = document.documentElement.clientWidth/2 - document.documentElement.clientHeight + "px"; 
            }
            else if(element.classList.contains("bot")) {
                element.style.bottom =  document.documentElement.clientWidth/2 - document.documentElement.clientHeight + "px"; 
            }
            else {
                element.style.top = moveSpeed * mouseY - document.documentElement.clientHeight/2 + "px";    
            }
            element.style.left = moveSpeed * mouseX - 0.05*document.documentElement.clientWidth + "px";
        }

        else {
            element.style.top = moveSpeed * mouseY + "px";
            element.style.left = moveSpeed * mouseX + document.documentElement.clientWidth/2 - document.documentElement.clientHeight/2 + "px";
        }
        
        moveSpeed -= 0.001;
    });
}
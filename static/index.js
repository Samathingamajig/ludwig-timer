const socket = io();
socket.on('connect', () => {
    console.log('connected');
});

const timeH1 = document.querySelector('#time');
const hoursSpan = document.querySelector('#hours');
const minsSpan = document.querySelector('#mins');
const secsSpan = document.querySelector('#secs');
const waitH1 = document.querySelector('#wait');

waitH1.hidden = false;

socket.on('time', ({ hours, minutes, seconds }) => {
    waitH1.hidden = true;
    timeH1.hidden = false;
    hoursSpan.innerText = hours;
    minsSpan.innerText = minutes;
    secsSpan.innerText = seconds;
});

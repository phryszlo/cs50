if (!localStorage.getItem('counter')) {
  localStorage.setItem('counter', 0)
}

function count() {
  let counter = localStorage.getItem('counter')
  counter ++
  document.querySelector('h1').innerHTML = counter
  localStorage.setItem('counter', counter)
  if (counter % 11 === 0) {
    // alert('mod 11')
  }
}

document.addEventListener('DOMContentLoaded', () => {
  //what will this line do if there is no value for counter?
  document.querySelector('h1').innerHTML = localStorage.getItem('counter')
  
  document.querySelector('button').onclick = count

  setInterval(count, 1)

})
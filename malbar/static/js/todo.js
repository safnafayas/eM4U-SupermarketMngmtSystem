let input = document.querySelector('.entered-list');
let addBtn = document.querySelector('.add-list');
let tasks = document.querySelector('.tasks');

// button disabled

input.addEventListener('keyup' , () =>{
    if(input.value.trim() != 0){
        addBtn.classList.add('active')
    }
})

//add new item to list

addBtn.addEventListener('click', () => {
    if (input.value.trim() != 0){
        let newItem = document.createElement('div');
        newItem.classList.add('item');
        newItem.innerHTML = `
        <p> ${input.value} </p>
        <div class="item-btn">
            <i class="material-icons assignment_turned_in" style="color: rgb(123, 201, 123);" >assignment_turned_in</i>
            <i class="material-icons close" style="color: rgb(216, 65, 65);">close</i>
        </div>`
        tasks.appendChild(newItem);
        input.value = '';
    }   else    {
        alert('Please enter a task')
    }
        
})


// delete item

tasks.addEventListener('click', (e) => {
    if (e.target.classList.contains('close')) {
        e.target.parentElement.parentElement.remove(); 
    }
})


// mark item
tasks.addEventListener('click', (e) => {
    if(e.target.classList.contains('assignment_turned_in'))
    {
        e.target.parentElement.parentElement.classList.toggle('completed');
    }
})
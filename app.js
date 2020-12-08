// This doesn't get the data from the element, it basically just acknowledges the presence of the data
const cafeList = document.querySelector('#cafe-list');
const form = document.querySelector('#add-cafe-form');

// create elements and render cafe
function renderList(doc){
    let li = document.createElement('li');
    let name = document.createElement('span');
    let deadline = document.createElement('span');
    let cross = document.createElement('div');
    

    li.setAttribute('data-id', doc.id)
    name.textContent = doc.data().name;
    deadline.textContent = doc.data.deadline;
    cross.textContent = 'x';
   

    li.appendChild(name)
    li.appendChild(deadline)
    li.appendChild(cross);
   

    cafeList.appendChild(li)

    //deleting data
    cross.addEventListener('click', (e) => {
        e.stopPropagation();
        let id = e.target.parentElement.getAttribute('data-id')
        db.collection('Tasks').doc(id).delete();
    })

}
//getting data

/* db.collection('Tasks').where('deadline', '==', 'December').get().then((snapshot) => {
   snapshot.docs.forEach(doc => {
       renderList(doc)
       
   });

}) */

//saving data
form.addEventListener('submit', (e) => {
    e.preventDefault();
    db.collection('Tasks').add({
        name: form.name.value,
        deadline: form.deadline.value
    })
    form.name.value = '';
    form.deadline.value ='';
})

//updating data
form.addEventListener('submit', (e) => {
    e.preventDefault();
    db.collection('Tasks').doc(id).update({
        name: form.name.value,
        deadline: form.deadline.value
    })
    form.name.value = '';
    form.deadline.value ='';

//real-time listener
db.collection('Tasks').orderBy('deadline').onSnapshot(snapshot =>
    { 
        let changes = snapshot.docChanges();
        changes.forEach(change => {
            if(change.type == 'added'){
                renderList(change.doc);
            }
            else if(change.type == 'removed'){
                let li = cafeList.querySelector('[data-id=' + change.doc.id + ']');
                cafeList.removeChild(li)
            }

        })
    })
var cardsDiv = document.querySelector("#cards")
var currentUsername = "";

function getUsername(element){
    console.log(element.value)
    currentUsername = element.value;
}

var selection = selection

function select_info(element){
    console.log(element.value)
    selection = element.value;
    return selection
}

function makeCoderCard(data) {
    if (selection == 'yes') {
        var res = `<div class= "card">
                        <img src="${data.avatar_url}" alt="${data.login}">
                        <div class="flex-1">
                            <h3>${data.login} - ${data.name}</h3>
                            <p>Location: ${data.location}</p>
                            <p>Repositories: ${data.public_repos}</p>
                        </div>
                    </div>`
        } else {
            var res = `<div class= "card">
                            <div class="flex-1">
                                <h3>${data.login} - ${data.name}</h3>
                                <p>Location: ${data.location}</p>
                                <p>Repositories: ${data.public_repos}</p>
                            </div>
                        </div>`
    }
    console.log(selection)
    return (res);
}

async function search(){
    var response = await fetch("https://api.github.com/users/" + currentUsername)
    var coderData = await response.json();
    console.log(coderData);
    cardsDiv.innerHTML = makeCoderCard(coderData) + cardsDiv.innerHTML;
}
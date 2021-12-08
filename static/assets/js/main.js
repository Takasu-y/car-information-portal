'use strict'
import {modelList} from './modelList.js'


let makerSelector = document.querySelectorAll("#id_maker").item(0);
makerSelector.addEventListener('change', () => {

    let modelSelector = document.querySelectorAll("#id_model").item(0);

    modelSelector.innerHTML = "";
    modelSelector.innerHTML =
    `
    <option value="select Model" selected="">select Model</option>
    <option value="">Any</option>
    `;

    modelList[makerSelector.value].forEach(model => {
        modelSelector.innerHTML += `<option value="${model}">${model}</option>`;
    });

})

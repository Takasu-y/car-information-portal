'use strict'

import {modelList} from './modelList.js'

console.log(modelList["Audi"]);

let selector = document.querySelectorAll("#id_maker").item(0);
selector.addEventListener('change', () => {
        const user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
        let  url = `https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getModels&make=${selector.value}`


        let headers = new Headers({
            "Content-Type" : "application/json",
            "User-Agent"   : user_agent
        })

        let response = fetch(url, {
            "headers": headers
        })


        console.log(response.headers);
})

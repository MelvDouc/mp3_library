
const API_URL = "http://localhost:5173/api/v1";


async function getData(url, defaultValue) {
    try{
        const response = await fetch(API_URL + url);
        const data = await response.json();
        return data;
    }  catch(e){
        console.log(e);
        return defaultValue

    }

}


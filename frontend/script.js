const API = "http://127.0.0.1:8000";

const API_KEY = "rag101";



const uploadBtn = document.getElementById("uploadBtn");

const askBtn = document.getElementById("askBtn");



uploadBtn.onclick = async () => {

    const file = document.getElementById("fileInput").files[0];

    if(!file){

        alert("Choose a document.");

        return;
    }

    const formData = new FormData();

    formData.append(
        "file",
        file
    );

    document.getElementById("uploadStatus").innerText =
        "Uploading document...";

    try{

        const response = await fetch(

            API + "/upload",

            {

                method:"POST",

                headers:{

                    "X-API-Key":API_KEY

                },

                body:formData

            }

        );

        const data = await response.json();

        document.getElementById("uploadStatus").innerText =
            data.message;

    }

    catch(err){

        document.getElementById("uploadStatus").innerText =
            "Upload failed.";
    }

};



askBtn.onclick = async () => {

    const question = document
        .getElementById("question")
        .value
        .trim();

    if(question===""){

        return;
    }

    document.getElementById("response").innerText =
        "Generating answer...";

    try{

        const response = await fetch(

            API + "/process",

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json",

                    "X-API-Key":API_KEY

                },

                body:JSON.stringify({

                    text:question

                })

            }

        );

        const data = await response.json();

        document.getElementById("response").innerText =
            data.result;

    }

    catch(err){

        document.getElementById("response").innerText =
            "Unable to generate response.";
    }

};
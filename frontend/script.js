const API = "http://127.0.0.1:8000";

const API_KEY = "rag101";

const fileInput = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");
const askBtn = document.getElementById("askBtn");
const responseEl = document.getElementById("response");

fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    fileName.innerText = file ? file.name : "No file selected";
    uploadStatus.innerText = "";
    uploadStatus.classList.remove("is-ready");
});

uploadBtn.onclick = async () => {

    const file = fileInput.files[0];

    if(!file){

        alert("Choose a document.");

        return;
    }

    const formData = new FormData();

    formData.append(
        "file",
        file
    );

    uploadBtn.disabled = true;
    uploadStatus.classList.remove("is-ready");
    uploadStatus.innerText = "Uploading document...";

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

        uploadStatus.innerText = data.message;
        uploadStatus.classList.add("is-ready");

    }

    catch(err){

        uploadStatus.innerText = "Upload failed.";

    }

    finally{

        uploadBtn.disabled = false;

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

    askBtn.disabled = true;
    responseEl.classList.remove("is-placeholder");
    responseEl.innerText = "Generating answer...";

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

        responseEl.innerText = data.result;

    }

    catch(err){

        responseEl.innerText = "Unable to generate response.";

    }

    finally{

        askBtn.disabled = false;

    }

};

const API = "http://127.0.0.1:8000";

const API_KEY = "rag101";

const fileInput = document.getElementById("fileInput");
const dropzone = document.getElementById("dropzone");
const fileName = document.getElementById("fileName");
const fileSub = document.getElementById("fileSub");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");

const askBtn = document.getElementById("askBtn");
const responseEl = document.getElementById("response");
const consoleState = document.getElementById("consoleState");

const step1 = document.getElementById("step-1");
const step1Status = document.getElementById("step-1-status");
const step2 = document.getElementById("step-2");
const step2Status = document.getElementById("step-2-status");
const step3 = document.getElementById("step-3");
const step3Status = document.getElementById("step-3-status");

function setStep(step, statusEl, state, label){

    step.classList.remove("is-active","is-complete");

    if(state){
        step.classList.add(state);
    }

    statusEl.innerText = label;
}

function showFile(file){

    fileName.innerText = file.name;
    fileSub.innerText = (file.size / 1024).toFixed(1) + " KB";

    uploadStatus.innerText = "";
    uploadStatus.classList.remove("is-ready");

    setStep(step1,step1Status,"is-active","File selected");
}

fileInput.addEventListener("change", () => {

    const file = fileInput.files[0];

    if(file){
        showFile(file);
    }

});

["dragenter","dragover"].forEach(evt => {

    dropzone.addEventListener(evt, (e) => {
        e.preventDefault();
        dropzone.classList.add("is-drag");
    });

});

["dragleave","drop"].forEach(evt => {

    dropzone.addEventListener(evt, (e) => {
        e.preventDefault();
        dropzone.classList.remove("is-drag");
    });

});

dropzone.addEventListener("drop", (e) => {

    const file = e.dataTransfer.files[0];

    if(file){
        fileInput.files = e.dataTransfer.files;
        showFile(file);
    }

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
    setStep(step1,step1Status,"is-active","Uploading");

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

        setStep(step1,step1Status,"is-complete","Indexed");
        setStep(step2,step2Status,"is-active","Ready");

    }

    catch(err){

        uploadStatus.innerText = "Upload failed.";
        setStep(step1,step1Status,null,"Failed — try again");

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
    responseEl.classList.add("is-loading");
    responseEl.innerText = "Generating answer";
    consoleState.innerText = "Generating";

    setStep(step2,step2Status,"is-active","Generating");
    setStep(step3,step3Status,"is-active","In progress");

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

        responseEl.classList.remove("is-loading");
        responseEl.innerText = data.result;
        consoleState.innerText = "Done";

        setStep(step2,step2Status,"is-complete","Answered");
        setStep(step3,step3Status,"is-complete","Received");

    }

    catch(err){

        responseEl.classList.remove("is-loading");
        responseEl.innerText = "Unable to generate response.";
        consoleState.innerText = "Error";

        setStep(step3,step3Status,null,"Failed — try again");

    }

    finally{

        askBtn.disabled = false;

    }

};

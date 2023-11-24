import React, {useRef, useState} from "react";
import addIcon from "../icons/Add.svg";
import SearchIcon from "../icons/SearchIcon.svg"
import Settings from "../icons/Settings.svg"
import Clear from "../icons/CloseBig.svg"
import LectureElement from "./LectureElement";

import "../styles/createview.scss"
import FileUI from "./FileUI";
import FileLecture from "./LectureUpload";

function CreateView({add_lecture}) {

    const handleUploadClick = () => {
        if (!lecFile) {
            console.log('111')
          return;
        }
        
        let formData = new FormData();
        formData.append('file', lecFile)
        // 👇 Uploading the file using the fetch API to the server
        fetch('https://d995-89-109-249-13.ngrok-free.app/upload_lecture', {
          method: 'POST',
          body: formData,

          // 👇 Set headers manually for single file upload
          headers: {
            // 'content-type': 'multipart/form-data',
            'Accept': '*/*',
            'Access-Control-Allow-Origin': '*',
          },
        })
          .then((res) => res.json())
          .then((data) => {add_lecture(data, FIO, title, theme);console.log(data)})
          .catch((err) => console.error(err));
      };


  const fileRef = useRef();
  const [file, setFile] = useState("");
  const [lecFile, setLecFile] = useState("")
  const [FIO, setFIO] = useState("")
  const [title, setTitle] = useState("")
  const [theme, setTheme] = useState("")

  return (
    <div className="createViewContainer">
      <div className="topBarWrapper">
        <a href="/" className="close"><img  src={Clear}/></a>
        <div className="addTitle ">Добавить Лекцию</div>
        <div className="spacer"/>
        </div>
      
      <div className="container">
        <FileUI file={file} setFile={setFile} fileRef={fileRef}/>
        <div className="input">
            ФИО
            <input onChange = {(e)=>{setFIO(e.target.value)}}placeholder="Введите лектора"/>
        </div>
        <div className="input">
            Название
            <input onChange = {(e)=>{setTitle(e.target.value)}}placeholder="Введите название лекции"/>
        </div>
        
        <div className="input">
            Тема
            <input onChange = {(e)=>{setTheme(e.target.value)}}placeholder="Выберите тему"/>
        </div>
        <FileLecture file={lecFile} setFile={setLecFile} />
        <div className={"upload button "+ ((!lecFile || !FIO || !theme || !title) ? 'not' : '')} onClick={handleUploadClick}>Готово</div>
      </div>
    </div>
  );
}

export default CreateView;

import React, {useRef, useState} from "react";
import addIcon from "../icons/Add.svg";
import SearchIcon from "../icons/SearchIcon.svg"
import Settings from "../icons/Settings.svg"
import Clear from "../icons/CloseBig.svg"
import LectureElement from "./LectureElement";

import "../styles/createview.scss"
import FileUI from "./FileUI";

function CreateView() {


    const fileRef = useRef();
  const [file, setFile] = useState("");
  const [fileType, setFileType] = useState("");
  const [fileName, setFileName] = useState("");
  const [fileOrig, setFileOrig] = useState();

  return (
    <div className="createViewContainer">
      <div className="topBarWrapper">
        <a href="/" className="close"><img  src={Clear}/></a>
        <div className="addTitle ">Добавить Лекцию</div>
        <div className="spacer"/>
        </div>
      
      <div className="container">
        <FileUI file={file} setFile={setFile} fileName={fileName} fileRef={fileRef} setFileName={setFileName} setFileOrig={setFileOrig} setFileType={setFileType} fileType={fileType} fileOrig={fileOrig}/>
        <div className="input">
            ФИО
            <input placeholder="Введите лектора"/>
        </div>
        <div className="input">
            Название
            <input placeholder="Введите название лекции"/>
        </div>
        
        <div className="input">
            Тема
            <input placeholder="Выберите тему"/>
        </div>
        <FileUI file={file} setFile={setFile} fileName={fileName} fileRef={fileRef} setFileName={setFileName} setFileOrig={setFileOrig} setFileType={setFileType} fileType={fileType} fileOrig={fileOrig}/>
        <div className="upload button">Готово</div>
      </div>
    </div>
  );
}

export default CreateView;

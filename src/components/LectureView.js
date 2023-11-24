import React, {useRef, useReducer, useState, useEffect} from "react";
import addIcon from "../icons/Add.svg";
import SearchIcon from "../icons/SearchIcon.svg"
import Settings from "../icons/Settings.svg"
import Clear from "../icons/CloseBig.svg"
import site_url from "../site"

import "../styles/lectureview.scss"
import FileUI from "./FileUI";
import FileLecture from "./LectureUpload";
import { useParams } from "react-router-dom";

function LectureView({lectures, nav}) {
  const {id} = useParams();
  let lecture = lectures[id]
  const [isG, setG] = useState(false)
  console.log(lecture, id)
  const [img, setImg] = useState('')
  useEffect(()=>{

  if (id >= lectures.length || id < 0) {
    nav('/')
    return
    }
    if (!img) {
        fetch(site_url+"get_image/?id="+lecture.data.id, {
        method: 'GET',
          
        headers: {
          // 'content-type': 'multipart/form-data',
          'Accept': 'image/png',
          "ngrok-skip-browser-warning": "1",
          'Access-Control-Allow-Origin': '*',
        },
      })
        .then((res) => res.blob())
        .then((blob) => {
            setImg(URL.createObjectURL(blob))
}
        )
        .catch((err) => console.error(err));
    }}
    )
  if (id >= lectures.length || id < 0) {
    nav('/')
    return
}


  
  return (
    <div className="lectureViewContainer">
      <div className="topBarWrapper">
        <a href="/" className="close"><img src={Clear}/></a>
        <div className="addTitle ">{lecture.title}</div>
        <div className="spacer"/>
        </div>
      
      <div className="container">
        <div className="imgWrapper" ><img alt="" src={img}/></div>
        <div className="upinfo">
            <div className="up">{lecture.FIO} · {lecture.theme}</div>
            <a download={lecture.title+".docx"}href={site_url+"get_docx?id="+lecture.data.id} className="button document">Скачать DOC</a>
            
        </div>
        <div>{lecture.data.short_descr}</div>
        <div onClick={()=>{setG(!isG)}}className="glosWrapper button">Глоссарий</div>
     </div>
        
        
       </div>
  );
}

export default LectureView;

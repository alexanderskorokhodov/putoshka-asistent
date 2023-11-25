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
  let {id} = useParams();
  let lecture = lectures[id]
  const [isG, setG] = useState(false)
  const [, forceUpdate] = useReducer(x => x + 1, 0);
  console.log(lecture, id)
  const [img_, setImg] = useState(<img alt="" src={""}/>)
  useEffect(()=>
    {
        if (id >= lectures.length || id < 0) {
            nav('/')
            return
        }
        if (!isG) {
            fetch(site_url+"get_image/?id="+lecture.data.id, {
                method: 'GET',
                headers: {
                    'Accept': 'image/png',
                    "ngrok-skip-browser-warning": "1",
                    'Access-Control-Allow-Origin': '*',
                },
      })
        .then((res) => res.blob())
        .then((blob) => {
            setImg(<img alt="" src={URL.createObjectURL(blob)}/>)
            setG(true)
            })
        .catch((err) => console.error(err));
        }
    }, [id]
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
        <div className="imgWrapper" >{img_}</div>
        <div className="upinfo">
            <div className="up">{lecture.FIO} · {lecture.theme}</div>
            <div>
            <a download={lecture.title+".docx"}href={site_url+"get_docx?id="+lecture.data.id} className="button document">DOCX</a>
            <a download={lecture.title+".pdf"}href={site_url+"get_pdf?id="+lecture.data.id} className="button document">PDF</a>
            </div>
        </div>
        <div>{lecture.data.short_descr}</div>
        <div onClick={()=>{
            setG(false);
            nav(`/glos/${id}`)
            forceUpdate()}}className="glosWrapper button">Глоссарий</div>
     </div>
        
        
       </div>
  );
}

export default LectureView;

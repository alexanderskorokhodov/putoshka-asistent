import React, {useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import Clear from "../icons/CloseBig.svg"
import "../styles/glosview.scss"

function GlosView({lectures, nav}){

    const {id} = useParams();
    let lecture = lectures[id]
    console.log(lecture, id)
    const [chosen_id, setId] = useState(-1);
    console.log(chosen_id)
    let view = lecture.data.terms.map((v, key) => {
        if ((chosen_id === -1) || (key === Number(chosen_id))) {
            // console.log(chosen_id, c, v)
            return <div className="glos" key={key} onClick={(e)=>{setId(key);}}>{(chosen_id === -1) ? v[0] : ((chosen_id === key) ? <div>{v[0]} {v[1]}</div> : "")}</div>
        } else {
            return <></>
        }
    })

    useEffect(()=>{

        if (id >= lectures.length || id < 0) {
          nav('/')
          return
        }
    })
    if (id >= lectures.length || id < 0) {
        nav('/')
        return
    }
    

    return <div className="container">
        <div className="topBarWrapper">
            <div onClick={()=>{(chosen_id === -1) ? nav(-1) : setId(-1)}} className="close"><img src={Clear}/></div>
            <div className="addTitle ">{lecture.title}</div>
            <div className="spacer"/>
        </div>
        <div className="dictView">{view}</div>
    </div>
}

export default GlosView;
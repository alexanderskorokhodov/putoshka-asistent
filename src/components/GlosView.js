import React, {useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import Clear from "../icons/CloseBig.svg"
import "../styles/glosview.scss"
import ReactPlayer from "react-player";
import useObjectURL from "use-object-url";
import site_url from "../site"


function GlosView({lectures, nav}){

    const {id} = useParams();
    let lecture = lectures[id]
    console.log(lecture, id)
    const [chosen_id, setId] = useState(-1);
    console.log(lecture.data.terms)
    const [mp3, setMp3] = useState("")
    useEffect(()=>{
    if (chosen_id!==-1 && !mp3) {
        fetch(site_url+`get_voice_term/?id=${lecture.data.id}&start=${lecture.data.terms[chosen_id][2]}&end=${lecture.data.terms[chosen_id][3]}`, {
        method: 'GET',
        headers: {
            'Accept': 'audio/mp3',
            "ngrok-skip-browser-warning": "1",
            'Access-Control-Allow-Origin': '*',
        },
})
.then((res) => {console.log(res);return res.blob()})
.then((blob) => {
    console.log(blob)
    setMp3(<audio src={useObjectURL(blob)} 
         />)})
    
    
.catch((err) => console.error(err));
}})

    let view = lecture.data.terms.map((v, key) => {
        if ((chosen_id === -1) || (key === Number(chosen_id))) {
            console.log(v)
            return <div className="glos" key={key} onClick={(e)=>{setId(key);}}>{(chosen_id === -1) ? 

            <div className="capitalize t">{v[0]}</div> :

             ((chosen_id === key) ?
              <div className="termin">
                <div className="capitalize t">
                    {v[0]}
                </div> 
                <div>· {v[1].toLowerCase()}</div>
                {mp3}
              </div> : "")}
            </div>
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
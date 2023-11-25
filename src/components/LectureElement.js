import React, { useEffect, useState, useReducer } from "react";
import site_url from '../site'
import "../styles/lecture.scss"


function LectureElement({id, nav, theme, date, title, short_desc, data}) {
    const func = ()=>{fetch(site_url+"get_image/?id="+data.id, {
        method: 'GET',
          
        // 👇 Set headers manually for single file upload
        headers: {
          // 'content-type': 'multipart/form-data',
          'Accept': 'image/png',
          "ngrok-skip-browser-warning": "1",
          'Access-Control-Allow-Origin': '*',
        },
      })
        .then((res) => res.blob())
        .then((blob) => {console.log(blob);
            var reader = new FileReader();
            reader.readAsDataURL(blob);
            reader.onloadend = function() {
                let base64data = reader.result;
                // console.log(base64data);
                setImg(URL.createObjectURL(blob))
}
        })
        .catch((err) => console.error(err));
    }
    const [img, setImg] = useState('')
    const [, forceUpdate] = useReducer(x => x + 1, 0);

    useEffect(()=>
    {func();forceUpdate()}, id)

    return <div onClick={()=>{func();nav('/lecture?id='+id)}} className="lecWrapper" key={data.id}>
        <div className="lecImgWrapper"> 
            <img className="lecImg" src={img} alt="image" />
        </div>
        <div className="lecDesc">
            <div className="lecTitle">{title}</div>
            <div className="lecShort light-text">{short_desc}</div>
            <div className="lecThemeDate light-text">
                {theme} · {date}
            </div>
        </div>
    </div>
}

export default LectureElement;
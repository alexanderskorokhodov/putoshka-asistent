import React from "react";

import "../styles/lecture.scss"

function LectureElement({img_link, theme, date, title, short_desc}) {

    return <div className="lecWrapper">
        <div className="lecImgWrapper"> 
            <img className="lecImg" src={img_link} />
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
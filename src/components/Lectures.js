import React, {useState} from "react";
import addIcon from "../icons/Add.svg";
import SearchIcon from "../icons/SearchIcon.svg"
import Settings from "../icons/Settings.svg"
import Clear from "../icons/Close.svg"
import LectureElement from "./LectureElement";
import server_url from "../site"

import "../styles/lectures.scss"

function Lectures({lectures, nav}) {

  // const [chosen_id, set_id] = useState(0);

  let id_ = -1;
  const lecView = lectures.map(
    (val) =>
    { 
      id_++;
      return <LectureElement id={id_} title={val.title} date={val.FIO} theme={val.theme} short_desc={ val.data['short_descr'].length > 25 ?val.data['short_descr'].slice(0, 25)+'...' : val.data['short_descr'] } 
      nav={
        nav} data={val.data}
      />
      
    }

  )
      
  
  
  return (
    <div className="lcsViewContainer">
      <div className="srchBrWrapper">
        <img src={SearchIcon} alt=""/>
        <input placeholder="Поиск"/>
        <img src={Settings} alt=""/>
        <img src={Clear} alt=""/>
        </div>

      <div onClick={()=>nav("/add")} className="loadButtonWrapper button">
        <img src={addIcon}/>
        Добавить
      </div>
      <div className="lcsContainer">
        {lecView}
        </div>
    </div>
  );
}

export default Lectures;

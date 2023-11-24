import React from "react";
import addIcon from "../icons/Add.svg";
import SearchIcon from "../icons/SearchIcon.svg"
import Settings from "../icons/Settings.svg"
import Clear from "../icons/Close.svg"
import LectureElement from "./LectureElement";

import "../styles/lectures.scss"

function Lectures({lectures}) {
  console.log(lectures)
  const lecView = lectures.map(
    (val)=>
    { console.log(val);
      return <LectureElement title={val.title} date={val.FIO} theme={val.theme} short_desc={ val.data['short_descr'].length > 25 ?val.data['short_descr'].slice(0, 25)+'...' : val.data['short_descr'] } 
  img_link="https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_5b3f4df6b70d4800a9cb6fb4_5b3f5635489e8d00ac4e2751/scale_1200"/>})
  
  return (
    <div className="lcsViewContainer">
      <div className="srchBrWrapper">
        <img src={SearchIcon}/>
        <input placeholder="Поиск"/>
        <img src={Settings}/>
        <img src={Clear}/>
        </div>

      <a href="/add" className="loadButtonWrapper button">
        <img src={addIcon}/>
        Добавить
      </a>
      <div className="lcsContainer">
        {lecView}
        </div>
    </div>
  );
}

export default Lectures;

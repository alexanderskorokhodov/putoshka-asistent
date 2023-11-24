import React from "react";
import addIcon from "../icons/Add.svg";
import SearchIcon from "../icons/SearchIcon.svg"
import Settings from "../icons/Settings.svg"
import Clear from "../icons/Close.svg"
import LectureElement from "./LectureElement";

import "../styles/lectures.scss"

function Lectures() {
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
        <LectureElement title="Лекция: Протоны" date="23 января 2023" theme="Физика" short_desc="Основные частицы атомного..." img_link="https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_5b3f4df6b70d4800a9cb6fb4_5b3f5635489e8d00ac4e2751/scale_1200"/>
        <LectureElement title="Лекция: Протоны" date="23 января 2023" theme="Физика" short_desc="Основные частицы атомного..." img_link="https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_5b3f4df6b70d4800a9cb6fb4_5b3f5635489e8d00ac4e2751/scale_1200"/>
        <LectureElement title="Лекция: Протоны" date="23 января 2023" theme="Физика" short_desc="Основные частицы атомного..." img_link="https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_5b3f4df6b70d4800a9cb6fb4_5b3f5635489e8d00ac4e2751/scale_1200"/>
        <LectureElement title="Лекция: Протоны" date="23 января 2023" theme="Физика" short_desc="Основные частицы атомного..." img_link="https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_5b3f4df6b70d4800a9cb6fb4_5b3f5635489e8d00ac4e2751/scale_1200"/>
        <LectureElement title="Лекция: Протоны" date="23 января 2023" theme="Физика" short_desc="Основные частицы атомного..." img_link="https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_5b3f4df6b70d4800a9cb6fb4_5b3f5635489e8d00ac4e2751/scale_1200"/>
        <LectureElement title="Лекция: Протоны" date="23 января 2023" theme="Физика" short_desc="Основные частицы атомного..." img_link="https://avatars.dzeninfra.ru/get-zen_doc/167204/pub_5b3f4df6b70d4800a9cb6fb4_5b3f5635489e8d00ac4e2751/scale_1200"/>
      </div>
    </div>
  );
}

export default Lectures;

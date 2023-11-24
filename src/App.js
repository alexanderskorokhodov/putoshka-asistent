import './styles/App.scss';
import Header from './components/Header';
import Lectures from './components/Lectures';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import CleanView from './components/CleanView';
import CreateView from './components/CreateView';
import React, {useState} from 'react';
import LectureView from './components/LectureView';
import GlosView from './components/GlosView';

import { useNavigate } from 'react-router';

function useStoredState(key, defaultValue) {
  // 👇 Load stored state into regular react component state
  const [state, setState] = useState(() => {
    const storedState = localStorage.getItem(key);
    // console.log(storedState)
    if (storedState) {
      // 🚩 Data is stored as string so need to parse
      return JSON.parse(storedState);
    }

    // No stored state - load default value.
    // It could be a function initializer or plain value.
    return defaultValue;
  });

  // 👇 Keeps the exact same interface as setState - value or setter function.
  const setValue = (value) => {
    const valueToStore = value;
    localStorage.setItem(key, JSON.stringify(valueToStore));
    setState(valueToStore);
  };

  // as const tells TypeScript you want tuple type, not array.
  return [state, setValue] ;
}


function App() {

  const add_lecture = (data, FIO, title, theme)=>{
    setLectures([...lectures, {data: data, FIO: FIO, theme:theme, title:title}])
  }
  const nav = useNavigate()

  const [lectures, setLectures] = useStoredState('lectures', [])

  return (
    <div className="App">
      <div className='left'>
        <Header/>
        <Lectures nav={nav} lectures={lectures}/>
      </div>
      <div className='right'>
          <Routes>
            <Route path="/" element={<CleanView/>} />
            <Route path="/add" element={<CreateView nav={nav}add_lecture={add_lecture}/>} />
            <Route path="/lecture/:id" element={<LectureView lectures={lectures} nav={nav}/>} />
            <Route path="/glos/:id" element={<GlosView lectures={lectures} nav={nav}/>} />
          </Routes>
      </div>
    </div>
  );
}

export default App;

import './styles/App.scss';
import Header from './components/Header';
import Lectures from './components/Lectures';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import CleanView from './components/CleanView';
import CreateView from './components/CreateView';

function App() {
  return (
    <div className="App">
      <div className='left'>
        <Header/>
        <Lectures/>
      </div>
      <div className='right'>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<CleanView/>} />
            <Route path="/add" element={<CreateView/>} />
          </Routes>
        </BrowserRouter>
      </div>
    </div>
  );
}

export default App;

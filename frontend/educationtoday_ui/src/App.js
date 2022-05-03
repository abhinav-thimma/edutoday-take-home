import './App.css';
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MostCited from './pages/MostCited';
import MostAffiliated from './pages/MostAffiliated';
import Home from './pages/Home';

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/mostcited" element={<MostCited />} />
          <Route path="/mostaffiliated" element={<MostAffiliated />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

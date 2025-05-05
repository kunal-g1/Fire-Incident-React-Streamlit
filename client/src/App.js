import React from 'react';
import './App.css';
import TableauDashboard from './Components/TableauDashboard';
import StreamlitEmbed from './Components/StreamlitEmbed';

function App() {
  return (
    <div className="App">
      <TableauDashboard />
      <StreamlitEmbed />
    </div>
  );
}

export default App;

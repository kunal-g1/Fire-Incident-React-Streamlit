import React from 'react';

const TableauDashboard = () => {
    const url = "https://public.tableau.com/app/profile/kunal.g1/viz/Fire_Incidents_2024/FireIncidents2024Dashboard";

    return (
      <div style={{ margin: '20px' }}>
        <h1>Fire Incidents Dashboard</h1>
        <a href={url} target="_blank" rel="noopener noreferrer" style={{ fontSize: '20px', textDecoration: 'none', color: '#0077b6' }}>
          Open Tableau Dashboard
        </a>
      </div>
    );
};

export default TableauDashboard;
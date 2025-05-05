import React from 'react';

const TableauDashboard = () => {
  const url = "https://public.tableau.com/app/profile/kunal.goel7443/viz/Fire_Incidents_2024/FireIncidents2024Dashboard?publish=yes";

  return (
    <div style={{ width: '100%', height: '800px' }}>
      <iframe
        title='Tableau'
        src={url}
        width="100%"
        height="100%"
        style={{ border: 'none' }}
      >
      </iframe>
    </div>
  );
};

export default TableauDashboard;
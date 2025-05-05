import React from 'react';

const StreamlitEmbed = () => {
  return (
    <iframe
      src="http://localhost:8510"
      title="Streamlit App"
      width="100%"
      height="800px"
      style={{ border: "none" }}
    ></iframe>
  );
};

export default StreamlitEmbed;
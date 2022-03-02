import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';


export default function App() {
  // ...
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const base_url = "https://soljit35-dev-ed.my.salesforce.com/"
  const token = "00D4L000000gmbH!AQsAQNtrsIaF8paoPGYUzjCUJovreEXTHbtQz2IMZzHi5qJXiMT1kcGh9U.55vxiRRucCu8FsYf7RuKbwO7kNw6jrr.kWe1N"
  
  data = {base_url: base_url, token: token}

    
  useEffect(() => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    };
    fetch('http://127.0.0.1:8000/candidature', requestOptions)
      .then((response) => {
      if (!response.ok) {
        throw new Error(
          `This is an HTTP error: The status is ${response.status}`
        );
      }
      return response.json();
      })
      .then((actualData) => {
        setData(actualData);
        setError(null);
      })
      .catch((err) => {
        setError(err.message);
        setData(null);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="App">
      <h1>Salesforce Condidatures</h1>
      {loading && <div>A moment please...</div>}
      {error && (
        <div>{`There is a problem fetching the post data - ${error}`}</div>
      )}
      <ul>
        {data &&
          data.map(({ First_Name__c, Last_Name__c, Year__c, Year_Of_Experience__c }) => (
            <li key={First_Name__c}>
              <h3>{Last_Name__c}</h3>
              <h3>{Year__c}</h3>
              <h3>{Year_Of_Experience__c}</h3>
            </li>
          ))}
      </ul>
    </div>
  );
}

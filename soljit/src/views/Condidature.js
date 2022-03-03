import React, { useState, useEffect } from 'react';
import axios from "axios"
import {Table} from "react-bootstrap"


export default function Condidature() {
    const [candidatures, setCandidatures] = useState([])
    const backendUrl = "http://127.0.0.1:8000/candidature"
    const postData = {
        "base_url": "https://soljit35-dev-ed.my.salesforce.com/",
         "token": "00D4L000000gmbH!AQsAQPPIIjH_fUVMez58h1hD9L_lvCXy5zvA2Iw.8e70TYS0ioVZl01rzvCPbCDU_ewh24x84SvZ9SaasRzY9nl2u_B5L9fV"
        }

    useEffect(() => {
        axios.post(backendUrl, postData)
      .then(function (response) {
        setCandidatures(response['data']['records'])
      })
      .catch(function (error) {
        console.log(error);
      });
    }, [])



    if(candidatures){
    return (
        <div>
            <h1>List of candidatures</h1>
            <Table>
            <tbody>
                <tr>

                    <th> First Name </th>
                    <th> Last Name </th>
                    <th> Year_Of_Experience </th>
                     
                </tr>
                {
                candidatures.map((model, i) =>
                    <tr key={i} >
                            <td> { model.First_Name__c } </td>
                            <td> { model.Last_Name__c}  </td>
                            <td> { model.Year_Of_Experience__c}  </td>
                    </tr>
                    )
                }
                </tbody>
            </Table>
        </div>
    );
    }
  

}

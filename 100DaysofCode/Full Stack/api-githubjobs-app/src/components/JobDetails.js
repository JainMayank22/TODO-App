import React, {useEffect, useContext } from 'react';
import JobsContext from '../context/jobs';

const JobDetails = () => {
  const { details, onResetPage } = useContext(JobsContext);
  // resetting the scroll to the top
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  const {
    type,
    title,
    description,
    location,
    company,
    company_url,
    company_logo,
    how_to_apply
  } = details;

  return (
    <div className="job-details">
      <div className="back-link">
        <a href="/#" onClick={onResetPage}>
          &lt;&lt; Back to results
        </a>
      </div>
      <div>
        {type} / {location}
      </div>
      <div className="main-section">
        <div className="left-section">
          <div className="title">{title}</div> <hr />
          <div
            className="job-description"
            dangerouslySetInnerHTML={{ __html: description }}
          ></div>
        </div>
        <div className="right-section">
          <div className="company-details">
            <h3>About company</h3>
            <img src={company_logo} alt={company} className="company-logo" />
            <div className="company-name">{company}</div>
            <a className="company-url" href={company_url}>
              {company_url}
            </a>
          </div>
          <div className="how-to-apply">
            <h3>How to apply</h3>
            <div dangerouslySetInnerHTML={{ __html: how_to_apply }}></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default JobDetails;

//  For job description display

            // {/* <div>{how_to_apply}</div> */}
//  {/*React avoids all html content to avoid the Cross Site Scripting (XSS) attacks react uses the below commented format */}
          // {/* <div className="job-description">{description}</div> */}
          // {/* but since we need to display the html in jsx expression we use the below line */}
          
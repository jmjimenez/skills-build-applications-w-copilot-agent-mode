
import logo from '../public/octofitapp-small.png';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';


function App() {
  const [showModal, setShowModal] = useState(false);
  return (
    <div className="App bg-light min-vh-100">
      {/* Bootstrap Navigation */}
      <nav className="navbar navbar-expand-lg mb-4">
        <div className="container-fluid">
          <a className="navbar-brand d-flex align-items-center" href="/">
            <img src={logo} alt="OctoFit Logo" style={{height: '48px', marginRight: '12px'}} />
            OctoFit Tracker
          </a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="/">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/activities">Activities</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/teams">Teams</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/leaderboard">Leaderboard</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container">
        {/* Bootstrap Heading */}
        <h1 className="display-4 mb-4 text-primary">Welcome to OctoFit Tracker</h1>

        {/* Bootstrap Card */}
        <div className="card shadow mb-4">
          <div className="card-body">
            {/* Remove logo from card, now in navbar */}
            <p className="lead">Track your fitness activities, join teams, and compete on the leaderboard!</p>
            <button className="btn btn-success me-2" onClick={() => setShowModal(true)}>Show Info Modal</button>
            <a className="btn btn-outline-primary" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">Learn React</a>
          </div>
        </div>

        {/* Bootstrap Table Example */}
        <div className="mb-4">
          <h2 className="h4 mb-3">Sample Activity Table</h2>
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>Activity</th>
                <th>Duration</th>
                <th>Calories</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Running</td>
                <td>30 min</td>
                <td>300</td>
              </tr>
              <tr>
                <td>Cycling</td>
                <td>45 min</td>
                <td>400</td>
              </tr>
              <tr>
                <td>Swimming</td>
                <td>60 min</td>
                <td>500</td>
              </tr>
            </tbody>
          </table>
        </div>

        {/* Bootstrap Modal Example */}
        {showModal && (
          <div className="modal show d-block" tabIndex="-1" role="dialog">
            <div className="modal-dialog" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">About OctoFit Tracker</h5>
                  <button type="button" className="btn-close" aria-label="Close" onClick={() => setShowModal(false)}></button>
                </div>
                <div className="modal-body">
                  <p>This app helps you log activities, join teams, and compete for fitness goals!</p>
                </div>
                <div className="modal-footer">
                  <button type="button" className="btn btn-secondary" onClick={() => setShowModal(false)}>Close</button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}


export default App;

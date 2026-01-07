// Project Dashboard Component

import React, { useEffect, useState } from 'react';
import api from '../api';

const ProjectDashboard = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    try {
      const response = await api.get('/projects/');
      setProjects(response.data);
    } catch (error) {
      console.error('Error fetching projects:', error);
    }
  };

  const updateStatus = async (projectId, newStatus) => {
     // In a real app, this would be a separate update call
     // For this PoC, we will simulate or implement a minimal update if the API supports it
     // The current API supports update
     try {
         await api.put(`/projects/${projectId}`, { status: newStatus });
         fetchProjects();
     } catch (error) {
         console.error('Error updating status:', error);
     }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'Idea': return '#e3f2fd';
      case 'PoC': return '#fff3e0';
      case 'Build': return '#e8f5e9';
      case 'Scale': return '#f3e5f5';
      default: return '#fff';
    }
  };

  return (
    <div className="container">
      <h2>Project Dashboard</h2>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '20px' }}>
        {projects.map((project) => (
          <div key={project.id} className="card" style={{ backgroundColor: getStatusColor(project.status) }}>
            <h3>{project.name}</h3>
            <span style={{
                display: 'inline-block',
                padding: '4px 8px',
                borderRadius: '4px',
                background: '#333',
                color: '#fff',
                fontSize: '0.8rem',
                marginBottom: '10px'
            }}>
                {project.status}
            </span>
            <p><strong>Problem:</strong> {project.problem_statement}</p>
            <p>{project.description}</p>
            {project.tags && <p><strong>Stack:</strong> {project.tags}</p>}
            {project.help_wanted_roles && (
                <div style={{ marginTop: '10px', padding: '10px', background: 'rgba(255,0,0,0.1)', border: '1px solid red', borderRadius: '4px' }}>
                    <strong>🔥 Help Wanted:</strong> {project.help_wanted_roles}
                </div>
            )}
             {/* Simple state transition simulation */}
             <div style={{marginTop: '10px'}}>
                 <small>Move to: </small>
                 {['Idea', 'PoC', 'Build', 'Scale'].map(status => (
                     status !== project.status && (
                        <button
                            key={status}
                            onClick={() => updateStatus(project.id, status)}
                            style={{ margin: '0 2px', fontSize: '0.7rem', cursor: 'pointer' }}
                        >
                            {status}
                        </button>
                     )
                 ))}
             </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProjectDashboard;

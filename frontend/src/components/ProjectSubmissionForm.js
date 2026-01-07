// Project Submission Form Component

import React, { useState } from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';

const ProjectSubmissionForm = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    problem_statement: '',
    status: 'Idea',
    vcs_url: '',
    tags: '',
    help_wanted_roles: '',
    owner_id: 1 // Hardcoded for PoC
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/projects/', formData);
      navigate('/');
    } catch (error) {
      console.error('Error submitting project:', error);
      alert('Failed to submit project');
    }
  };

  return (
    <div className="container">
      <div className="card" style={{ maxWidth: '600px', margin: '0 auto' }}>
        <h2>Submit New Idea</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Project Name</label>
            <input type="text" className="form-control" name="name" value={formData.name} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Problem Statement</label>
            <textarea className="form-control" name="problem_statement" value={formData.problem_statement} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Description</label>
            <textarea className="form-control" name="description" value={formData.description} onChange={handleChange} required />
          </div>
          <div className="form-group">
            <label>Phase</label>
            <select className="form-control" name="status" value={formData.status} onChange={handleChange}>
              <option value="Idea">Idea</option>
              <option value="PoC">PoC</option>
              <option value="Build">Build</option>
              <option value="Scale">Scale</option>
            </select>
          </div>
          <div className="form-group">
            <label>VCS URL (Optional for Idea)</label>
            <input type="text" className="form-control" name="vcs_url" value={formData.vcs_url} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>Tech Stack Tags (comma separated)</label>
            <input type="text" className="form-control" name="tags" value={formData.tags} onChange={handleChange} placeholder="React, Python, Kafka" />
          </div>
          <div className="form-group">
            <label>Help Wanted (Roles needed)</label>
            <input type="text" className="form-control" name="help_wanted_roles" value={formData.help_wanted_roles} onChange={handleChange} placeholder="Frontend, QA" />
          </div>
          <button type="submit" className="btn btn-primary">Submit Idea</button>
        </form>
      </div>
    </div>
  );
};

export default ProjectSubmissionForm;

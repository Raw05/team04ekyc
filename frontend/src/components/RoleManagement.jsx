import React from 'react';

const RoleManagement = () => {
  const users = [
    { id: 1, username: 'JohnDoe', role: 'admin' },
    { id: 2, username: 'JaneDoe', role: 'reviewer' },
  ];

  const handleRoleChange = (id, newRole) => {
    console.log(`User ${id} role changed to ${newRole}`);
  };

  return (
    <div>
      <h2>Role Management</h2>
      <table>
        <thead>
          <tr>
            <th>Username</th>
            <th>Role</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.username}</td>
              <td>{user.role}</td>
              <td>
                <select
                  value={user.role}
                  onChange={(e) => handleRoleChange(user.id, e.target.value)}
                >
                  <option value="admin">Admin</option>
                  <option value="reviewer">Reviewer</option>
                  <option value="auditor">Auditor</option>
                </select>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};


export default RoleManagement;

const tbody = document.getElementById('employees-body');
async function loadEmployees() {
  try {
    const employees = await api('/employees');
    document.getElementById('employee-count').textContent = `${employees.length} employees in your directory`;
    tbody.innerHTML = employees.map(e => `<tr><td><b>${e.name}</b><div style="color:#999;font-size:10px;margin-top:3px">${e.email}</div></td><td>${e.department}</td><td>${e.role}</td><td><span class="status" style="${e.status === 'Inactive' ? 'background:#f3f3f5;color:#888' : ''}">${e.status}</span></td><td>${e.status === 'Active' ? `<button class="button" onclick="deactivateEmployee(${e.id})">Deactivate</button>` : ''}</td></tr>`).join('') || '<tr><td colspan="5">No employees found.</td></tr>';
    const select = document.getElementById('employee-select');
    if (select) select.innerHTML = employees.filter(e => e.status === 'Active').map(e => `<option value="${e.id}">${e.name} · ${e.department}</option>`).join('');
  } catch (error) { document.getElementById('employee-error').textContent = `${error.message}. Is the backend running?`; }
}
async function deactivateEmployee(id) {
  try { await api(`/employees/${id}/deactivate`, { method: 'PATCH' }); await loadEmployees(); }
  catch (error) { document.getElementById('employee-error').textContent = error.message; }
}
document.getElementById('employee-form').addEventListener('submit', async event => {
  event.preventDefault(); const form = Object.fromEntries(new FormData(event.currentTarget));
  try { await api('/employees', { method: 'POST', body: JSON.stringify(form) }); event.currentTarget.reset(); document.getElementById('employee-error').textContent = ''; await loadEmployees(); }
  catch (error) { document.getElementById('employee-error').textContent = error.message; }
});
loadEmployees();

const attendanceForm = document.getElementById('attendance-form');
const dateInput = document.getElementById('attendance-date');
const filterDate = document.getElementById('filter-date');
dateInput.value = todayISO(); filterDate.value = todayISO();
async function loadAttendance() {
  try {
    const params = filterDate.value ? `?day=${filterDate.value}` : '';
    const rows = await api(`/attendance${params}`);
    document.getElementById('attendance-body').innerHTML = rows.map(row => `<tr><td>${row.employee_name}<div style="color:#999;font-size:10px">${row.department || ''}</div></td><td>${row.attendance_date}</td><td>${row.check_in || '—'}</td><td>${row.check_out || '—'}</td><td><span class="status">${row.status}</span></td></tr>`).join('') || '<tr><td colspan="5">No records for this date.</td></tr>';
  } catch (error) { document.getElementById('attendance-error').textContent = `${error.message}. Is the backend running?`; }
}
filterDate.addEventListener('change', loadAttendance);
attendanceForm.addEventListener('submit', async event => {
  event.preventDefault(); const data = Object.fromEntries(new FormData(attendanceForm));
  for (const key of ['check_in', 'check_out']) if (!data[key]) data[key] = null;
  try { await api('/attendance', { method: 'POST', body: JSON.stringify(data) }); document.getElementById('attendance-error').textContent = ''; filterDate.value = data.attendance_date; await loadAttendance(); }
  catch (error) { document.getElementById('attendance-error').textContent = error.message; }
});
loadEmployees().catch(() => {});
async function loadEmployees() {
  const employees = await api('/employees');
  document.getElementById('employee-select').innerHTML = employees.filter(e => e.status === 'Active').map(e => `<option value="${e.id}">${e.name} · ${e.department}</option>`).join('');
}
loadAttendance();
